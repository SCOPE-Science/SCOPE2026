"""Independent checks of the strong-odd coloring count for finite ladders."""
from collections import defaultdict
from itertools import product


def ladder(n):
    assert n >= 2
    # Vertex 2*i is the upper vertex of rung i; 2*i+1 is the lower.
    g = [set() for _ in range(2*n)]
    edges = [(2*i, 2*i+1) for i in range(n)]
    edges += [(2*i+r, 2*(i+1)+r) for i in range(n-1) for r in range(2)]
    for u,v in edges:
        g[u].add(v)
        g[v].add(u)
    return [tuple(sorted(a)) for a in g], edges


def is_strong_odd(colors, graph, edges):
    if any(colors[a] == colors[b] for a,b in edges):
        return False
    for neighbors in graph:
        occur = {}
        for v in neighbors:
            c = colors[v]
            occur[c] = occur.get(c, 0) + 1
        if any(z % 2 == 0 for z in occur.values()):
            return False
    return True


def is_square_proper(colors, graph, edges):
    if any(colors[a] == colors[b] for a,b in edges):
        return False
    for neighbors in graph:
        if len(set(colors[v] for v in neighbors)) != len(neighbors):
            return False
    return True


def falling_four(k):
    return k*(k-1)*(k-2)*(k-3)


def formula(n, k):
    return falling_four(k) * (k*k-7*k+13)**(n-2)


def brute(n, k):
    graph, edges = ladder(n)
    count = 0
    sqcount = 0
    for colors in product(range(k), repeat=2*n):
        a = is_strong_odd(colors, graph, edges)
        b = is_square_proper(colors, graph, edges)
        assert a == b, (n,k,colors,a,b)
        count += a
        sqcount += b
    return count, sqcount, k**(2*n)


def odd_neighbor_ok(colors):
    freq = {}
    for c in colors: freq[c] = freq.get(c, 0) + 1
    return all(m % 2 for m in freq.values())


def state_count(n,k):
    # Independent transfer recurrence directly using properness and
    # the odd-neighborhood test; no square-coloring characterization.
    columns = [(u,v) for u in range(k) for v in range(k) if u != v]
    states = defaultdict(int)
    for a in columns:
        for b in columns:
            if a[0] == b[0] or a[1] == b[1]: continue
            if not odd_neighbor_ok([a[1],b[0]]): continue
            if not odd_neighbor_ok([a[0],b[1]]): continue
            states[(a,b)] += 1
    for _ in range(2,n):
        ns = defaultdict(int)
        for (a,b), count in states.items():
            for c in columns:
                if b[0] == c[0] or b[1] == c[1]:continue
                if not odd_neighbor_ok([a[0], b[1], c[0]]):continue
                if not odd_neighbor_ok([a[1], b[0], c[1]]):continue
                ns[(b,c)] += count
        states = ns
    return sum(v for (a,b),v in states.items()
               if odd_neighbor_ok([a[0],b[1]])
               and odd_neighbor_ok([a[1],b[0]]))


def main():
    cases = [(2,k) for k in range(2,9)]
    cases += [(3,k) for k in range(2,7)]
    cases += [(4,k) for k in range(2,6)]
    cases += [(5,k) for k in range(2,5)]
    total=0
    for n,k in cases:
        count, square, raw = brute(n,k)
        assert count == square == formula(n,k),(n,k,count,square,formula(n,k))
        total += raw
    transfer_cases=0
    for n in range(2,17):
        for k in range(2,9):
            value=state_count(n,k)
            assert value == formula(n,k),(n,k,value,formula(n,k))
            transfer_cases+=1
    for k in range(2,20):
        assert formula(2,k) == falling_four(k)
        if k>=4:
            assert formula(10,k) == formula(9,k)*(k*k-7*k+13)
    print(f"VERIFICATION_OK brute_cases={len(cases)} raw_assignments={total} transfer_cases={transfer_cases} test_lengths=2..16 palettes=2..8")

if __name__ == '__main__': main()
