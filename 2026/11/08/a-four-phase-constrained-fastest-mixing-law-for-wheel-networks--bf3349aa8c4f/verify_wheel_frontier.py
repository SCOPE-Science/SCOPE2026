"""Independent finite tests of exact constrained wheel-chain mixing formula.

Requires Python 3 standard library only. The mathematical theorem for all sizes
and all real thresholds is proved analytically in RESULT.md; these tests are
supplemental rather than a substitute for that proof.
"""
from fractions import Fraction
from itertools import combinations
from math import pi, sin, isclose


def spectral_data(n):
    a = 4 * sin(pi / n)**2
    b = 4 * sin(pi * (n//2) / n)**2
    return a,b


def result(n, t, a=None, b=None):
    if a is None: a,b = spectral_data(n)
    one = Fraction(1) if isinstance(a, Fraction) else 1.0
    t1 = 2 * (one-one/n)/(a+b)
    t2 = 2*n / ((n+2)*a+n*b)
    t3 = n/(2*(n+2)-b)
    if t <= t1:
        p = one/n
        q = t1
        mu = (one-one/n)*(b-a)/(b+a)
    elif t <= t2:
        p = one-(a+b)*t/2
        q = t
        mu = (b-a)*t/2
    elif t <= t3:
        p = (2-b*t)/(n+2)
        q = t
        mu = ((n+1)*b*t-n)/(n+2)
    else:
        p = one-2*t
        q = t
        mu = 2*(n+1)*t-n
    return p,q,mu,(t1,t2,t3)


def det3(M):
    a,b,c=M[0];d,e,f=M[1];g,h,i=M[2]
    return a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)


def solve3(A,z):
    det=det3(A)
    if abs(float(det))<1e-11: return None
    return tuple(det3([[z[r] if c==j else A[r][c] for c in range(3)] for r in range(3)])/det for j in range(3))


def reference_lp(n,t,a,b,exact=False):
    # Explicit, independent enumeration of all vertices of the 3-variable LP.
    # Constraints are linear; objective s bounds |all nonconstant modes|.
    C=[([-1,0,0],0),([1,0,0],Fraction(1,n) if exact else 1/n),([0,-1,0],-t),
       ([1,2,0],1),([0,0,-1],0),
       ([-(n+1),0,-1],-1),([(n+1),0,-1],1),
       ([-1,-a,-1],-1),([1,b,-1],1)]
    best=None
    tol=1e-7 if not exact else 0
    for inds in combinations(range(len(C)),3):
        A=[C[i][0] for i in inds];z=[C[i][1] for i in inds]
        v=solve3(A,z)
        if v is None:continue
        if all(float(sum(x*y for x,y in zip(row,v))-rhs)<=tol for row,rhs in C):
            if best is None or v[2]<best[2]: best=v
    if best is None: raise AssertionError('LP has no feasible vertex')
    return best


def check():
    numeric=0
    for n in range(4,51):
        a,b=spectral_data(n)
        p0,q0,mu0,(t1,t2,t3)=result(n,0,a,b)
        assert 0<t1<t2<t3<=0.5+1e-9,(n,t1,t2,t3)
        thresholds=[0,t1,t2,t3,0.5]
        for i in range(1,35): thresholds.append(i/70)
        for t in thresholds:
            p,q,mu,_=result(n,t,a,b)
            assert p>=-1e-9 and q>=t-1e-9 and n*p<=1+1e-9 and p+2*q<=1+1e-9
            modes=[abs(1-(n+1)*p)]
            modes += [abs(1-p-4*q*sin(pi*k/n)**2) for k in range(1,n)]
            assert isclose(max(modes),mu,abs_tol=2e-9), (n,t,p,q,mu,max(modes))
            ref=reference_lp(n,t,a,b)
            assert isclose(float(ref[2]),mu,abs_tol=3e-8),(n,t,mu,ref)
            numeric+=1

    exact=0
    for n,a,b in [(4,Fraction(2),Fraction(4)),(6,Fraction(1),Fraction(4))]:
        qs=[Fraction(i,40) for i in range(21)]
        _,_,_,ts=result(n,Fraction(0),a,b)
        qs += list(ts)
        for t in qs:
            p,q,mu,_=result(n,t,a,b)
            ref=reference_lp(n,t,a,b,True)
            assert mu==ref[2], (n,t,mu,ref)
            assert mu==max(abs(1-(n+1)*p), abs(1-p-a*q), abs(1-p-b*q))
            exact+=1
    print('PASS:', numeric,'independent floating-point LP/spectral comparisons,',exact,
          'exact-rational LP checks, all transition boundaries')


if __name__=='__main__':check()
