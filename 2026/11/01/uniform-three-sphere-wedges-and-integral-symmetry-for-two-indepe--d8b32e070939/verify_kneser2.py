#!/usr/bin/env python3
"""Standalone checks for the 2-independence complex of the two-subset Kneser graph.
No dependencies beyond Python 3 standard library. This is a finite cross-check,
not the all-parameter proof, which uses a contractible cover and the pair LES.
"""
from itertools import combinations, permutations
from collections import Counter
from math import comb


def graph(n):
    E = list(combinations(range(n), 2))
    nbr = [sum(1 << j for j, f in enumerate(E)
               if i != j and not(set(e) & set(f)))
           for i, e in enumerate(E)]
    return E, nbr


def faces(n):
    E, nbr = graph(n)
    F = [0]
    # Add one Kneser vertex at a time, while checking its new degree and the
    # degrees of its neighbors. Previously present vertices are already valid.
    for i in range(len(E)):
        bit = 1 << i
        extra = []
        for m in F:
            old_neighbors = nbr[i] & m
            if old_neighbors.bit_count() > 1:
                continue
            if old_neighbors:
                j = old_neighbors.bit_length() - 1
                if (nbr[j] & m).bit_count():
                    continue
            extra.append(m | bit)
        F.extend(extra)
    assert len(F) == len(set(F))
    return E, nbr, F


def matching(F, nv):
    U = set(F)
    partners = {}
    for i in range(nv):
        bit = 1 << i
        for m in F:
            top = m | bit
            if not (m & bit) and m in U and top in U:
                partners[m] = top
                partners[top] = m
                U.remove(m)
                U.remove(top)
    return partners, U


def acyclic(F, partners):
    # Reverse each matched face-to-coface Hasse arrow; retain all other arrows
    # from coface to face. Kahn deletion checks the *entire* directed graph.
    FS = set(F)
    arcs = {f: [] for f in F}
    indeg = {f: 0 for f in F}
    cnt = 0
    for top in F:
        m = top
        while m:
            bit = m & -m
            bottom = top ^ bit
            assert bottom in FS
            if partners.get(bottom) == top:
                src, dst = bottom, top
            else:
                src, dst = top, bottom
            arcs[src].append(dst)
            indeg[dst] += 1
            cnt += 1
            m ^= bit
    queue = [f for f, d in indeg.items() if d == 0]
    j = 0
    while j < len(queue):
        a = queue[j]
        j += 1
        for b in arcs[a]:
            indeg[b] -= 1
            if indeg[b] == 0:
                queue.append(b)
    assert j == len(F)
    return cnt


def signed_perm_character(n, E, F, p):
    ix = {e: i for i, e in enumerate(E)}
    act = [ix[tuple(sorted((p[a], p[b])))] for a, b in E]
    L = 0
    for m in F:
        if m == 0:
            continue
        I = [i for i in range(len(E)) if m >> i & 1]
        J = [act[i] for i in I]
        if sorted(J) != I:
            continue
        inv = sum(J[i] > J[j] for i in range(len(J)) for j in range(i + 1, len(J)))
        L += (-1) ** (len(I) - 1 + inv)
    return 1 - L  # since wedge spheres have only reduced H_3, sign (-1)^3


def exterior_char(n, p, k=4):
    cyc = []
    unseen = set(range(n))
    while unseen:
        i = min(unseen)
        j = i
        ell = 0
        while j in unseen:
            unseen.remove(j)
            ell += 1
            j = p[j]
        cyc.append(ell)
    pol = [1]
    for ell in cyc:
        new = pol + [0] * ell
        coeff = -(-1) ** ell
        for i, c in enumerate(pol):
            new[i + ell] += coeff * c
        pol = new
    # Divide by 1+t to remove invariant permutation vector.
    q = [0] * len(pol)
    q[0] = pol[0]
    for i in range(1, len(pol)):
        q[i] = pol[i] - q[i - 1]
    assert q[-1] == 0
    return q[k] if k < len(q) else 0


