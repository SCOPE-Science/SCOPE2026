#!/usr/bin/env python3
"""Exact checks for the sparse binary-approval equitable allocation theorem.

Only Python's standard library is needed.  This is a finite corroboration of
an analytic Hall-theorem proof, not a proof by sampling.
"""
from itertools import combinations, product


def hall_target(n, goods):
    vals = []
    for mask in range(1, 1 << n):
        subset = {i for i in range(n) if mask & (1 << i)}
        neighbors = sum(bool(set(g) & subset) for g in goods)
        vals.append(neighbors // len(subset))
    return min(vals)


def slot_matching(n, goods, k):
    # An augmenting-path matching from k individually labeled agent slots to goods.
    # left labels a*k+s for each agent a and slot s; right labels goods indices.
    owners = [-1] * len(goods)
    def augment(slot, used):
        agent = slot // k
        for g, approvals in enumerate(goods):
            if agent not in approvals or g in used:
                continue
            used.add(g)
            if owners[g] == -1 or augment(owners[g], used):
                owners[g] = slot
                return True
        return False
    for slot in range(n * k):
        if not augment(slot, set()):
            raise AssertionError('Hall deficiency at target')
    result = [-1] * len(goods)
    for g, slot in enumerate(owners):
        if slot >= 0:
            result[g] = slot // k
    for g, a in enumerate(result):
        if a == -1:
            result[g] = next(i for i in range(n) if i not in goods[g])
    return result


def verify_instance(n, goods):
    assert all(len(set(g)) <= 2 for g in goods)
    degs = [sum(i in g for g in goods) for i in range(n)]
    assert len(set(degs)) == 1
    d = degs[0]
    k = hall_target(n, goods)
    assert k >= d // 2
    assignment = slot_matching(n, goods, k)
    utility = [sum(a == i and i in goods[g] for g, a in enumerate(assignment)) for i in range(n)]
    assert utility == [k] * n
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            other = sum(assignment[g] == j and i in goods[g] for g in range(len(goods)))
            assert other <= k + 1, (n, goods, k, utility, i, j, other)
    return k


def enumerate_regular(n, d):
    # Goods with zero approvers can be added without changing any utility.
    types = list(combinations(range(n), 1)) + list(combinations(range(n), 2))
    counts = [0] * len(types)
    remaining = [d] * n
    def rec(pos):
        if pos == len(types):
            if all(x == 0 for x in remaining):
                goods = [types[j] for j, count in enumerate(counts) for _ in range(count)]
                yield goods
            return
        typ = types[pos]
        cap = min(remaining[a] for a in typ)
        for x in range(cap+1):
            counts[pos] = x
            for a in typ: remaining[a] -= x
            yield from rec(pos+1)
            for a in typ: remaining[a] += x
        counts[pos] = 0
    yield from rec(0)


def brute_max_common(n, goods):
    # Independent direct allocation census for deliberately tiny examples.
    if len(goods) > 9:
        return None
    best = -1
    for allocation in product(range(n), repeat=len(goods)):
        utilities = [0] * n
        for g, a in enumerate(allocation):
            if a in goods[g]:
                utilities[a] += 1
        if len(set(utilities)) == 1:
            best = max(best, utilities[0])
    return best


def orient_regular(n, goods):
    # Edge-by-edge Euler-balancing via augmenting a directed Euler tour of an
    # arbitrary temporary pairing of odd-degree vertices, then deleting it.
    assert all(len(g) == 2 for g in goods)
    d = sum(0 in g for g in goods)
    assert all(sum(i in g for g in goods) == d for i in range(n))
    edges = [tuple(g) for g in goods]
    odd = [i for i in range(n) if d % 2]
    assert len(odd) % 2 == 0
    edges += [(odd[i], odd[i+1]) for i in range(0, len(odd), 2)]
    adj = [[] for _ in range(n)]
    for eid, (a,b) in enumerate(edges):
        adj[a].append((b,eid)); adj[b].append((a,eid))
    seen = set()
    result = [-1] * len(goods)
    # Traverse each nontrivial component, consuming every edge once.
    for s in range(n):
        stack = [(s,-1)]
        route = []
        while stack:
            v, entering = stack[-1]
            while adj[v] and adj[v][-1][1] in seen:
                adj[v].pop()
            if not adj[v]:
                stack.pop()
                if entering >= 0:
                    route.append((v, entering))
            else:
                w, eid = adj[v].pop()
                seen.add(eid)
                stack.append((w,eid))
        # route lists vertex reached by each incoming edge in reverse Euler order;
        # each associated edge is directed TOWARDS this vertex.
        for v, eid in route:
            if eid < len(goods):
                result[eid] = v
    assert all(x >= 0 for x in result)
    return result


def verify_orientation(n, goods):
    assign = orient_regular(n, goods)
    d = sum(0 in g for g in goods)
    utilities = [sum(a == i for a in assign) for i in range(n)]
    assert set(utilities) <= {d // 2, (d + 1) // 2}
    for i in range(n):
        for j in range(n):
            other = sum(assign[g] == j and i in goods[g] for g in range(len(goods)))
            assert other <= utilities[i] + 1
    assert sum(utilities) == len(goods)  # Pareto optimality witness


def main():
    counts={}
    brute=0
    for n, ds in ((3, range(0, 5)), (4, range(0, 4))):
        for d in ds:
            total=0
            for goods in enumerate_regular(n, d):
                k=verify_instance(n, goods)
                if len(goods) <= 7 and total % 13 == 0:
                    assert brute_max_common(n, goods) == k
                    brute+=1
                if goods and all(len(g)==2 for g in goods):
                    assert k == d // 2
                    verify_orientation(n, goods)
                total+=1
            counts[(n,d)]=total
    # Nonlaminar full-approval graph example, namely K4.
    k4=list(combinations(range(4), 2))
    assert verify_instance(4,k4)==1
    verify_orientation(4,k4)
    # For two agents, the nonapprover hypothesis fails sharply.
    assert brute_max_common(2, [(0,1)]) == -1
    print('VERIFY_OK', 'counts=',counts,'direct_optimum_checks=',brute,
          'K4=',len(k4),'two_agent_exception=confirmed')

if __name__=='__main__':
    main()
