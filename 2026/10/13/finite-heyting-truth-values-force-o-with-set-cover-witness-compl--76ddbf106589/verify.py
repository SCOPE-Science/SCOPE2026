from itertools import combinations


def all_posets(n):
    """Generate all labeled partial orders on {0,...,n-1}."""
    for mask in range(1 << (n * n)):
        if any(((mask >> (i*n+i)) & 1) == 0 for i in range(n)):
            continue
        bad = False
        for i in range(n):
            for j in range(i+1, n):
                if ((mask >> (i*n+j)) & 1) and ((mask >> (j*n+i)) & 1):
                    bad = True
                    break
            if bad:
                break
        if bad:
            continue
        good = True
        for i in range(n):
            for j in range(n):
                if not ((mask >> (i*n+j)) & 1):
                    continue
                for k in range(n):
                    if ((mask >> (j*n+k)) & 1) and not ((mask >> (i*n+k)) & 1):
                        good = False
                        break
                if not good:
                    break
            if not good:
                break
        if good:
            yield mask


def upsets(n, rel):
    H = []
    for s in range(1 << n):
        ok = True
        for x in range(n):
            if (s >> x) & 1:
                for y in range(n):
                    if ((rel >> (x*n+y)) & 1) and not ((s >> y) & 1):
                        ok = False
                        break
            if not ok:
                break
        if ok:
            H.append(s)
    return H


def neg(a, H):
    # Largest upset disjoint from a.
    v = 0
    for h in H:
        if h & a == 0:
            v |= h
    assert v in H
    return v


def j(a, H):
    return neg(neg(a, H), H)


def regular_atoms(H):
    regs = [h for h in H if j(h, H) == h]
    atoms = []
    for r in regs:
        if r == 0:
            continue
        if not any(s != 0 and s != r and (s & ~r) == 0 for s in regs):
            atoms.append(r)
    return regs, atoms


def minimum_clause(F, H):
    E = 0
    for u in F:
        E |= u
    INF = 10**9
    # Dynamic programming on regularized joins.  From a regular state r,
    # adding u reaches j(r join u), which equals j(raw_join join u).
    dp = {j(0, H): 0}
    for u in F:
        nxt = dict(dp)
        for r, c in dp.items():
            nr = j(r | u, H)
            nxt[nr] = min(nxt.get(nr, INF), c + 1)
        dp = nxt
    return min(c for r, c in dp.items() if (E & ~r) == 0)


def minimum_atom_cover(F, H):
    E = 0
    for u in F:
        E |= u
    target = j(E, H)
    _, atoms = regular_atoms(H)
    target_atoms = [p for p in atoms if (p & ~target) == 0]
    full = (1 << len(target_atoms)) - 1
    masks = []
    for u in F:
        ju = j(u, H)
        m = 0
        for i, p in enumerate(target_atoms):
            if (p & ~ju) == 0:
                m |= 1 << i
        masks.append(m)
    INF = 10**9
    dp = [INF] * (1 << len(target_atoms))
    dp[0] = 0
    for m in masks:
        nxt = dp[:]
        for s, c in enumerate(dp):
            if c < INF:
                nxt[s | m] = min(nxt[s | m], c + 1)
        dp = nxt
    return dp[full], len(atoms)


poset_count = 0
family_count = 0
for n in range(1, 5):
    for rel in all_posets(n):
        poset_count += 1
        H = upsets(n, rel)
        regs, atoms = regular_atoms(H)

        # Sanity-check the Boolean-skeleton join identity on every pair.
        for a in H:
            for b in H:
                assert j(a | b, H) == j(j(a, H) | j(b, H), H)

        # Exhaust every set of distinct witness truth values.
        for fm in range(1 << len(H)):
            F = [H[i] for i in range(len(H)) if (fm >> i) & 1]
            m_clause = minimum_clause(F, H)
            m_cover, atom_count = minimum_atom_cover(F, H)
            assert m_clause == m_cover
            assert m_clause <= atom_count
            family_count += 1

# Sharpness: in the k-atom powerset Boolean algebra, singleton witness
# values need exactly k witnesses to cover the top value.
for k in range(1, 13):
    universe = (1 << k) - 1
    singleton_values = [1 << i for i in range(k)]
    best = k + 1
    for mask in range(1 << k):
        union = 0
        used = 0
        for i, u in enumerate(singleton_values):
            if (mask >> i) & 1:
                union |= u
                used += 1
        if union == universe:
            best = min(best, used)
    assert best == k

assert poset_count == 242
assert family_count == 172740
print(f"VERIFY_OK {family_count} witness-family checks over {poset_count} labeled posets through four points; sharpness k<=12")
