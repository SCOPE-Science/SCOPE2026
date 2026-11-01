#!/usr/bin/env python3
"""Reproduce exact periodic counts for synchronous binary majority on perfect binary trees.
Only Python standard library is used. The analytic proof is separate.
"""
from itertools import product

STATES = tuple(product((0, 1), repeat=2))

def recurrence(h):
    u,v=1,0
    for _ in range(h):
        u,v=u*(u+2*v),u*u
    return (2*u,2*(u*u+v*v),u*u+v*v-u,2*v*v)

def graph(h):
    nodes=2**(h+1)-1
    adj=[[] for _ in range(nodes)]
    for i in range(1,nodes):
        p=(i-1)//2
        adj[i].append(p)
        adj[p].append(i)
    return adj

def step(state,adj):
    out=0
    for i,nb in enumerate(adj):
        a=sum((state>>j)&1 for j in nb)
        bit=(state>>i)&1
        if 2*a>len(nb): bit=1
        elif 2*a<len(nb): bit=0
        if bit:out|=1<<i
    return out

def exhaustive(h):
    adj=graph(h); n=len(adj)
    fixed=ret2=rootflip=0
    for s in range(1<<n):
        t=step(s,adj)
        if t==s:fixed+=1
        if step(t,adj)==s:
            ret2+=1
            if (t^s)&1:rootflip+=1
    return (fixed,ret2,(ret2-fixed)//2,rootflip)

def dynamic_independent(h):
    # Counts of 2-return states in a child subtree with externally prescribed
    # parent pair (p0,p1), root pair (s0,s1); no factorization is assumed.
    A={(p,s):int(s==(p[1],p[0])) for p in STATES for s in STATES}
    for _ in range(h-1):
        B={}
        for p in STATES:
            for s in STATES:
                B[p,s]=sum(A[s,c]*A[s,d] for c in STATES for d in STATES
                           if ((p[0]+c[0]+d[0]>=2)==bool(s[1]))
                           and ((p[1]+c[1]+d[1]>=2)==bool(s[0])))
        A=B
    def root_valid(s,c,d):
        def tied(x,y,old):return x if x==y else old
        return tied(c[0],d[0],s[0])==s[1] and tied(c[1],d[1],s[1])==s[0]
    total=rootflip=0
    for s in STATES:
        contribution=sum(A[s,c]*A[s,d] for c in STATES for d in STATES
                         if root_valid(s,c,d))
        total+=contribution
        if s[0]!=s[1]:rootflip+=contribution
    return total,rootflip

def fixed_dp(h):
    # Independent time-independent majority recursion.
    A={(p,s):int(p==s) for p in (0,1) for s in (0,1)}
    for _ in range(h-1):
        B={}
        for p in (0,1):
            for s in (0,1):
                B[p,s]=sum(A[s,c]*A[s,d] for c in (0,1) for d in (0,1)
                           if ((p+c+d>=2)==bool(s)))
        A=B
    return sum(A[s,c]*A[s,d] for s in (0,1) for c in (0,1) for d in (0,1)
               if (c+d<2 and s==0) or (c+d>0 and s==1))

def main():
    cases=0
    for h in range(1,9):
        fixed,ret2,orbits,root_flip=recurrence(h)
        assert (ret2,root_flip)==dynamic_independent(h)
        assert fixed==fixed_dp(h)
        if h<=3:
            ex=exhaustive(h)
            assert ex==(fixed,ret2,orbits,root_flip),(h,ex,(fixed,ret2,orbits,root_flip))
        print('height',h,'vertices',2**(h+1)-1,'fixed',fixed,
              'return2',ret2,'primitive_2_orbits',orbits,'root_flipping_states',root_flip)
        cases+=1
    print('BINARY_TREE_MAJORITY_VERIFY_OK',cases,'independent_DP_heights_and_3_exhaustive_heights')

if __name__=='__main__':main()
