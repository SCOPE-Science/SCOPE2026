"""Exact finite tests for optimal limited domination on the depth-two Sierpiński graph.

Run: python3 verify_sierpinski2_limited.py
The finite tests are corroboration; the family proof is combinatorial.
"""
from itertools import combinations
from math import factorial


def graph(m):
    v=[(i,j) for i in range(m) for j in range(m)]
    adj=[set() for _ in v]
    for i in range(m):
        for j in range(m):
            for h in range(m):
                if j!=h: adj[m*i+j].add(m*i+h)
                if i!=j: adj[m*i+j].add(m*j+i)
    return adj


def valid(m,k,D,adj):
    S=set(D)
    return (all(i in S or bool(adj[i]&S) for i in range(m*m)) and
            all(len(adj[i]-S)<=k for i in S))


def symmetric_masks(m,r):
    """Enumerates selected vertex sets from off-diagonal undirected edge patterns."""
    edges=list(combinations(range(m),2))
    for bits in range(1 << len(edges)):
        degrees=[0]*m
        selected=[]
        for pos,(i,j) in enumerate(edges):
            if (bits>>pos)&1:
                degrees[i]+=1; degrees[j]+=1
                selected.extend((m*i+j,m*j+i))
        if any(r-d not in (0,1) for d in degrees): continue
        selected.extend(m*i+i for i,d in enumerate(degrees) if r-d==1)
        yield tuple(sorted(selected))


def involutions(m):
    return sum(factorial(m)//(2**j*factorial(j)*factorial(m-2*j))
               for j in range(m//2+1))


def looped_two_regular_count(m):
    # Labelled SET of path components with loops at both endpoints (size>=2)
    # and ordinary cycles (size>=3); exponential generating-function convolution.
    # Recurrence for coefficients of exp(sum_{l>=2} x^l/2+sum_{l>=3} x^l/(2l)).
    # Use integer arithmetic by direct component recurrence.
    if m==0:return 1
    if m==1:return 0
    # Component of 0: path on s vertices (s!/2) or cycle ((s-1)!/2).
    total=0
    for s in range(2,m+1):
        from math import comb
        p=factorial(s)//2
        c=factorial(s-1)//2 if s>=3 else 0
        total+=comb(m-1,s-1)*(p+c)*looped_two_regular_count(m-s)
    return total


def main():
    brute_cases=0
    for m in range(2,5):
        adj=graph(m)
        for k in range(1,m):
            r=m-k
            actual={D for D in combinations(range(m*m),m*r) if valid(m,k,D,adj)}
            predicted=set(symmetric_masks(m,r))
            assert actual==predicted,(m,k,len(actual),len(predicted))
            brute_cases+=1
    values=[]
    for m in range(2,7):
        adj=graph(m)
        counts={}
        for r in range(1,m):
            choices=list(symmetric_masks(m,r))
            assert len(set(choices))==len(choices)
            assert all(valid(m,m-r,B,adj) for B in choices)
            counts[r]=len(choices)
            assert counts[r]==counts.get(m-r,counts[r]) if m-r in counts else True
            if r in (1,m-1):assert len(choices)==involutions(m)
            if r==2:assert len(choices)==looped_two_regular_count(m)
        assert all(counts[r]==counts[m-r] for r in counts)
        values.append((m,counts))
    print('VERIFY_OK exhaustive_graph_cases=%d matrix_sizes=2..6 exact_counts=%s' %
          (brute_cases,values))


if __name__=='__main__':
    main()
