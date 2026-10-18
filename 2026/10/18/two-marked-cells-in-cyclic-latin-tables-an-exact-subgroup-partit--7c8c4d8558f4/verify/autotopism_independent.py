"""Brute-force row-column-symbol autotopisms for small cyclic addition squares."""
from itertools import permutations
from math import gcd


def direct_autotopisms(n):
    pp = list(permutations(range(n)))
    result = []
    for row_perm in pp:
        for col_perm in pp:
            sym_perm = [(row_perm[z] + col_perm[0]) % n for z in range(n)]
            if all((row_perm[i] + col_perm[j]) % n == sym_perm[(i+j) % n]
                   for i in range(n) for j in range(n)):
                result.append((row_perm, col_perm, tuple(sym_perm)))
    return result


def main():
    checked = 0
    for n in range(2, 6):
        actual = set(direct_autotopisms(n))
        predicted = set()
        for u in range(1, n):
            if gcd(u, n) != 1:
                continue
            for a in range(n):
                for b in range(n):
                    rp = tuple((u*i+a) % n for i in range(n))
                    cp = tuple((u*j+b) % n for j in range(n))
                    sp = tuple((u*z+a+b) % n for z in range(n))
                    predicted.add((rp, cp, sp))
        assert actual == predicted, n
        for g in range(1, n):
            fixed = [aut for aut in actual if aut[0][0]==0 and aut[1][0]==0 and aut[1][g]==g]
            expect = [u for u in range(1,n) if gcd(u,n)==1 and u*g%n==g]
            assert len(fixed)==len(expect), (n,g)
            checked += 1
        print(f"n={n}: all {len(actual)} autotopisms equal affine diagonal-unit formula")
    print(f"PASS: complete brute-force autotopisms for n=2,...,5; {checked} double-marker stabilizer checks")

if __name__ == '__main__':
    main()
