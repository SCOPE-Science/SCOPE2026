"""Exact rational checks for a priced perfect matching in a balanced biclique.

This program checks representative finite instances. The theorem for all orders
and all positive prices follows from the accompanying analytic proof.
Python >=3.9; standard library only.
"""
from fractions import Fraction as F
from math import isclose


def inverse(a):
    n = len(a)
    b = [list(row) + [F(int(i == j)) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        p = next(k for k in range(j,n) if b[k][j])
        b[j],b[p] = b[p],b[j]
        q = b[j][j]
        b[j] = [z/q for z in b[j]]
        for k in range(n):
            if k != j and b[k][j]:
                q=b[k][j]
                b[k]=[v-q*w for v,w in zip(b[k],b[j])]
    return [row[n:] for row in b]


def build(n, a, b):
    N=2*n
    L=[[F(0) for j in range(N)] for i in range(N)]
    for i in range(n):
        for j in range(n):
            w=a if i==j else b
            ii=i; jj=n+j
            L[ii][ii]+=w; L[jj][jj]+=w
            L[ii][jj]-=w; L[jj][ii]-=w
    return L


def kirchhoff_matrix(n,a,b):
    N=2*n
    L=build(n,a,b)
    M=[[L[i][j]+F(1,N) for j in range(N)] for i in range(N)]
    V=inverse(M)
    return N*(sum(V[i][i] for i in range(N))-1)


def kirchhoff_spectrum(n,a,b):
    return 2*n*(F(n-1,n*b)+F(n-1,2*a+(n-2)*b)+F(1,2*(a+(n-1)*b)))


def tcrit(n):
    return F(n*n*(4*n*n-11*n+8),(n-2)*(4*n**3-11*n*n+10*n-4))


def obj(n,t,x):
    b=1/(n*(t*x+n-1))
    return kirchhoff_spectrum(n,x*b,b)


def derivative_reduced(n,t,x):
    """Derivative of F=(t*x+n-1)*H, with K=2*n*n*F."""
    q=F(n-1); p=F(n-2,2); A=F(n-1,2); C=F(n-1,n); B=F(1,2)
    return t*C+A*(t*p-q)/(x+p)**2+B*q*(t-1)/(x+q)**2


def root(n,t):
    from math import isfinite
    t=float(t)
    if t >= float(tcrit(n)):
        return 0.
    lo=0.; hi=1.
    while derivative_reduced(n,t,hi)<0:
        hi*=2
        assert isfinite(hi) and hi<1.e12
    for _ in range(100):
        mid=(lo+hi)/2
        if derivative_reduced(n,t,mid)<0:lo=mid
        else:hi=mid
    return (lo+hi)/2


def noninvariant_matrix(n, t, raw):
    N=2*n
    budget=sum((t if i==j else F(1))*raw[i*n+j] for i in range(n) for j in range(n))
    L=[[F(0) for _ in range(N)] for _ in range(N)]
    for i in range(n):
        for j in range(n):
            w=raw[i*n+j]/budget
            L[i][i]+=w; L[n+j][n+j]+=w
            L[i][n+j]-=w; L[n+j][i]-=w
    M=[[L[i][j]+F(1,N) for j in range(N)] for i in range(N)]
    V=inverse(M)
    return N*(sum(V[i][i] for i in range(N))-1)


def run():
    count=0; checkpoints=0; critical=0; nonsymmetric=0
    for n in range(3,8):
        for t in (F(1,4),F(3,5),F(1),F(6,5),F(3,2),F(2),F(4)):
            for x in (F(0),F(1,3),F(1),F(2)):
                b=1/(n*(t*x+n-1));a=x*b
                assert n*t*a+n*(n-1)*b==1
                val=kirchhoff_matrix(n,a,b)
                assert val==kirchhoff_spectrum(n,a,b)
                assert val==obj(n,t,x)
                count+=1
        c=tcrit(n)
        assert derivative_reduced(n,c,F(0))==0
        assert derivative_reduced(n,F(1),F(1))==0
        assert F(1)<c
        for t in (c, c+F(1,3),c+F(3,2)):
            assert derivative_reduced(n,t,F(0))>=0
            v=obj(n,t,F(0))
            for x in (F(1,100), F(1,4),F(1),F(3),F(10)):
                assert obj(n,t,x)>v
                checkpoints+=1
        t=c-F(1,100)
        assert derivative_reduced(n,t,F(0))<0
        small=F(1,10000)
        assert obj(n,t,small)<obj(n,t,F(0))
        critical+=1
        # The fixed unweighted crown and biclique Kf values are known.
        assert kirchhoff_spectrum(n,F(0),F(1)) == F(4*n**3-11*n*n+10*n-4,(n-2)*(n-1))
        assert kirchhoff_spectrum(n,F(1),F(1)) == 4*n-3
    # Independent individual-edge allocations, not restricted to two weight classes.
    # Rationally compare to the proved boundary optimum for prices above threshold.
    import random
    rng=random.Random(20261009)
    for n in (3,4,5):
        for t in (tcrit(n),tcrit(n)+F(1,2), tcrit(n)+F(3)):
            best=obj(n,t,F(0))
            for _ in range(24):
                raw=[F(rng.randint(1,9)) for j in range(n*n)]
                other=noninvariant_matrix(n,t,raw)
                assert other>best
                nonsymmetric+=1
    for s in (-2.,-1.,0.,1.,2.,3.):
        y=max(1-s/2,0)
        for n in (100,400,1600):
            t=1+s/n
            x=root(n,t)
            if s !=2:
                assert abs(x-y)<(20/n) + 1e-6, (s,n,x,y)
            else:
                assert x<20/n
            critical+=1
    print(f'VERIFY_OK {count} exact-rational matrix-inverse/spectrum/budget identities; {checkpoints} boundary-optimality comparisons; {critical} threshold/window checks; {nonsymmetric} exact nonsymmetric feasible competitors')
    print('Finite tests do not prove the theorem or its asymptotic limits.')


if __name__=='__main__':run()
