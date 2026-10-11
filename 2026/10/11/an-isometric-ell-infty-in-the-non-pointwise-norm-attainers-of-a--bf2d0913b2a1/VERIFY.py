"""Exact finite sanity checks for the strict local-slope construction.

The infinite theorem is proved analytically, not by enumeration.
"""
from fractions import Fraction
from itertools import product


def check(alpha, nmax, a):
    assert all(alpha[i] > 0 for i in range(nmax))
    assert all(alpha[i] >= alpha[i+1] for i in range(nmax-1))
    assert alpha[0] <= Fraction(1, 3)
    r = [1-2*t for t in alpha]
    f = []
    for n in range(1, nmax+1):
        k = (n & -n).bit_length()-1
        q = ((n >> k)-1)//2
        f.append((-1)**q*r[n-1]*a[k%len(a)])
    b = max(map(abs,a))
    pair_count = 0
    for i in range(nmax):
        for j in range(i+1,nmax):
            d = 2-alpha[i]-2*alpha[j]
            assert 1 <= d < 2
            assert abs(f[i]-f[j]) <= b*d
            assert d-(r[i]+r[j]) == alpha[i]
            pair_count += 1
    for i in range(nmax):
        vals=[]
        for j in range(nmax):
            if i==j: continue
            u,v=sorted((i,j))
            d=2-alpha[u]-2*alpha[v]
            vals.append(abs(f[i]-f[j])/d)
        assert max(vals) <= b*(1-alpha[i]/2)
    return pair_count


def main():
    cases=0
    pairs=0
    N=48
    for alpha in ([Fraction(1,3**i) for i in range(1,N+1)],
                  [Fraction(1,i+2) for i in range(1,N+1)],
                  [Fraction(1,3*i) for i in range(1,N+1)]):
        for coeffs in product((-2, 0, 1, 3), repeat=3):
            pairs+=check(alpha,N,coeffs)
            cases+=1
    print(f'VERIFY_OK exact_rational_cases={cases} pair_tests={pairs} local_bounds={cases*N} theorem_requires_infinite_proof=True')


if __name__ == '__main__':
    main()
