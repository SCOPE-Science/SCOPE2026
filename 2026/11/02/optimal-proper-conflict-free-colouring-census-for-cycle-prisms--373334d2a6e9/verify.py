#!/usr/bin/env python3
"""Exact finite-state and independent labelled-colouring checks for the prism PCF enumerator.
Python standard library only. All arithmetic is integral."""
from itertools import product
from math import prod

def rung_states(q):
    return [(a,b) for a in range(q) for b in range(q) if a!=b]

def matrix(q, require_three=False):
    ss=rung_states(q)
    pairs=[(a,b) for a in ss for b in ss if a[0]!=b[0] and a[1]!=b[1]]
    index={v:i for i,v in enumerate(pairs)}
    nxt=[[] for _ in pairs]
    for i,(a,b) in enumerate(pairs):
        for c in ss:
            j=index.get((b,c))
            if j is None:continue
            t=len({a[0],c[0],b[1]})
            u=len({a[1],c[1],b[0]})
            if (t==3 and u==3) if require_three else (t>=2 and u>=2):
                nxt[i].append(j)
    return pairs,nxt

def trace_power(nxt,n):
    N=len(nxt)
    a=[[int(i==j) for j in range(N)] for i in range(N)]
    for _ in range(n):
        b=[[0]*N for _ in range(N)]
        for i in range(N):
            ai=a[i]; bi=b[i]
            for k,v in enumerate(ai):
                if v:
                    for j in nxt[k]: bi[j]+=v
        a=b
    return sum(a[i][i] for i in range(N))

def charpoly_from_traces(nxt):
    # Faddeev–LeVerrier/Newton identities applied to tr(T^k).
    N=len(nxt)
    a=[[int(i==j) for j in range(N)] for i in range(N)]
    ps=[]
    for k in range(1,N+1):
        b=[[0]*N for _ in range(N)]
        for i in range(N):
            bi=b[i]
            for h,coef in enumerate(a[i]):
                if coef:
                    for j in nxt[h]:bi[j]+=coef
        a=b
        ps.append(sum(a[i][i] for i in range(N)))
    # charpoly x^N+c1*x^(N-1)+...+cN
    c=[1]
    for k in range(1,N+1):
        numer=sum(c[k-j]*ps[j-1] for j in range(1,k+1))
        assert numer%k==0, (k,numer)
        c.append(-numer//k)
    return c

def mul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]+=x*y
    return out

def power(poly,exp):
    a=[1]
    for _ in range(exp):a=mul(a,poly)
    return a

def expect_poly(q):
    # Ascending coefficient representation of expected characteristic polynomials.
    factors = ([( [0,1],6),([-1,0,0,1],4)] if q==3 else
        [([0,1],48),([-2,1],1),([-1,1],6),([1,1],2),
        ([2,1,1],3),([-2,0,-1,1],2),([4,-6,-4,1],1),
        ([4,-2,6,3,1],3)])
    p=[1]
    for f,m in factors:p=mul(p,power(f,m))
    assert p[-1]==1
    return p[::-1]

def direct(q,n):
    # Independent graph-edge test: no use of the transfer-state construction.
    edges=[]; neighbors=[[] for _ in range(2*n)]
    for i in range(n):
        edges.extend([(i,(i+1)%n), (n+i,n+(i+1)%n), (i,n+i)])
    for a,b in edges:
        neighbors[a].append(b);neighbors[b].append(a)
    count=0
    for word in product(range(q),repeat=2*n):
        if any(word[a]==word[b] for a,b in edges):continue
        if all(len({word[u] for u in neighbors[v]})>=2 for v in range(2*n)):
            count+=1
    return count

def determinant_series_4():
    # Constant-first coefficient polynomials for det(I-t*T_4).
    factors=[([1,-2],1),([1,-1],6),([1,1],2),([1,1,2],3),
             ([1,-1,0,-2],2),([1,-4,-6,4],1),
             ([1,3,6,-2,4],3)]
    p=[1]
    for f,m in factors:p=mul(p,power(f,m))
    return p

def log_derivative_sequence(d,N):
    # a_n=[t^n](-t*d'(t)/d(t)) via exact formal power-series division.
    a=[0]
    for n in range(1,N+1):
        a.append(-n*(d[n] if n<len(d) else 0)
                 -sum(d[j]*a[n-j] for j in range(1,min(n,len(d)-1)+1)))
    return a

def main():
    a3,t3=matrix(3)
    a4,t4=matrix(4)
    assert len(a3)==18 and len(a4)==84
    assert sum(map(len,t3))==12 and sum(map(len,t4))==384
    assert charpoly_from_traces(t3)==expect_poly(3)
    assert charpoly_from_traces(t4)==expect_poly(4)
    print('CHARPOLY_OK dimensions 18 84')
    d=determinant_series_4()
    a=log_derivative_sequence(d,18)
    assert len(d)==37 and all(a[n]==trace_power(t4,n) for n in range(3,19))
    print('RATIONAL_SERIES_OK n=3..18')
    series4=[264,384,3600,17472,75936,427152,2071632,10365504]
    for n,v in enumerate(series4,3):assert trace_power(t4,n)==v
    for n in range(3,19):
        assert trace_power(t3,n)==(12 if n%3==0 else 0)
    print('TRANSFER_OK n3=3..18 n4=3..10')
    direct_tests=0
    for q,N in ((3,7),(4,5)):
        _,t=matrix(q)
        for n in range(3,N+1):
            d=direct(q,n)
            assert d==trace_power(t,n),(q,n,d)
            direct_tests+=q**(2*n)
    print('DIRECT_OK assignments',direct_tests)
    _,t4h=matrix(4,True)
    assert charpoly_from_traces(t4h)==expect_three_hom()
    for n in range(3,13):assert trace_power(t4h,n)==(24 if n%4==0 else 0)
    print('HOMOGENEOUS_OK n=3..12')
    base=((0,1),(1,0))
    ix={v:i for i,v in enumerate(a4)}
    for cols in ([(0,1),(1,0),(2,3)],[(0,1),(1,0),(2,3),(3,2)],
                 [(0,1),(1,0),(2,3),(0,1),(2,3)]):
        states=[ix[(cols[i],cols[(i+1)%len(cols)])] for i in range(len(cols))]
        assert a4[states[0]]==base
        assert all(states[(i+1)%len(states)] in t4[states[i]] for i in range(len(states)))
    print('CONSTRUCTIVE_OK lengths 3,4,5 share a base')
    print('VERIFY_OK')

def expect_three_hom():
    p=[1]
    for f,k in [([0,1],60),([-1,1],6),([1,1],6),([1,0,1],6)]:p=mul(p,power(f,k))
    return p[::-1]
if __name__=='__main__':main()
