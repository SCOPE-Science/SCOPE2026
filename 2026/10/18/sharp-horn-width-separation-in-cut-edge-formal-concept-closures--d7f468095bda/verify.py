#!/usr/bin/env python3
"""Independent finite checks for complete-graph cut-incidence closure.
Only finite checks; universal statements follow from the accompanying proof.
"""
from itertools import combinations
from collections import defaultdict
from math import factorial


def edges(n):
    return list(combinations(range(n), 2))


def actual_closure(n, mask):
    es = edges(n)
    universe = (1 << len(es)) - 1
    meet = universe
    matches = 0
    for s in range(1 << (n-1)):
        cut = 0
        for j, (u, v) in enumerate(es):
            if (bool(s & (1 << u))) != (bool(s & (1 << v))):
                cut |= 1 << j
        if (cut & mask) == mask:
            matches += 1
            meet &= cut
    return meet, matches


def predicted_closure(n, mask):
    es = edges(n)
    universe = (1 << len(es)) - 1
    graph = [[] for _ in range(n)]
    for j, (a, b) in enumerate(es):
        if mask >> j & 1:
            graph[a].append(b)
            graph[b].append(a)
    color = [None] * n
    component = [-1] * n
    comp = 0
    for root in range(n):
        if color[root] is not None:
            continue
        color[root] = 0
        component[root] = comp
        stack = [root]
        while stack:
            a = stack.pop()
            for b in graph[a]:
                if color[b] is None:
                    color[b] = 1-color[a]
                    component[b] = comp
                    stack.append(b)
                elif color[b] == color[a]:
                    return universe
        comp += 1
    return sum((1 << j) for j, (a, b) in enumerate(es)
               if component[a] == component[b] and color[a] != color[b])


def rules3(n):
    es = edges(n)
    idx = {e: j for j, e in enumerate(es)}
    def edge(a, b):
        return 1 << idx[tuple(sorted((a, b)))]
    ans = []
    for a, b, c, d in __import__('itertools').permutations(range(n), 4):
        ant = edge(a,b)|edge(b,c)|edge(c,d)
        ans.append((ant,edge(a,d)))
    universe = (1 << len(es))-1
    for a,b,c in combinations(range(n), 3):
        ant = edge(a,b)|edge(b,c)|edge(a,c)
        ans.append((ant,universe))
    return tuple(set(ans))


def saturate(mask, rules):
    while True:
        nextmask = mask
        for ante, conseq in rules:
            if (mask & ante) == ante:
                nextmask |= conseq
        if nextmask == mask:
            return mask
        mask = nextmask


def expected_concepts(n):
    # Exponential formula: weighted set partitions, w_1=1 and
    # w_s = 2^(s-1)-1 for s>=2, counts of unordered two-colorings.
    bell = [0]*(n+1)
    bell[0] = 1
    from math import comb
    for m in range(1,n+1):
        bell[m] = sum(comb(m-1,s-1) * (1 if s==1 else 2**(s-1)-1)*bell[m-s]
                      for s in range(1,m+1))
    return bell[n]+1


def check(n):
    es = edges(n)
    # Full cut enumeration for n<=6, all subsets of E.
    rules = rules3(n)
    covered = 0
    fibers = defaultdict(int)
    for mask in range(1 << len(es)):
        truth, matches = actual_closure(n, mask)
        pred = predicted_closure(n, mask)
        assert truth == pred, (n,mask,truth,pred)
        sat = saturate(mask, rules)
        assert sat == truth,(n,mask,sat,truth)
        if mask == truth:
            covered += 1
        fibers[truth] += 1
    assert covered == expected_concepts(n),(n,covered,expected_concepts(n))
    print(f'EXHAUSTIVE n={n} subsets={1<<len(es)} closed={covered} triple_rules={len(rules)} PASS')
    return fibers


def direct_width_test(n):
    es=edges(n)
    idx={e:j for j,e in enumerate(es)}
    allmask=(1<<len(es))-1
    d=2*((n-2)//2)+1
    # Witness: odd d-cycle with one outsider. All proper subsets fail to force e.
    C=list(range(d))
    outsider=d
    cycle=0
    for a,b in zip(C,C[1:]+C[:1]):
        cycle|=1<<idx[tuple(sorted((a,b)))]
    target=1<<idx[tuple(sorted((outsider,C[0])))]
    assert actual_closure(n,cycle)[0] & target
    for j in range(len(es)):
        if cycle >> j & 1:
            assert not actual_closure(n,cycle^(1<<j))[0] & target
    # Verify bound: for every F and every e forced by F but absent,
    # there is some subset of F of size <=d that already forces e.
    # On small n feasible via caching all closures.
    if n<=6:
        closes=[predicted_closure(n,F) for F in range(1<<len(es))]
        for F in range(len(closes)):
            if F.bit_count()<=d:
                continue
            missing=closes[F]&~F
            if not missing:
                continue
            witness=0
            sub=F
            while True:
                if sub.bit_count()<=d:
                    witness |= closes[sub]
                if not sub:
                    break
                sub=(sub-1)&F
            assert (missing & ~witness)==0,(n,F,missing,missing&~witness)
        print(f'DIRECT_BOUND n={n} width={d} exhaustive=PASS lower_witness=PASS')
    else:
        print(f'DIRECT_BOUND n={n} width={d} lower_witness=PASS')


if __name__=='__main__':
    for n in (4,5,6):
        check(n)
        direct_width_test(n)
    for n in (7,8,9):
        direct_width_test(n)
    print('VERIFY_OK exact_cut_closure=PASS iterative_width_three=PASS direct_arity_bound=PASS concept_number=PASS')
