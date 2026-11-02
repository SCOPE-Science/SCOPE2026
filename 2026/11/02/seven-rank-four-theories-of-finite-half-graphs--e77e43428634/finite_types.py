#!/usr/bin/env python3
"""Exact first-order quantifier-rank profiles of uncoloured finite half-graphs.

No external packages or input files. Run: python3 finite_types.py
Tuple recursion includes repeated vertices and uses global type dictionaries
for comparisons between structures of different orders.
"""
from itertools import product

def half_graph_adj(x, y, n):
    if x < n and y >= n:
        return x <= y - n
    if y < n and x >= n:
        return y <= x - n
    return False

def atom_code(t, n):
    """Canonical ternary code of equality/adjacency on a labelled tuple."""
    code = 0
    power = 1
    for i, a in enumerate(t):
        for b in t[:i]:
            value = 2 if a == b else (1 if half_graph_adj(a, b, n) else 0)
            code += power * value
            power *= 3
    return code

class Interner:
    def __init__(self):
        self.ids = [dict() for _ in range(5)]
    def intern(self, rank, s):
        d = self.ids[rank]
        if s not in d:
            d[s] = len(d)
        return d[s]

def rank4_types(n, pool):
    domain = tuple(range(2*n))
    # The longest tuples have no quantifiers remaining.
    type3 = {t: pool.intern(1, frozenset(atom_code(t+(z,), n) for z in domain))
             for t in product(domain, repeat=3)}
    type2 = {t: pool.intern(2, frozenset(type3[t+(z,)] for z in domain))
             for t in product(domain, repeat=2)}
    type1 = {(x,): pool.intern(3, frozenset(type2[(x,z)] for z in domain))
             for x in domain}
    type0 = pool.intern(4, frozenset(type1.values()))
    return type0, (len(set(type1.values())),len(set(type2.values())),len(set(type3.values())))

def rankq_types(n, q, pool):
    # General calculation for q <= 3, independent of rank-four tuple tables.
    domain = tuple(range(2*n))
    levels = {t: atom_code(t, n) for t in product(domain, repeat=q)}
    for j in range(q-1,-1,-1):
        levels = {t: pool.intern(q-j, frozenset(levels[t+(z,)] for z in domain))
                  for t in product(domain, repeat=j)}
    return levels[()]

def main():
    pool=Interner()
    rows=[]
    for n in range(1,16):
        tag, counts=rank4_types(n,pool)
        rows.append((n,tag,counts))
    print('RANK4 n id vertex_pair_triple_counts')
    for n,tag,counts in rows:
        print(n,tag,*counts)
    assert [r[1] for r in rows] == list(range(7))+[6]*8
    for q, expected in ((1,[0]*15),(2,[0]+[1]*14),(3,[0,1]+[2]*13)):
        # Separate fresh dictionary for each quantifier rank.
        pp=Interner()
        ids=[rankq_types(n,q,pp) for n in range(1,16)]
        print('RANK',q,'IDS',ids)
        assert ids==expected
    print('FINITE_TYPE_CENSUS_PASS: seven rank-four classes, H7..H15 equal')

if __name__=='__main__':
    main()
