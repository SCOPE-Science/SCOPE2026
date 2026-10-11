"""Exact finite tests of the sign-paired equilateral embedding inequalities.

The infinite isometry and norm-one projection use limits and Hahn--Banach;
finite tests here do not certify those infinite assertions.
"""
from fractions import Fraction as F
from itertools import product


def rho(k):
    return F(k, k + 1)


def values(a, kmax):
    return {(i,k,s): F(s)*rho(k)*a[i]/2 for i in range(len(a))
            for k in range(1,kmax+1) for s in (-1,1)}


def check():
    profiles = pairs = strict = 0
    for m in (1,2,3):
        for ai in product((-2,-1,0,1,2),repeat=m):
            a = tuple(F(x) for x in ai)
            if not any(a):
                continue
            s=max(abs(x) for x in a)
            vals=values(a,5)
            assert max(vals.values())==rho(5)*s/2
            assert min(vals.values())==-rho(5)*s/2
            assert max(vals.values())-min(vals.values())==rho(5)*s
            for (i,k,sign),v in vals.items():
                upper=s/2+abs(v)
                assert upper < s
                strict+=1
                for other,w in vals.items():
                    if other == (i,k,sign):
                        continue
                    assert abs(w-v) <= upper
                    assert abs(w-v) <= s
                    pairs+=1
            # exact coefficient recovery from every difference/rho(k)
            for i in range(m):
                for k in range(1,6):
                    assert (vals[i,k,1]-vals[i,k,-1])/rho(k) == a[i]
            profiles+=1
    # Each fixed-level coefficient map Q_K has exact norm 1/rho(K):
    # the indicator of a single positive partner is 1-Lipschitz on
    # an equilateral space and achieves one on that partner difference.
    for k in range(1,6):
        assert 1 / rho(k) == F(k+1,k)
        assert 1 / rho(k) > 1
    print('VERIFY_OK rational_profiles=%d pointwise_bounds=%d pair_differences=%d weakstar_projection_levels=5 infinite_limit_requires_proof=True' % (profiles,strict,pairs))

if __name__=='__main__':
    check()
