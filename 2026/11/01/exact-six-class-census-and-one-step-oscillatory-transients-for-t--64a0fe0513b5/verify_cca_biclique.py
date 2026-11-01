#!/usr/bin/env python3
"""Exact arithmetic checks for three-colour cyclic cellular automata on bicliques.
Only scientific verification, without external dependencies.
"""
from collections import Counter, defaultdict
from itertools import product
from math import comb

# Support encoding: bit c means colour c is present (c=0,1,2).
def support_step(A, B):
    out = 0
    for c in range(3):
        if A & (1 << c):
            successor = (c + 1) % 3
            new_color = successor if B & (1 << successor) else c
            out |= 1 << new_color
    return out


def support_map(pair):
    a, b = pair
    return support_step(a, b), support_step(b, a)


def support_signature(pair):
    visited = {}
    path = []
    while pair not in visited:
        visited[pair] = len(path)
        path.append(pair)
        pair = support_map(pair)
    t = visited[pair]
    orbit = path[t:]
    assert len(orbit) in (1, 2), (t, orbit)
    if len(orbit) == 1:
        period = 3 if orbit[0] == (7, 7) else 1
    else:
        period = 4
    return t, period


def q(m, k):
    return sum((-1) ** j * comb(k, j) * (k-j) ** m for j in range(k + 1))


def expected(a, b):
    ua, ub = 2**a - 2, 2**b - 2
    ra, rb = 3**a - 3*2**a + 3, 3**b - 3*2**b + 3
    return {
        (0,1): 3,
        (0,3): ra*rb,
        (0,4): 6*ua*ub,
        (1,1): 6+3*(ua+ub+ua*ub),
        (1,4): 3*(ua*rb+ra*ub),
        (2,1): 6*(ua+ub)+3*(ra+rb),
    }


def direct_step(state, a, b):
    left, right = state[:a], state[a:]
    lc = set(left)
    rc = set(right)
    return tuple((x+1)%3 if (x+1)%3 in rc else x for x in left) + \
           tuple((y+1)%3 if (y+1)%3 in lc else y for y in right)


def direct_signature(state, a, b):
    visited = {}
    path = []
    while state not in visited:
        visited[state] = len(path)
        path.append(state)
        state = direct_step(state, a, b)
        if len(path)>14:
            raise AssertionError('Unexpected long transient/period')
    return visited[state], len(path)-visited[state]


def main():
    by=defaultdict(Counter)
    support_rows=[]
    for A in range(1,8):
        for B in range(1,8):
            sig=support_signature((A,B))
            by[sig][(A.bit_count(),B.bit_count())] += 1
            support_rows.append((A,B,*support_map((A,B)),*sig))
    groups={
      (0,1): {(1,1):3},
      (0,3): {(3,3):1},
      (0,4): {(2,2):6},
      (1,1): {(1,1):6,(1,2):3,(2,1):3,(2,2):3},
      (1,4): {(2,3):3,(3,2):3},
      (2,1): {(1,2):6,(1,3):3,(2,1):6,(3,1):3},
    }
    assert {x:dict(y) for x,y in by.items()} == groups
    assert len(support_rows)==49
    print('SUPPORT_TABLE_49_OK')
    for sig in sorted(groups):
        print('SUPPORT_CLASS',sig,'weights',dict(sorted(groups[sig].items())))
    print('FULL_SUPPORT_TABLE: A,B -> A_next,B_next; entry_time, eventual_period')
    for row in support_rows:
        print(*row)
    checked=0
    # Independent brute-force coloured-vertex simulation, not the support_map.
    for a in range(1,6):
      for b in range(1,6):
        if a+b>9:
            continue
        counts=Counter()
        for state in product(range(3),repeat=a+b):
            sig=direct_signature(state,a,b)
            counts[sig]+=1
            A=sum(1<<i for i in set(state[:a]))
            B=sum(1<<i for i in set(state[a:]))
            assert sig==support_signature((A,B)),(a,b,state,sig,support_signature((A,B)))
            checked+=1
        formulas=expected(a,b)
        assert counts==Counter({k:v for k,v in formulas.items() if v}), (a,b,counts,formulas)
        assert sum(counts.values())==3**(a+b)
        if a==b or (a,b) in [(2,3),(3,4),(4,5)]:
            print('FULL_CENSUS_OK',a,b,dict(sorted(counts.items())))
    for a in range(1,15):
        for b in range(1,15):
            formula=expected(a,b)
            tab=Counter()
            for A in range(1,8):
                for B in range(1,8):
                    tab[support_signature((A,B))]+=q(a,A.bit_count())*q(b,B.bit_count())
            assert tab==Counter({k:v for k,v in formula.items() if v})
            assert sum(formula.values())==3**(a+b)
            assert formula[(0,3)]%3==0 and formula[(0,4)]%4==0
    print('FORMULA_ALL_196_PARAMETER_PAIRS_OK')
    print('DIRECT_LABELLED_CONFIGURATIONS',checked)
    print('CCA_BICLIQUE_EXACT_VERIFY_OK')

if __name__=='__main__':
    main()
