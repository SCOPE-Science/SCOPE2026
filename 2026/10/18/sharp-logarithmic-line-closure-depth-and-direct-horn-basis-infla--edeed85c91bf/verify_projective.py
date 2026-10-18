"""Self-contained finite checks for projective closure implication formulas (prime fields)."""
from itertools import product, combinations
from math import comb, factorial, ceil, log2
from functools import lru_cache


def projective_points(p,d):
    pts=[]
    for v in product(range(p),repeat=d):
        if not any(v):continue
        first=next(x for x in v if x)
        inv=pow(first,-1,p)
        norm=tuple((inv*x)%p for x in v)
        if norm not in pts:pts.append(norm)
    return pts

def testing(p,d):
    pts=projective_points(p,d)
    N=len(pts); index={v:i for i,v in enumerate(pts)}
    @lru_cache(None)
    def span(mask):
        vectors=[pts[i] for i in range(N) if (mask>>i)&1]
        space={(0,)*d}
        for v in vectors:
            space={tuple((a[j]+c*v[j])%p for j in range(d)) for a in space for c in range(p)}
        got=0
        for v in space:
            if any(v):
                first=next(x for x in v if x)
                norm=tuple(x*pow(first,-1,p)%p for x in v)
                got|=1<<index[norm]
        return got
    # exact pseudo-intent definition: all proper pseudo-intents Q have cl(Q) within S
    pseudos=[]; clp=[]
    bysize=sorted(range(1<<N),key=lambda x:x.bit_count())
    for S in bysize:
        if span(S)==S:continue
        if all(not (Q & S == Q) or clQ & ~S == 0 for Q,clQ in zip(pseudos,clp)):
            pseudos.append(S);clp.append(span(S))
    assert len(pseudos)==comb(N,2),(p,d,len(pseudos),comb(N,2))
    assert all(S.bit_count()==2 for S in pseudos)
    grouped=unit=0
    bysize_counts={}
    for S in range(1<<N):
        roots=span(S)&~S
        bitset=S
        while bitset:
            bit=bitset & -bitset
            roots &= ~span(S^bit)
            bitset ^=bit
        if roots:
            grouped+=1;unit+=roots.bit_count(); bysize_counts[S.bit_count()]=bysize_counts.get(S.bit_count(),0)+1
    total_grouped=total_unit=0
    for r in range(2,d+1):
        independent=1
        for j in range(r):independent*= N -(p**j-1)//(p-1)
        assert independent%factorial(r)==0
        independent//=factorial(r)
        total_grouped+=independent
        total_unit+=independent*(p-1)**(r-1)
        assert bysize_counts.get(r,0)==independent,(p,d,r,bysize_counts.get(r,0),independent)
    assert (grouped,unit)==(total_grouped,total_unit),(p,d,grouped,unit,total_grouped,total_unit)
    # For basis subset selected as independent coordinate axes, exact worst synchronous rounds.
    S=sum(1<<index[tuple(int(i==j) for i in range(d))] for j in range(d))
    rounds=0;X=S
    while X!=span(S):
        new=X
        indices=[i for i in range(N) if X>>i&1]
        for a,b in combinations(indices,2):new |= span((1<<a)|(1<<b))
        assert new!=X
        X=new;rounds+=1
    assert rounds==ceil(log2(d)),(p,d,rounds)
    # Exhaustive closure and two-round upper bound for every S at rank <=3; higher dim chosen samples.
    samples=range(1<<N) if d==3 else [0,1,(1<<N)-1,S]+[(i*11939+12637)%(1<<N) for i in range(100)]
    for S0 in samples:
        X=S0
        for _ in range(ceil(log2(d))):
            new=X
            ids=[i for i in range(N) if X>>i&1]
            for a,b in combinations(ids,2): new |=span((1<<a)|(1<<b))
            X=new
        assert X==span(S0),(p,d,S0,X,span(S0))
    print('OK',f'PG({d-1},{p})','points',N,'pseudo_intents',len(pseudos),'direct_grouped',grouped,'direct_unit',unit,'max_rounds',rounds,'subsets',len(samples))

if __name__=='__main__':
 for p,d in [(2,3),(3,3),(2,4)]:testing(p,d)
