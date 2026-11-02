"""Reproducibility checks for the mixed-monomial dual Toeplitz defect.

Requires only Python 3 standard library. Uses exact rational moments for
all finite algebraic identities; floating point is used only for asymptotic
sanity checks, not as a proof of any infinite-dimensional statement.
"""
from fractions import Fraction as F
from math import sqrt, isclose

checks=0

def check(assertion):
    global checks
    assert assertion
    checks += 1

def radial_moment(k):
    """Normalized disk integral of |z|^(2k)."""
    return F(1,k+1)

def gp_direct(m,ell):
    """Norm squared of (I-P)(conj(z)^m sqrt(n+1) z^n), n=ell+m."""
    if ell < -m:
        return F(0)
    n=ell+m
    raw=F(n+1,n+m+1)
    if ell<0:
        return raw
    projected=F(ell+1,ell+m+1)
    # Norm^2 of sqrt(n+1) * projected z^ell
    return raw-F(n+1,1)*projected*projected*radial_moment(ell)

def cp_direct(p,q,ell):
    if ell < -p or ell < -q:
        return 0.0
    n=ell+p
    k=ell+q
    # Raw inner product of sqrt(n+1)*z^n conj(z)^p and counterpart
    base=F(1,ell+p+q+1)
    if ell>=0:
        base -= F(ell+1,(ell+p+1)*(ell+q+1))
    return sqrt((n+1)*(k+1))*float(base)

def a_formula(m,ell):
    if ell < -m:
        return F(0)
    if ell<0:
        return F(ell+m+1,ell+2*m+1)
    L=ell+1
    return F(m*m,(L+m)*(L+2*m))

def c_formula(p,q,ell):
    if ell < -p or ell < -q:
        return 0.0
    if ell<0:
        return sqrt((ell+p+1)*(ell+q+1))/(ell+p+q+1)
    L=ell+1
    return p*q/((L+p+q)*sqrt((L+p)*(L+q)))

def delta_formula(p,q,ell):
    L=ell+1
    return F(p*p*q*q*(p-q)**2,(L+p)*(L+q)*(L+2*p)*(L+2*q)*(L+p+q)**2)

def eigs(p,q,ell,eta):
    a=float(a_formula(p,ell)); b=float(a_formula(q,ell));
    cp=c_formula(p,q,ell)
    determinant=eta*eta*max(0,a*b-cp*cp)
    if ell>=0:
        determinant=eta*eta*float(delta_formula(p,q,ell))
    trace=eta*eta*b-a
    radical=sqrt(trace*trace+4*determinant)
    # Stable small root (do not subtract nearly equal floating point numbers).
    if trace>=0:
        positive=(trace+radical)/2
        negative=-determinant/positive if positive else 0.0
    else:
        negative=(trace-radical)/2
        positive=-determinant/negative if negative else 0.0
    return positive,negative

for p in range(1,10):
    for q in range(1,10):
        for ell in range(-10,150):
            A=a_formula(p,ell); B=a_formula(q,ell)
            check(gp_direct(p,ell)==A)
            check(gp_direct(q,ell)==B)
            check(isclose(cp_direct(p,q,ell), c_formula(p,q,ell),rel_tol=2e-14,abs_tol=3e-14))
            if ell>=0 and p!=q:
                # Compare squared inner product with the exact Gram determinant.
                L=ell+1
                corr_sq=F(p*p*q*q,(L+p)*(L+q)*(L+p+q)**2)
                check(A*B-corr_sq==delta_formula(p,q,ell))
                check(delta_formula(p,q,ell)>0)
            if p!=q:
                u,v=eigs(p,q,ell,F(3,4))
                check(u>=-1e-12 and v<=1e-12)
                if ell>=0:
                    check(u>0 and v<0)
for m in range(1,20):
    for N in range(m,3*m+10):
        total=sum((gp_direct(m,n-m) for n in range(N+1)),F(0))
        tail=m*sum((F(1,j) for j in range(N+2,N+m+2)),F(0))
        check(total+tail==m)

for p,q in [(1,2),(2,1),(2,5),(5,2),(3,7)]:
    for eta in [F(1,3),F(1,1),F(p,q),F(5,1)]:
        s=float(eta*eta*q*q-p*p)
        g=float(eta*eta*p*p*q*q*(p-q)**2)
        for ell in [10**5,10**6]:
            L=ell+1
            positive,negative=eigs(p,q,ell,float(eta))
            if eta == F(p,q):
                cplus=p*p*(3*(p-q)+sqrt(13)*abs(p-q))/2
                cminus=p*p*(sqrt(13)*abs(p-q)-3*(p-q))/2
                check(isclose(positive*L**3,cplus,rel_tol=0.005))
                check(isclose(-negative*L**3,cminus,rel_tol=0.005))
            elif s>0:
                check(isclose(positive*L**2,s,rel_tol=0.005))
                check(isclose(-negative*L**4,g/s,rel_tol=0.005))
            else:
                check(isclose(-negative*L**2,-s,rel_tol=0.005))
                check(isclose(positive*L**4,g/(-s),rel_tol=0.005))

print('PASS:',checks,'exact moment, Gram, trace, inertia and asymptotic assertions')
