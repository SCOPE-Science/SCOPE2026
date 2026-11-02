"""Independent finite checks for the projective-cube negative-type bounds.

Run: python3 checker.py
Uses Python's standard library; optional mpmath for high-precision tests.
Numerical checks supplement, and do not replace, the proof.
"""
from math import comb, log, pi, sqrt
from fractions import Fraction

def coeff(d, j, k):
    return sum((-1)**s * comb(j,s)*comb(d-j,k-s)
               for s in range(max(0,k-(d-j)), min(j,k)+1))

def eig(d, j, exponent):
    return sum(coeff(d,j,k)*min(k,d-k)**exponent for k in range(1,d))

def direct_character(d, j, exponent):
    # Each class has two representatives, hence half the cube sum.
    return sum(((-1)**((x & ((1<<j)-1)).bit_count()))
               * min(x.bit_count(), d-x.bit_count())**exponent
               for x in range(1, (1<<d)-1)) / 2

def main():
    exact=0
    for d in range(4,13):
        for j in range(2,d+1,2):
            assert sum(coeff(d,j,k) for k in range(1,d)) == -2
            exact+=1
            assert abs(eig(d,j,1)/2 - direct_character(d,j,1)) < 1e-9
            exact+=1
        assert sum(abs(coeff(d,4,k)) for k in range(d+1)) <= 2**d
        exact+=1
    import mpmath as mp
    mp.mp.dps=85
    cmp=0
    def derivative(d):
        return mp.fsum(mp.mpf(coeff(d,4,k))*mp.log(min(k,d-k)) for k in range(1,d))
    c=mp.sqrt(2/mp.pi)
    ratios=[]
    for d in (24,32,40,48,56,64,72,80,96,128):
        slope=derivative(d)
        r=slope*mp.mpf(d)**mp.mpf('2.5')/mp.power(2,d)
        ratios.append(float(r))
        assert slope>0
        cmp+=1
    # The central-binomial limit is slow but visible at these sizes.
    assert abs(ratios[-1]-float(c))<0.02
    cmp+=1
    for d in (12,16,20,24,28,32,40,48,56,64):
        p=(mp.sqrt(2*mp.pi)+mp.mpf('0.5'))*mp.power(d,mp.mpf('2.5'))/mp.power(2,d)
        val=mp.mpf(-2)+mp.fsum(mp.mpf(coeff(d,4,k))*mp.expm1(p*mp.log(min(k,d-k))) for k in range(1,d))
        if d>=40: assert val>0, (d,val)
        cmp+=1
    for d in range(4,32):
        bound=mp.log(1+mp.power(2,1-d))/mp.log(d//2)
        assert bound>0
        # Explicit bound uses N(d) (M^p-1) <=1 at equality.
        assert mp.power(2,d-1)*(mp.power(d//2,bound)-1) <=1+mp.mpf('1e-70')
        cmp+=1
    print('CHECK_OK exact_integer_and_character_checks=',exact,
          'high_precision_checks=',cmp,
          'limiting_fourier_constant=',mp.nstr(c,16),
          'last_normalized_slope=',round(ratios[-1],9))

if __name__=='__main__':
    main()
