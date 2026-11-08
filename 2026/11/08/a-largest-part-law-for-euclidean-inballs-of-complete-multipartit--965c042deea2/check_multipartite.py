"""Small-case exact checks for complete-multipartite symmetric-edge inballs.
Only Python's standard library is needed; these finite tests do not replace the proof.
"""
from itertools import combinations_with_replacement, product
from fractions import Fraction

def exact_rank(rows,n):
    """Incremental exact reduced echelon basis over rational numbers."""
    basis={}
    for raw in rows:
        v=[Fraction(q) for q in raw]
        for col in sorted(basis):
            if v[col]:
                t=v[col]
                v=[a-t*b for a,b in zip(v,basis[col])]
        pivot=next((i for i,x in enumerate(v) if x),None)
        if pivot is None:continue
        q=v[pivot]
        v=[a/q for a in v]
        for col,b in list(basis.items()):
            if b[pivot]:
                t=b[pivot]
                basis[col]=[a-t*c for a,c in zip(b,v)]
        basis[pivot]=v
        if len(basis)>=n-1:break
    return len(basis)

def test(parts):
    n=sum(parts); group=[j for j,m in enumerate(parts) for _ in range(m)]
    E=[(i,j) for i in range(n) for j in range(i) if group[i]!=group[j]]
    L=max(parts);k=sum(v==L for v in parts)
    B=(n*n)//4; T=n*L-(L%2); M=max(B,T)
    best=-1; far=[]
    for z in product(range(3),repeat=n):
        if min(z):continue
        if any(abs(z[i]-z[j])>1 for i,j in E):continue
        s=sum(z); q=n*sum(v*v for v in z)-s*s
        if q>best: best=q; far=[]
        if q==best:far.append(tuple(n*v-s for v in z))
    assert best==M, ('radius',parts,M,best)
    if T>B: expected=n-1-k*(L-1) if L%2==0 else max(0,n-k*L-1)
    else:expected=0
    actual=n-1-exact_rank(far,n)
    assert actual==expected, ('incenter-dim',parts,expected,actual)
    return actual,len(far)

if __name__=='__main__':
    tested=0;positive=0
    for n in range(3,8):
        for k in range(3,n+1):
            for parts in combinations_with_replacement(range(1,n-k+2),k):
                if sum(parts)!=n: continue
                dim,c=test(parts);tested+=1;positive+=bool(dim)
    for parts in ((3,3,3),(2,2,2,2),(3,3,2),(5,4,1,1),(4,2,2,1),(3,3,3,2)):
        dim,c=test(parts); tested+=1
        print('CHECK',parts,'dim',dim,'contact',c)
    print('MULTIPARTITE_EXACT_CHECKS_PASSED',tested,'nonunique_small',positive)
