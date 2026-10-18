"""Exact verification of the four-prime digit-sandwich covering classification.
Requires Python 3 only. No probabilistic arithmetic or external dependencies.
"""
from math import prod
from collections import Counter

P = (3, 7, 11, 13)
L = prod(P)
D = (1, 3, 7, 9)
CASES = tuple((d, m) for d in D for m in range(1, 7))
EXPECTED = {
    0: tuple(range(0, L, 11)),
    1: (2499,),
    2: tuple(range(0, L, 11)),
    3: (231, 420, 759),
    4: tuple(range(0, L, 11)),
    5: (651,),
}

# First method: literal test of every complete residue, with 24 conditions.
def direct(t):
    ans = []
    T = t if t > 0 else 6
    for r in range(L):
        ok = True
        for d, m in CASES:
            R = (10**m - 1) // 9
            value = d * R * 10**(T+m) + r * 10**m + d * R
            if not any(value % p == 0 for p in P):
                ok = False
        if ok:
            ans.append(r)
    return tuple(ans)

# Second method: independent CRT, using 24-bit masks of prime coverage.
# The t-dependent powers are taken modulo p, and repunits are generated
# recursively in residues; no large decimal concatenation is constructed.
def masks_for_prime(p, t):
    result = {}
    for r in range(p):
        covered = 0
        for bit, (d, m) in enumerate(CASES):
            rep = 0
            for _ in range(m):
                rep = (10*rep + 1) % p
            z = (d*rep*pow(10,t+m,p) + r*pow(10,m,p) + d*rep) % p
            if z == 0:
                covered |= 1 << bit
        result[r] = covered
    return result

def crt_classification(t):
    masks = {p: masks_for_prime(p, t) for p in P}
    full = (1 << len(CASES)) - 1
    return tuple(r for r in range(L) if
                 (masks[3][r%3] | masks[7][r%7] |
                  masks[11][r%11] | masks[13][r%13]) == full)

def verify_irredundant():
    # Each of the four primes has one essential witness for center 231.
    witness = {}
    for p in P:
        for d, m in CASES:
            R = (10**m-1)//9
            value = d*R*10**(3+m) + 231*10**m + d*R
            if value%p==0 and all(value%q for q in P if q!=p):
                witness[p]=(d,m)
                break
        assert p in witness, ('prime not essential',p)
    return witness

def main():
    assert L == 3003
    for t in range(6):
        a=direct(t)
        b=crt_classification(t)
        expected=EXPECTED[t]
        assert a==b==expected, (t,a,b,expected)
        print('t mod 6:',t,'qualifying residues:',len(a),'non-11:',tuple(x for x in a if x%11))
    witnesses=verify_irredundant()
    print('irredundance witnesses for n=231:',witnesses)
    assert {x for t in (1,3,5) for x in EXPECTED[t] if x%11} == {2499,420,651}
    print('verified all',6*3003*len(CASES),'direct residue-case checks and CRT-mask cross-checks')

if __name__=='__main__':
    main()
