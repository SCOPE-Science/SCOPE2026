#!/usr/bin/env python3
"""Recompute two finite homotopy classifications of graph robust-clique complexes."""
from collections import Counter,deque
from math import comb

EXPECTED={5:{2:{1:8},3:{3:28},4:{5:56},5:{7:67},6:{9:42},7:{11:7},8:{},9:{}},
          6:{2:{1:10},3:{3:45},4:{5:120},5:{7:206},6:{9:225},7:{11:139},8:{13:33},9:{15:1},10:{}}}

def test(n):
    N=3*n; T=1<<N
    adj=[0]*N
    for r in range(3):
        for c in range(n):
            v=r*n+c
            if r<2:
                w=v+n;adj[v]|=1<<w;adj[w]|=1<<v
            if c<n-1:
                w=v+1;adj[v]|=1<<w;adj[w]|=1<<v
    # First algorithm: the branching recurrence for the independence number.
    independence_number=bytearray(T)
    for s in range(1,T):
        bit=s&-s;v=bit.bit_length()-1
        independence_number[s]=max(independence_number[s^bit],1+independence_number[s&~(bit|adj[v])])
    # Independent algorithm: Boolean independent-set detection, followed by
    # a max-over-submasks zeta transform.
    independent=bytearray(T);independent[0]=1
    independently_computed_alpha=bytearray(T)
    for s in range(1,T):
        bit=s&-s;v=bit.bit_length()-1
        if independent[s^bit] and not (adj[v]&s):
            independent[s]=1;independently_computed_alpha[s]=s.bit_count()
    for v in range(N):
        b=1<<v
        for s in range(T):
            if s&b and independently_computed_alpha[s^b]>independently_computed_alpha[s]:
                independently_computed_alpha[s]=independently_computed_alpha[s^b]
    assert independence_number==independently_computed_alpha
    assert independence_number[-1]==(N+1)//2
    for k,expected in EXPECTED[n].items():
        alive=bytearray(T)
        for s in range(1,T):alive[s]=(independence_number[s]<k)
        valid_count=sum(alive)
        # Each vertex is used once as an elementary matching pivot.
        # partner[s]=t means s is the matched lower-dimensional face of t.
        partner=[-1]*T
        for v in range(N):
            b=1<<v
            for s in range(1,T):
                if (s&b) or not alive[s]:continue
                t=s|b
                if alive[t]:
                    alive[s]=alive[t]=0
                    partner[s]=t;partner[t]=s
        crit=Counter(s.bit_count()-1 for s in range(1,T) if alive[s])
        assert dict(crit)==({0:1}|expected),(n,k,crit,expected)
        total_matched=sum(p>=0 for p in partner)//2
        assert 2*total_matched+sum(crit.values())==valid_count
        # Exhaustively verify no directed gradient cycle in the entire
        # nonempty face-poset Hasse diagram (without relying on pivot theory).
        valid=bytearray(T)
        indegree=[0]*T
        for s in range(1,T):valid[s]=(independence_number[s]<k)
        for s in range(1,T):
            if not valid[s]:continue
            rest=s
            while rest:
                b=rest&-rest;rest^=b
                t=s^b
                if t==0:continue
                if partner[t]==s:indegree[s]+=1 # matched t -> s
                else:indegree[t]+=1                 # unmatched s -> t
        queue=deque(s for s in range(1,T) if valid[s] and indegree[s]==0)
        num=0
        while queue:
            s=queue.popleft();num+=1
            rest=s
            while rest:
                b=rest&-rest;rest^=b;t=s^b
                if t and partner[t]!=s:
                    indegree[t]-=1
                    if indegree[t]==0:queue.append(t)
            t=partner[s]
            if t>s:
                indegree[t]-=1
                if indegree[t]==0:queue.append(t)
        assert num==valid_count,(n,k,num,valid_count)
        # Independent reduced Euler check.
        euler=-1+sum(((-1)**(s.bit_count()-1)) for s in range(1,T) if valid[s])
        expected_euler=sum(((-1)**d)*c for d,c in expected.items())
        assert euler==expected_euler,(n,k,euler,expected_euler)
        print(f'GRID_3x{n} k={k} faces={valid_count} pairs={total_matched} critical={dict(crit)} DAG={num} Euler={euler}',flush=True)
    print(f'GRID_3x{n}_PASS',flush=True)

if __name__=='__main__':
    test(5);test(6)
    print('VERIFY_OK',flush=True)
