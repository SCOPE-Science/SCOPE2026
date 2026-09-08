import math, json, os
from mn_check import partitions, conj, char_table, class_size
HERE = os.path.dirname(os.path.abspath(__file__))

def hook_dim(la):
    # hook-length formula
    n = sum(la)
    cells = [(r, c) for r, row in enumerate(la) for c in range(row)]
    prod = 1
    for (r, c) in cells:
        arm = la[r] - c - 1
        leg = sum(1 for row in la[r+1:] if row > c)
        prod *= (arm + leg + 1)
    return math.factorial(n) // prod

tables = {}
for n in (6, 7, 8):
    parts, tab = char_table(n)
    parts_sorted = sorted(parts)
    cs = {str(mu): class_size(n, mu) for mu in parts}
    assert sum(cs.values()) == math.factorial(n)
    # hook-length cross-check on identity class
    ident = tuple([1] * n)
    for la in parts:
        assert tab[(la, ident)] == hook_dim(la), (n, la)
    # n-cycle check: +-1 iff hook
    ncyc = (n,)
    for la in parts:
        v = tab[(la, ncyc)]
        is_hook = len(la) + (la[0] if la else 0) - 1 == n
        if is_hook:
            assert abs(v) == 1, (n, la, v)
        else:
            assert v == 0, (n, la, v)
    tables[str(n)] = {
        "parts": [list(p) for p in parts_sorted],
        "class_sizes": {str(list(k)): v for k, v in ((mu, class_size(n, mu)) for mu in parts)},
        "chars": {str(list(a)) + "|" + str(list(m)): tab[(a, m)] for a in parts for m in parts},
    }
    print(n, "hook+ncycle checks passed")

with open(os.path.join(HERE, "char_tables.json"), "w") as f:
    json.dump(tables, f)
print("wrote char_tables.json")