def cross_polytope_orientation():
    E = list(combinations(range(4), 2))
    # Join of three oriented 0-spheres: ([01]-[23])*([02]-[13])*([03]-[12]).
    factors = [((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))]
    C = {}
    for choices in __import__('itertools').product((0, 1), repeat=3):
        t = [factors[i][ch] for i, ch in enumerate(choices)]
        ix = [E.index(x) for x in t]
        sgn = (-1) ** (sum(choices) + sum(ix[i] > ix[j] for i in range(3) for j in range(i+1, 3)))
        key = tuple(sorted(ix))
        C[key] = C.get(key, 0) + sgn
    assert len(C) == 8 and set(C.values()) == {-1, 1}
    boundary = Counter()
    for I, c in C.items():
        for i in range(3):
            J = I[:i] + I[i+1:]
            boundary[J] += c * (-1) ** i
    assert all(z == 0 for z in boundary.values())
    # Four non-star triangles, one per ground triple, have alternating signs.
    for j in range(4):
        R = tuple(i for i in range(4) if i != j)
        key = tuple(sorted(E.index(e) for e in combinations(R, 2)))
        assert C[key] == (-1) ** j
    ix = {e:i for i,e in enumerate(E)}
    for p in permutations(range(4)):
        mapped = [ix[tuple(sorted((p[a],p[b])))] for a,b in E]
        D = {}
        for I, c in C.items():
            J = [mapped[i] for i in I]
            sgn = (-1) ** sum(J[i] > J[j] for i in range(3) for j in range(i+1, 3))
            key = tuple(sorted(J))
            D[key] = D.get(key, 0) + c * sgn
        parity = (-1) ** sum(p[i] > p[j] for i in range(4) for j in range(i+1, 4))
        assert all(D.get(x,0) == parity*c for x,c in C.items())
    return len(C)


def main():
    print('octahedral cycle 24 permutation signs and four boundary coefficients: VERIFIED', cross_polytope_orientation())
    for n in range(4, 9):
        E, nbr, F = faces(n)
        if n == 6:
            # Totally separate direct subset enumeration.
            brute = []
            for m in range(1 << len(E)):
                if all((nbr[i] & m).bit_count() <= 1 for i in range(len(E)) if (m >> i) & 1):
                    brute.append(m)
            assert set(F) == set(brute)
        pairs, crit = matching(F, len(E))
        assert 0 not in crit
        assert all(m.bit_count() == 4 for m in crit)
        assert len(crit) == comb(n - 1, 4) if n >= 5 else not crit
        assert len(F) == 2 * (len(pairs) // 2) + len(crit)
        hasse = acyclic(F, pairs)
        # The topological proof is for all n; these cases test the same definition.
        fv = dict(sorted(Counter(m.bit_count() - 1 for m in F if m).items()))
        red_euler = sum((-1)**d * z for d,z in fv.items()) - 1
        assert red_euler == -comb(n-1,4) if n >= 5 else red_euler == 0
        print(f'n={n} vertices={len(E)} nonempty={len(F)-1} face_vector={fv} pairs={len(pairs)//2} critical3={len(crit)} hasse={hasse} redEuler={red_euler} PASS')
        if n in (5, 6):
            hist = Counter()
            for p in permutations(range(n)):
                direct = signed_perm_character(n, E, F, p)
                expected = exterior_char(n, p)
                assert direct == expected, (n,p,direct,expected)
                hist[direct] += 1
            print(f'  all {__import__("math").factorial(n)} symmetry Lefschetz traces match exterior fourth power: PASS; trace_hist={dict(sorted(hist.items()))}')
    print('KNESER_2_INDEPENDENCE_ALL_N_STRUCTURAL_THEOREM_FINITE_CHECKS_VERIFIED')

if __name__ == '__main__':
    main()
