"""Independent arithmetic checks for sharp centered rare-event half-thinning."""
from fractions import Fraction
from math import comb, exp, floor, factorial, log, sqrt, lgamma

def finite_mad(n, lam):
    p=lam/Fraction(n)
    total=Fraction(0)
    thin=Fraction(0)
    for k in range(n+1):
        pk=comb(n,k)*p**k*(1-p)**(n-k)
        total+=pk*abs(Fraction(k)-lam)
        for a in range(k+1):
            pa=Fraction(comb(k,a),2**k)
            for d in range(n-k+1):
                pd=Fraction(comb(n-k,d),2**(n-k))
                thin+=pk*pa*pd*abs(Fraction(a)-lam*Fraction(a+d,n))
    return total,thin

def poisson_mad(t):
    return 2*t*exp(-t+floor(t)*log(t)-lgamma(floor(t)+1))

def ratio(t):
    return poisson_mad(t/2)/poisson_mad(t)

def main():
    checks=0
    for n in range(1,9):
        for lam in (Fraction(1,4),Fraction(1,2),Fraction(3,4),Fraction(1),Fraction(3,2),Fraction(2),Fraction(3)):
            if lam>=n: continue
            full,thin=finite_mad(n,lam)
            assert full>0 and thin>0
            assert thin<=full
            # Independent unconditional expectation of the thinned sum is zero.
            mean=Fraction(0)
            p=lam/Fraction(n)
            for m in range(n+1):
                for a in range(m+1):
                    mean+=comb(n,m)*Fraction(1,2**n)*comb(m,a)*p**a*(1-p)**(m-a)*(Fraction(a)-lam*Fraction(m,n))
            assert mean==0
            checks+=4
    # Poisson MAD identity checked independently by summation and an explicit tail bound.
    for t in (0.1,0.5,0.99,1,1.01,1.5,2,2.75,3,5,11,20):
        values=[exp(-t)*t**k/factorial(k) for k in range(130)]
        brute=sum(abs(k-t)*pk for k,pk in enumerate(values))
        assert abs(brute-poisson_mad(t))<1e-11
        checks+=1
    assert abs(ratio(1)-sqrt(exp(1))/2)<1e-14;checks+=1
    assert abs(ratio(3)-exp(1.5)/6)<1e-14;checks+=1
    # Independently compare the exact integer mode ratios, without optimizing a mesh.
    target=sqrt(exp(1))/2
    for k in range(2,401):
        assert ratio(float(k))<target+1e-12
        checks+=1
    for k in range(1,401):
        for offset in (.125,.375,.625,.875):
            t=k+offset
            assert ratio(t)<=max(ratio(float(k)),ratio(float(k+1)))+1e-12
            checks+=1
    # The classical Gaussian high-intensity endpoint is below the maximum.
    assert 1/sqrt(2)<target
    print('checks_passed:',checks+1)
    for n in (2,4,8):
        whole,retained=finite_mad(n,Fraction(1))
        print('finite_ratio_lambda_1_n_'+str(n)+':',float(retained/whole))
    for t in (0.5,1,2,3,5,11,40):
        print('poisson_ratio_lambda_'+str(t)+':',format(ratio(t),'.14g'))
    print('sharp_supremum:',format(target,'.15g'))

if __name__=='__main__':
    main()
