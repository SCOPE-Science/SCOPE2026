"""Exact-integer enclosure for a finite ordinal Frank-copula counterexample.

All interval endpoints are signed integers divided by P=10**20. The
transcendental enclosures follow from elementary, explicitly bounded
positive Taylor series; no floating-point/third-party packages are used.
"""
from fractions import Fraction
from functools import lru_cache

P=10**20
THETA=15
CUTS=(14357,20483,25318,29517,33333,36901,40301,43591,46812,50000,
      53188,56409,59699,63099,66667,70483,74682,79517,85643)
T=tuple(j*(P//100000) for j in CUTS)
assert len(T)==19 and all(0<T[i]<T[i+1] for i in range(18))
assert all(T[j]+T[18-j]==P for j in range(19))

def ceildiv(a,b):
    assert b>0
    return -((-a)//b)

def lower(q):
    return q.numerator*P//q.denominator

def upper(q):
    return ceildiv(q.numerator*P,q.denominator)

@lru_cache(None)
def exp_neg(k):
    """Return rigorous scaled enclosure of exp(-k/P), 0<=k<=15P."""
    assert 0<=k<=15*P
    x=Fraction(k,P)
    term=Fraction(1)
    s=term
    N=85
    for j in range(1,N+1):
        term=term*x/j
        s+=term
    next_term=term*x/(N+1)
    rem=next_term/(1-x/Fraction(N+2))
    assert rem>=0
    return lower(1/(s+rem)), upper(1/s)

def log_y(ylo,yhi):
    """Return rigorous enclosure for ln(y), with y in [ylo/P,yhi/P] subset [1,3]."""
    assert P<=ylo<=yhi<=3*P
    a=Fraction(ylo-P,ylo+P)
    b=Fraction(yhi-P,yhi+P)
    assert 0<=a<=b<1
    N=22
    def sums(v):
        acc=Fraction(0)
        power=v
        for j in range(N):
            acc+=2*power/(2*j+1)
            power*=v*v
        return acc,power
    sl,_=sums(a)
    sh,nextpower=sums(b)
    tail=2*nextpower/((2*N+1)*(1-b*b))
    return lower(sl),upper(sh+tail)

def frank_c(u,v):
    """Return scaled enclosed C_15(u/P,v/P)."""
    m=min(u,v); n=max(u,v)
    qlo,qhi=exp_neg(15*P)
    dlo,dhi=exp_neg(15*(n-m))
    nlo,nhi=exp_neg(15*n)
    olo,ohi=exp_neg(15*(P-m))
    alo=P+dlo-nhi-ohi
    ahi=P+dhi-nlo-olo
    den_lo=P-qhi
    den_hi=P-qlo
    assert 0<den_lo<=den_hi and alo>0
    ylo=max(P,(P*alo)//den_hi)
    yhi=ceildiv(P*ahi,den_lo)
    L,H=log_y(ylo,yhi)
    return m-ceildiv(H,THETA),m-(L//THETA)

def certify():
    # E(X) cancels; Var(X)=sum_{i,j}(min(t_i,t_j)-t_i*t_j).
    variance=0
    covlo=covhi=0
    for u in T:
        for v in T:
            base=u*v//P # exact because thresholds are multiples of 10**15
            assert u*v%P==0
            variance+=min(u,v)-base
            c_lo,c_hi=frank_c(u,v)
            covlo+=c_lo-base
            covhi+=c_hi-base
    assert variance>0 and covlo>0
    # Upper bound on Spearman rho via two Debye sums; integral
    # series evaluated using integral-tail zeta bounds.
    N=35
    z2_lower=sum((Fraction(1,j*j) for j in range(1,N+1)),Fraction(0))+Fraction(1,N+1)
    z3_upper=sum((Fraction(1,j**3) for j in range(1,N+1)),Fraction(0))+Fraction(1,2*N*N)
    q_upper=Fraction(exp_neg(THETA*P)[1],P)
    e1_upper=q_upper/(1-q_upper)+THETA*q_upper/(1-q_upper)**2
    rho_upper=1-Fraction(12,THETA**2)*z2_lower+Fraction(48,THETA**3)*z3_upper+Fraction(12,THETA**2)*e1_upper
    # Claim follows from strict cross multiplication on rational numbers.
    assert Fraction(covlo,variance)>rho_upper
    print('theta',THETA,'categories',len(T)+1)
    print('corr_lower',format(float(Fraction(covlo,variance)),'.14f'))
    print('corr_upper',format(float(Fraction(covhi,variance)),'.14f'))
    print('rho_upper',format(float(rho_upper),'.14f'))
    print('certified_gap_lower',format(float(Fraction(covlo,variance)-rho_upper),'.14f'))
    print('proof: strictly positive rational gap, using Taylor enclosures and integral test')
    print('cutpoints',','.join(f'{i/100000:.5f}' for i in CUTS))
    return (covlo,covhi,variance,rho_upper)

if __name__=='__main__':
    certify()
