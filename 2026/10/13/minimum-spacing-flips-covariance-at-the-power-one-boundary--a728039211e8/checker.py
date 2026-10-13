from fractions import Fraction
from math import factorial, comb, sqrt

def ey(m):
    return Fraction(1,m*m)

def vary(m):
    return Fraction(m-1,m**4*(m+1))

def ep(m,q):
    return Fraction(factorial(m)*factorial(q),factorial(m+q-1))

def eyp(m,q):
    pref=Fraction(factorial(q)*factorial(m-1),factorial(m+q))
    return pref*sum((Fraction(1,m)**r for r in range(q+1)),Fraction(0))

def cov(m,q):
    return eyp(m,q)-ey(m)*ep(m,q)

def ep2(m,q):
    den=factorial(m+2*q-1)
    return (Fraction(m*factorial(m-1)*factorial(2*q),den)
            +Fraction(m*(m-1)*factorial(m-1)*factorial(q)**2,den))

def varp(m,q):
    return ep2(m,q)-ep(m,q)**2

def integrate_m2(q):
    # 2 int_0^(1/2) x [x^q+(1-x)^q] dx
    def ix(p): return Fraction(1,2**(p+1)*(p+1))
    s=ix(q+1)
    for j in range(q+1):
        s += comb(q,j)*((-1)**j)*ix(j+1)
    return 2*s

def integrate_m3(q):
    # 6 int_0^(1/3) {x^(q+1)(1-3x)+2x[(1-2x)^(q+1)-x^(q+1)]/(q+1)} dx
    def ix(p): return Fraction(1,3**(p+1)*(p+1))
    s=ix(q+1)-3*ix(q+2)
    t=Fraction(0)
    for j in range(q+2):
        t += comb(q+1,j)*((-2)**j)*ix(j+1)
    t -= ix(q+2)
    s += Fraction(2,q+1)*t
    return 6*s

def cond_greenwood(m,t):
    u=1-m*t
    # direct conditional expansion using E sum X_i^2 = 2/(m+1)
    return m*t*t+2*t*u+u*u*Fraction(2,m+1)

def closed_cond_greenwood(m,t):
    u=1-m*t
    return Fraction(1,m)+Fraction(m-1,m*(m+1))*u*u

def run():
    direct_checks=0
    for q in range(1,10):
        assert integrate_m2(q)==eyp(2,q)
        assert integrate_m3(q)==eyp(3,q)
        direct_checks += 2

    formula_checks=0
    sign_checks=0
    greenwood_checks=0
    variance_checks=0
    threshold_checks=0
    for m in range(2,501):
        for q in range(1,13):
            pref=Fraction(factorial(q)*factorial(m-1),factorial(m+q))
            bracket=sum((Fraction(1,m)**r for r in range(q+1)),Fraction(0))-1-Fraction(q,m)
            assert cov(m,q)==pref*bracket
            formula_checks += 1
            if q==1:
                assert cov(m,q)==0
            else:
                assert cov(m,q)<0
                assert varp(m,q)>0
                sign_checks += 1
                variance_checks += 1

        c2=Fraction(-2*(m-1),m**3*(m+1)*(m+2))
        assert cov(m,2)==c2
        vg=Fraction(4*(m-1),(m+1)**2*(m+2)*(m+3))
        assert varp(m,2)==vg
        rho2=Fraction((m+1)*(m+3),m*m*(m+2))
        assert cov(m,2)**2 == rho2*vary(m)*vg
        greenwood_checks += 3

        for num,den in [(0,1),(1,5),(1,3),(2,5),(3,5)]:
            # t=(num/den)/m, always below 1/m for listed fractions except zero
            t=Fraction(num,den*m)
            assert cond_greenwood(m,t)==closed_cond_greenwood(m,t)
            threshold_checks += 1

    # fixed-q asymptotic correlation constants: numerical checks at large m
    asymptotic_checks=0
    for q in range(2,8):
        V=factorial(2*q)-factorial(q)**2*(q*q+1)
        target=-factorial(q)*(q-1)/sqrt(V)
        for m in [10000,50000]:
            cc=float(cov(m,q))/sqrt(float(vary(m)*varp(m,q)))
            scaled=sqrt(m)*cc
            assert abs(scaled-target) < 0.02
            asymptotic_checks += 1

    print('VERIFY_OK')
    print(f'direct_simplex_checks={direct_checks}')
    print(f'integer_covariance_checks={formula_checks}')
    print(f'negative_sign_checks={sign_checks}')
    print(f'variance_checks={variance_checks}')
    print(f'greenwood_checks={greenwood_checks}')
    print(f'threshold_checks={threshold_checks}')
    print(f'asymptotic_checks={asymptotic_checks}')
    print('max_exact_m=500')

if __name__=='__main__':
    run()
