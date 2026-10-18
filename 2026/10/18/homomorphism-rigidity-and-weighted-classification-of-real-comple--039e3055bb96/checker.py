#!/usr/bin/env python3
"""Exact rational verification of illustrative complete-multipartite evolution-algebra maps."""
from fractions import Fraction as F

H3 = [[F(2,3),F(-1,3),F(2,3)],
      [F(-1,3),F(2,3),F(2,3)],
      [F(2,3),F(2,3),F(-1,3)]]
I1 = [[F(1)]]
I2 = [[F(1),F(0)],[F(0),F(1)]]
S2 = [[F(0),F(1)],[F(1),F(0)]]

def dot(a,b): return sum((x*y for x,y in zip(a,b)),F(0))
def groups(sizes):
    out=[]; p=0
    for n in sizes: out.append(list(range(p,p+n))); p+=n
    return out

def structure(sizes, weights):
    gr=groups(sizes); n=sum(sizes)
    S=[[F(0) for _ in range(n)] for _ in range(n)]
    for a,vs in enumerate(gr):
        for i in vs:
            for b,ws in enumerate(gr):
                if a!=b:
                    for j in ws: S[i][j]=F(weights[a])
    return S

def mapping(src_sizes, dst_sizes, permutation, t, orths):
    g=groups(src_sizes); h=groups(dst_sizes); n=sum(src_sizes)
    T=[[F(0) for _ in range(n)] for _ in range(n)] # row = source, column = target
    for a,vs in enumerate(g):
        ws=h[permutation[a]]
        O=orths[a]
        assert len(vs)==len(ws)==len(O)
        assert all(len(row)==len(ws) for row in O)
        assert all(sum(row)==1 for row in O)
        assert all(dot([O[x][j] for x in range(len(ws))], [O[x][k] for x in range(len(ws))])==int(j==k) for j in range(len(ws)) for k in range(len(ws)))
        for i,src in enumerate(vs):
            for j,dst in enumerate(ws): T[src][dst]=F(t[a])*O[i][j]
    return T

def mapcheck(sizes1,c,sizes2,d,permutation,t,orths):
    X=structure(sizes1,c);Y=structure(sizes2,d)
    T=mapping(sizes1,sizes2,permutation,t,orths)
    n=sum(sizes1)
    assert n==sum(sizes2)
    # f(e_i e_j) = f(e_i) f(e_j) for every pair of basis vectors.
    for i in range(n):
        for j in range(n):
            lhs=[sum((X[i][k]*T[k][u] for k in range(n)),F(0)) if i==j else F(0) for u in range(n)]
            rhs=[sum((T[i][k]*T[j][k]*Y[k][u] for k in range(n)),F(0)) for u in range(n)]
            assert lhs==rhs,(i,j,lhs,rhs)
    return n

def test():
    # Non-monomial isomorphism of a three-part weighted algebra.
    assert mapcheck([3,2,1],[2,3,5],[3,2,1],[4,6,10],[0,1,2],[F(1,2)]*3,[H3,S2,I1])==6
    # Different part ordering, weights permuted and rescaled.
    assert mapcheck([2,3,1],[2,3,5],[1,2,3],[10,4,6],[1,2,0],[F(1,2)]*3,[I2,H3,I1])==6
    # Bipartite case: arbitrary positive weights yield a nontrivial scaling.
    assert mapcheck([2,3],[1,1],[2,3],[1,8],[0,1],[F(1,2),F(1,4)],[S2,H3])==5
    # Graph adjacency vs graph random walk: balanced singular tripartite graph.
    assert mapcheck([3,3,3],[1,1,1],[3,3,3],[F(1,6)]*3,[0,1,2],[6,6,6],[H3,H3,H3])==9
    # The weight-ratio criterion gives a genuine mismatch for a singular graph.
    sizes=[1,2,3]; deg=[sum(sizes)-i for i in sizes]
    assert len(set(deg))==3
    assert len(set(F(1)/F(1,x) for x in deg))==3
    # Independence of the target square classes for all partition counts 2,...,8.
    for r in range(2,9):
        v=[[int(a!=b) for b in range(r)] for a in range(r)]
        # If sum_a u_a v_a=0, then sum_a u_a =u_b for all b;
        # r>=2 forces each u_b=0, hence matrix has full rank.
        # Fraction-valued Gaussian elimination, requiring only the standard library.
        mat=[[F(x) for x in row] for row in v]
        determinant=F(1)
        for j in range(r):
            pivot=next((i for i in range(j,r) if mat[i][j]),None)
            assert pivot is not None
            if pivot!=j:
                mat[pivot],mat[j]=mat[j],mat[pivot]
                determinant=-determinant
            w=mat[j][j]
            determinant*=w
            for i in range(j+1,r):
                factor=mat[i][j]/w
                for k in range(j,r): mat[i][k]-=factor*mat[j][k]
        assert determinant==(-1)**(r-1)*(r-1)
    print('CHECKER_OK: four exact multiplication certificates and square-class independence r=2,...,8')
if __name__=='__main__': test()
