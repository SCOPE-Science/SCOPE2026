#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations


def traceable(u_parent, u_child, v_edge, p, pi):
    return v_edge <= p or (u_parent <= pi and u_child <= pi)


def check_predicate_nesting():
    grid = [Fraction(i, 4) for i in range(5)]
    for up in grid:
        for uc in grid:
            for ve in grid:
                for p1 in grid:
                    for p2 in grid:
                        if p1 > p2:
                            continue
                        for q1 in grid:
                            for q2 in grid:
                                if q1 > q2:
                                    continue
                                if traceable(up, uc, ve, p1, q1) and not traceable(up, uc, ve, p2, q2):
                                    raise AssertionError('traceability predicate is not nested')


def simulate(tree, trace_edges):
    # tree[v] = (parent, birth_time, recover_time, diagnose_time).
    # Times are absolute Fractions. A vertex is born only if its parent is active at birth_time.
    children = {v: [] for v in tree}
    for v, (par, bt, rt, dt) in tree.items():
        if par is not None:
            children[par].append(v)
    infected = {0}
    active = {0}
    recovered = set()
    events = []
    for v, (par, bt, rt, dt) in tree.items():
        if par is not None:
            events.append((bt, 0, 'birth', v))
        events.append((rt, 1, 'recover', v))
        events.append((dt, 2, 'diagnose', v))
    events.sort()

    def component(seed):
        seen = {seed}
        stack = [seed]
        while stack:
            x = stack.pop()
            par = tree[x][0]
            if par is not None and par in infected:
                e = tuple(sorted((par, x)))
                if e in trace_edges and par not in seen:
                    seen.add(par); stack.append(par)
            for c in children[x]:
                if c in infected:
                    e = tuple(sorted((x, c)))
                    if e in trace_edges and c not in seen:
                        seen.add(c); stack.append(c)
        return seen

    for t, _, kind, v in events:
        par, bt, rt, dt = tree[v]
        if kind == 'birth':
            if par in active:
                infected.add(v); active.add(v)
        elif kind == 'recover':
            if v in active:
                active.remove(v); recovered.add(v)
        elif kind == 'diagnose':
            if v not in active:
                continue
            comp = component(v)
            active.difference_update(comp)
            # Recovered infected vertices remain in `infected` and can transmit tracing through the graph.
    return frozenset(infected)


def check_finite_pruning():
    # Two deterministic event trees chosen to exercise sibling branches, backward tracing,
    # and a recovered intermediate that remains a tracing conduit.
    F = Fraction
    trees = [
        {
            0:(None,F(0),F(20),F(20)),
            1:(0,F(1),F(12),F(8)),
            2:(0,F(2),F(5),F(20)),
            3:(1,F(3),F(20),F(6)),
            4:(2,F(4),F(20),F(9)),
            5:(4,F(7),F(20),F(20)),
        },
        {
            0:(None,F(0),F(30),F(30)),
            1:(0,F(1),F(4),F(30)),  # recovers but can remain a tracing conduit
            2:(1,F(2),F(30),F(10)),
            3:(0,F(3),F(30),F(30)),
            4:(2,F(5),F(30),F(7)),
            5:(3,F(6),F(30),F(12)),
        },
    ]
    for tree in trees:
        edges = [tuple(sorted((par,v))) for v,(par,_,_,_) in tree.items() if par is not None]
        subsets = []
        for r in range(len(edges)+1):
            for comb in combinations(edges,r):
                subsets.append(frozenset(comb))
        for weak in subsets:
            iw = simulate(tree, weak)
            for strong in subsets:
                if not weak.issubset(strong):
                    continue
                is_ = simulate(tree, strong)
                if not is_.issubset(iw):
                    raise AssertionError((weak,strong,iw,is_))


if __name__ == '__main__':
    check_predicate_nesting()
    check_finite_pruning()
    print('VERIFY_OK')
