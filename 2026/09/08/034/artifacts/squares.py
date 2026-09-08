import math, json, os
from collections import Counter
from mn_check import partitions, conj, char_table, class_size
HERE = os.path.dirname(os.path.abspath(__file__))

def kron(n, parts, tab, a, b, c):
    fn = math.factorial(n)
    s = sum(class_size(n, mu) * tab[(a, mu)] * tab[(b, mu)] * tab[(c, mu)] for mu in parts)
    assert s % fn == 0, (n, a, b, c, s)
    return s // fn

results = {}
for n in (6, 7, 8):
    parts, tab = char_table(n)
    parts_sorted = sorted(parts)  # lexicographic
    # square vectors
    sq = {}
    for la in parts:
        sq[la] = tuple(kron(n, parts, tab, la, la, nu) for nu in parts_sorted)
    # group by vector; check collisions up to conjugation
    from collections import defaultdict
    groups = defaultdict(list)
    for la in parts:
        groups[sq[la]].append(la)
    collisions = {str(k): v for k, v in groups.items() if len(v) > 1}
    # non-conjugate-pair analysis
    # canonical rep: pair {la, conj(la)}; check any equal vectors across different classes
    def canon(la):
        c = conj(la)
        return min(la, c), max(la, c)
    canon_map = {}
    for la in parts:
        canon_map.setdefault(canon(la), []).append(la)
    classes = list(canon_map.keys())
    cross_collision = []
    for i in range(len(classes)):
        for j in range(i+1, len(classes)):
            # compare representatives: all members share? check: conjugates have same square? verify
            pass
    # verify conjugates share squares
    conj_ok = all(sq[la] == sq[conj(la)] for la in parts)
    # check distinct classes have distinct vectors
    rep_vecs = {}
    sep_ok = True
    for cl in classes:
        v = sq[cl[0]]
        assert sq[cl[1]] == v, ("conj mismatch", n, cl)
        rep_vecs[cl] = v
    vecs = list(rep_vecs.values())
    distinct = len(set(vecs)) == len(classes)
    # separators: for each pair of distinct classes, lex-first nu with differing coeff
    seps = {}
    for i in range(len(classes)):
        for j in range(i+1, len(classes)):
            ci, cj = classes[i], classes[j]
            vi, vj = rep_vecs[ci], rep_vecs[cj]
            for k, nu in enumerate(parts_sorted):
                if vi[k] != vj[k]:
                    seps[str((ci, cj))] = {"nu": list(nu), "g1": vi[k], "g2": vj[k]}
                    break
            else:
                sep_ok = False
                seps[str((ci, cj))] = None
    # supports
    supports = {str(la): [list(nu) for nu, g in zip(parts_sorted, sq[la]) if g > 0] for la in parts}
    results[str(n)] = {
        "p": len(parts),
        "nclasses": len(classes),
        "conj_ok": conj_ok,
        "distinct_up_to_conj": distinct,
        "collisions": {str(k): [list(x) for x in v] for k, v in groups.items() if len(v) > 1},
        "separators": seps,
        "squares": {str(la): list(sq[la]) for la in parts},
        "order": [list(p) for p in parts_sorted],
    }
    print(n, "classes:", len(classes), "distinct:", distinct, "conj_ok:", conj_ok, "sep_ok:", sep_ok)
    if not distinct:
        print("COLLISIONS:", collisions)

with open(os.path.join(HERE, "square_vectors.json"), "w") as f:
    json.dump(results, f, indent=1)
print("wrote square_vectors.json")
