"""Reproducibility checks for signed inverse-Gram cycle Kaczmarz sampling.

Python 3 standard library only. Finite checks support, never replace,
the analytic all-dimensions proof in RESULT.md.
"""
import math
import random


def inverse(a):
    n = len(a)
    x = [list(map(float, row)) + [float(i == j) for j in range(n)]
         for i, row in enumerate(a)]
    for k in range(n):
        h = max(range(k, n), key=lambda i: abs(x[i][k]))
        x[h], x[k] = x[k], x[h]
        assert abs(x[k][k]) > 1e-12
        div = x[k][k]
        for j in range(k, 2*n):
            x[k][j] /= div
        for i in range(n):
            if i != k:
                factor = x[i][k]
                for j in range(k, 2*n):
                    x[i][j] -= factor*x[k][j]
    return [row[n:] for row in x]


def solve(a,b):
    return [sum(x*y for x,y in zip(row,b)) for row in inverse(a)]


def eigenvalues(a):
    a = [row[:] for row in a]
    n = len(a)
    for _ in range(150*n*n):
        i, j = max(((i,j) for i in range(n) for j in range(i+1,n)),
                   key=lambda ij: abs(a[ij[0]][ij[1]]))
        if abs(a[i][j]) < 3e-13:
            break
        tau = (a[j][j]-a[i][i])/(2*a[i][j])
        t = math.copysign(1,tau)/(abs(tau)+math.sqrt(1+tau*tau)) if tau else 1
        c=1/math.sqrt(1+t*t)
        s=t*c
        old=a[i][j]
        a[i][i]-=t*old
        a[j][j]+=t*old
        a[i][j]=a[j][i]=0.
        for k in range(n):
            if k!=i and k!=j:
                u,v=a[k][i],a[k][j]
                a[k][i]=a[i][k]=c*u-s*v
                a[k][j]=a[j][k]=s*u+c*v
    else:
        raise AssertionError('Jacobi method did not converge')
    return sorted(a[i][i] for i in range(n))


def cholesky(a):
    n=len(a)
    b=[[0.]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1):
            v=a[i][j]-sum(b[i][k]*b[j][k] for k in range(j))
            if i==j:
                assert v>0
                b[i][j]=math.sqrt(v)
            else:
                b[i][j]=v/b[j][j]
    return b


def example(n,t,w):
    c=[[0.]*n for _ in range(n)]
    for i in range(n-1):
        c[i][i+1]=c[i+1][i]=w
    c[0][-1]=c[-1][0]=-t*w
    diagonal=[1.]*n
    for _ in range(20):
        for i in range(n):
            c[i][i]=diagonal[i]
        inv=inverse(c)
        residual=[inv[i][i]-1 for i in range(n)]
        if max(map(abs,residual))<1e-13:
            break
        jac=[[-inv[i][j]**2 for j in range(n)] for i in range(n)]
        change=solve(jac,[-r for r in residual])
        diagonal=[a+b for a,b in zip(diagonal,change)]
    else:
        raise AssertionError('diagonal normalization failed')
    assert min(eigenvalues(c))>0
    return c,inverse(c)


def theta(n,t):
    ell=n-1
    if t<=1/ell:
        return 0.
    lo,hi=0.,math.pi/ell
    for _ in range(90):
        mid=(lo+hi)/2
        if math.sin(mid)/math.sin(ell*mid)>t:
            hi=mid
        else:
            lo=mid
    return (lo+hi)/2


def test(n,t,rand):
    w=.015
    c,g=example(n,t,w)
    b=cholesky(g)
    counter=0
    for row in b:
        assert abs(sum(x*x for x in row)-1)<1e-9
        counter+=1
    ang=theta(n,t)
    phi=(n-1)*ang
    q=[c[i][i]+2*w*math.cos(ang) for i in range(n)]
    for i in (0,n-1):
        q[i]=c[i][i]+w*(math.cos(ang)-t*math.cos(phi))
    T=sum(q)
    assert min(q)>0 and T>0
    counter+=1
    S=[[((q[i]-c[i][i]) if i==j else -c[i][j]) for j in range(n)]
       for i in range(n)]
    es=eigenvalues(S)
    assert es[0]>-2e-9, (n,t,es)
    assert sum(abs(x)<1e-8 for x in es)==(1 if t<1/(n-1)-1e-12 else 2)
    counter+=2
    assert abs(T-(sum(c[i][i] for i in range(n)) +
                  2*w*((n-1)*math.cos(ang)-t*math.cos(phi))))<1e-10
    counter+=1
    vectors=[(math.cos(i*ang),math.sin(i*ang)) for i in range(n)]
    for i in range(n):
        for axis in range(2):
            assert abs(sum(S[i][j]*vectors[j][axis] for j in range(n)))<1e-8
            counter+=1
    p=[x/T for x in q]
    h=[[sum(p[k]*b[k][i]*b[k][j] for k in range(n)) for j in range(n)]
       for i in range(n)]
    assert abs(eigenvalues(h)[0]-1/T)<2e-9
    counter+=1
    for _ in range(12):
        probs=[rand.random()+0.001 for _ in range(n)]
        probs=[x/sum(probs) for x in probs]
        h2=[[sum(probs[k]*b[k][i]*b[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]
        assert eigenvalues(h2)[0]<=1/T+2e-9
        counter+=1
        angles=[rand.uniform(-math.pi,math.pi) for _ in range(n)]
        objective=sum(c[i][i] for i in range(n))
        objective+=2*w*(sum(math.cos(angles[i+1]-angles[i]) for i in range(n-1))-
                         t*math.cos(angles[-1]-angles[0]))
        assert objective<=T+2e-9
        counter+=1
    return counter


def main():
    rand=random.Random(361820)
    count=0
    for n in range(5,13):
        tcrit=1/(n-1)
        for t in (.04,tcrit,tcrit*1.1,.5,1.,1.75,3.):
            count+=test(n,t,rand)
    for n in range(5,13):
        assert abs(theta(n,1)-math.pi/n)<1e-12
        count+=1
    print('PASS:',count,'assertion groups across 56 normalized inverse-Gram examples')

if __name__=='__main__':
    main()
