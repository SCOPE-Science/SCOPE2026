"""Exact small-field checks of the adjoint-rank polynomial for radical-square-zero quiver algebras.

Run: python3 graph_rank_verify.py
Uses Python's standard library only. Finite tests are not proofs of universal assertions.
"""
from collections import Counter
from itertools import product, combinations
from math import comb


def rank_mod_p(rows, p):
    rows = [list(v) for v in rows]
    if not rows:
        return 0
    nr, nc = len(rows), len(rows[0]); r = 0
    for c in range(nc):
        pivot = next((i for i in range(r, nr) if rows[i][c] % p), None)
        if pivot is None: continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        inv = pow(rows[r][c] % p, -1, p)
        rows[r] = [(a * inv) % p for a in rows[r]]
        for i in range(nr):
            if i != r and rows[i][c] % p:
                t = rows[i][c]
                rows[i] = [(a - t*b) % p for a,b in zip(rows[i], rows[r])]
        r += 1
        if r == nr: break
    return r


def components(n, edges, selected):
    parent = list(range(n))
    def find(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    for k,(u,v) in enumerate(edges):
        if selected & (1 << k):
            u,v = find(u),find(v)
            parent[u] = v
    return len({find(i) for i in range(n)})


def matroid_rank(n, edges, mask):
    return n-components(n, edges, mask)


def spectral_by_flats(n, edges, q):
    m = len(edges); answer = Counter()
    for F in range(1 << m):
        rF = matroid_rank(n, edges, F)
        if any(matroid_rank(n, edges, F | (1<<k)) == rF
               for k in range(m) if not(F >> k & 1)):
            continue
        # Proper colorings of contraction equal exact-zero-set colorings.
        chrom = 0
        for coloring in product(range(q), repeat=n):
            if all(((coloring[u] == coloring[v]) == bool(F >> k & 1))
                   for k,(u,v) in enumerate(edges)):
                chrom += 1
        for S in range(1 << m):
            if S & ~F: continue
            answer[m-F.bit_count()+matroid_rank(n, edges, S)] += (
                chrom*q**(m-F.bit_count())*(q-1)**S.bit_count())
    return Counter({k:v for k,v in answer.items() if v})


def spectral_by_support(n, edges, q):
    m = len(edges); answer = Counter()
    for coloring in product(range(q), repeat=n):
        zero = sum((1 << k) for k,(u,v) in enumerate(edges)
                   if coloring[u] == coloring[v])
        for S in range(1 << m):
            if S & ~zero: continue
            answer[m-zero.bit_count()+matroid_rank(n, edges, S)] += (
                q**(m-zero.bit_count())*(q-1)**S.bit_count())
    return answer


def spectral_by_direct_ranks(n, edges, q):
    m = len(edges); result = Counter()
    for d in product(range(q), repeat=n):
        for x in product(range(q), repeat=m):
            rows=[]
            for k,(u,v) in enumerate(edges):
                a = [0]*(n+m)
                a[u] = -x[k] % q
                a[v] = x[k] % q
                a[n+k] = (d[u]-d[v]) % q
                rows.append(a)
            result[rank_mod_p(rows, q)] += 1
    return result


def brute_commuting(n, edges, q):
    m = len(edges); total=0
    elem=list(product(range(q), repeat=n+m))
    for a in elem:
        for b in elem:
            if all(((a[u]-a[v])*b[n+k] - (b[u]-b[v])*a[n+k]) % q == 0
                   for k,(u,v) in enumerate(edges)):
                total += 1
    return total


def check_case(name,n,edges,q,direct=True,brute=False):
    a = spectral_by_flats(n,edges,q)
    b = spectral_by_support(n,edges,q)
    assert a==b,(name,q,a,b)
    if direct:
        c = spectral_by_direct_ranks(n,edges,q)
        assert a==c,(name,q,a,c)
    assert sum(a.values())==q**(n+len(edges)),(name,q,a)
    commuting=sum(v*q**(n+len(edges)-r) for r,v in a.items())
    if brute: assert commuting == brute_commuting(n,edges,q)
    print(name,q,sorted(a.items()),'commuting=',commuting)
    return a


def main():
    triangle=[(0,1),(1,2),(2,0)]
    path=[(0,1),(1,2),(2,3)]
    star=[(0,1),(0,2),(0,3)]
    square=[(0,1),(1,2),(2,3),(3,0)]
    diamond=[(0,1),(1,2),(2,0),(0,3),(2,3)]
    for name,n,edges,q,brute in [
        ('edge',2,[(0,1)],2,True),
        ('triangle',3,triangle,2,True),
        ('triangle',3,triangle,3,True),
        ('path',4,path,2,True),
        ('star',4,star,2,True),
        ('square',4,square,2,True),
        ('diamond',4,diamond,2,False),
        ('path',4,path,3,False),
        ('star',4,star,3,False),
        ('square',4,square,3,False),
    ]:
        poly=check_case(name,n,edges,q,brute=brute)
        if name in ('path','star'):
            expected=Counter({k:q*comb(3,k)*(q*q-1)**k for k in range(4)})
            assert poly==expected,(name,q,poly,expected)
    # K5 over F2 cannot achieve full rank: at least three vertices share a color.
    K5=list(combinations(range(5),2)); a=spectral_by_flats(5,K5,2)
    assert max(a)==9 and len(K5)==10,(max(a),a)
    assert a == spectral_by_direct_ranks(5,K5,2)
    assert a == spectral_by_flats(5,[(v,u) if k%2 else (u,v) for k,(u,v) in enumerate(K5)],2)
    print('K5',2,'max_rank=',max(a),'radical_dim=',len(K5))
    print('VERIFY_OK')

if __name__=='__main__': main()
