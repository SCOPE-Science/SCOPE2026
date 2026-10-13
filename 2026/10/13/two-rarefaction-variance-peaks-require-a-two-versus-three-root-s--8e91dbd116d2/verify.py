#!/usr/bin/env python3
"""Exact checks of rooted ultrametric five-tip rarefaction identities.
Only Python 3 standard library is required; all arithmetic is rational.
"""
from fractions import Fraction as Q
from itertools import combinations

N=4
zero=(Q(0),)*N

def basis(i):
    return tuple(Q(int(j==i)) for j in range(N))

def add(a,b):
    return tuple(x+y for x,y in zip(a,b))

def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))

def scale(a,c):
    return tuple(c*x for x in a)

def merge(*args):
    z=zero
    for a in args:z=add(z,a)
    return z

def mask_edges(tree):
    edges=[]
    def recurse(node,parent=None):
        if isinstance(node,int):
            mask=1<<node;height=zero
        else:
            left,right,height=node
            lm=recurse(left,height)
            rm=recurse(right,height)
            mask=lm|rm
        if parent is not None:
            edges.append((mask,sub(parent,height)))
        return mask
    assert recurse(tree)==31
    return edges

def pd_values(tree,k):
    edges=mask_edges(tree)
    out=[]
    for inds in combinations(range(5),k):
        S=sum(1<<i for i in inds)
        val=zero
        for mask,weight in edges:
            if S&mask:val=add(val,weight)
        out.append(val)
    return out

def quadratic(values):
    mean=scale(merge(*values),Q(1,len(values)))
    out={}
    for vec in values:
        d=sub(vec,mean)
        for i in range(N):
            for j in range(i,N):
                c=d[i]*d[j]*(1 if i==j else 2)/len(values)
                out[(i,j)]=out.get((i,j),Q(0))+c
    return {key:value for key,value in out.items() if value}

def diff(P,Q):
    return {i: P.get(i,0)-Q.get(i,0) for i in set(P)|set(Q) if P.get(i,0)!=Q.get(i,0)}

def scaled(P,c):return {key:c*v for key,v in P.items() if v}

def expected(d):return {key:Q(value) for key,value in d.items() if value}

def eq(P,Q):
    assert P==expected(Q),(P,expected(Q))

# x1,...,x4 are consecutive positive coalescence-time increments.
x1,x2,x3,x4=map(basis,range(4))
t1=x1;t2=merge(x1,x2);t3=merge(x1,x2,x3);H=merge(x1,x2,x3,x4)
comb=(0,(4,(3,(1,2,t1),t2),t3),H)
balanced=(0,((1,2,t1),(3,4,t2),t3),H)
Vcomb={k:quadratic(pd_values(comb,k)) for k in (2,3)}
Vbal={k:quadratic(pd_values(balanced,k)) for k in (2,3)}
eq(scaled(diff(Vcomb[3],Vcomb[2]),100),{
    (1,1):12,(1,2):18,(1,3):8,(2,2):15,(2,3):12})
eq(scaled(diff(Vbal[3],Vbal[2]),25),{
    (1,1):3,(1,2):2,(1,3):2,(2,2):2,(2,3):4})

# Coordinates now H,a,b,c: A cherry age a, B cherry age b,
# B three-tip ancestral age c, root age H.
H,a,b,c=map(basis,range(4))
two_three=((0,1,a),(2,(3,4,b),c),H)
V={k:quadratic(pd_values(two_three,k)) for k in range(1,6)}
assert V[1]=={} and V[5]=={}
eq(scaled(diff(V[2],V[3]),100),{
    (0,0):15,(0,1):-18,(0,2):2,(0,3):-14,
    (1,1):-12,(1,2):16,(1,3):26,
    (2,2):-12,(2,3):6,(3,3):-9})
eq(scaled(diff(V[4],V[3]),100),{
    (0,0):-9,(0,1):-6,(0,2):14,(0,3):10,
    (1,1):3,(1,2):-14,(1,3):14,
    (2,2):3,(2,3):-6,(3,3):-9})

def evalq(P,coords):
    return sum(coeff*coords[i]*coords[j] for (i,j),coeff in P.items())
values={k:evalq(V[k],(10,1,6,7)) for k in range(1,6)}
assert values=={1:Q(0),2:Q(789,100),3:Q(171,25),4:Q(174,25),5:Q(0)},values

# Independent direct tabulation with actual positive branch lengths.
e=mask_edges(two_three)
EW=[(bit,sum(weight[i]*[10,1,6,7][i] for i in range(4))) for bit,weight in e]
assert len(EW)==8 and all(weight>0 for bit,weight in EW)
for k in range(1,6):
    obs=[]
    for inds in combinations(range(5),k):
        sample=sum(1<<i for i in inds)
        obs.append(sum(length for bit,length in EW if bit&sample))
    avg=Q(sum(obs),len(obs))
    v=sum((Q(x)-avg)**2 for x in obs)/len(obs)
    assert v==values[k],(k,v,values[k])
print('VERIFY_OK identities=4 exact_subset_profiles=5 witness_positive_edges=8')
