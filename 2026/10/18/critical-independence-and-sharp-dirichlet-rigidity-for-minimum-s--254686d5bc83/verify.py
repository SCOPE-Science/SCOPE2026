"""Deterministic checks of uniform-simplex threshold and Dirichlet sensitivity identities."""
from fractions import Fraction as F
from math import comb
from scipy.integrate import quad

def exact_uniform_cov(m,t):
    t=F(t)
    return ((1-m*t)*(1-t)**(m-1)-max(F(0),1-m*t)**m)/F(m*(m-1))

def exact_m3_alpha2_exceedance(u):
    """Conditional E[N_3(1/3)|min=u] for Dirichlet(2,2,2)."""
    u=F(u); s=1-3*u
    den=u*(u+s)+s*s/F(6)
    num=u*(u+s)/F(3)+s*s*F(13,162)
    return F(1)+num/den

def beta_integral_cov(k):
    """Independent exact-rational integration for Cov(Q, N(1/(k+1)))."""
    t=F(1,k+1)
    # Integrate (k-1)*(y^2+2*(1-y)^2/k - 2/(k+1))*(1-y)^(k-2)
    # expanded using binomial powers y^j, integral t..1 y^q dy.
    poly=[F(0)]*(k+1)
    for j in range(k-1):
        b=F(k-1)*comb(k-2,j)*((-1)**j)
        poly[j]+=b*F(2,k)
        poly[j+1]+=b*F(-4,k)
        poly[j+2]+=b*(1+F(2,k))
        poly[j]+=b*F(-2,k+1)
    integral=sum(coef*(1-t**(i+1))/F(i+1) for i,coef in enumerate(poly))
    return k*integral

def verify():
    checks=0
    # Threshold sign crossing and exact zero, all exact rationals.
    for m in range(3,60):
        for t in [F(1,3*m),F(1,m),F(2,m+1),F(9,10)]:
            v=exact_uniform_cov(m,t)
            if t<F(1,m): assert v>0
            elif t==F(1,m): assert v==0
            else: assert v<0
            checks+=1
    # Analytically integrated Dirichlet uniform Q,N covariance.
    for k in range(2,22):
        cv=beta_integral_cov(k)
        expected=-F(k-1)*F(k**k,(k+1)**(k+2))
        assert cv==expected,(k,cv,expected)
        checks+=1
    # For alpha=2,m=3 exact conditional values and local limit.
    for h in [F(1,1000),F(1,10000),F(1,100000),F(1,1000000)]:
        val=exact_m3_alpha2_exceedance(F(1,3)-h)
        ratio=(val-F(4,3))/h**2
        assert abs(ratio-F(2))<F(100)*h
        checks+=1
    # Numerical integration for non-integral alpha supports expansion.
    for alpha in [0.5,2.,3.]:
        for h in [0.0001,0.0002,0.0005]:
            u=1/3-h; s=1-3*u
            f=lambda y: ((u+s*y)*(u+s*(1-y)))**(alpha-1)
            mean=1+quad(f,1/3,2/3,epsabs=1e-13)[0]/quad(f,0,1,epsabs=1e-13)[0]
            ratio=(mean-4/3)/h**2
            assert abs(ratio-2*(alpha-1))<80*h,(alpha,h,ratio)
            checks+=1
    print('PASS',checks,'exact-rational / independent-integration / expansion checks')

if __name__=='__main__': verify()
