"""Exact rational checks of finite-tree epidemic variance identity and extremizers.

Scientific objects only: an infection starts at vertex zero and each vertex
has an independently sampled conditional outward-edge probability Q in {1/4,3/4}.
"""
from fractions import Fraction as F
from itertools import product
from math import comb

Q=(F(1,4),F(3,4))
q=sum(Q)/2
v=sum(z*z for z in Q)/2-q*q
assert q==F(1,2) and v==F(1,16)

def moment(k,s):
    return sum((z**s)*(1-z)**(k-s) for z in Q)/2

def calc(par):
    n=len(par)
    kids=[[] for _ in range(n)]
    for i in range(1,n):kids[par[i]].append(i)
    depth=[0]*n
    for i in range(1,n):depth[i]=depth[par[i]]+1
    anc=[]
    for j in range(n):
        t=j; ar=[j]
        while t: t=par[t]; ar.append(t)
        anc.append(set(ar))
    tree_score=F(0)
    for i in range(n):
        for j in range(i+1,n):
            if i in anc[j] or j in anc[i]:continue
            w=max(anc[i]&anc[j],key=lambda t:depth[t])
            tree_score+=q**(depth[i]+depth[j]-depth[w]-2)
    # Exact probability measure for outgoing-open-edge configurations.
    M1=M2=F(0)
    B1=B2=F(0)
    for mask in product((0,1),repeat=n-1):
        prob=F(1)
        for i in range(n):
            out=[mask[c-1] for c in kids[i]]
            prob*=moment(len(out),sum(out))
        reachable=[True]+[False]*(n-1)
        for i in range(1,n):reachable[i]=reachable[par[i]] and bool(mask[i-1])
        s=sum(reachable)
        M1+=prob*s; M2+=prob*s*s
        bp=F(1)
        for bit in mask:bp*= q if bit else (1-q)
        B1+=bp*s;B2+=bp*s*s
    assert M1==B1
    assert M2-M1*M1-(B2-B1*B1)==2*v*tree_score,(par,M1,M2,B1,B2,tree_score)
    if not tree_score:
        assert all(len(ch)<=1 for ch in kids)
    else:
        assert q**(n-3)<=tree_score<=F(comb(n-1,2))
    return tree_score

for n in range(1,8):
    count=0;lo=None;hi=None
    for tail in product(*[range(i) for i in range(1,n)]):
        score=calc((0,)+tail); count+=1
        if score:
            lo=score if lo is None else min(lo,score)
            hi=score if hi is None else max(hi,score)
    if n>=3:
        assert lo==q**(n-3),(n,lo)
        assert hi==comb(n-1,2),(n,hi)
    print('n',n,'trees',count,'positive-min',str(lo),'max',str(hi))
# Classical independent exponential contact/recovery special case.
for beta,gamma in [(F(1),F(1)),(F(2),F(5)),(F(3),F(2))]:
    x=beta/(beta+gamma)
    variance=gamma*beta**2/((gamma+2*beta)*(gamma+beta)**2)
    assert variance==x*x*(1-x)/(1+x)
print('VERIFY_OK')
