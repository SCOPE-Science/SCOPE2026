#!/usr/bin/env python3
"""Exact finite-state checks for complete-graph collision conditioning.

No external packages needed. Mathematical proof is in RESULT.md; finite
enumerations here are not used to infer validity at unbounded state size.
"""
from fractions import Fraction as F
from itertools import combinations, permutations
from random import Random

def configuration_killing(q, A):
    return sum((q[i][j]+q[j][i] for i,j in combinations(A,2)), F(0))

def pair_uniform(q):
    n=len(q)
    vals={q[i][j]+q[j][i] for i,j in combinations(range(n),2)}
    return len(vals)==1

def degree_uniform(q):
    n=len(q)
    ds={sum((q[i][j]+q[j][i] for j in range(n) if j!=i),F(0)) for i in range(n)}
    return len(ds)==1

def k_uniform(q,k):
    vals={configuration_killing(q,A) for A in combinations(range(len(q)),k)}
    return len(vals)==1

def q_from_s(s):
    n=len(s)
    q=[[F(0)]*n for _ in range(n)]
    for i,j in combinations(range(n),2):
        q[i][j]=q[j][i]=F(s[i][j],2)
    return q

def rates_from_integer_matrix(n,rng):
    q=[[F(0)]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i!=j:q[i][j]=F(rng.randint(1,7))
    return q

def check_generator(q,k):
    n=len(q)
    configs=list(permutations(range(n),k))
    index={s:i for i,s in enumerate(configs)}
    nstates=len(configs)
    check=0
    for a,s in enumerate(configs):
        occupied=set(s)
        vacancy=[v for v in range(n) if v not in occupied]
        allowed=F(0)
        for p in range(k):
            for v in vacancy:
                t=list(s);t[p]=v
                b=index[tuple(t)]
                assert b!=a
                assert q[s[p]][v]>0
                allowed+=q[s[p]][v]
                check+=1
        rejected=configuration_killing(q,occupied)
        direct=sum((q[s[p]][v] for p in range(k) for v in range(n) if v!=s[p]),F(0))
        assert direct==allowed+rejected
    return nstates,check

def weighted_cycle_example(n):
    s=[[F(0)]*n for _ in range(n)]
    for i,j in combinations(range(n),2):
        v=F(4) if (i-j)%n in (1,n-1) else F(2)
        s[i][j]=s[j][i]=v
    return q_from_s(s)

def is_connected(n, edges):
    if n<2:return True
    seen={0}; todo=[0]
    while todo:
        a=todo.pop()
        for i,j in edges:
            v=j if i==a else i if j==a else None
            if v is not None and v not in seen:
                seen.add(v);todo.append(v)
    return len(seen)==n

def sparse_rates(n, edges):
    q=[[F(0)]*n for _ in range(n)]
    for i,j in edges:
        q[i][j]=F(1);q[j][i]=F(1)
    return q

def check_all_connected_unweighted(n):
    pairs=list(combinations(range(n),2))
    tests=0
    for mask in range(1,1<<len(pairs)):
        edges=[pairs[i] for i in range(len(pairs)) if (mask>>i)&1]
        if not is_connected(n,edges):continue
        q=sparse_rates(n,edges)
        for k in range(2,n):
            expected=degree_uniform(q) if k==n-1 else (len(edges)==len(pairs))
            assert k_uniform(q,k)==expected,(n,mask,k)
            tests+=1
    return tests

def main():
    rng=Random(314159)
    checks=0
    for n in range(3,9):
        for rep in range(400):
            q=rates_from_integer_matrix(n,rng)
            for k in range(2,n):
                expected=degree_uniform(q) if k==n-1 else pair_uniform(q)
                assert k_uniform(q,k)==expected, (n,k,rep)
                checks+=1
    for n in range(4,13):
        q=weighted_cycle_example(n)
        assert degree_uniform(q)
        assert not pair_uniform(q)
        assert k_uniform(q,n-1)
        assert all(not k_uniform(q,k) for k in range(2,n-1))
        d=sum((q[0][j]+q[j][0] for j in range(1,n)),F(0))
        assert configuration_killing(q,range(n-1))==F(n-2,2)*d
        checks+=n
    n=4
    q=weighted_cycle_example(n)
    m,edges=check_generator(q,3)
    assert m==24
    assert edges==72
    # Explicit matching class exception for four states: three particle
    # collision killing is uniform while the two-particle killing varies.
    for q4 in (
        [[F(0),F(1),F(2),F(3)], [F(1),F(0),F(3),F(2)],
         [F(2),F(3),F(0),F(1)], [F(3),F(2),F(1),F(0)]],
        weighted_cycle_example(4)):
        assert k_uniform(q4,3) and not k_uniform(q4,2)
        m,ed=check_generator(q4,3)
        assert m==24 and ed==72
        checks+=m+ed
    for n in range(3,7):
        checks+=check_all_connected_unweighted(n)
    # A sparse regular example: every cyclic nearest-neighbor rate 1, and
    # exactly one vacancy. The collision rate is constant 2(n-2).
    for n in range(4,13):
        e={(min(i,(i+1)%n),max(i,(i+1)%n)) for i in range(n)}
        q=sparse_rates(n,e)
        assert degree_uniform(q) and not pair_uniform(q)
        assert k_uniform(q,n-1)
        assert all(not k_uniform(q,k) for k in range(2,n-1))
        assert configuration_killing(q,range(n-1))==2*(n-2)
        checks+=n
    print('PASS:',checks,'exact classification tests; 24-state generator checked')

if __name__=='__main__':main()
