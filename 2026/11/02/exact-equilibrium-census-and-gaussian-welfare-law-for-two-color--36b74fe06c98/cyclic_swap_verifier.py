"""Independent exact arithmetic checks for the cyclic homophilic swap game.

Run: python3 cyclic_swap_verifier.py
The exhaustive step checks every binary vertex coloring through n=14.
The transfer-matrix checks are exact integer arithmetic.
"""
from itertools import product
from math import comb


def is_equilibrium(word):
    n = len(word)
    for i in range(n):
        ni = ((i - 1) % n, (i + 1) % n)
        old_i = sum(word[k] == word[i] for k in ni)
        for j in range(i + 1, n):
            if word[i] == word[j]:
                continue
            nj = ((j - 1) % n, (j + 1) % n)
            old_j = sum(word[k] == word[j] for k in nj)
            swapped = list(word)
            swapped[i], swapped[j] = swapped[j], swapped[i]
            new_i = sum(swapped[k] == word[i] for k in nj)
            new_j = sum(swapped[k] == word[j] for k in ni)
            if new_i > old_i and new_j > old_j:
                return False
    return True


def expected_structure(word):
    n = len(word)
    cuts = sum(word[i] != word[(i+1) % n] for i in range(n))
    if cuts <= 2:
        return True
    return all(not (word[(i-1) % n] == word[(i+1) % n] != word[i])
               for i in range(n))


def exact_fixed_count(n, a):
    if a == 0 or a == n:
        return 1
    b = n-a
    count = n
    for r in range(2, min(a//2, b//2)+1):
        contribution_numerator = n*comb(a-r-1, r-1)*comb(b-r-1, r-1)
        assert contribution_numerator % r == 0
        count += contribution_numerator // r
    return count


def matrix_polynomial(n):
    pairs = [(0,0),(0,1),(1,0),(1,1)]
    # The coefficient dictionary for each entry of T(z)^n.
    T = [[{} for _ in pairs] for _ in pairs]
    for i, (a,b) in enumerate(pairs):
        for j, (c,d) in enumerate(pairs):
            if b == c and not (a == d and a != b):
                T[i][j] = {int(c != d): 1}
    U = [[{0:int(i==j)} if i==j else {} for j in range(4)] for i in range(4)]
    for _ in range(n):
        V = [[{} for _ in range(4)] for _ in range(4)]
        for i in range(4):
            for k in range(4):
                for j in range(4):
                    for p, u in U[i][k].items():
                        for q, v in T[k][j].items():
                            V[i][j][p+q] = V[i][j].get(p+q,0)+u*v
        U = V
    out = {}
    for i in range(4):
        for p,v in U[i][i].items():
            out[p] = out.get(p,0)+v
    out[2] = out.get(2,0)+2*n
    return out


def lucas(n):
    p,q=2,1
    for _ in range(n):p,q=q,p+q
    return p


def sixth_period(n):
    p,q=2,1
    for _ in range(n):p,q=q,q-p
    return p


def run():
    exhaustively_checked=0
    for n in range(3,15):
        by_a=[0]*(n+1)
        by_w={}
        for word in product((0,1), repeat=n):
            observed=is_equilibrium(word)
            assert observed == expected_structure(word), (n,word)
            exhaustively_checked+=1
            if observed:
                by_a[sum(word)]+=1
                cuts=sum(word[i]!=word[(i+1)%n] for i in range(n))
                by_w[cuts] = by_w.get(cuts,0)+1
        for a,observed in enumerate(by_a):
            assert observed == exact_fixed_count(n,a), (n,a,observed)
        assert by_w == matrix_polynomial(n), (n, by_w, matrix_polynomial(n))
    for n in range(3,34):
        P=matrix_polynomial(n)
        assert sum(P.values()) == lucas(n)+sixth_period(n)+2*n
        # Exact enumeration by the number of cyclic monochromatic runs.
        expected={0:2, 2:n*(n-1)}
        for r in range(2,n//4+1):
            x=sum(n*comb(a-r-1,r-1)*comb(n-a-r-1,r-1)//r
                  for a in range(2*r,n-2*r+1))
            expected[2*r]=x
        assert {k:v for k,v in P.items() if v} == {k:v for k,v in expected.items() if v}, (n,P,expected)
    print('PASS: exhaustive direct utility checks of',exhaustively_checked,
          'colorings (n=3..14), 12 fixed-composition layers, and 31 exact transfer-matrix comparisons.')

if __name__ == '__main__':
    run()
