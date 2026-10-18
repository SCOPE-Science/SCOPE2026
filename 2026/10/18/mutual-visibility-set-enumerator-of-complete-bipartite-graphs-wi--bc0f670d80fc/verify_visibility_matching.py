#!/usr/bin/env python3
"""Independent graph-distance exhaustive check of matching-deleted biclique visibility."""
from collections import deque
from math import comb, factorial


def is_mv_bruteforce(a,b,t,mask):
    n=a+b
    adj=[[] for _ in range(n)]
    for i in range(a):
        for j in range(b):
            if i < t and i == j: continue
            adj[i].append(a+j); adj[a+j].append(i)
    def dist(src,target,exclude=0):
        d=[-1]*n
        d[src]=0
        todo=deque([src])
        while todo:
            u=todo.popleft()
            if u==target: return d[u]
            for v in adj[u]:
                if d[v]>=0 or (exclude>>v &1): continue
                d[v]=d[u]+1
                todo.append(v)
        return -1
    selected=[v for v in range(n) if mask>>v&1]
    for index,u in enumerate(selected):
        for v in selected[index+1:]:
            # Globally shortest path and shortest path with other selected vertices deleted.
            if dist(u,v,mask & ~(1<<u) & ~(1<<v))!=dist(u,v,0):
                return False
    return True


def formula_count(a,b,t):
    def multinomial(x,y,c):
        d=x-c; e=y-c; f=t-x-y+c
        if min(c,d,e,f)<0: return 0
        return factorial(t)//(factorial(c)*factorial(d)*factorial(e)*factorial(f))
    p=[0]*(a+b+1)
    for x in range(t+1):
        for y in range(t+1):
            for c in range(max(0,x+y-t),min(x,y)+1):
                w=multinomial(x,y,c)
                for u in range(a-t+1):
                    for v in range(b-t+1):
                        A=x+u; B=y+v
                        sA=a-A; sB=b-B
                        if A>=2 and sB<=2 and x-c==sB: continue
                        if B>=2 and sA<=2 and y-c==sA: continue
                        if c>=1 and (sA==0 or sB==0 or (sA==sB==1 and t-x-y+c==1)): continue
                        p[A+B]+=w*comb(a-t,u)*comb(b-t,v)
    return p


def check():
    cases=0; num_graph_labels=0
    for a in range(3,7):
        for b in range(3,7):
            if a>b: continue
            for t in range(0,min(a,b)):
                if a+b>12: continue
                brute=[0]*(a+b+1)
                for mask in range(1<<(a+b)):
                    if is_mv_bruteforce(a,b,t,mask):
                        brute[mask.bit_count()]+=1
                pred=formula_count(a,b,t)
                if pred!=brute:
                    raise AssertionError(f'MISMATCH {(a,b,t)}: formula={pred} brute={brute}')
                cases+=1; num_graph_labels+=1<<(a+b)
                print(f'{a},{b},{t}: counts={sum(pred)} degree={max(i for i,v in enumerate(pred) if v)} leading={pred[max(i for i,v in enumerate(pred) if v)]}')
    param_checks=0
    for a in range(3,12):
        for b in range(a,12):
            previous=formula_count(a,b,0)
            for t in range(1,min(a,b)):
                p=formula_count(a,b,t)
                degree=max(i for i,v in enumerate(p) if v)
                expected=(a-t)*(b-t)+(1+2*(a==3)+2*(b==3))*(t==1)
                assert degree==a+b-2, (a,b,t,'degree')
                assert p[degree]==expected, (a,b,t,p[degree],expected)
                assert all(x<=y for x,y in zip(p,previous)), (a,b,t,'monotonicity')
                previous=p;param_checks+=1
    print('ADDITIONAL',param_checks,'full-polynomial algebraic checks of degree, leading coefficient and monotonicity')
    print('VALIDATED',cases,'graph parameter cases and',num_graph_labels,'vertex subsets', 'VERIFICATION_OK')

if __name__=='__main__':check()
