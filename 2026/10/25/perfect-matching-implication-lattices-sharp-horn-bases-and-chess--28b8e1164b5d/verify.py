"""Standalone finite checks for perfect-matching concept closure lattices.

All calculations reconstruct the incidence context; no result tables are imported.
"""
from itertools import permutations, combinations
from math import comb, factorial


def matching_tuple_edges(n):
    return tuple((r, c) for r in range(n) for c in range(n))


def concept_extents(n):
    all_edges = frozenset(matching_tuple_edges(n))
    perms = tuple(frozenset((r, p[r]) for r in range(n)) for p in permutations(range(n)))
    # Generate all extents as intersections of permutation attributes.  This
    # closure-saturation algorithm never assumes the asserted description.
    ext = {all_edges}
    todo = [all_edges]
    while todo:
        obj = todo.pop()
        for pm in perms:
            nxt = obj & pm
            if nxt not in ext:
                ext.add(nxt)
                todo.append(nxt)
    return all_edges, perms, ext


def rank_of(C, universe, n):
    if C == universe:
        return n
    if len(C) == n:
        return n - 1
    return len(C)


def predicted_mu(A, B, universe, n):
    if A == B:
        return 1
    if B != universe and len(B) <= n - 2:
        return (-1)**(len(B) - len(A))
    if B != universe:
        m = n - len(A)
        return (-1)**(m - 1)*(m - 1)
    if len(A) == n:
        return -1
    m = n - len(A)
    return -sum((-1)**j * comb(m, j)**2 * factorial(j) for j in range(m+1))


def check(n):
    universe, perms, ext = concept_extents(n)
    all_matching_sets = set()
    for P in perms:
        for k in range(n+1):
            for F in combinations(P, k):
                all_matching_sets.add(frozenset(F))
    expected = {F for F in all_matching_sets if len(F) <= n-2 or len(F) == n}
    expected.add(universe)
    assert ext == expected, ('closed_sets',n,len(ext),len(expected))
    expected_size = 1 + factorial(n) + sum(comb(n,k)**2*factorial(k) for k in range(n-1))
    assert len(ext) == expected_size
    sorted_C = sorted(ext, key=lambda a:(rank_of(a,universe,n),len(a),sorted(a)))
    mu = {}
    num_intervals = 0
    for lower in sorted_C:
        for upper in sorted_C:
            if not lower <= upper:
                continue
            if lower == upper:
                mu[(lower,upper)] = 1
            else:
                val = -sum(mu[(lower,X)] for X in sorted_C if lower<=X and X<upper)
                mu[(lower,upper)] = val
            assert mu[(lower,upper)] == predicted_mu(lower,upper,universe,n), (n,lower,upper,mu[(lower,upper)])
            num_intervals += 1
    rank_counts = [sum(rank_of(C,universe,n)==i for C in ext) for i in range(n+1)]
    assert all(rank_counts[i]**2>rank_counts[i-1]*rank_counts[i+1] for i in range(1,n))
    # Reduced Euler characteristic of the matching (chessboard) complex.
    signed_faces = -sum((-1)**len(F) for F in all_matching_sets)
    assert signed_faces == mu[(frozenset(),universe)]
    # Direct minimum-premise Horn basis, independently tested on all subsets.
    if n <= 4:
        edge_index = {e:i for i,e in enumerate(matching_tuple_edges(n))}
        bit_pm = tuple(sum(1<<edge_index[e] for e in P) for P in perms)
        universe_bits = (1 << (n*n))-1
        rules = []
        if n == 2:
            for e in edge_index:
                one = 1<<edge_index[e]
                P = next(p for p in bit_pm if p & one)
                rules.append((one,P))
        else:
            for a,b in combinations(edge_index,2):
                if a[0]==b[0] or a[1]==b[1]:
                    rules.append(((1<<edge_index[a])|(1<<edge_index[b]),universe_bits))
            near = set()
            for P in perms:
                for drop in P:
                    premise = frozenset(P-{drop})
                    near.add((sum(1<<edge_index[e] for e in premise),1<<edge_index[drop]))
            rules.extend(sorted(near))
            assert len(rules) == n*n*(n-1) + n*factorial(n)
        minimum_nonclosed = []
        for subset in range(1<<(n*n)):
            consistent = [P for P in bit_pm if subset & P == subset]
            correct = universe_bits
            for P in consistent:
                correct &= P
            direct = subset
            for premise,conclusion in rules:
                if subset & premise == premise:
                    direct |= conclusion
            assert direct == correct,(n,subset,direct,correct)
            if correct != subset and all((r[0] & subset)!=r[0] or r[0]==subset for r in rules):
                minimum_nonclosed.append(subset)
        assert set(minimum_nonclosed)==set(p for p,_ in rules)
        print('HORN',n,'subsets',1<<(n*n),'necessary_premises',len(rules),'one_round=PASS')
    print('EXHAUSTIVE',n,'closed',len(ext),'intervals',num_intervals,'ranks',rank_counts,'mobius',signed_faces,'PASS')


if __name__ == '__main__':
    for n in range(2,5):
        check(n)
    print('VERIFY_OK independent_context_closure=PASS all_intervals=PASS strict_logconcavity=PASS chessboard_euler=PASS')
