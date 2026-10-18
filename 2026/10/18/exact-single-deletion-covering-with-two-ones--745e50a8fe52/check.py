"""Exact arithmetic checks for a constant-weight-two deletion covering theorem.

No external packages. The proof is symbolic; this program checks independent
instances and the exact rational dual inequalities.
"""
from fractions import Fraction as F
from itertools import combinations


def qweight(z):
    t = F(-1, 2)
    plus = lambda k: max(F(0), t ** k)
    q0 = F(1, 3) + sum((t ** k for k in z), F(0))/6
    penalty = sum((sum((plus(z[j]) for j in range(3) if i != j), F(0)) for i in range(3) if z[i] == 0), F(0))/12
    return q0 - penalty


def check_dual(n):
    D = n - 2
    lower = [(a, b, D - 1 - a - b) for a in range(D) for b in range(D - a)]
    upper = [(a, b, D - a - b) for a in range(D + 1) for b in range(D - a + 1)]
    assert all(qweight(y) >= 0 for y in lower)
    assert all(sum((qweight(tuple(x[j] - (i == j) for j in range(3)))
                    for i in range(3) if x[i]), F(0)) <= 1 for x in upper)
    total = sum((qweight(y) for y in lower), F(0))
    bound = n * (n-1) // 6
    assert total > bound - 1, (n, total, bound)
    return total


def check_cover(n):
    pairs = list(combinations(range(n), 2))
    output = set()
    for i, j in pairs:
        w = ['0']*n
        w[i] = w[j] = '1'
        for k in range(n): output.add(''.join(w[:k] + w[k+1:]))
    assert len(output) == n*(n-1)//2
    classes = [[(i,j) for i,j in pairs if (i+j)%3 == r] for r in range(3)]
    size = n*(n-1)//6
    assert min(map(len, classes)) == size
    admissible = 0
    for C in classes:
        covered = set()
        for i,j in C:
            w=['0']*n
            w[i] = w[j] = '1'
            for k in range(n): covered.add(''.join(w[:k]+w[k+1:]))
        if len(C) == size and covered == output: admissible += 1
    assert admissible > 0
    return admissible


def main():
    for n in range(3, 61):
        z = check_dual(n)
        c = check_cover(n)
        if n <= 15 or n in [20,30,40,50,60]:
            print(f'n={n}, optimum={n*(n-1)//6}, covering_residue_classes={c}, dual={z.numerator}/{z.denominator}')
    print('PASS: exact rational dual and complete deletion balls for n=3..60')

if __name__ == '__main__':
    main()
