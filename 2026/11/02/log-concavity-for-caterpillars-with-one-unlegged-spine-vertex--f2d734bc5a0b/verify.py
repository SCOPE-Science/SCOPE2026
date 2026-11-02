#!/usr/bin/env python3
"""Independent finite checks for domination-polynomial log-concavity with one bare caterpillar spine vertex.

Requires Python 3 standard library. Run: python3 verify.py
"""
from itertools import product
from math import comb


def add(a,b):
    z=[0]*max(len(a),len(b))
    for i,v in enumerate(a):z[i]+=v
    for i,v in enumerate(b):z[i]+=v
    return z

def sub(a,b):
    z=add(a,[-v for v in b]);assert min(z)>=0
    return z

def mul(a,b):
    z=[0]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):z[i+j]+=v*w
    return z

def trim(a):
    while len(a)>1 and a[-1]==0:a.pop()
    return a

def U(t):
    assert t>=1
    q=[0]+[comb(t,j-1)+(j==t) for j in range(1,t+2)]
    return q

def claimed(a):
    assert a[0]>=1 and a[-1]>=1
    zeros=[i for i,t in enumerate(a) if not t]
    assert len(zeros)<=1
    if not zeros:
        r=[1]
        for t in a:r=mul(r,U(t))
        return trim(r)
    j=zeros[0]; assert 0<j<len(a)-1
    p=mul(mul([1,1],U(a[j-1])),U(a[j+1]))
    p[a[j-1]+a[j+1]]-=1
    assert min(p)>=0
    for i,t in enumerate(a):
        if i not in (j-1,j,j+1):p=mul(p,U(t))
    return trim(p)

def graph(a):
    n=len(a);adj=[[] for _ in range(n)]
    for i in range(n-1):adj[i].append(i+1);adj[i+1].append(i)
    for i,t in enumerate(a):
        for _ in range(t):
            j=len(adj);adj.append([i]);adj[i].append(j)
    return adj

def brute(a):
    adj=graph(a);n=len(adj);ans=[0]*(n+1)
    closed=[(1<<i)|sum(1<<j for j in adj[i]) for i in range(n)]
    allmask=(1<<n)-1
    for S in range(1<<n):
        cover=0
        for i in range(n):
            if (S>>i)&1:cover|=closed[i]
        if cover==allmask:ans[S.bit_count()]+=1
    return trim(ans)

def tree_dp(a):
    adj=graph(a);n=len(adj)
    def go(v,p):
        A=[0,1];B=[1];C=[1]; # accumulator for products
        for w in adj[v]:
            if w==p:continue
            aa,bb,cc=go(w,v)
            A=mul(A,add(add(aa,bb),cc))
            B=mul(B,add(aa,bb))
            C=mul(C,bb)
        # A includes chosen root; B must have a child chosen;
        # C has no chosen children and relies on parent.
        return trim(A),trim(sub(B,C)),trim(C)
    x,y,_=go(0,-1)
    return trim(add(x,y))

def lc(poly):
    return all(poly[j]**2>=poly[j-1]*poly[j+1] for j in range(1,len(poly)-1))


def main():
    exact=0
    # All small one-gap caterpillars, compared with literal subset enumeration.
    for k in range(3,7):
        for j in range(1,k-1):
            for rest in product((1,2),repeat=k-1):
                a=list(rest);a.insert(j,0)
                if k+sum(a)>15:continue
                p=claimed(a)
                assert p==brute(a),(a,p,brute(a))
                assert lc(p),a
                exact+=1
    print('EXHAUSTIVE_OK',exact)
    dp_count=0
    # Entire rectangular grid, with a polynomial-time independent tree DP.
    for k in range(3,9):
        for j in range(1,k-1):
            for rest in product((1,2,3),repeat=k-1):
                a=list(rest);a.insert(j,0)
                p=claimed(a)
                assert p==tree_dp(a),(a,p,tree_dp(a))
                assert lc(p),a
                dp_count+=1
    print('TREE_DP_OK',dp_count)
    margin_count=0
    # Check the only Turan inequality changed adversely by subtracting x^(a+c).
    for a in range(1,81):
        for c in range(1,81):
            s=a+c;t=a*c
            lhs=(s**6+9*s**5+19*s**4+27*s**3+52*s**2+36*s
                 -12*s**3*t-36*s**2*t+120*s*t+144*t*t)
            assert lhs>0
            P=mul(mul([1,1],U(a)),U(c)); P[s]-=1
            margin=P[s]**2-P[s-1]*P[s+1]
            assert lhs==144*margin,(a,c,lhs,margin)
            assert lc(P),(a,c)
            margin_count+=1
    print('MARGIN_OK',margin_count)
    print('VERIFY_OK')

if __name__=='__main__':main()
