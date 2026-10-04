#!/usr/bin/env python3
from collections import deque
from itertools import product


def poly_add(a,b):
    n=max(len(a),len(b)); c=[0]*n
    for i,v in enumerate(a): c[i]+=v
    for i,v in enumerate(b): c[i]+=v
    while len(c)>1 and c[-1]==0: c.pop()
    return c

def poly_shift_scale(a,scale):
    return [0]+[scale*v for v in a]

def dp_Q(alpha,beta):
    F={(0,0):[1],(0,1):[0],(1,0):[0],(1,1):[0]}
    for aa,bb in zip(alpha,beta):
        G={(0,0):[0],(0,1):[0],(1,0):[0],(1,1):[0]}
        for (a,b),P in F.items():
            if any(P):
                G[(0,b)]=poly_add(G[(0,b)],P)
                if b==0:
                    na=a if bb==1 else 0
                    G[(na,1)]=poly_add(G[(na,1)],poly_shift_scale(P,bb))
        H={(0,0):[0],(0,1):[0],(1,0):[0],(1,1):[0]}
        for (a,b),P in G.items():
            if any(P):
                H[(a,0)]=poly_add(H[(a,0)],P)
                if a==0:
                    nb=b if aa==1 else 0
                    H[(1,nb)]=poly_add(H[(1,nb)],poly_shift_scale(P,aa))
        F=H
    Q=[0]
    for P in F.values(): Q=poly_add(Q,P)
    if len(alpha)==1 and alpha[0]==beta[0]==1:
        while len(Q)<3: Q.append(0)
        Q[2]-=1
    while len(Q)>1 and Q[-1]==0: Q.pop()
    return Q

def make_graph(alpha,beta):
    A=[];B=[]; idx=0
    for i,c in enumerate(alpha):
        cls=list(range(idx,idx+c));idx+=c;A.append(cls)
    for j,c in enumerate(beta):
        cls=list(range(idx,idx+c));idx+=c;B.append(cls)
    adj=[set() for _ in range(idx)]
    for i,Ac in enumerate(A):
        for j,Bc in enumerate(B):
            if j<=i:
                for u in Ac:
                    for v in Bc:
                        adj[u].add(v);adj[v].add(u)
    return A,B,adj

def distances(adj):
    n=len(adj); D=[]
    for s in range(n):
        d=[-1]*n;d[s]=0;q=deque([s])
        while q:
            u=q.popleft()
            for v in adj[u]:
                if d[v]<0:d[v]=d[u]+1;q.append(v)
        D.append(d)
    return D

def is_resolving(mask,D):
    n=len(D); S=[s for s in range(n) if mask>>s&1]
    if not S and n>1:return False
    seen=set()
    for v in range(n):
        r=tuple(D[v][s] for s in S)
        if r in seen:return False
        seen.add(r)
    return True

def criterion(mask,A,B):
    n=sum(map(len,A))+sum(map(len,B)); T=set(v for v in range(n) if not(mask>>v&1))
    if not T and n>=1:return True
    S=set(range(n))-T
    if not S:return n==1
    omitA=[];omitB=[]
    for C in A:
        q=sum(v in T for v in C)
        if q>1:return False
        omitA.append(q==1)
    for C in B:
        q=sum(v in T for v in C)
        if q>1:return False
        omitB.append(q==1)
    p=len(A)
    for i in range(p):
        if omitA[i]:
            for j in range(i+1,p):
                if omitA[j] and not any(any(v in S for v in B[k]) for k in range(i+1,j+1)):
                    return False
        if omitB[i]:
            for j in range(i+1,p):
                if omitB[j] and not any(any(v in S for v in A[k]) for k in range(i,j)):
                    return False
    return True

def main():
    graph_types=subset_checks=poly_checks=0;max_order=0
    for p in range(1,5):
        for alpha in product((1,2,3), repeat=p):
            for beta in product((1,2,3), repeat=p):
                n=sum(alpha)+sum(beta)
                if n>10: continue
                A,B,adj=make_graph(alpha,beta);D=distances(adj)
                brute=[0]*(n+1)
                for mask in range(1<<n):
                    r=is_resolving(mask,D); c=criterion(mask,A,B)
                    subset_checks+=1
                    if r!=c:
                        raise SystemExit(f'criterion mismatch alpha={alpha} beta={beta} mask={mask}')
                    if r: brute[n-mask.bit_count()]+=1
                Q=dp_Q(alpha,beta)
                Q=Q+[0]*(n+1-len(Q))
                if Q[:n+1]!=brute:
                    raise SystemExit(f'polynomial mismatch alpha={alpha} beta={beta} dp={Q[:n+1]} brute={brute}')
                graph_types+=1;poly_checks+=n+1;max_order=max(max_order,n)
    print(f'VERIFY_OK graph_types={graph_types} subset_checks={subset_checks} polynomial_checks={poly_checks} max_order={max_order}')
if __name__=='__main__':main()
