"""Independent finite checks for primitive two-cycle counts on full rooted trees.

Model: synchronous, sink-free parallel chip-firing on nonnegative chip heights.
"""
from itertools import product
from math import prod, comb, log, exp


def tree(d, h):
    # Breadth-first labelled full d-ary rooted tree of height h.
    edges = []
    frontier = [0]
    nxt = 1
    for _ in range(h):
        children = []
        for v in frontier:
            for _ in range(d):
                w = nxt
                nxt += 1
                edges.append((v, w))
                children.append(w)
        frontier = children
    return nxt, edges


def orbit_dp(d, h):
    a, b = 0, 1
    for _ in range(h):
        a, b = d*b*(a+b)**(d-1), (a+b)**(d-1)*(a+(d+1)*b)
    return a


def direct_edge_cover_count(d, h):
    nv, edges = tree(d, h)
    total = 0
    hist = [0] * (d+1)
    for mask in range(1 << len(edges)):
        c = [0]*nv
        for i, (u, v) in enumerate(edges):
            if (mask >> i) & 1:
                c[u] += 1
                c[v] += 1
        if all(c):
            weight = prod(c)
            total += weight
            hist[c[0]] += weight
    return total, hist


def microscopic_orbit_count(d, h):
    nv, edges = tree(d, h)
    nbr = [[] for _ in range(nv)]
    for u, v in edges:
        nbr[u].append(v)
        nbr[v].append(u)
    deg = [len(ns) for ns in nbr]
    def update(config):
        firing = [config[v] >= deg[v] for v in range(nv)]
        return tuple(config[v] - deg[v]*firing[v]
                     + sum(firing[w] for w in nbr[v]) for v in range(nv))
    count = 0
    configs = 0
    for cfg in product(*(range(2*x) for x in deg)):
        configs += 1
        y = update(cfg)
        if y != cfg and update(y) == cfg:
            count += 1
    assert count % 2 == 0
    return count//2, configs


def main():
    cover_cases = [(2,1),(2,2),(2,3),(3,1),(3,2),(4,1),(4,2),(5,1)]
    for d, h in cover_cases:
        a = orbit_dp(d, h)
        b, hist = direct_edge_cover_count(d, h)
        assert a == b, (d, h, a, b)
        aa, bb = 0, 1
        for _ in range(h-1):
            aa, bb = d*bb*(aa+bb)**(d-1), (aa+bb)**(d-1)*(aa+(d+1)*bb)
        predicted = [0]+[k*comb(d,k)*bb**k*aa**(d-k) for k in range(1,d+1)]
        assert hist == predicted, (d,h,hist,predicted)
        print(f'EDGE_COVER d={d} h={h} orbits={a} root_hist={hist} OK')
    micro_cases = [(2,1),(2,2),(3,1),(4,1)]
    for d, h in micro_cases:
        a = orbit_dp(d, h)
        b, configs = microscopic_orbit_count(d,h)
        assert a == b, (d, h, a, b)
        print(f'MICRO d={d} h={h} confined_configs={configs} orbits={b} OK')
    vals=[orbit_dp(2,h) for h in range(1,6)]
    assert vals==[2,30,9350,859413750,7323520810533593750], vals
    print('BINARY_SEQUENCE', vals)
    d=2
    r=0.0
    partial=0.0
    for j in range(48):
        partial += d**(-j-1)*log((1+r)**(d-1)*(d+1+r))
        r = d/(d+1+r)
    lower = exp((d-1)/d*partial)
    upper = exp((d-1)/d*partial+log(2**(d-1)*(d+2))*d**(-48)/d)
    assert lower < 2.043244 < upper+0.000001
    print(f'ENTROPY d=2 lower={lower:.13f} upper={upper:.13f} (mathematical tail inequality)')
    print('FULL_TREE_CHIP_CYCLES_VERIFY_OK')


if __name__ == '__main__':
    main()
