#!/usr/bin/env python3
"""Exact finite-ring tests for the iterated quadratic value-set theorem.

Run: python3 verify_dickson_2adic_images.py
Only Python's standard library is required.
"""

def step(x, modulus):
    return (x*x-2) % modulus


def iterate(x, r, modulus):
    for _ in range(r):
        x = step(x, modulus)
    return x


def residue_ball(center, exponent, k):
    modulus=1 << k
    if k <= exponent:
        return {center % modulus}
    return {(center + (j << exponent)) % modulus
            for j in range(1 << (k-exponent))}


def predicted_image(r, k):
    modulus=1 << k
    c=iterate(194, r-2, modulus)
    return (residue_ball(-1, r+2, k)
            | residue_ball(2, 2*r+3, k)
            | residue_ball(c, 2*r+5, k))


def predicted_count(r, k):
    a=1 << max(0,k-r-2)
    if k <= 2*r+2:
        return a+1
    return a+(1 << max(0,k-2*r-3))+(1 << max(0,k-2*r-5))


def nu2(n):
    if n == 0:
        raise ValueError('zero has no finite 2-adic valuation')
    return (abs(n) & -abs(n)).bit_length()-1


def main():
    tests=0
    for r in range(2, 10):
        c=194
        for _ in range(r-2):
            c=c*c-2
        assert nu2(c-2)==2*r+2,(r,'center gap')
        assert c%8==2
        for k in range(1, 17):
            modulus=1 << k
            observed={iterate(x,r,modulus) for x in range(modulus)}
            exact=predicted_image(r,k)
            assert observed == exact,(r,k,len(observed),len(exact))
            assert len(observed)==predicted_count(r,k),(r,k,'count')
            tests+=1
    # Test all residue classes at deeper precisions for the first four iterates.
    deep=0
    for r in range(2, 6):
        for k in (17,18):
            modulus=1 << k
            observed={iterate(x,r,modulus) for x in range(modulus)}
            assert observed == predicted_image(r,k)
            assert len(observed)==predicted_count(r,k)
            deep+=1
    for r in range(2, 15):
        k=2*r+5
        count=predicted_count(r,k)
        density_num=(1 << (r+3))+5
        assert count == density_num
        assert count/(1 << k)==2**(-r-2)+2**(-2*r-3)+2**(-2*r-5)
    print('VERIFY_OK grid_cases=',tests,'deep_cases=',deep,
          'maximum_r=14','maximum_direct_modulus=262144',
          'image_sets_exact=True','density_arithmetic=True')


if __name__=='__main__':
    main()
