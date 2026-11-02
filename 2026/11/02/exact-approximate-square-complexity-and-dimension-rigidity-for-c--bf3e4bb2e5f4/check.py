"""Finite exact cross-checks for a deleted-symbol column-tree survivor system.
Scientific statements are proved analytically; these are regression examples.
"""
import math,random,itertools

def check_case(m,n,A,seed,depth):
    B=sorted(set(a for a,b in A))
    assert 2<=m<n and len(B)>=2 and all(sum(a==c for a,b in A)>=2 for c in B)
    rng=random.Random(seed)
    levels={():[()]}
    labels={}
    columns=[()]
    for k in range(depth):
        for v in columns:
            labels[v]=rng.choice(A)
        columns=[v+(b,) for v in columns for b in B]
    words=[()]
    for k in range(1,depth+1):
        words=[w+(digit,) for w in words for digit in A if digit!=labels[tuple(a for a,b in w)]]
        theta=math.floor(k*math.log(m)/math.log(n)+1e-12)
        cells={(tuple(a for a,b in w[:k]),tuple(b for a,b in w[:theta])) for w in words}
        expected=(len(A)-1)**theta*len(B)**(k-theta)
        assert len(words)==(len(A)-1)**k,(k,len(words))
        assert len(cells)==expected,(k,len(cells),expected)
    return (m,n,len(A),len(B),seed,depth)

if __name__=='__main__':
    A1=[(0,0),(0,1),(0,3),(1,1),(1,2),(2,0),(2,3)]
    A2=[(0,0),(0,1),(1,2),(1,3)]
    tests=[check_case(3,4,A1,seed,5) for seed in range(4)]
    tests +=[check_case(2,5,A2,seed,6) for seed in range(4)]
    for t in tests:print('PASS',*t)
    # Check the deterministic algebraic equality/strictness of the
    # weighted concavity inequality for rationally-described count vectors.
    for counts in [(2,2),(3,2),(2,2,2),(3,2,2),(4,4,4)]:
        R=len(counts);T=sum(counts)-1
        lam=math.log(2)/math.log(5)
        boxmass=(R**(1-lam))*(T**lam)
        for J in range(R):
            survivors=[v-(b==J) for b,v in enumerate(counts)]
            hm=sum(v**lam for v in survivors)
            assert hm<=boxmass+1e-10
            assert (abs(hm-boxmass)<1e-10)==(len(set(survivors))==1)
    print('ALL_CHECKS_PASS')
