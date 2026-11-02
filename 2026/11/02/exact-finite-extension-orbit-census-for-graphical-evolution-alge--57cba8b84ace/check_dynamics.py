#!/usr/bin/env python3
"""Independent finite-field enumeration of squaring dynamics of graph evolution algebras.
For every case, all states are traversed directly; ranks are computed independently over F2.
"""
from itertools import product
from collections import Counter
from math import gcd

POLY={1:0b11,2:0b111,3:0b1011,4:0b10011}
def mul(a,b,f):
    p=POLY[f]; out=0
    while b:
        if b&1:out^=a
        b>>=1;a<<=1
        if a & (1<<f):a^=p
    return out

def bits_rank(rows,n):
    b=[int(x) for x in rows]; row=0
    for col in range(n):
        pivot=next((i for i in range(row,len(b)) if (b[i]>>col)&1),None)
        if pivot is None:continue
        b[row],b[pivot]=b[pivot],b[row]
        for j in range(len(b)):
            if j!=row and (b[j]>>col)&1:b[j]^=b[row]
        row+=1
        if row==len(b):break
    return row

def mm(A,B,n):
    return [sum((1<<j) for j in range(n) if ((sum(((A[i]>>k)&1)*((B[k]>>j)&1) for k in range(n)))&1)) for i in range(n)]

def ident(n):return [(1<<i) for i in range(n)]
def power(A,n,t):
    P=ident(n)
    for _ in range(t):P=mm(P,A,n)
    return P

def graph_parts(parts):
    groups=[g for i,m in enumerate(parts) for g in [i]*m]
    return [sum(1<<j for j in range(len(groups)) if groups[j]!=groups[i]) for i in range(len(groups))]

def apply(A,x,f):
    return tuple(xor_squares(row,x,f) for row in A)
def xor_squares(mask,x,f):
    a=0
    for j,y in enumerate(x):
        if (mask>>j)&1: a ^= mul(y,y,f)
    return a

def direct(A,f):
    n=len(A);q=2**f; states=list(product(range(q),repeat=n))
    transitions={x:apply(A,x,f) for x in states}
    tails=Counter(); periods=Counter()
    for x in states:
        seen={}; order=[];v=x
        while v not in seen:
            seen[v]=len(order);order.append(v);v=transitions[v]
        tails[seen[v]]+=1;periods[len(order)-seen[v]]+=1
    fixed={m:sum(1 for x in states if iterate(transitions,x,m)==x) for m in range(1,2*f+4)}
    return tails,periods,fixed

def iterate(T,x,m):
    for _ in range(m):x=T[x]
    return x

def predicted(A,f):
    n=len(A);q=2**f; ranks=[bits_rank(power(A,n,t),n) for t in range(n+1)]
    s=ranks[-1]
    cumulative=[q**(s+n-r) for r in ranks]
    tails=Counter({i: (cumulative[i]-(cumulative[i-1] if i else 0)) for i in range(n+1)})
    fixed={m:2**(gcd(m,f)*(n-bits_rank([u^v for u,v in zip(power(A,n,m*f//gcd(m,f)),ident(n))],n))) for m in range(1,2*f+4)}
    return tails,fixed,ranks

def multipartite_formula(parts,f):
    n=sum(parts);r=len(parts);o=sum(t%2 for t in parts);e=r-o;s=o if o%2==0 else o-1
    ranks=([n, r-(r%2),s if e==0 else o]+[s]*max(0,n-2))[:n+1]
    q=2**f; cu=[q**(s+n-t) for t in ranks]
    tails=Counter({j:cu[j]-(cu[j-1] if j else 0) for j in range(len(ranks))})
    fixed={m:(1 if o==0 else 2**(gcd(m,f)*((o-1) if o%2 else (o-int(bool(m%2 and f%2)))))) for m in range(1,2*f+4)}
    return tails,fixed,ranks

def test(A,f,label,parts=None):
    n=len(A);tail,period,fix=direct(A,f)
    pt,pf,ranks=predicted(A,f)
    assert all(tail[i]==pt[i] for i in set(tail)|set(pt)),('TAIL',label,f,tail,pt)
    assert fix==pf,('FIX',label,f,fix,pf)
    if parts is not None:
        mt,mf,mr=multipartite_formula(parts,f)
        assert ranks==mr,('RANK',label,f,ranks,mr)
        assert all(tail[i]==mt[i] for i in set(tail)|set(mt)),('MTAIL',label,f,tail,mt)
        assert fix==mf,('MFIX',label,f,fix,mf)
    return label, f,n,dict(sorted(tail.items())),{i:fix[i] for i in range(1,min(7,max(fix)+1))}

def main():
    cases=[]
    for parts,f in [([2],1),([2,2],2),([1,2],2),([1,1],3),([1,1],4),([1,2],4),([1,1,1],2),([1,2,2],2),([2,1,1],2),([2,2,1],2),([1,1,2,2],1),([1,1,1,1],2),([1,1,1,2],1),([1,1,2],2),([1,1,1,1,1],1)]:
        if sum(parts)<=6:
            cases.append(test(graph_parts(parts),f,'parts:'+','.join(map(str,parts)),parts))
    for n,edges,f in [(3,[(0,1),(1,2)],3),(4,[(0,1),(1,2),(2,3)],2),(4,[(0,1),(1,2),(2,3),(3,0)],2),(4,[(0,1),(0,2),(0,3)],2),(5,[(0,1),(1,2),(2,3),(3,4),(4,0)],1),(3,[(0,1),(1,2),(2,0)],2)]:
        A=[0]*n
        for i,j in edges:A[i]^=1<<j;A[j]^=1<<i
        cases.append(test(A,f,'graph:'+str(edges)))
    for c in cases:print(c)
    print('EVOLUTION_SQUARE_ORBIT_CENSUS_OK',len(cases))
if __name__=='__main__':main()
