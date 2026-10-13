"""Standalone exact checks for minimal forts in triangular graphs."""
from collections import Counter
from itertools import combinations
from math import comb, factorial


def candidate_type(n, edges, mask):
    deg = [0] * n
    incident = [[] for _ in range(n)]
    for j, (u,v) in enumerate(edges):
        if mask >> j & 1:
            deg[u] += 1
            deg[v] += 1
            incident[u].append(v)
            incident[v].append(u)
    if min(deg) >= 1:
        if all(deg[u] == 1 or deg[v] == 1 for j,(u,v) in enumerate(edges) if mask >> j & 1):
            return 'star_forest'
    if 0 in deg and all(d in (0,2) for d in deg):
        root = next((v for v,d in enumerate(deg) if d==2), None)
        if root is None:
            return None
        seen = {root}
        todo = [root]
        while todo:
            v = todo.pop()
            for w in incident[v]:
                if w not in seen:
                    seen.add(w)
                    todo.append(w)
        if len(seen) == sum(d==2 for d in deg):
            return 'proper_cycle'
    return None


def direct_enumerate(n):
    edges = list(combinations(range(n),2))
    m = len(edges)
    E = (1<<m)-1
    adjacent = [0]*m
    for a,(u,v) in enumerate(edges):
        for b,(s,t) in enumerate(edges):
            if a!=b and (u==s or u==t or v==s or v==t):
                adjacent[a] |= (1<<b)
    fort = bytearray(1<<m)
    has_proper = bytearray(1<<m)
    hist=Counter()
    count=Counter()
    for mask in range(1,1<<m):
        outside = E ^ mask
        isfort = True
        while outside:
            bit = outside & -outside
            e = bit.bit_length()-1
            if (adjacent[e] & mask).bit_count() == 1:
                isfort = False
                break
            outside -= bit
        fort[mask] = isfort
        subs = mask
        while subs:
            bit = subs & -subs
            submask=mask^bit
            if fort[submask] or has_proper[submask]:
                has_proper[mask] = 1
                break
            subs -= bit
        direct_min = bool(isfort and not has_proper[mask])
        kind=candidate_type(n,edges,mask) if direct_min else None
        if direct_min and kind is None:
            raise AssertionError(('missing predicted type',n,mask))
        if direct_min:
            hist[mask.bit_count()] +=1
            count[kind]+=1
        if n<=6 and not direct_min:
            predicted=candidate_type(n,edges,mask)
            if predicted is not None:
                raise AssertionError(('spurious candidate',n,mask,predicted))
    return hist, count


def star_forest_polys(max_n):
    # Labelled SET construction, computed by choosing the component of vertex zero.
    # component size s=2 has 1 labelled star, s>=3 has s rooted stars.
    S=[Counter() for _ in range(max_n+1)]
    S[0][0]=1
    for n in range(1,max_n+1):
        for size in range(2,n+1):
            ways=comb(n-1,size-1) * (1 if size==2 else size)
            for k,v in S[n-size].items():
                S[n][k+size-1] += ways*v
    return S


def predicted_coeffs(n, S):
    c=Counter(S[n])
    for length in range(3,n):
        c[length] += comb(n,length)*factorial(length-1)//2
    return +c


if __name__=='__main__':
    max_n=20
    star=star_forest_polys(max_n)
    total=0
    for n in range(2,8):
        got, kinds=direct_enumerate(n)
        expected=predicted_coeffs(n,star)
        assert got==expected, (n,got,expected)
        total += 1<<comb(n,2)
        print(f'n={n} minimal={sum(got.values())} star={kinds["star_forest"]} proper_cycle={kinds["proper_cycle"]} polynomial={dict(sorted(got.items()))}')
    for n in range(2,max_n+1):
        c=predicted_coeffs(n,star)
        assert c and min(c)>=1 and max(c)<=n-1
        assert all(v>0 for v in c.values())
    print(f'PASS: exact full-subset minimal-fort comparisons n=2..7, {total} subsets, labelled component recurrences n<=20')
