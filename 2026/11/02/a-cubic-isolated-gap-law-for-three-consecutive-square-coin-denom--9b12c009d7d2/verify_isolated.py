"""Independent exact Apéry/GCD enumeration for isolated gaps of three consecutive squares.
Run with Python 3; no external dependencies.
"""
import heapq

def dijkstra_apery(a, b, c):
    best = [None] * a
    best[0] = 0
    heap = [(0, 0)]
    while heap:
        value, residue = heapq.heappop(heap)
        if best[residue] != value:
            continue
        for step in (b, c):
            nxt = (residue + step) % a
            val = value + step
            if best[nxt] is None or val < best[nxt]:
                best[nxt] = val
                heapq.heappush(heap, (val, nxt))
    assert all(v is not None for v in best)
    return best

def independent_count(aper, a):
    height = [(v - r) // a for r, v in enumerate(aper)]
    assert height[0] == 0
    return (sum(max(0, height[r] - max(height[r-1], height[r+1]))
                for r in range(1, a-1))
            + max(0, height[-1] - height[-2]))

def proposed_apery(n):
    k = (n-3)//4
    L = 4*(n-1)
    a,b,c = n*n, (n+1)**2, (n+2)**2
    values = [None] * a
    for r in range(k+1):
        for q in range(L+1 if r == 0 else L):
            w = q*b + r*c
            residue = w % a
            assert values[residue] is None
            values[residue] = w
    assert all(v is not None for v in values)
    return values

def main():
    total = 0
    for n in range(3, 84, 4):
        a, b, c = n*n, (n+1)**2, (n+2)**2
        aper = dijkstra_apery(a,b,c)
        assert aper == proposed_apery(n), n
        got = independent_count(aper, a)
        assert got == n**3 + 1, (n,got)
        total += a
    # Completely separate membership/singleton checks for two starting examples.
    for n in (3, 7, 11):
        a,b,c = n*n,(n+1)**2,(n+2)**2
        aper = dijkstra_apery(a,b,c)
        bound=max(aper)
        representable=[(v>=aper[v%a]) for v in range(bound+2)]
        direct=sum(not representable[i] and representable[i-1] and representable[i+1]
                   for i in range(1,bound+1))
        assert direct == n**3+1, (n,direct)
    print('PASS: 21 parameters n=3,7,...,83; {} Apéry residues; independent Dijkstra, candidate representatives, heights; 3 brute membership cases.'.format(total))

if __name__=='__main__': main()
