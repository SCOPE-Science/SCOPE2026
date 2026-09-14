# Dependency-free certificate for the degree-12 Belyi passport triple.
# Checks cycle types, product identity, transitivity, genus; optionally (sympy) group order.
s0 = (0, 2, 1, 8, 4, 11, 3, 7, 9, 6, 10, 5)
s1 = (9, 0, 8, 2, 3, 4, 6, 5, 7, 1, 11, 10)
s2 = (1, 3, 9, 6, 5, 10, 0, 8, 4, 2, 11, 7)
n = 12


def comp(a, b):
    return tuple(a[b[i]] for i in range(n))


def ctype(p):
    vis = [False] * n
    out = []
    for i in range(n):
        if not vis[i]:
            j, ln = i, 0
            while not vis[j]:
                vis[j] = True
                j = p[j]
                ln += 1
            out.append(ln)
    return tuple(sorted(out, reverse=True))


def main():
    assert ctype(s0) == (4, 2, 2, 1, 1, 1, 1), ctype(s0)
    assert ctype(s1) == (6, 3, 2, 1), ctype(s1)
    assert ctype(s2) == (6, 4, 2), ctype(s2)
    assert comp(comp(s0, s1), s2) == tuple(range(n)), "product must be identity"
    invs = []
    for p in (s0, s1, s2):
        q = [0] * n
        for i, v in enumerate(p):
            q[v] = i
        invs.append(tuple(q))
    seen, stack = {0}, [0]
    while stack:
        i = stack.pop()
        for g in (s0, s1, s2, *invs):
            if g[i] not in seen:
                seen.add(g[i])
                stack.append(g[i])
    assert len(seen) == 12, seen
    assert sum(n - len(ctype(p)) for p in (s0, s1, s2)) == 2 * n - 2
    print("ALL EXACT CHECKS PASSED: types, product, transitivity, genus 0")
    try:
        from sympy.combinatorics import Permutation
        from sympy.combinatorics.perm_groups import PermutationGroup
        G = PermutationGroup([Permutation(list(s0)), Permutation(list(s1)), Permutation(list(s2))])
        assert G.order() == 479001600 and G.is_transitive()
        print("SYMPY CHECK PASSED: |H| = 479001600, transitive (H = S12 with primitivity)")
    except ImportError:
        print("(sympy not installed; group-order check skipped)")


if __name__ == "__main__":
    main()
