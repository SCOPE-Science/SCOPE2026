"""Reproducible finite checks for reachability-based approval-profile enumeration.

An approval profile records the positive-length reachability sets of a mapping.
These tests check small labeled sets and exact combinatorial counting recurrences.
They do not replace the general counting and singularity arguments.
"""
from collections import Counter
from itertools import product
from math import comb, factorial, exp, e


def closure(f):
    """Positive-length reachability profile for a total mapping on 0..n-1."""
    n = len(f)
    ans = []
    for i in range(n):
        j = f[i]
        seen = set()
        while j not in seen:
            seen.add(j)
            j = f[j]
        ans.append(tuple(sorted(seen)))
    return tuple(ans)


def predicted_fiber_size(f):
    """Product of cyclic orderings and choices for tree roots entering cycles."""
    n = len(f)
    cyclic_parts = []
    visited = set()
    for v in range(n):
        if v in visited:
            continue
        local = {}
        path = []
        q = v
        while q not in local and q not in visited:
            local[q] = len(path)
            path.append(q)
            q = f[q]
        if q in local:
            cyclic_parts.append(set(path[local[q]:]))
        visited.update(path)
    value = 1
    for cyc in cyclic_parts:
        s = len(cyc)
        b = sum(i not in cyc and f[i] in cyc for i in range(n))
        value *= factorial(s - 1) * (s ** b)
    return value


def connected_count(n):
    # Cayley rooted trees with n-s+1 vertices and prescribed root.
    return sum(comb(n, s) * ((n - s + 1) ** (n - s - 1) if n > s else 1)
               for s in range(1, n + 1))


def exact_counts(N):
    c = [0] + [connected_count(n) for n in range(1, N+1)]
    p = [1]
    for n in range(1, N+1):
        p.append(sum(comb(n - 1, k - 1) * c[k] * p[n - k]
                     for k in range(1, n+1)))
    return c, p


def finite_checks():
    connected, profile_counts = exact_counts(6)
    for n in range(1, 7):
        fibers = Counter()
        reference = {}
        for f in product(range(n), repeat=n):
            key = closure(f)
            fibers[key] += 1
            reference[key] = f
        assert len(fibers) == profile_counts[n], (n,len(fibers),profile_counts[n])
        counted_connected = 0
        for key, count in fibers.items():
            f = reference[key]
            assert count == predicted_fiber_size(f), (n,key,count)
            # Weak components of mapping correspond to distinct terminal cycles.
            cycle_representatives = set()
            for i in range(n):
                j = i
                while j not in key[j]:
                    j = f[j]
                cycle_representatives.add(tuple(sorted(key[j])))
            if len(cycle_representatives) == 1:
                counted_connected += 1
        assert counted_connected == connected[n], (n,counted_connected,connected[n])
        print(f'n={n}: distinct={len(fibers)}, connected={counted_connected}, functions={n**n}, fiber_formula=passed')


def asymptotic_checks():
    a = e * (exp(1 / e) - 1)
    c, p = exact_counts(150)
    print('a=',format(a,'.15f'),'a*exp(a)=',format(a * exp(a),'.15f'))
    for n in (20,50,100,150):
        ratio = (p[n] * n) / (n**n)
        print(f'n={n}: scaled_profile_count={ratio:.12f}, connected_fraction={c[n]/p[n]:.12f}')
    # Convergence is slow but the scaled quantities move toward their derived values.
    assert p[150] * 150 / (150**150) < a * exp(a)
    assert c[150] / p[150] > exp(-a)
    print('asymptotic finite sanity checks=passed')


if __name__ == '__main__':
    finite_checks()
    asymptotic_checks()
