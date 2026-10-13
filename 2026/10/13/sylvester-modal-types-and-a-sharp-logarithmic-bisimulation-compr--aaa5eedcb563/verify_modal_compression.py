#!/usr/bin/env python3
"""Independent finite checks for modal type recurrence and bisimulation quotient bounds.

No external dependencies. Run: python verify_modal_compression.py
"""
from collections import Counter
from itertools import product
from math import comb


def type_census(q, a, h):
    out = [a]
    for _ in range(h):
        x = out[-1]
        out.append(a * sum(comb(x, j) for j in range(1, min(q, x) + 1)))
    return out


def hierarchy(q, h):
    n = (q**(h+1)-1)//(q-1)
    children = [tuple(q*u+j for j in range(1, q+1)) if q*u+1<n else () for u in range(n)]
    levels = [0]*n
    for u in range(n):
        for v in children[u]: levels[v] = levels[u]+1
    assert max(levels)==h
    return children, levels


def rooted_types(colors, children):
    typ = [None]*len(children)
    for u in reversed(range(len(children))):
        typ[u] = (colors[u], frozenset(typ[v] for v in children[u]))
    return typ


def partition_refinement(colors, children):
    # Independently compute greatest bisimulation of a fixed finite frame.
    current = tuple(colors)
    for _ in range(len(children)+1):
        keys=[(colors[u],frozenset(current[v] for v in children[u])) for u in range(len(children))]
        dictionary={}
        nxt=tuple(dictionary.setdefault(x,len(dictionary)) for x in keys)
        if nxt==current:return current
        current=nxt
    raise AssertionError('partition refinement failed to stabilize')


def same_partition(x, y):
    return all((x[i]==x[j])==(y[i]==y[j]) for i in range(len(x)) for j in range(len(x)))


def run_case(q,a,h):
    children, levels=hierarchy(q,h)
    n=len(children)
    counts=Counter(); dist=Counter(); maximum=0; good=0
    predicted=type_census(q,a,h)
    level_caps=sum(min(q**(h-k),predicted[k]) for k in range(h+1))
    for colors in product(range(a),repeat=n):
        types=rooted_types(colors,children)
        count=len(set(types));maximum=max(maximum,count);dist[count]+=1
        counts[types[0]]+=1
        refined=partition_refinement(colors,children)
        assert same_partition(types,refined), ('partition mismatch',q,a,h,colors)
        assert all((levels[i]==levels[j]) or (types[i]!=types[j]) for i in range(n) for j in range(i+1,n))
        assert count<=level_caps
        good+=1
    assert len(counts)==predicted[h], ('type recurrence mismatch',q,a,h,len(counts),predicted[h])
    print('CASE_OK',f'q={q}',f'a={a}',f'h={h}',f'valuations={good}',f'root_types={len(counts)}',f'max_quotient={maximum}',f'level_upper_bound={level_caps}',f'quotient_sizes={dict(sorted(dist.items()))}')
    return good


def main():
    # Sylvester recurrence for the binary/one-proposition specialization.
    xs=type_census(2,2,5)
    assert xs[:5]==[2,6,42,1806,3263442],xs
    assert all(xs[i+1]==xs[i]*(xs[i]+1) for i in range(len(xs)-1))
    total=0
    for q,a,h in [(2,2,3),(3,2,2),(2,3,2),(2,2,2),(3,1,2)]:
        total+=run_case(q,a,h)
    print('VERIFY_OK',total,'exhaustive valuations','binary Sylvester steps',len(xs)-1)

if __name__=='__main__': main()
