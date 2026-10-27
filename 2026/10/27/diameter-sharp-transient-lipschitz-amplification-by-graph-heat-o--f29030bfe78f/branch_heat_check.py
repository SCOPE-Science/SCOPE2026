"""Independent finite-dimensional checks for diameter-sharp heat amplification on rooted trees.
Only scientific computations; a numerical check is not a proof of limiting sharpness.
"""
import math
import numpy as np
from scipy.linalg import expm


def generator_even(b,h):
    # States: root, marked branch depths 1..h, all other branch depths 1..h.
    n=2*h+1
    Q=np.zeros((n,n),dtype=float)
    def add(i,j,r): Q[i,j]+=r;Q[i,i]-=r
    add(0,1,1);add(0,h+1,b-1)
    for j in range(1,h+1):
        for base in (0,h):
            i=base+j
            add(i,0 if j==1 else i-1,1)
            if j<h:add(i,i+1,b)
    f=np.array([0]+[-j for j in range(1,h+1)]+[j for j in range(1,h+1)],float)
    return Q,f,0,1


def generator_odd(b,h):
    # Two b-ary rooted trees of height h with one root-bridge edge.
    n=2*h+2
    Q=np.zeros((n,n),dtype=float)
    def add(i,j,r): Q[i,j]+=r;Q[i,i]-=r
    add(0,h+1,1);add(h+1,0,1)
    for base in (0,h+1):
        for j in range(h+1):
            i=base+j
            if j<h:add(i,i+1,b)
            if j>0:add(i,i-1,1)
    f=np.array([-j for j in range(h+1)]+[1+j for j in range(h+1)],float)
    return Q,f,h+1,0


def trial(kind,b,h):
    Q,f,u,v=(generator_even(b,h) if kind=='even' else generator_odd(b,h))
    assert np.max(abs(Q.sum(axis=1)))<1e-10
    t=b**(-.5)
    p=expm(t*Q)
    amp=abs((p@f)[u]-(p@f)[v])
    D=2*h if kind=='even' else 2*h+1
    epsilon=t+math.exp(-math.sqrt(b))*sum((math.sqrt(b))**j/math.factorial(j) for j in range(h))
    lb=D*(1-2*epsilon-(1/b if kind=='even' else 0))
    assert amp>=lb-1e-9 and amp<=D+1e-10, (kind,b,h,amp,lb,D)
    return kind,b,h,round(float(amp/D),10),round(float(lb/D),10)

if __name__=='__main__':
    for kind in ('even','odd'):
        for h in (1,2,3,4):
            for b in (2,3,5,10,25,100,1000,10000):
                print(*trial(kind,b,h))


def full_tree(kind,b,h):
    adj=[[]];f=[0.];
    def node(value):adj.append([]); f.append(float(value)); return len(adj)-1
    def link(u,v):adj[u].append(v);adj[v].append(u)
    def descendants(parent,depth,sign,offset):
        if depth>=h:return
        for _ in range(b):
            child=node(offset+sign*(depth+1));link(parent,child)
            descendants(child,depth+1,sign,offset)
    if kind=='even':
        marked=None
        for k in range(b):
            sign=-1 if k==0 else 1
            child=node(sign);link(0,child)
            if k==0:marked=child
            descendants(child,1,sign,0)
        u,v=0,marked
    else:
        right=node(1);link(0,right)
        descendants(0,0,-1,0)
        descendants(right,0,1,1)
        u,v=right,0
    n=len(adj);L=np.zeros((n,n))
    for i,nei in enumerate(adj):
        L[i,i]=len(nei)
        for j in nei:L[i,j]-=1
    return L,np.array(f),u,v


def verify_full_vs_quotient():
    count=0
    for kind in ('even','odd'):
        for h in (1,2,3):
            for b in (2,3):
                Q,qf,qu,qv=(generator_even(b,h) if kind=='even' else generator_odd(b,h))
                L,f,u,v=full_tree(kind,b,h)
                t=b**(-.5)
                x=abs((expm(t*Q)@qf)[qu]-(expm(t*Q)@qf)[qv])
                y=abs((expm(-t*L)@f)[u]-(expm(-t*L)@f)[v])
                assert abs(x-y)<1e-10,(kind,h,b,x,y)
                assert max(abs(f[a]-f[z]) for a in range(len(f)) for z in np.where(L[a,:]<-.5)[0])<=1+1e-12
                count+=1
    return count

if __name__=='__main__':
    print('full graph cross-checks:',verify_full_vs_quotient())
