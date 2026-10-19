"""Standalone finite numerical checks for wheel-chain spectral rigidity.
Standard library only. Run: python3 verify.py
"""
import math
import random


def wheel(m, spoke, rim):
    n=m+1
    p=[[0.0]*n for _ in range(n)]
    for i in range(m):
        j=i+1
        p[0][j]=p[j][0]=spoke[i]
        k=(i+1)%m+1
        p[j][k]=p[k][j]=rim[i]
    for i in range(n):
        p[i][i]=1.0-sum(p[i])
    assert min(p[i][i] for i in range(n)) >= -1e-12
    return p


def eigvalsh(a):
    a=[row[:] for row in a]
    n=len(a)
    for _ in range(80*n*n):
        v=0.0; pair=None
        for i in range(n):
            for j in range(i+1,n):
                if abs(a[i][j])>v:
                    v=abs(a[i][j]);pair=(i,j)
        if v<2e-14:
            break
        i,j=pair
        theta=.5*math.atan2(2*a[i][j], a[j][j]-a[i][i])
        c=math.cos(theta);s=math.sin(theta)
        aii,ajj,aij=a[i][i],a[j][j],a[i][j]
        a[i][i]=c*c*aii-2*s*c*aij+s*s*ajj
        a[j][j]=s*s*aii+2*s*c*aij+c*c*ajj
        a[i][j]=a[j][i]=0.0
        for k in range(n):
            if k not in (i,j):
                u,w=a[k][i],a[k][j]
                a[k][i]=a[i][k]=c*u-s*w
                a[k][j]=a[j][k]=s*u+c*w
    else:
        raise RuntimeError('Jacobi eigenvalue solver did not converge')
    return sorted(a[i][i] for i in range(n))


def parameters(m):
    u=2-2*math.cos(2*math.pi/m)
    v=2-2*math.cos(2*math.pi*(m//2)/m)
    r=(v-u)/(v+u)
    mu=(1-1/m)*r
    p=1/m
    q=2*(1-p)/(u+v)
    return u,v,r,mu,p,q


def verify(m,spoke,rim):
    u,v,r,mu,p0,q0=parameters(m)
    p=wheel(m,spoke,rim)
    eig=eigvalsh(p)
    assert abs(eig[-1]-1)<1e-9, (m,eig)
    spectral=max(abs(a) for a in eig[:-1])
    assert spectral+1e-9>=mu, (m,spectral,mu)
    eps=max(0.0,spectral-mu)
    b=eps+math.sqrt(2*(mu+eps)*(1+u/v)*eps)
    h=eps/u+2*eps/(r*(u+v))
    rhs_q=h+b/(2*math.sin(math.pi/m)*math.sin(2*math.pi/m))
    rhs_p=u*rhs_q+b
    dq=math.sqrt(sum((q-q0)**2 for q in rim)/m)
    dp=math.sqrt(sum((p-p0)**2 for p in spoke)/m)
    assert dq<=rhs_q+2e-8, ('rim',m,dq,rhs_q)
    assert dp<=rhs_p+2e-8, ('spoke',m,dp,rhs_p)
    return spectral


def main():
    checks=0
    rng=random.Random(204701)
    for m in range(4,20):
        u,v,r,mu,p,q=parameters(m)
        assert u>0 and v>u and u+v>=4
        assert r>=1/(m-1)-1e-14
        assert 2*q+p<=1+1e-12
        assert abs(verify(m,[p]*m,[q]*m)-mu)<1e-9
        checks+=8
        for trial in range(280):
            if trial<140:
                scale=.3+.69*rng.random()
                ps=[(scale/m)*(.75+.25*rng.random()) for i in range(m)]
                qs=[(.1+.65*rng.random())*q for i in range(m)]
            else:
                # Small asymmetric perturbations near the analytically optimal kernel.
                scale=1-10**(-rng.uniform(2.0,5.0))
                xs=[rng.uniform(-1,1) for _ in range(m)]
                xbar=sum(xs)/m
                ps=[p*scale + p*(1-scale)*.15*(xi-xbar) for xi in xs]
                qs=[q*(1+(.005+rng.random()*.003)*(xi-xbar)) for xi in xs]
            assert min(ps)>0 and min(qs)>0 and sum(ps)<=1+1e-12
            assert all(ps[i]+qs[i]+qs[(i-1)%m]<1+1e-12 for i in range(m))
            verify(m,ps,qs)
            checks+=5
    # Two small exact-rational invariant examples; m=4 and m=6.
    assert abs(parameters(4)[3]-.25)<1e-13
    assert abs(parameters(4)[5]-.25)<1e-13
    assert abs(parameters(6)[3]-.5)<1e-13
    assert abs(parameters(6)[5]-1/3)<1e-13
    checks+=4
    print('VERIFY_OK',checks,'finite assertions; wheel m=4..19')

if __name__=='__main__':
    main()
