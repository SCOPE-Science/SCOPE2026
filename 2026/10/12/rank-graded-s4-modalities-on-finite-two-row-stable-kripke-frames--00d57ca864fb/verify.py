#!/usr/bin/env python3
"""Exact finite verification of two-row S4 interior-operator rank polynomials.

Uses only the Python standard library. Exhaustive bounds are explicit in main().
"""
from collections import Counter
from itertools import product
from math import comb

assertions = 0

def check(ok, message):
    global assertions
    assertions += 1
    if not ok:
        raise AssertionError(message)


def points(n):
    return tuple((a,j) for a in range(2) for j in range(n))


def lattice(n):
    pts=points(n)
    index={x:i for i,x in enumerate(pts)}
    meet=[[index[(min(x[0],y[0]), min(x[1],y[1]))]
           for y in pts] for x in pts]
    join=[[index[(max(x[0],y[0]), max(x[1],y[1]))]
           for y in pts] for x in pts]
    return pts,meet,join


def bound_sublattices(n):
    pts,meet,join=lattice(n)
    N=len(pts); bot=0; top=N-1
    internal=[i for i in range(N) if i not in (bot,top)]
    histogram=Counter()
    accepted=[]
    for word in range(1<<len(internal)):
        mask=(1<<bot)|(1<<top)
        for b,i in enumerate(internal):
            if word>>b&1: mask|=1<<i
        members=[i for i in range(N) if mask>>i&1]
        good=all((mask>>meet[i][j]&1) and (mask>>join[i][j]&1)
                 for i in members for j in members)
        if good:
            histogram[len(members)]+=1
            accepted.append(mask)
    return histogram,accepted


def predicted(n):
    h=Counter()
    for m in range(2,n+1):
        for c in range(m+1):
            words=m-c+1-(2 if c==0 else 0)
            h[m+c]+=comb(n-2,m-2)*words
    return +h


def word_classification(n,mask):
    seq=[]
    for j in range(n):
        low=(mask>>j)&1; high=(mask>>(n+j))&1
        if low or high: seq.append('C' if low and high else ('A' if low else 'B'))
    return (mask&1)!=0 and ((mask>>(2*n-1))&1)!=0 and (
        all({'A':0,'C':1,'B':2}[seq[i]] <= {'A':0,'C':1,'B':2}[seq[i+1]] for i in range(len(seq)-1)))


def make_interior(n,mask,meet,join):
    N=2*n
    S=[i for i in range(N) if mask>>i&1]
    results=[]
    for x in range(N):
        below=[s for s in S if meet[x][s]==s]
        assert below
        t=below[0]
        for y in below[1:]:t=join[t][y]
        results.append(t)
    return tuple(results)


def is_interior(f,meet,join):
    N=len(f)
    if f[-1]!=N-1: return False
    for x in range(N):
        if meet[x][f[x]]!=f[x] or f[f[x]]!=f[x]:return False
    for x in range(N):
        for y in range(N):
            if f[meet[x][y]]!=meet[f[x]][f[y]]:return False
    return True


def gf_polys(nmax):
    # Expands the claimed rational bivariate generating function exactly.
    # G(z,u)=u^2*(1+u-z*(1+u+u^2))^2/
    #          [(1-z*(1+u))^2*(1-z*(1+u^2))].
    # Represent polynomials as Counter(exponent -> coefficient).
    def mul(a,b):
        ans=Counter()
        for i,x in a.items():
            for j,y in b.items():ans[i+j]+=x*y
        return {i:c for i,c in ans.items() if c}
    def scale(a,k):return {x:y*k for x,y in a.items()}
    a={0:1,1:1} # 1+u
    b={0:1,1:1,2:1}
    d={0:1,1:1}
    e={0:1,2:1}
    ans=[]
    for q in range(nmax-1):
        # coefficient of z^q of numerator: z^0 u²*a², z^1 -2u²*a*b, z² u²*b²
        numerator=[mul(a,a),scale(mul(a,b),-2),mul(b,b)]
        coeff=Counter()
        for delta in range(min(q,2)+1):
            t=q-delta
            for j in range(t+1):
                # (1-z*d)^-2 coefficient (j+1)d^j;
                # (1-z*e)^-1 coefficient e^(t-j)
                poly={0:1}
                for _ in range(j):poly=mul(poly,d)
                for _ in range(t-j):poly=mul(poly,e)
                poly=mul(poly,numerator[delta])
                for p,c in poly.items():coeff[p+2]+=(j+1)*c
        ans.append(+coeff)
    return ans


