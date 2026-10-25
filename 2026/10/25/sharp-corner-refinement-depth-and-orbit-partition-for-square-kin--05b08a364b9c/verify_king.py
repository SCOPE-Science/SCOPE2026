"""Reproducible finite corroboration for corner-marked king-graph refinement."""
from collections import Counter, defaultdict


def run(n):
    vertices = [(i,j) for i in range(n) for j in range(n)]
    edges = {v: [w for w in vertices if w != v and max(abs(w[0]-v[0]),abs(w[1]-v[1])) == 1] for v in vertices}
    colors = {v: (0 if v == (0,0) else 1) for v in vertices}
    counts = [len(set(colors.values()))]
    for r in range(1,n+1):
        keys = {v: (colors[v],tuple(sorted(Counter(colors[w] for w in edges[v]).items()))) for v in vertices}
        alphabet = {key:k for k,key in enumerate(sorted(set(keys.values())))}
        new = {v:alphabet[keys[v]] for v in vertices}
        colors = new
        counts.append(len(set(colors.values())))
        for i in range(r+1):
            if r < n and i < n:
                pass
        if r <= n-1:
            inside = {v for v in vertices if max(v) <= r}
            seen = {}
            for v in inside:
                sig = tuple(sorted(v))
                c = colors[v]
                assert c not in seen or seen[c] == sig, (n,r,v,seen.get(c))
                seen[c] = sig
            assert all(colors[w] not in seen for w in vertices if w not in inside), (n,r,"global unique")
        if r == n-1:
            for v in vertices:
                for w in vertices:
                    assert (colors[v] == colors[w]) == (sorted(v) == sorted(w)), (n,v,w)
            assert len(set(colors.values())) == n*(n+1)//2
            assert all(colors[v] == colors[(v[1],v[0])] for v in vertices)
        if r==n:
            assert colors == prior_colors, (n, 'not stable at n-1')
        prior_colors = colors.copy()
    assert len(set(colors.values())) == n*(n+1)//2
    assert colors[(0,n-1)] != colors[(n-1,n-1)]
    # Symmetry lower bound: before the final strict round the two outer corners still agree.
    x,y=(0,n-1),(n-1,n-1)
    cols={v:(0 if v==(0,0) else 1) for v in vertices}
    for r in range(n-1):
        assert cols[x] == cols[y], (n,r)
        keys={v:(cols[v],tuple(sorted(Counter(cols[w] for w in edges[v]).items()))) for v in vertices}
        alphabet={key:k for k,key in enumerate(sorted(set(keys.values())))}
        cols={v:alphabet[keys[v]] for v in vertices}
    assert cols[x] != cols[y]
    return n,len(vertices),counts


def main():
    rows=[run(n) for n in range(3,16)]
    for n,order,counts in rows:
        print('n=%d vertices=%d colors_round_0_to_n=%s' % (n,order,','.join(map(str,counts))))
    print('ALL_TESTS_PASS n=3..15 (13 exact classifications, layer separation, lower-bound pairs, fixed-point rounds)')

if __name__ == '__main__':main()
