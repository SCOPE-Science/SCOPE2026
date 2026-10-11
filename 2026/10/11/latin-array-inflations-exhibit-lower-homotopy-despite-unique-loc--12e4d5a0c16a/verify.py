"""Exact binary boundary and face-count checks for parity-check simplicial complexes."""
from itertools import combinations, product
from math import comb

def faces(n,q):
    result=[[] for _ in range(n)]
    for k in range(1,n+1):
        for inds in combinations(range(n),k):
            for vals in product(range(q),repeat=k):
                if k<n or sum(vals)%q==0:
                    result[k-1].append(tuple(zip(inds,vals)))
    return result

def rank_mod2(rows):
    basis={}
    for v in rows:
        while v:
            p=v.bit_length()-1
            if p in basis:v^=basis[p]
            else:
                basis[p]=v
                break
    return len(basis)

def checks(n,q):
    ff=faces(n,q)
    ranks=[]
    for k in range(1,n):
        older={f:i for i,f in enumerate(ff[k-1])}
        rows=[0]*len(ff[k-1])
        for col,face in enumerate(ff[k]):
            for i in range(len(face)):
                rows[older[face[:i]+face[i+1:]]]^=(1<<col)
        ranks.append(rank_mod2(rows))
    b=[0]*n
    for k in range(n):
        d_lower=ranks[k-1] if k>0 else 1
        d_upper=ranks[k] if k<n-1 else 0
        b[k]=len(ff[k])-d_lower-d_upper
    expected=(q-1)*(q**(n-1)-(q-1)**(n-1))
    assert b==([0]*(n-2)+[expected,0] if n>=3 else [expected,0]),(n,q,b,expected)
    assert len(ff[-1])==q**(n-1)
    for inds in combinations(range(n),n-1):
        for vals in product(range(q),repeat=n-1):
            assert sum(1 for facet in ff[-1] if all((i,a) in facet for i,a in zip(inds,vals)))==1
    return n,q,list(map(len,ff)),ranks,b
if __name__=='__main__':
    total=0
    for q in (2,3,4):
        for n in range(2,6):
            if n==5 and q==4:continue
            print(checks(n,q))
            total+=1
    print('VERIFY_OK',total)
