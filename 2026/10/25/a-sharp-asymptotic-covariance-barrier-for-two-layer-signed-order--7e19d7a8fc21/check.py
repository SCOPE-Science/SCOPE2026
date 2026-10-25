"""Independent rational-moment and limiting-spectrum checks for two-layer signed order polytopes."""
from fractions import Fraction as F
from math import factorial,sqrt

def beta(a,b):
    return F(factorial(a-1)*factorial(b-1), factorial(a+b-1))

def integral_monomial(t_power, endpoint_power, p):
    return beta(t_power+1,p+endpoint_power)

def base_moments(p):
    # Direct integration in the positive unit cube and p negative-coordinate sectors.
    v=F(1)+p*beta(1,p)
    mi=F(1,2) - beta(2,p)
    mi+=(p-1)*(beta(1,p)+beta(2,p))/2
    mi/=v
    mii=(F(1,3)+beta(3,p)+(p-1)*(beta(1,p)+beta(2,p)+beta(3,p))/3)/v
    mij=(F(1,4)-(beta(2,p)+beta(3,p))+(p-2)*(beta(1,p)+2*beta(2,p)+beta(3,p))/4)/v
    return mi,mii-mi*mi,mij-mi*mi

def rational_spectrum(p,q):
    n=p+q
    mu,diag,off=base_moments(p)
    # Independent conditional-mixture computation using E[T^j] via beta ratios.
    et=F(p+1,n+1)
    et2=F((p+1)*(p+2),(n+1)*(n+2))
    vt=et2-et*et
    e_one_minus_t_sq=F(q*(q+1),(n+1)*(n+2))
    xeig=et2*(diag-off)
    yeig=F(q+2,12*q)*e_one_minus_t_sq
    ax=et2*(diag+(p-1)*off)+p*mu*mu*vt
    ay=F((q+1)**2,4*q)*vt+F(q-1,12*q)*e_one_minus_t_sq
    # squared off-diagonal C has rational coefficients; C=sqrt(pq)*mu*(q+1)/(2q)*vt.
    c2=p*q*(mu*F(q+1,2*q)*vt)**2
    return xeig,yeig,ax,ay,c2

def analytic_spectrum(p,q):
    n=p+q
    m=F((p-1)*(p+2),2*p*(p+1))
    cp=F(p**3+3*p*p+14*p+48,12*p*(p+1)*(p+2))
    cl=F(p**4+4*p**3-7*p*p+26*p+24,12*p*(p+1)**2*(p+2))
    s=F((p+1)*(p+2),(n+1)*(n+2))
    v=F((p+1)*q,(n+1)**2*(n+2))
    xeig=s*cp
    yeig=F((q+1)*(q+2),12*(n+1)*(n+2))
    ax=s*cl+p*m*m*v
    ay=F((q+1)**2*(p+1),4*(n+1)**2*(n+2))+F((q-1)*(q+1),12*(n+1)*(n+2))
    c2=p*q*(m*F(q+1,2*q)*v)**2
    return xeig,yeig,ax,ay,c2

def kappa(p,q):
    xe,ye,ax,ay,c2=map(float,analytic_spectrum(p,q))
    lamplus=(ax+ay+sqrt((ax-ay)**2+4*c2))/2
    lamminus=(ax+ay-sqrt((ax-ay)**2+4*c2))/2
    return max(lamplus,xe,ye)/min(lamminus,xe,ye)

if __name__ == '__main__':
    tested=0
    for p in range(3,25):
        for q in range(2,22):
            a=rational_spectrum(p,q); b=analytic_spectrum(p,q)
            assert a==b,(p,q,a,b)
            assert min(b[:4])>0 and b[4]>0
            assert b[2]*b[3]>b[4]
            tested+=1
    for p in [40,100,500,1000]:
        assert 3.999 < kappa(p,p)<4.2, (p,kappa(p,p))
    for alpha in (0.1,.25,.4,.6,.75,.9):
        n=2000
        p=round(n*alpha);q=n-p
        assert kappa(p,q)>4.05,(p,q,kappa(p,q))
    assert kappa(5,5)>1
    print('VERIFY_OK independent_exact_moment_pairs=%d balanced_limit=%s' %(tested,kappa(1000,1000)))
