"""Exact-arithmetic verification for multitype fraction-of-like-neighbors swapping.
No external dependencies. This is corroboration, not a substitute for the proof.
Run: python3 verify_biclique.py
"""
from functools import lru_cache
from itertools import product


def compositions(total, k):
    if k == 1:
        yield (total,)
    else:
        for first in range(total + 1):
            for rest in compositions(total - first, k - 1):
                yield (first,) + rest


def data(r, s, a, b):
    d = [b * x - a * y for x, y in zip(r, s)]
    h = a + b
    plus = sum(max(0, (x - b + h - 1) // h) for x in d)
    minus = sum(max(0, (-a - x + h - 1) // h) for x in d)
    return d, plus, minus


def neighbours(r, s, a, b):
    k = len(r)
    d, _, _ = data(r, s, a, b)
    for i in range(k):
        if d[i] <= b:
            continue
        for j in range(k):
            if d[j] >= -a:
                continue
            rr, ss = list(r), list(s)
            rr[i] -= 1
            rr[j] += 1
            ss[i] += 1
            ss[j] -= 1
            assert min(rr) >= 0 and min(ss) >= 0
            yield tuple(rr), tuple(ss)


def direct_profit(colours, a, b, i, j):
    """Explicit original and exchanged agents' fractions, without imbalance formula."""
    utype = colours[i]
    vtype = colours[j]
    if utype == vtype:
        return False
    nleft = colours[:a]
    nright = colours[a:]
    old_u = nright.count(utype)
    old_v = nleft.count(vtype)
    mutated = list(colours)
    mutated[i], mutated[j] = mutated[j], mutated[i]
    new_u = mutated[:a].count(utype)
    new_v = mutated[a:].count(vtype)
    return new_u * b > old_u * a and new_v * a > old_v * b


def small_explicit():
    colstates = comparisons = legal = equilibria = 0
    for a in range(1, 5):
        for b in range(1, 5):
            for k in (2, 3):
                for C in product(range(k), repeat=a+b):
                    r = tuple(C[:a].count(i) for i in range(k))
                    s = tuple(C[a:].count(i) for i in range(k))
                    d, plus, minus = data(r, s, a, b)
                    colour_moves = list(neighbours(r, s, a, b))
                    for u in range(a):
                        for v in range(a, a+b):
                            # Cross-multiply to recover original strict utility conditions.
                            i, j = C[u], C[v]
                            strict = direct_profit(C,a,b,u,v)
                            by_formula = (d[i] > b and d[j] < -a)
                            assert strict == by_formula, (a,b,k,C,u,v,d)
                            comparisons += 1
                            legal += strict
                    assert (not colour_moves) == (plus == 0 or minus == 0)
                    assert (not colour_moves) == (max(d) <= b or min(d) >= -a)
                    colstates += 1
                    equilibria += not colour_moves
    return colstates,comparisons,legal,equilibria


def all_profiles():
    profile_states=edges=multi_terminal=0
    maximum=0
    for a in range(1,9):
        for b in range(1,9):
            for k in range(2,5):
                @lru_cache(None)
                def paths(r,s):
                    nonlocal edges
                    nxt=list(neighbours(r,s,a,b))
                    d,p,q=data(r,s,a,b)
                    assert min(p,q) <= min(a-1,b-1), (r,s,a,b,k,p,q)
                    if not nxt:
                        assert min(p,q)==0
                        return (0,0,frozenset({(r,s)}))
                    lo,hi=10**10,-1
                    terminal=set()
                    for rr,ss in nxt:
                        _,pn,qn=data(rr,ss,a,b)
                        assert pn==p-1 and qn==q-1, (r,s,rr,ss,a,b)
                        low,high,terminal_s=paths(rr,ss)
                        lo=min(lo,low+1)
                        hi=max(hi,high+1)
                        # Too many terminal profiles could be huge: restrict stored profiles to 32.
                        terminal.update(list(terminal_s)[:32])
                        edges+=1
                    assert lo==hi==min(p,q), (r,s,a,b,k,lo,hi,p,q)
                    return lo,hi,frozenset(list(terminal)[:32])
                for r in compositions(a,k):
                    for s in compositions(b,k):
                        small,big,term=paths(r,s)
                        maximum=max(maximum,big)
                        multi_terminal += len(term)>1
                profile_states+=paths.cache_info().currsize
    return profile_states,edges,multi_terminal,maximum


def witness():
    a,b=2,7
    r,s=[0,0,2],[2,2,3]
    d,p,q=data(r,s,a,b)
    assert d==[-4,-4,8] and p==1 and q==2
    old_phi=sum(x*y for x,y in zip(r,s))
    rr,ss=list(neighbours(tuple(r),tuple(s),a,b))[0]
    new_phi=sum(x*y for x,y in zip(rr,ss))
    assert (old_phi,new_phi)==(6,5)
    return old_phi,new_phi

if __name__=='__main__':
    print('EXPLICIT_COLORINGS_PAIR_CHECKS',small_explicit())
    print('PROFILE_STATES_EDGE_CHECKS_MULTIPLE_TERMINALS_MAX_DEPTH',all_profiles())
    print('ORDINARY_MONOCHROME_EDGE_POTENTIAL_DECREASE',witness())
    print('ALL_CHECKS_PASSED')
