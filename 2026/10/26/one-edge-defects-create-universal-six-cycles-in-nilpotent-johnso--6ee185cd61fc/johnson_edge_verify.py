"""Reproducibility check: single-edge deletion in binary Johnson XOR dynamics.
Only finite checks; infinite proof supplied separately in mathematical result."""
from itertools import combinations
from math import comb
from random import Random

def rank(rows):
    piv={}
    for row in rows:
        x=row
        while x:
            p=x.bit_length()-1
            if p not in piv:
                piv[p]=x
                break
            x^=piv[p]
    return len(piv)

def build(n,k):
    subs=list(combinations(range(n),k))
    N=len(subs)
    adj=[]
    for i,s in enumerate(subs):
        a=sum(1<<j for j,t in enumerate(subs) if len(set(s)&set(t))==k-1)
        adj.append(a)
    u=0
    v=(adj[0]&-adj[0]).bit_length()-1
    arr=adj.copy();arr[u]^=1<<v;arr[v]^=1<<u
    return adj,arr,u,v

def apply(rows,x):
    return sum((((r&x).bit_count()&1)<<i) for i,r in enumerate(rows))

def power2(rows):
    ans=[]
    for r in rows:
        z=0
        while r:
            t=r&-r
            z^=rows[t.bit_length()-1]
            r^=t
        ans.append(z)
    return ans

def product(X,Y):
    ans=[]
    for r in X:
        z=0
        while r:
            t=r&-r
            z^=Y[t.bit_length()-1]
            r^=t
        ans.append(z)
    return ans

def verify(n,k,exhaustive=False):
    A,B,u,v=build(n,k);N=len(A);r=comb(n-2,k-1)
    assert rank(A)==r and rank(B)==r+2,(n,k,rank(A),rank(B),r)
    A2=power2(A)
    assert not any(A2),(n,k,'A^2 !=0')
    B2=power2(B)
    assert rank(B2)==4,(n,k,rank(B2))
    B3=product(B2,B)
    B4=power2(B2)
    B6=product(B4,B2)
    # B^8 = B^2 (because B restricted to image B^2 has order 6)
    B8=power2(B4)
    assert B8==B2,(n,k,'B^8 != B^2')
    # rank/kernel of B^3 + I on recurrent subspace: dimension 2
    cols=[1<<u,1<<v,apply(A,1<<u),apply(A,1<<v)]
    assert rank(cols)==4
    for col in cols: assert apply(B6,col)==col
    persistent=set()
    U={0}
    for col in cols:U|={x^col for x in list(U)}
    assert len(U)==16
    three={x for x in U if apply(B3,x)==x}
    assert len(three)==4
    fixed={x for x in U if apply(B,x)==x}
    assert fixed=={0}
    assert all(apply(B6,x)==x for x in U)
    # independent population through t=0,1,2
    expected=(16,2**(N-r+2),2**N)
    if exhaustive:
        counts=[0]*3
        for x in range(1<<N):
            a=x
            for t in range(3):
                if a in U:
                    counts[t]+=1
                    break
                a=apply(B,a)
        assert tuple((sum(counts[:j+1]) for j in range(3)))==expected,(n,k,counts,expected)
    else:
        rng=Random(41929+n*100+k)
        for _ in range(500):
            x=rng.randrange(1<<N)
            y=apply(B2,x)
            assert y in U
            assert apply(B6,y)==y
    print('CHECK', n,k,'vertices',N,'rank_A',r,'rank_B',rank(B),'rank_B2',rank(B2),'periods',len(fixed),len(three)-len(fixed),len(U)-len(three),'cumulative_depths',expected,'exhaustive',exhaustive)

if __name__=='__main__':
    for n,k,ex in [(4,2,True),(6,2,True),(6,4,True),(8,2,False),(8,4,False),(8,6,False),(10,2,False),(10,4,False),(10,6,False)]:verify(n,k,ex)
    print('JOHNSON_EDGE_DEFECT_VERIFY_OK')
