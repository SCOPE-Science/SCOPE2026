"""Finite exact checks for shuffled tent-map mixing enumeration.

Uses only Python standard library. Proof of all-grid formulas is in RESULT.md.
"""
from itertools import permutations
from math import comb, factorial, gcd


def transitive_with_reflection(p):
    n = len(p)
    todo, seen = [0], {0}
    while todo:
        u = todo.pop()
        for v in (p[u], n - 1 - u):
            if v not in seen:
                seen.add(v)
                todo.append(v)
    return len(seen) == n


def primitive_graph(out):
    n = len(out)
    reverse = [[] for _ in range(n)]
    for i in range(n):
        for j in out[i]:
            reverse[j].append(i)

    def reach(edges):
        seen, todo = {0}, [0]
        while todo:
            for j in edges[todo.pop()]:
                if j not in seen:
                    seen.add(j)
                    todo.append(j)
        return len(seen) == n

    if not reach(out) or not reach(reverse):
        return False
    dist, queue = [-1] * n, [0]
    dist[0] = 0
    for i in queue:
        for j in out[i]:
            if dist[j] == -1:
                dist[j] = dist[i] + 1
                queue.append(j)
    period = 0
    for i in range(n):
        for j in out[i]:
            period = gcd(period, abs(dist[i] + 1 - dist[j]))
    return period == 1


def tent_fine_graph(n, sigma):
    # Independent length-1/(2n) Markov graph, computed from tent images.
    out = []
    for fine in range(2*n):
        coarse_image = fine if fine < n else (2*n - 1 - fine)
        j = sigma[coarse_image]
        out.append((2*j, 2*j+1))
    return out


def counts(kmax):
    t = [1]
    for k in range(1, kmax+1):
        t.append(factorial(2*k+1) - sum(
            comb(k, j)*t[j]*factorial(2*(k-j))
            for j in range(k)))
    return t


def main():
    t = counts(70)
    expected = {3: 4, 5: 80, 7: 3552}
    sample_total = 0
    for n, want in expected.items():
        n_good = 0
        for p in permutations(range(n)):
            k = (n - 1)//2
            E = tuple(2*i if i < k else (2*k if i == k else 2*(2*k-i)+1) for i in range(n))
            U = tuple(p[E[i]] for i in range(n))
            group = transitive_with_reflection(U)
            fine = primitive_graph(tent_fine_graph(n, p))
            assert group == fine, (n, p)
            n_good += int(fine)
            sample_total += 1
        assert n_good == want == t[(n-1)//2]
    assert t[:5] == [1, 4, 80, 3552, 271104], t[:5]
    for k in range(1, 71):
        n = 2*k+1
        assert 0 < t[k] <= factorial(n)
        assert factorial(n) == sum(comb(k, j)*t[j]*factorial(2*(k-j))
                                    for j in range(k+1))
    # The following checks are finite tests of the asymptotic formula, not proofs.
    from fractions import Fraction
    e = Fraction(factorial(141)-t[70], factorial(141))
    lead = Fraction(2, 141)+Fraction(3, 141**2)+Fraction(22, 141**3)
    assert abs(float(e-lead)) < 2e-6
    print(f'VERIFY_OK {sample_total} full fine-graph comparisons; '
          f'70 exact recurrence levels; N=3,5,7 counts {tuple(expected.values())}')

if __name__ == '__main__':
    main()