def main():
    total_subsets=0; total_sublattices=0; operator_tables=0
    prev=None
    for n in range(2,9):
        hist,subsets=bound_sublattices(n)
        pred=predicted(n)
        check(hist==pred,('rank polynomial',n,hist,pred))
        total_subsets+=1<<(2*n-2)
        total_sublattices+=len(subsets)
        check(len(subsets)==sum(hist.values()),('total',n))
        check(set(hist)==set(range(2,2*n+1)),('support',n))
        check(hist[2]==1 and hist[2*n]==1 and hist[2*n-1]==2,
              ('boundary ranks',n))
        check(hist[3]==2*(n-1),('rank three',n))
        check(sum(hist.values())==((n*n+11*n+6)*(1<<(n-2)))//8,
              ('ungraded count',n))
        allmasks=set(subsets)
        # Test the word condition against *every* bounded subset, not only sublattices.
        for rest in range(1<<(2*n-2)):
            internal=[i for i in range(2*n) if i not in (0,2*n-1)]
            mask=(1<<0)|(1<<(2*n-1))
            for b,i in enumerate(internal):
                if rest>>b&1:mask|=1<<i
            check((mask in allmasks)==word_classification(n,mask),
                  ('word classification',n,mask))
        # Test every constructed interior operator on the small and medium cases.
        if n<=6:
            _,meet,join=lattice(n)
            for mask in subsets:
                f=make_interior(n,mask,meet,join)
                check(is_interior(f,meet,join),('operator axioms',n,mask))
                check(sum(f[i]==i for i in range(2*n))==mask.bit_count(),
                      ('fixset rank',n,mask))
                operator_tables+=1
        prev=hist
    # Unrestricted full operator tables, independent from fixed-set construction.
    # 4^4 + 6^6 = 46912 candidate functions.
    for n in (2,3):
        _,meet,join=lattice(n)
        h=Counter()
        N=2*n
        for entries in product(range(N),repeat=N):
            if is_interior(entries,meet,join):
                h[len(set(i for i in range(N) if entries[i]==i))]+=1
        check(h==predicted(n),('unrestricted maps',n,h,predicted(n)))
    for n,poly in enumerate(gf_polys(10),start=2):
        check(poly==predicted(n),('bivariate rational generating function',n,poly,predicted(n)))
    stable,modal_ranks=stable_bimodule_small_case()
    print('VERIFY_OK',assertions,'exact assertions;',total_subsets,
          'bounded subset candidates exhaustively tested through n=8;',
          total_sublattices,'bounded sublattices through n=8;',
          operator_tables,'interior operator tables checked through n=6;',
          '46912 unrestricted function tables screened through n=3;',
          '65536 stable-bimodule candidates screened (16 stable, 4 S4) on n=2;',
          'bivariate generating function checked through n=10')

def stable_bimodule_small_case():
    """Directly screen all 2^(4*4) relations on C2 x C2 for S4 stable frames."""
    global assertions
    n=2
    pts,meet,join=lattice(n)
    N=len(pts)
    top=N-1
    leq=lambda x,y: meet[x][y]==x
    filters=[{w for w in range(N) if leq(x,w)} for x in range(N)]
    def relation_valid(R):
        def rr(w,v):return bool(R>>(w*N+v)&1)
        # stable (iv), stable (ii)
        if any(rr(top,v)!=(v==top) for v in range(N)):return False
        if any(not rr(w,top) for w in range(N)):return False
        # bimodule monotonicity
        for w in range(N):
            for v in range(N):
                if rr(w,v):
                    for wp in range(N):
                        if leq(wp,w):
                            for vp in range(N):
                                if leq(v,vp) and not rr(wp,vp):return False
        # stable (i)
        for w in range(N):
            for v1 in range(N):
                for v2 in range(N):
                    if rr(w,v1) and rr(w,v2) and not rr(w,meet[v1][v2]):
                        return False
        # stable (iii)
        for w1 in range(N):
            for w2 in range(N):
                for v in range(N):
                    if rr(meet[w1][w2],v):
                        if not any(rr(w1,v1) and rr(w2,v2) and leq(meet[v1][v2],v)
                                   for v1 in range(N) for v2 in range(N)):
                            return False
        return True
    stable=0; s4=Counter(); distinct_maps=set()
    for R in range(1<<(N*N)):
        if not relation_valid(R):continue
        stable+=1
        outputs=[]
        for F in filters:
            of={w for w in range(N) if all(not(R>>(w*N+v)&1) or v in F for v in range(N))}
            check(of in filters,('box not filter',R,of))
            outputs.append(filters.index(of))
        # outputs are indices of filters ordered by reverse W; relabel as
        # elements of L_n through coordinate order reversal.
        rev=lambda i:pts.index((1-pts[i][0],n-1-pts[i][1]))
        f=tuple(rev(outputs[rev(i)]) for i in range(N))
        if is_interior(f,meet,join):
            s4[len({i for i in range(N) if f[i]==i})]+=1
            distinct_maps.add(f)
    check(s4==predicted(n),('direct stable relation check',stable,s4,predicted(n)))
    check(len(distinct_maps)==sum(s4.values()),'distinct modal operators')
    return stable,s4

if __name__=='__main__':
    main()
