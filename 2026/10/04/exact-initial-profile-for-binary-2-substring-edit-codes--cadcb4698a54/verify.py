#!/usr/bin/env python3
from itertools import product
import json
from pathlib import Path

K=2
EXPECTED={1:1,2:1,3:1,4:1,5:2,6:3,7:5,8:8}
WITNESS8=["11111111","11100000","11001010","10001101","01101001","01010110","00011100","00000011"]

def replacements(k):
    out=[""]
    for ell in range(1,k+1):
        out.extend("".join(p) for p in product("01", repeat=ell))
    return out

REPL=replacements(K)

def ball_direct(x,k=K):
    # At most one k-substring edit: replace one substring u by v,
    # |u|,|v|<=k, not both empty; include the no-error output x.
    n=len(x); out={x}
    for a in range(0,min(k,n)+1):
        for i in range(n-a+1):
            for v in REPL:
                if a==0 and len(v)==0:
                    continue
                out.add(x[:i]+v+x[i+a:])
    return out

def is_one_edit_target(x,y,k=K):
    # Independent target-scanning predicate: test every possible removed
    # length a and inserted length b using prefix/suffix agreement.
    n=len(x); m=len(y)
    if x==y:
        return True
    for a in range(0,min(k,n)+1):
        for b in range(0,k+1):
            if a==0 and b==0 or m != n-a+b:
                continue
            for i in range(n-a+1):
                if i+b>m:
                    continue
                if x[:i]==y[:i] and x[i+a:]==y[i+b:]:
                    return True
    return False

def ball_scan(x,k=K):
    n=len(x); out=set()
    lo=max(0,n-k); hi=n+k
    for m in range(lo,hi+1):
        for p in product("01", repeat=m):
            y="".join(p)
            if is_one_edit_target(x,y,k):
                out.add(y)
    return out

def greedy_color_order(P,adj):
    # Produces vertices and nondecreasing greedy color numbers. Each color
    # class is independent in the candidate subgraph, hence color count is
    # an upper bound on any clique contained in P.
    verts=[]; bounds=[]; U=P; color=0
    while U:
        color+=1; Q=U
        while Q:
            bit=Q & -Q; v=bit.bit_length()-1
            verts.append(v); bounds.append(color)
            U &= ~bit; Q &= ~bit; Q &= ~adj[v]
    return verts,bounds

def maximum_clique(adj):
    n=len(adj); best=[]; nodes=0
    def expand(P,R):
        nonlocal best,nodes
        nodes+=1
        if not P:
            if len(R)>len(best): best=R[:]
            return
        verts,bounds=greedy_color_order(P,adj)
        for idx in range(len(verts)-1,-1,-1):
            if len(R)+bounds[idx] <= len(best):
                return
            v=verts[idx]; bit=1<<v
            if P & bit:
                expand(P & adj[v], R+[v])
                P &= ~bit
    expand((1<<n)-1,[])
    return best,nodes

def graph_for_n(n):
    words=[format(i,f"0{n}b") for i in range(1<<n)]
    balls=[]
    for x in words:
        a=ball_direct(x); b=ball_scan(x)
        assert a==b, (n,x,len(a),len(b), sorted(a^b)[:3])
        balls.append(a)
    adj=[0]*(1<<n)
    edges=0
    for i in range(1<<n):
        for j in range(i):
            if balls[i].isdisjoint(balls[j]):
                adj[i] |= 1<<j; adj[j] |= 1<<i; edges+=1
    return words,balls,adj,edges

def main():
    profile={}; details={}
    for n in range(1,9):
        words,balls,adj,edges=graph_for_n(n)
        clique,nodes=maximum_clique(adj)
        profile[n]=len(clique)
        details[n]={"compatibility_edges":edges,"search_nodes":nodes,"witness":[words[i] for i in clique]}
        assert len(clique)==EXPECTED[n], (n,len(clique),EXPECTED[n])
        if n==8:
            idx={w:i for i,w in enumerate(words)}
            for a in range(len(WITNESS8)):
                for b in range(a):
                    assert balls[idx[WITNESS8[a]]].isdisjoint(balls[idx[WITNESS8[b]]])
    assert profile==EXPECTED
    print("VERIFY_OK profile="+",".join(str(profile[n]) for n in range(1,9)))
    print("N8_WITNESS="+",".join(WITNESS8))
    print("N8_SEARCH_NODES="+str(details[8]["search_nodes"]))
    return profile,details

if __name__=='__main__':
    profile,details=main()
