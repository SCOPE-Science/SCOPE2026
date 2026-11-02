"""Independent finite checks of arithmetic progressions under restricted rational approximation.
The infinite theorem follows from the separate proofs, not these checks.
"""
from math import gcd

obstructions = 0
for m in range(3, 25):
    for residue in range(1, m):
        for t in range(3, 25):
            p, q = t, m*t + (1 if residue > 1 else -1)
            assert gcd(p, q) == 1
            elements = [v for v in range(1, q) if v % m == residue]
            assert elements
            for v in elements:
                remainder = (v*p) % q
                assert m*min(remainder, q-remainder) >= q
                obstructions += 1

odd_inverse = 0
for q in range(3, 211):
    for p in range(1, q):
        if gcd(p, q) > 1:
            continue
        witnesses = [v for v in range(1, q, 2) if (v*p) % q in (1, q-1)]
        assert witnesses, (p,q)
        odd_inverse += 1

# Literal simple periodic counterexample, through every tested denominator.
for q in range(13, 104):
    for p in range(1, q):
        if gcd(p, q) > 1:
            continue
        v1 = [v for v in range(1,q) if v%4==1]
        v3 = [v for v in range(1,q) if v%4==3]
        if not (v1 and v3):continue
        d_odd = min(min((v*p)%q,q-(v*p)%q) for v in v1+v3)
        assert d_odd == 1, (p,q,d_odd)
print(f'VERIFY_OK obstructions={obstructions} odd_inverse_pairs={odd_inverse} odd_union=PASS finite_only=YES')
