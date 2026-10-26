"""Exact rational checks of the finite-element metric-tree positivity theorem.

Run: python3 verify.py (Python standard library only).
Finite checks supplement, not replace, the all-tree proof.
"""
from fractions import Fraction as F
from random import Random


def solve(A, B):
    n = len(A)
    aug = [[F(v) for v in A[i]] + [F(v) for v in B[i]] for i in range(n)]
    for col in range(n):
        pivot = next((i for i in range(col, n) if aug[i][col]), None)
        assert pivot is not None, 'matrix unexpectedly singular'
        aug[col], aug[pivot] = aug[pivot], aug[col]
        den = aug[col][col]
        aug[col] = [v / den for v in aug[col]]
        for i in range(n):
            if i != col:
                fac = aug[i][col]
                if fac:
                    aug[i] = [a - fac*b for a,b in zip(aug[i], aug[col])]
    return [row[n:] for row in aug]


def operator(n, edges, t):
    M = [[F(0) for _ in range(n)] for _ in range(n)]
    K = [[F(0) for _ in range(n)] for _ in range(n)]
    for i, j, length in edges:
        h=F(length)
        M[i][i] += h/3; M[j][j] += h/3
        M[i][j] += h/6; M[j][i] += h/6
        inv = 1/h
        K[i][i] += inv; K[j][j] += inv
        K[i][j] -= inv; K[j][i] -= inv
    H = [[M[i][j] + t*K[i][j] for j in range(n)] for i in range(n)]
    return solve(H,M)


def check_tree(n, edges):
    assert len(edges) == n-1
    adj={i:set() for i in range(n)}
    for a,b,h in edges:
        assert h>0
        adj[a].add(b);adj[b].add(a)
    assert all(adj[i] for i in range(n))
    threshold=max(h*h/F(6) for _,_,h in edges)
    times=[F(0),threshold/F(5),threshold/F(2),threshold*F(999,1000),threshold,threshold*F(1001,1000),threshold*2]
    tests=0
    for t in times:
        P=operator(n,edges,t)
        assert all(sum(row)==1 for row in P), ('mass conservation',n,t)
        assert all(P[i][i]>0 for i in range(n))
        if t:
            assert all(P[i][j]>0 for i in range(n) for j in adj[i]), ('adjacent positive',n,t)
        if t==0 or t>=threshold:
            assert all(P[i][j]>=0 for i in range(n) for j in range(n)), ('nonnegative',n,t)
        else:
            witnesses=[]
            for u,v,h in edges:
                if t<h*h/F(6):
                    if len(adj[u])>1:
                        w=next(w for w in adj[u] if w!=v)
                        witnesses.append((v,w))
                    else:
                        w=next(w for w in adj[v] if w!=u)
                        witnesses.append((u,w))
            assert witnesses and all(P[i][j]<0 for i,j in witnesses), ('strict witness',n,t,witnesses)
        tests+=1
    return tests


def main():
    rng=Random(4096)
    length_choices=[F(1,3),F(1,2),F(2,3),F(3,4),F(1),F(5,4),F(3,2),F(2),F(5,2),F(3)]
    num=0; cases=0
    for n in range(3,9):
        for rep in range(9):
            edges=[(i,rng.randrange(i),rng.choice(length_choices)) for i in range(1,n)]
            num+=check_tree(n,edges)
            cases+=1
    # Explicit no-branch path, irregular star, broom, and a two-vertex exception.
    examples=[(5,[(0,1,F(1)),(1,2,F(7,3)),(2,3,F(1,2)),(3,4,F(4,3))]),
              (6,[(0,i,F(i+1,2)) for i in range(1,6)]),
              (7,[(0,1,F(2)),(1,2,F(1,2)),(1,3,F(4,3)),(3,4,F(3)),(3,5,F(1)),(5,6,F(5,4))])]
    for n, edges in examples:
        num+=check_tree(n,edges);cases+=1
    for h in [F(1,2),F(2),F(7,3)]:
        for t in [F(0),h*h/F(60),h*h/F(6),h*h]:
            P=operator(2,[(0,1,h)],t)
            assert all(P[i][j]>=0 for i in range(2) for j in range(2))
            num+=1
    print(f'PASS: {cases} distinct trees (3-8 vertices), {num} exact rational step/matrix checks; two-vertex exception included.')

if __name__=='__main__': main()
