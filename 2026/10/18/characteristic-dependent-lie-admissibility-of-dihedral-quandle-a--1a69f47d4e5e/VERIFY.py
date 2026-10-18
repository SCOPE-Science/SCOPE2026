"""Exact integer Jacobi coefficient checker for dihedral quandle algebras.
No floating-point arithmetic, external packages or probabilistic steps.
"""
from collections import defaultdict
from math import gcd


def bracket(i, j, n):
    out = defaultdict(int)
    out[(2*j-i) % n] += 1
    out[(2*i-j) % n] -= 1
    return dict(out)


def jacobi(i, j, k, n):
    total = defaultdict(int)
    for x, y, z in ((i, j, k), (j, k, i), (k, i, j)):
        for t, ct in bracket(y, z, n).items():
            for u, cu in bracket(x, t, n).items():
                total[u] += ct * cu
    return {u: c for u, c in total.items() if c}


def obstruction_gcd(n):
    answer = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for coefficient in jacobi(i, j, k, n).values():
                    answer = gcd(answer, abs(coefficient))
    return answer


def run():
    expected = {1:0, 2:0, 3:0, 4:2, 5:1, 6:1, 7:1,
                8:1, 9:3, 10:1, 11:1, 12:1}
    for n, target in expected.items():
        actual = obstruction_gcd(n)
        assert actual == target, (n, actual, target)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    J = jacobi(i, j, k, n)
                    assert all(c % target == 0 for c in J.values()) if target > 1 else True
    # The universal witness, with no coinciding basis labels for n >= 13.
    integral_witness = {-5:1,-4:-1,-3:-1,-2:1,4:-1,5:1,6:1,7:-1}
    for n in range(13, 101):
        residues = {a % n for a in integral_witness}
        assert len(residues) == 8
        assert jacobi(0,1,2,n) == {a % n:c for a,c in integral_witness.items()}
    assert jacobi(0,1,2,4) == {2:2,0:-2}
    # Directly exhibit a nonzero bracket in the char-3 order-nine exception.
    assert bracket(0,1,9) == {2:1,8:-1}
    print('VERIFY_OK: all n=1..12, all ordered basis triples; n=13..100 witness checks')

if __name__ == '__main__':
    run()
