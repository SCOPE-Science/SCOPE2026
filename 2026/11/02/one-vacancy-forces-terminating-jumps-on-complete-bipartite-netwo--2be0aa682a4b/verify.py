"""Exact arithmetic checks for jump dynamics on complete bipartite networks.

Run: python verify.py.  Requires only Python 3.9+ standard library.
"""
from fractions import Fraction as Q
from collections import defaultdict
import random


def peak(f, lam):
    return f / lam if f <= lam else (1 - f) / (1 - lam)


def ratio(state, vertex, left_size):
    color = state[vertex]
    assert color[0] in ('R', 'B')
    neighbor_range = range(left_size, len(state)) if vertex < left_size else range(left_size)
    occupied = [state[v] for v in neighbor_range if state[v] != '.']
    return Q(1 + sum(c[0] == color[0] for c in occupied), 1 + len(occupied))


def step(state, src, dst, left_size, lam):
    assert state[dst] == '.' and state[src] != '.'
    before = peak(ratio(state, src, left_size), lam)
    out = list(state)
    out[dst] = state[src]
    out[src] = '.'
    after = peak(ratio(out, dst, left_size), lam)
    return tuple(out), before, after


def witness():
    # K_{3,3}: left a1,a2,a3; right b1,b2,b3.
    # Initially R1 at a1, R2 at b1, R3 at b2, B at b3.
    state = ('R1', '.', '.', 'R2', 'R3', 'B')
    initial = state
    lam = Q(9, 20)
    moves = [(3, 1), (5, 2), (1, 3), (2, 5)]
    target = [(Q(0), Q(20, 33)), (Q(20, 27), Q(10, 11)),
              (Q(0), Q(20, 33)), (Q(20, 27), Q(10, 11))]
    for (src, dst), (expected_before, expected_after) in zip(moves, target):
        state, before, after = step(state, src, dst, 3, lam)
        assert (before, after) == (expected_before, expected_after), (before, after)
        assert after > before
    assert state == initial
    return target


def macro_states(s, t, red, blue):
    # State (vacancy_part, number_of_red_in_left), vacancy_part in ('A','B').
    ans = []
    for v in ('A', 'B'):
        left_count = s - (v == 'A')
        right_count = t - (v == 'B')
        for x in range(red + 1):
            y = left_count - x
            if 0 <= y <= blue and 0 <= red - x <= right_count and 0 <= blue - y <= right_count:
                ans.append((v, x))
    return ans


def endpoints(states):
    S = set(states)
    edges = set()
    for v, x in S:
        if v == 'A':
            for w in [('B', x), ('B', x+1)]:
                if w in S:edges.add(frozenset(((v, x), w)))
    return edges


def actual_edges(s, t, red, blue, util_red, util_blue):
    S = macro_states(s, t, red, blue)
    directed = set()
    for vacancy, x in S:
        left = s - (vacancy == 'A')
        right = t - (vacancy == 'B')
        y = left - x
        reds_right = red - x
        blues_right = blue - y
        if vacancy == 'A':
            for color, count, same_left, U in [('R', reds_right, x, util_red),
                                                ('B', blues_right, y, util_blue)]:
                if not count:continue
                old = U(Q(1+same_left, 1+left))
                new = U(Q(count, right))
                dest = ('B', x + (color == 'R'))
                assert dest in S
                if new > old:directed.add(((vacancy, x), dest))
        else:
            for color, count, same_right, U in [('R', x, reds_right, util_red),
                                                 ('B', y, blues_right, util_blue)]:
                if not count:continue
                old = U(Q(1+same_right, 1+right))
                new = U(Q(count, left))
                dest = ('A', x - (color == 'R'))
                assert dest in S
                if new > old:directed.add(((vacancy, x), dest))
    return S, directed


def assert_acyclic(states, directed):
    neighbors = defaultdict(list)
    for a,b in directed: neighbors[a].append(b)
    done = set(); active = set()
    def search(u):
        if u in active:raise AssertionError('directed cycle')
        if u in done:return
        active.add(u)
        for v in neighbors[u]:search(v)
        active.remove(u);done.add(u)
    for u in states:search(u)


def sweep():
    checked = 0
    random_generator = random.Random(12345678)
    for red in range(1, 10):
        for blue in range(1, red + 1):
            for s in range(1, red + blue + 1):
                t = red + blue + 1 - s
                S = macro_states(s, t, red, blue)
                E = endpoints(S)
                assert len(S) <= 2 * (blue + 1)
                assert len(E) <= max(0, len(S) - 1)
                for lam in [Q(1, 10), Q(9, 20), Q(1, 2), Q(4, 5)]:
                    U = lambda z, lam=lam: peak(z, lam)
                    nodes, arcs = actual_edges(s, t, red, blue, U, U)
                    assert nodes == S
                    assert all(frozenset((a,b)) in E for a,b in arcs)
                    assert all((b,a) not in arcs for a,b in arcs)
                    assert_acyclic(S, arcs)
                    checked += 1
                # Independent arbitrary color-dependent payoffs, not necessarily unimodal.
                Ur = {Q(i,j):Q(random_generator.randrange(10000),10000)
                      for j in range(1,red+blue+2) for i in range(j+1)}
                Ub = {Q(i,j):Q(random_generator.randrange(10000),10000)
                      for j in range(1,red+blue+2) for i in range(j+1)}
                nodes, arcs = actual_edges(s,t,red,blue,Ur.__getitem__,Ub.__getitem__)
                assert all(frozenset((a,b)) in E for a,b in arcs)
                assert all((b,a) not in arcs for a,b in arcs)
                assert_acyclic(S,arcs)
                checked += 1
    return checked


if __name__ == '__main__':
    print('Exact four-step improving cycle:', witness())
    print('One-vacancy macro-dynamics instances checked:', sweep())
    print('PASS')
