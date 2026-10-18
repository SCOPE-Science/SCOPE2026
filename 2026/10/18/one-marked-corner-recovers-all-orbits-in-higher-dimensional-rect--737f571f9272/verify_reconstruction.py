"""Check the exact predecessor-deck and joint-pair reconstruction identities."""
from itertools import product, combinations_with_replacement
from collections import Counter
from math import prod

def signature(v, cap):
    return Counter(v), Counter(L-x for x,L in zip(v,cap))

def recover(deck, dimension, max_level):
    p=len(deck)
    if not p: return Counter({0:dimension})
    S=Counter()
    for card in deck:S.update(card)
    c=Counter({0:dimension-p})
    c[1]=S[0]-p*c[0]
    for j in range(1,max_level): c[j+1]=S[j]-(p-1)*c[j]
    assert all(a>=0 for a in c.values())
    return +c

def delta_card(base,card):
    return Counter(card)-Counter(base),Counter(base)-Counter(card)


def check(dims):
    cap=tuple(n-1 for n in dims)
    d=len(dims)
    for v in product(*[range(n) for n in dims]):
        A,B=signature(v,cap)
        lower=[];upper=[]
        for i in range(d):
            if v[i]>0:
                u=list(v);u[i]-=1;lower.append(signature(tuple(u),cap))
            if v[i]<cap[i]:
                u=list(v);u[i]+=1;upper.append(signature(tuple(u),cap))
        recA=recover([x for x,y in lower],d,max(cap)+1)
        recB=recover([y for x,y in upper],d,max(cap)+1)
        assert recA==A and recB==B,(dims,v,A,B,recA,recB)
        pairs=[]
        for x,y in lower:
            neg=Counter(A)-Counter(x)
            pos=Counter(y)-Counter(B)
            # inspect signed differences, rather than only positive histogram subtraction
            aa=[j for j in A if A[j]-x[j]==1]
            bb=[j for j in set(B)|set(y) if y[j]-B[j]==1]
            assert len(aa)==1 and len(bb)==1
            a=aa[0];b=bb[0]-1
            assert a>0 and b>=0 and x[a-1]==A[a-1]+1 and y[b]==B[b]-1
            pairs.append((a,b))
        for x,y in upper:
            aa=[j for j in set(A)|set(x) if x[j]-A[j]==1]
            bb=[j for j in B if B[j]-y[j]==1]
            assert len(aa)==1 and len(bb)==1
            # If the increased A coordinate had old value zero, then
            # the successor card reveals the missing zero-coordinate pair.
            a=aa[0]-1
            b=bb[0]
            if a==0:pairs.append((a,b))
        assert Counter(pairs)==Counter((x,L-x) for x,L in zip(v,cap)),(dims,v,pairs)

if __name__=='__main__':
    cases=points=0
    for d in range(3,6):
        for dims in combinations_with_replacement(range(2,6),d):
            if prod(dims)>1500:continue
            check(dims);cases+=1;points+=prod(dims)
    print('PASS deck identities and joint reconstruction:',cases,'parameter tuples,',points,'vertices')
