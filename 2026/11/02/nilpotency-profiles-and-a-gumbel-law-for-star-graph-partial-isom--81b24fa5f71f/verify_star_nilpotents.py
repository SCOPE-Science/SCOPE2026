"""Independent enumerator for nilpotent partial isometries of finite stars.
Uses raw partial maps, metric tests, and direct iteration; no theorem classification.
"""
from itertools import combinations, permutations
from math import factorial, comb
from collections import Counter

def explicit(m):
    n=m+1
    rank_index=Counter()
    total_isometries=0
    vertices=tuple(range(n))
    for r in range(n+1):
        for domain in combinations(vertices,r):
            for image in combinations(vertices,r):
                for perm in permutations(image):
                    f=dict(zip(domain,perm))
                    if any((1 if (a==0 or b==0) else 2) !=
                           (1 if (f[a]==0 or f[b]==0) else 2)
                           for a,b in combinations(domain,2)):
                        continue
                    total_isometries+=1
                    # A partial injection is nilpotent iff its directed graph
                    # has no directed cycle. Calculate the index without theory.
                    current=f
                    for k in range(1,n+2):
                        if not current:
                            rank_index[(r,k)]+=1
                            break
                        current={a:f[b] for a,b in current.items() if b in f}
    return total_isometries,rank_index

def predicted(m):
    # coefficient m![z^m] exp(sum_{j=1}^L u^{j-1} z^j)
    # via combinatorial recurrence of labelled sequences of chains.
    out=Counter()
    last=Counter()
    for L in range(1,m+1):
        dp=Counter({(0,0):1})
        for v in range(1,m+1):
            for j in range(1,min(v,L)+1):
                # component containing the least-labelled vertex is an
                # ordered path of length j: choose j-1 other labels, order all j.
                for (nr,ru),cnt in list(dp.items()):
                    if nr==v-j:
                        dp[(v,ru+j-1)]+=cnt*comb(v-1,j-1)*factorial(j)
        cur=Counter({r:val for (v,r),val in dp.items() if v==m})
        for r,val in cur.items():
            diff=val-last[r]
            if diff:out[(r,L)]=diff
        last=cur
    out[(1,2)]+=2*m
    out[(2,3)]+=m*(m-1)
    return out

def rook(m):
    return sum(comb(m,r)*comb(m-1,r)*factorial(r) for r in range(m))

def sym_partial(m):
    return sum(comb(m,r)**2*factorial(r) for r in range(m+1))

if __name__=='__main__':
    for m in range(1,6):
        got_n,got=explicit(m)
        expect=predicted(m)
        expect_n=2*sym_partial(m)+m*m+2*m
        assert got_n==expect_n,(m,got_n,expect_n)
        assert got==expect,(m,got,expect)
        assert sum(got.values())==rook(m)+m*(m+1)
        print('m=',m, 'isometries=',got_n,'nilpotents=',sum(got.values()),'nilpotency profile=',dict(sorted(got.items())))
    print('VERIFY_OK')
