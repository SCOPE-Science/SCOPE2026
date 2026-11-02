"""Independent finite checks of a two-adic valuation theorem for Stirling differences.

Run: python3 verify.py
Pure Python standard library; modular arithmetic is exact.
"""
from math import comb, factorial

K = 15
FAC = factorial(K)
VF = sum(K // 2**i for i in range(1, 5))
assert VF == 11


def valuation(z):
    assert z != 0
    return (z & -z).bit_length() - 1


def difference_mod(n, a, b, digits):
    """Return 15! times the Stirling difference modulo 2**digits."""
    modulus = 1 << digits
    delta = sum((-1)**(K-j) * comb(K,j)
                * (pow(j, a*(1<<n), modulus)
                   - pow(j, b*(1<<n), modulus))
                for j in range(1, K+1))
    return delta % modulus


def direct_stirling_mod(M, k, modulus):
    """Independent recurrence, not using the exponential formula."""
    v = [0]*(k+1)
    v[0] = 1
    for i in range(1, M+1):
        for j in range(min(i,k),0,-1):
            v[j] = (v[j-1]+j*v[j])%modulus
        v[0]=0
    return v[k]


def predict(n,a,b):
    if a < b:
        a,b=b,a
    if a == b: return None
    r=valuation(a-b)
    A=n+r+1
    B=b*(1<<n)-5
    if A<B: return A
    if B<A: return B
    return ('at_least', A+1)


def check(n,a,b):
    expected=predict(n,a,b)
    threshold=expected[1] if isinstance(expected,tuple) else expected
    bits=threshold+VF+24
    num=difference_mod(n,a,b,bits)
    got=(valuation(num)-VF) if num else None
    if isinstance(expected,tuple):
        assert got is None or got>=expected[1], (n,a,b,got,expected)
    else:
        assert got==expected, (n,a,b,got,expected)
    return got


def main():
    # The finite coefficient certificate is independently recomputed.
    mod=1<<13; n=10
    terms=[]
    for j in range(1,16,2):
        quot=(pow(j,1<<n,1<<(n+13))-1)%(1<<(n+13))
        assert quot%(1<<n)==0
        terms.append(comb(15,j)*(quot//(1<<n)))
    assert sum(terms)%mod==4096
    assert sum(comb(15,j) for j in (2,6,10,14))==8128

    cases=0
    for n in (10,11,12,13):
        for b in (1,2,3,5):
            for d in (1,2,3,4,7,16,29,1<<20,3<<40):
                check(n,b+d,b)
                cases+=1
    # Probe the saturation boundary with enormous but succinct exponents.
    for n,b in ((10,1),(10,2),(11,1)):
        r=b*(1<<n)-n-6
        for h in (-3,-2,-1,0,1,2,3):
            d=1<<(r+h)
            check(n,b+d,b)
            cases+=1

    # Independent recurrence (different algorithm) on small finite indices.
    recurrence_pairs=0
    n=10
    for a,b in ((2,1),(3,1),(5,2)):
        mod=1<<36
        left=direct_stirling_mod(a*(1<<n),K,mod)
        right=direct_stirling_mod(b*(1<<n),K,mod)
        num=difference_mod(n,a,b,36+VF)
        oddfac=FAC>>VF
        # (num / 2**VF) / oddfac modulo 2**36.
        quotient=((num>>VF)*pow(oddfac,-1,mod))%mod
        assert (left-right)%mod==quotient
        recurrence_pairs+=1
    print('VERIFY_OK coefficient_residue=4096 even_binomial_sum=8128 cases=',cases,
          'independent_recurrence_pairs=',recurrence_pairs)

if __name__=='__main__':
    main()
