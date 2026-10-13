"""Exact checks for two-step conjugate gradients on one-dimensional Poisson paths.

No external Python packages are needed. These tests support, but do not replace,
the formulas and infinite-family proofs in RESULT.md.
"""
from fractions import Fraction as Q


def matvec(v):
    n = len(v)
    return tuple(2 * v[i] - (v[i-1] if i else 0) -
                 (v[i+1] if i+1 < n else 0) for i in range(n))


def dot(a, b):
    return sum((x*y for x, y in zip(a,b)), Q(0))


def forcing(k, even, r, pad=0):
    hat = list(range(1,k+1)) + (list(range(k,0,-1)) if even
                                  else list(range(k-1,0,-1)))
    return tuple([Q(r),Q(0),Q(0)] + [Q(v) for v in hat] +
                 [Q(0)]*(1+pad))


def moments(b):
    ab=matvec(b)
    return dot(b,b),dot(b,ab),dot(ab,ab),dot(ab,matvec(ab))


def direct_cg_two(b):
    n=len(b)
    x=[Q(0)]*n
    residual=list(b)
    search=residual[:]
    rr=dot(residual,residual)
    for _ in range(2):
        ap=matvec(search)
        alpha=rr/dot(search,ap)
        x=[a+alpha*p for a,p in zip(x,search)]
        residual=[v-alpha*w for v,w in zip(residual,ap)]
        rr_new=dot(residual,residual)
        beta=rr_new/rr
        search=[u+beta*w for u,w in zip(residual,search)]
        rr=rr_new
    return tuple(x)


def claimed(k,even,r):
    r=Q(r)
    if even:
        S=Q(k*(k+1)*(2*k+1),3)
        m2base,m3base=4,6
        A=Q(8*k**3+12*k**2+22*k-30,3)
        B=Q(4*k**3+6*k**2+2*k,3)
        C=Q(4*k**3-18*k**2+26*k,3)
        N=2*r**4-2*r**3+A*r**2-B*r-C
    else:
        S=Q(k*(2*k*k+1),3)
        m2base,m3base=6,12
        N=None
    m0=r*r+S
    m1=2*r*r+2*k
    m2=5*r*r+m2base
    m3=14*r*r-2*r+m3base
    D=m1*m3-m2*m2
    expanded=m0*m3-m1*m2-2*(m0*m2-m1*m1)
    if even:
        assert expanded == N
    else:
        N=expanded
        if r==0:
            assert N==4*k*(2*k-3)
    return (m0,m1,m2,m3),D,N


cases=0
negative=0
for k in range(2,36):
    for even in (False,True):
        for r in (Q(1,8),Q(1,4),Q(1,2),Q(3,4),Q(1),Q(2),Q(7,2)):
            for pad in (0,3):
                b=forcing(k,even,r,pad)
                m=moments(b)
                expected,D,N=claimed(k,even,r)
                assert m==expected,(k,even,r,'moments')
                assert D>0
                ab=matvec(b)
                x=direct_cg_two(b)
                galerkin=tuple(((m[0]*m[3]-m[1]*m[2])*u-
                                (m[0]*m[2]-m[1]**2)*v)/D
                               for u,v in zip(b,ab))
                assert x==galerkin
                assert x[0]==r*N/D
                if x[0]<0: negative+=1
                cases+=1

r=Q(1,2)
b=forcing(2,True,r)
assert direct_cg_two(b)[0]==Q(-29,171)
assert direct_cg_two(tuple(2*x for x in b))[0]==Q(-58,171)
assert all(v>=0 for v in b)
for k in range(2,36):
    # Sign-at-zero, sign-at-one and strict convexity coefficients.
    _,D0,N0=claimed(k,True,0)
    _,_,N1=claimed(k,True,1)
    assert D0>0 and N0<0 and N1==2*(k+1)*(4*k-5)>0
    _,Do,No=claimed(k,False,0)
    assert Do==12*(2*k-3)>0 and No==4*k*(2*k-3)>0
print('VERIFY_OK exact_moment_and_CG_cases=',cases,
      'negative_first_components=',negative,
      'witness=',str(Q(-58,171)),sep='')
