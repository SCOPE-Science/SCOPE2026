"""Finite checks of Boolean support and of the layer-wise decay bound."""
from itertools import combinations
from math import prod


def activate(s, edges):
    result = 0
    for target, parents in edges:
        if all(s & (1 << j) for j in parents):
            result |= 1 << target
    return result


def layers(n, edges):
    result = [(1 << n) - 1]
    while True:
        s = result[-1]
        nxt = activate(s, edges)
        assert (s & nxt) == nxt
        if nxt == s:
            return result
        result.append(nxt)


def check_small_patterns():
    n = 4
    possible = [(i, parents) for i in range(n)
                for parents in combinations((j for j in range(n) if j != i), 2)]
    assert len(possible) == 12
    fixed_count = empty_count = 0
    for mask in range(1 << len(possible)):
        edges = [e for k, e in enumerate(possible) if mask & (1 << k)]
        core = layers(n, edges)[-1]
        empty_count += core == 0
        union = 0
        for s in range(1 << n):
            if activate(s, edges) != s:
                continue
            fixed_count += 1
            union |= s
            for i in range(n):
                scale_times_input = sum(target == i and all(s & (1 << j) for j in parents)
                                        for target, parents in edges)
                # With unit weights and tau=4, each active term contributes
                # exactly one to tau*P_i at q=1/2 on the support. The response
                # z/(1+z) is at least 1/2 iff z>=1, and zero iff z=0.
                if s & (1 << i):
                    assert scale_times_input >= 1
                else:
                    assert scale_times_input == 0
        assert union == core
    print(f'Checked {1 << len(possible)} patterns, {fixed_count} Boolean fixed supports, {empty_count} empty cores')


def check_layer_bounds():
    edges = [(0, (1, 2)), (1, (2, 3)), (3, (4, 0)), (4, (0, 1))]
    active = layers(5, edges)
    assert active == [31, 27, 24, 0]
    h, tau = 0.04, 5.0  # Unit recoveries, unit weights, and L=1.
    rho = 1 - h
    coeff = [1.0]
    for _ in active[2:]:
        coeff.append(1 + (h * tau / rho) * coeff[-1])
    x = [0.9, 0.4, 0.7, 0.8, 0.1]
    for t in range(101):
        assert all(0 <= v <= 1 for v in x)
        for k, s in enumerate(active[1:], start=1):
            bound = coeff[k - 1] * (1 + t)**(k - 1) * rho**t
            for i, v in enumerate(x):
                if not s & (1 << i):
                    assert v <= bound * (1 + 1e-12), (k, i, t, v, bound)
        nxt = [rho * v for v in x]
        for i, parents in edges:
            nxt[i] += h * tau * (1 - x[i]) * prod(x[j] for j in parents)
        x = nxt
    print('Checked layer envelopes for V_0,V_1,V_2,V_3 =', active, 'at times 0 through 100')


if __name__ == '__main__':
    check_small_patterns()
    check_layer_bounds()
