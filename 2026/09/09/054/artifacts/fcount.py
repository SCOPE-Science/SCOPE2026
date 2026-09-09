"""Fast F+ counting in linear 4-graphs via corner enumeration.

Key structural facts used (linearity => link of v is a matching of triples):
- Every core vertex of an F+ copy lies in exactly 3 blocks (corner).
- At corner v with link triples T1,T2,T3 (each = 2 core + 1 private),
  the 7 core vertices carry a Fano structure with through-lines {v,a_i,b_i}.
- Given the 7-set + 3 through-lines, there are exactly 2 Fano completions
  (triangle-decompositions of K_{2,2,2}); each completion fixes the 4 off-triples.
"""
import itertools

def build_pair_map(edges):
    pmap = {}
    for i, e in enumerate(edges):
        s = sorted(e)
        for a in range(4):
            for b in range(a+1, 4):
                pmap[(s[a], s[b])] = i
    return pmap

def k222_completions(abc):
    """abc = ((a1,b1),(a2,b2),(a3,b3)): pairs partitioning the 6 off-core points.
    Yield the ('exactly 2') triangle-decompositions of K6 minus this matching."""
    (a1, b1), (a2, b2), (a3, b3) = abc
    # octahedron K_{2,2,2} with parts {a1,b1},{a2,b2},{a3,b3}: triangles pick one per part
    tris = [(x, y, z) for x in (a1, b1) for y in (a2, b2) for z in (a3, b3)]
    # find decompositions: 4 disjoint-cover triangles covering all 12 cross pairs
    out = []
    def pairs_of(t):
        x, y, z = sorted(t)
        return {(x, y), (x, z), (y, z)}
    # brute force: choose 4 triples covering 12 pairs
    for combo in itertools.combinations(tris, 4):
        cov = set()
        ok = True
        for t in combo:
            for p in pairs_of(t):
                if p in cov:
                    ok = False
                    break
                cov.add(p)
            if not ok:
                break
        if ok and len(cov) == 12:
            out.append(combo)
            if len(out) == 2:
                break
    return out

def count_Fplus(edges, cap=None):
    """Count (corner, block-7-set) F+ copies. Each copy has 7 corners -> returns n_copies."""
    E = [frozenset(e) for e in edges]
    m = len(E)
    pmap = build_pair_map([sorted(e) for e in edges])
    # links
    byv = {}
    for i, e in enumerate(E):
        for v in e:
            byv.setdefault(v, []).append(i)
    total = 0
    for v, lst in byv.items():
        triples = [tuple(sorted(E[i] - {v})) for i in lst]
        d = len(lst)
        for combo in itertools.combinations(range(d), 3):
            i, j, k = combo
            Ti, Tj, Tk = triples[i], triples[j], triples[k]
            # try all private-position assignments (3^3=27)
            for pi in range(3):
                for pj in range(3):
                    for pk in range(3):
                        ci = [Ti[t] for t in range(3) if t != pi]
                        cj = [Tj[t] for t in range(3) if t != pj]
                        ck = [Tk[t] for t in range(3) if t != pk]
                        priv = {Ti[pi], Tj[pj], Tk[pk]}
                        core = {v} | set(ci) | set(cj) | set(ck)
                        if len(core) != 7:
                            continue
                        if len(priv - core) != 3:
                            continue
                        comps = k222_completions((tuple(ci), tuple(cj), tuple(ck)))
                        for comp in comps:
                            ok = True
                            offpriv = set()
                            for t in comp:
                                x, y, z = sorted(t)
                                bi = pmap.get((x, y))
                                if bi is None:
                                    ok = False
                                    break
                                B = E[bi]
                                if B - {x, y, z} == B - core and len(B & core) == 3:
                                    (q,) = tuple(B - core)
                                    if q in priv or q in offpriv or q in core:
                                        ok = False
                                        break
                                    offpriv.add(q)
                                else:
                                    ok = False
                                    break
                            if ok:
                                total += 1
                                if cap is not None and total >= cap:
                                    return total
    # each F+ copy counted once per corner (7 corners)
    assert total % 7 == 0, total
    return total // 7
