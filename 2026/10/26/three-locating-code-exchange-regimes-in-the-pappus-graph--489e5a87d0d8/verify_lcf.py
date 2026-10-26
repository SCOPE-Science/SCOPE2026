"""Exhaustive locating-code and exchange check from the 18-cycle LCF model."""
from collections import Counter, deque
from itertools import combinations

N = 18
steps = (5, 7, -7, 7, -7, -5) * 3
adj = [0] * N
for v in range(N):
    for w in ((v + 1) % N, (v - 1) % N, (v + steps[v]) % N):
        adj[v] |= 1 << w
        adj[w] |= 1 << v
assert all(x.bit_count() == 3 for x in adj)


def good(s, kind):
    if kind == 'LD':
        signatures = [adj[v] & s for v in range(N) if not (s >> v) & 1]
    elif kind == 'ID':
        signatures = [(adj[v] | (1 << v)) & s for v in range(N)]
    else:
        signatures = [adj[v] & s for v in range(N)]
    return 0 not in signatures and len(set(signatures)) == len(signatures)


def minimum(kind):
    for k in range(N + 1):
        codes = []
        for c in combinations(range(N), k):
            s = sum(1 << v for v in c)
            if good(s, kind):
                codes.append(s)
        if codes:
            return k, codes
    raise AssertionError(kind)


def graph(codes):
    ix = {c: i for i, c in enumerate(codes)}
    H = [set() for _ in codes]
    for i, s in enumerate(codes):
        for v in range(N):
            if (s >> v) & 1:
                rem = s ^ (1 << v)
                for u in range(N):
                    if not (s >> u) & 1:
                        j = ix.get(rem | (1 << u))
                        if j is not None and j != i:
                            H[i].add(j)
    assert all(i in H[j] for i, ns in enumerate(H) for j in ns)
    return H


def components(H):
    left = set(range(len(H)))
    out = []
    while left:
        i = min(left); seen = {i}; q = deque([i]); left.remove(i)
        while q:
            u = q.popleft()
            for v in H[u]:
                if v not in seen:
                    seen.add(v); q.append(v); left.remove(v)
        out.append(seen)
    return sorted(out, key=lambda s: -len(s))


def eccentricities(H):
    ecc = []
    for a in range(len(H)):
        d = {a: 0}; q = deque([a])
        while q:
            u = q.popleft()
            for v in H[u]:
                if v not in d:
                    d[v] = d[u] + 1
                    q.append(v)
        ecc.append(max(d.values()) if len(d) == len(H) else None)
    return Counter(ecc)


def ordered(d):
    return dict(sorted(d.items()))


def main():
    A = [1, 3, 5, 7, 9, 11, 13, 15, 17]
    assert all(not ((adj[x] >> y) & 1) for x in A for y in A)
    for kind, minsize, count, edges, sizes in [
        ('LD', 6, 18, 0, [1] * 18),
        ('ID', 9, 1028, 3780, [514, 514]),
        ('OLD', 10, 2025, 13770, [2025]),
    ]:
        k, codes = minimum(kind)
        H = graph(codes)
        cc = components(H)
        assert (k, len(codes), sum(map(len,H))//2, list(map(len,cc))) == (minsize,count,edges,sizes)
        print(kind, 'minimum', k, 'codes',len(codes),'edges',sum(map(len,H))//2,'components',list(map(len,cc)))
        print(kind,'degrees',ordered(Counter(map(len,H))))
        if len(cc)==1:
            ec=eccentricities(H)
            print(kind,'eccentricities',ordered(ec))
        if kind=='ID':
            comps=[ordered(Counter(sum((s>>a)&1 for a in A) for i,s in enumerate(codes) if i in comp)) for comp in cc]
            print('ID component X-part counts',comps)
            assert {tuple(c) for c in comps}=={tuple(range(0,5)),tuple(range(5,10))}
            assert [sum(len(H[i]&component) for i in component)//2 for component in cc]==[1890,1890]
        if kind=='OLD':
            assert ordered(eccentricities(H))=={6:729,7:972,8:324}
            assert ordered(Counter(map(len,H)))=={12:729,14:972,16:324}
    print('ALL_LCF_CHECKS_PASS')

if __name__=='__main__': main()
