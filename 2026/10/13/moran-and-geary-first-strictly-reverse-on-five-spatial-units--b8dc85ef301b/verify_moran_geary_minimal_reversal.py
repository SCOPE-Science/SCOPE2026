#!/usr/bin/env python3
from itertools import combinations, permutations
from fractions import Fraction

EXPECTED_CONNECTED_UNLABELED = {2:1,3:2,4:6,5:21}
EXPECTED_REVERSAL_CLASSES = {2:0,3:0,4:0,5:11}


def edge_list(n):
    return list(combinations(range(n),2))


def graph_from_mask(n,mask):
    edges=edge_list(n)
    adj=[set() for _ in range(n)]
    for i,(u,v) in enumerate(edges):
        if (mask>>i)&1:
            adj[u].add(v); adj[v].add(u)
    return adj


def connected(n,mask):
    if n==0: return False
    adj=graph_from_mask(n,mask)
    seen={0}; stack=[0]
    while stack:
        u=stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v); stack.append(v)
    return len(seen)==n


def canonical_mask(n,mask):
    edges=edge_list(n)
    idx={e:i for i,e in enumerate(edges)}
    raw=[]
    for i,(u,v) in enumerate(edges):
        if (mask>>i)&1:
            raw.append((u,v))
    best=None
    for p in permutations(range(n)):
        m2=0
        for u,v in raw:
            a,b=sorted((p[u],p[v]))
            m2 |= 1<<idx[(a,b)]
        if best is None or m2<best:
            best=m2
    return best


def unlabeled_connected_masks(n):
    E=len(edge_list(n))
    reps=set()
    for mask in range(1<<E):
        if connected(n,mask):
            reps.add(canonical_mask(n,mask))
    return sorted(reps)


def metrics(n,mask,bits):
    adj=graph_from_mask(n,mask)
    m=sum(len(a) for a in adj)//2
    S0=2*m
    vals=[(bits>>i)&1 for i in range(n)]
    k=sum(vals)
    assert 0<k<n
    mean=Fraction(k,n)
    z=[Fraction(v)-mean for v in vals]
    den=sum(v*v for v in z)
    mor_num=Fraction(0)
    geary_num=Fraction(0)
    for u in range(n):
        for v in adj[u]:
            mor_num += z[u]*z[v]
            geary_num += (Fraction(vals[u])-Fraction(vals[v]))**2
    I=Fraction(n,S0)*mor_num/den
    C=Fraction(n-1,2*S0)*geary_num/den
    return I,C


def binary_formula(n,mask,bits):
    adj=graph_from_mask(n,mask)
    m=sum(len(a) for a in adj)//2
    ones={i for i in range(n) if (bits>>i)&1}
    k=len(ones)
    q=0
    for u,v in edge_list(n):
        if v in adj[u] and ((u in ones)!=(v in ones)):
            q+=1
    s=sum(len(adj[u]) for u in ones)
    I=Fraction(2*k*k*m + n*(n-2*k)*s - n*n*q, 2*k*m*(n-k))
    C=Fraction(n*(n-1)*q, 2*m*k*(n-k))
    return I,C


def has_reversal(n,mask):
    vals=[]
    for bits in range(1,(1<<n)-1):
        vals.append((bits,*metrics(n,mask,bits)))
    for (b1,I1,C1),(b2,I2,C2) in combinations(vals,2):
        if (I1-I2)*(C1-C2)>0:
            return True,(b1,I1,C1,b2,I2,C2)
    return False,None


def is_regular(n,mask):
    adj=graph_from_mask(n,mask)
    ds={len(a) for a in adj}
    return len(ds)==1

# Complete unlabeled graph census through n=5, independently canonicalized.
reps_by_n={n:unlabeled_connected_masks(n) for n in range(2,6)}
reversal_class_counts={}
for n in range(2,6):
    reps=reps_by_n[n]
    assert len(reps)==EXPECTED_CONNECTED_UNLABELED[n], (n,len(reps))
    rc=0
    for mask in reps:
        # direct definitions vs closed binary formulas
        for bits in range(1,(1<<n)-1):
            assert metrics(n,mask,bits)==binary_formula(n,mask,bits)
        yes,_=has_reversal(n,mask)
        rc += int(yes)
        if is_regular(n,mask):
            # Regular graph identity for every nonconstant binary field.
            for bits in range(1,(1<<n)-1):
                I,C=metrics(n,mask,bits)
                assert C == Fraction(n-1,n)*(1-I)
    reversal_class_counts[n]=rc
    assert rc==EXPECTED_REVERSAL_CLASSES[n], (n,rc)

# General identity checked exhaustively on binary fields for every connected graph class n<=5.
for n in range(2,6):
    for mask in reps_by_n[n]:
        adj=graph_from_mask(n,mask)
        m=sum(len(a) for a in adj)//2
        S0=2*m
        deg=[len(a) for a in adj]
        for bits in range(1,(1<<n)-1):
            vals=[(bits>>i)&1 for i in range(n)]
            mean=Fraction(sum(vals),n)
            z=[Fraction(v)-mean for v in vals]
            den=sum(v*v for v in z)
            I,C=metrics(n,mask,bits)
            weighted=sum(Fraction(deg[i])*z[i]*z[i] for i in range(n))/den
            rhs=Fraction(n-1,S0)*weighted - Fraction(n-1,n)*I
            assert C==rhs

# P5 witness.
def path_mask(n):
    edges=edge_list(n); idx={e:i for i,e in enumerate(edges)}
    m=0
    for i in range(n-1):
        m |= 1<<idx[(i,i+1)]
    return m

pm=path_mask(5)
# A: endpoint singleton at vertex 4 -> 00001 in order 0..4
A=1<<4
# B: adjacent internal pair vertices 2,3 -> 00110 if printed left-to-right 0..4
B=(1<<2)|(1<<3)
assert metrics(5,pm,A)==(Fraction(-1,16),Fraction(5,8))
assert metrics(5,pm,B)==(Fraction(1,24),Fraction(5,6))
assert (metrics(5,pm,A)[0]-metrics(5,pm,B)[0])*(metrics(5,pm,A)[1]-metrics(5,pm,B)[1])>0

# Explicit path family algebra for all n>=5.
for n in range(5,501):
    IA=Fraction(-1,(n-1)*(n-1))
    CA=Fraction(n,2*(n-1))
    IB=Fraction(n*n-4*n-4,2*(n-1)*(n-2))
    CB=Fraction(n,2*(n-2))
    assert IB>IA and CB>CA
    assert IB-IA == Fraction(n*(n*n-5*n+2),2*(n-2)*(n-1)*(n-1))

print('VERIFY_OK')
print('connected_unlabeled_counts', EXPECTED_CONNECTED_UNLABELED)
print('reversal_class_counts', reversal_class_counts)
print('P5_A', metrics(5,pm if False else path_mask(5),1<<4))
print('P5_B', metrics(5,path_mask(5),(1<<2)|(1<<3)))
print('path_family_checked_n_5_to_500')
