"""Checks local stability formulas for two-token softmax sphere dynamics.

Uses only the Python standard library; it is a finite numerical check, not a
substitute for the analytical proof in RESULT.md.
"""
import math


def update(z, a, b, sharpness, step):
    """Full (self-inclusive) softmax normalization update on (S^1)^2."""
    out = []
    for i in range(2):
        scores = [sharpness * (z[i][0]*z[j][0] + z[i][1]*z[j][1]) for j in range(2)]
        # stable two-value softmax
        m = max(scores)
        weights = [math.exp(s-m) for s in scores]
        den = sum(weights)
        m0 = sum(weights[j]*z[j][0] for j in range(2))/den
        m1 = sum(weights[j]*z[j][1] for j in range(2))/den
        v = (z[i][0]+step*a*m0, z[i][1]-step*b*m1)
        norm = math.hypot(*v)
        if norm == 0:
            raise ZeroDivisionError('undefined normalization')
        out.append((v[0]/norm, v[1]/norm))
    return out


def point(signs, offsets=(0.0, 0.0)):
    return [(d, sign*math.sqrt(1.0-d*d)) for sign,d in zip(signs,offsets)]


def diff_jac(signs, a, b, sharpness, step, h=1e-6):
    cols=[]
    for k in range(2):
        offs=[0.0,0.0]
        offs[k]=h
        zp=update(point(signs,offs),a,b,sharpness,step)
        offs[k]=-h
        zm=update(point(signs,offs),a,b,sharpness,step)
        cols.append([(zp[i][0]-zm[i][0])/(2*h) for i in range(2)])
    return [[cols[j][i] for j in range(2)] for i in range(2)]


def verify(a,b,sharpness,step,signs,which):
    t=math.tanh(sharpness)
    if which=='antipodal':
        denom=abs(1-step*b*t)
        expected=[[1+step*a*(1+t)/2, step*a*(1-t)/2],
                  [step*a*(1-t)/2, 1+step*a*(1+t)/2]]
        exact_radii=((1+step*a)/denom,(1+step*a*t)/denom)
    else:
        denom=abs(1-step*b)
        expected=[[1+step*a/2, step*a/2],[step*a/2,1+step*a/2]]
        exact_radii=((1+step*a)/denom,1/denom)
    expected=[[v/denom for v in row] for row in expected]
    got=diff_jac(signs,a,b,sharpness,step)
    discrepancy=max(abs(expected[i][j]-got[i][j]) for i in range(2) for j in range(2))
    assert discrepancy<1e-8,(which,got,expected,discrepancy)
    nxt=update(point(signs),a,b,sharpness,step)
    assert all(abs(nxt[i][1]+signs[i])<1e-12 for i in range(2)),(which,nxt)
    nn=update(nxt,a,b,sharpness,step)
    assert all(abs(nn[i][1]-signs[i])<1e-12 for i in range(2)),(which,nn)
    return exact_radii


def main():
    for alpha in (0.4,0.6,1.0,3.0):
        for eta in (2.5,4.,10.,20.):
            a,b=1.,2.
            if eta*b*math.tanh(alpha)>1:
                bi=verify(a,b,alpha,eta,(1,-1),'antipodal')
                assert (bi[0]<1) == (b*math.tanh(alpha)>a and eta>2/(b*math.tanh(alpha)-a))
            if eta*b>1:
                co=verify(a,b,alpha,eta,(1,1),'consensus')
                assert (co[0]<1)==(eta>2/(b-a))
    alpha=1.0; eta=10.0; a=1.0; b=2.0
    for signs in ((1,1),(1,-1)):
        z=point(signs,(1e-3,-7e-4))
        for step in range(240):
            z=update(z,a,b,alpha,eta)
        target=point(signs)
        err=max(math.dist(z[i],target[i]) for i in range(2))
        assert err<1e-10,(signs,err)
    t=math.tanh(alpha)
    print('PASS: 32 analytical/finite-difference Jacobian cases and 2 attracting 240-step trajectories')
    print('Example alpha=1, a=1, b=2, eta=10:')
    print('antipodal one-step eigenvalues', (1+eta*a)/(eta*b*t-1), (1+eta*a*t)/(eta*b*t-1))
    print('consensus one-step eigenvalues', (1+eta*a)/(eta*b-1), 1/(eta*b-1))
    print('large-step necessary sharpness floor',math.atanh(a/b))
    print('sharp critical sharpness at eta=10',math.atanh((a+2/eta)/b))
    print('critical antipodal step',2/(b*t-a))


if __name__=='__main__':
    main()
