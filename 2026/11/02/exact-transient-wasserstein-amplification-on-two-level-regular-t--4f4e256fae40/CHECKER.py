"""Reproducible tests for two-layer homogeneous-tree W1 semigroup formulas.
Requires Python 3, NumPy and SciPy. Run: python CHECKER.py.
"""
import math
import numpy as np
from scipy.linalg import expm
from scipy.optimize import linprog


def tree_incidence(b, k):
    """Root has b children, each child has k leaves; edges oriented outward."""
    if b < 2 or k < 2:
        raise ValueError("b and k must be at least two")
    edges = []
    next_vertex = 1
    for i in range(b):
        parent = next_vertex
        next_vertex += 1
        edges.append((0, parent))
        for j in range(k):
            leaf = next_vertex
            next_vertex += 1
            edges.append((parent, leaf))
    B = np.zeros((next_vertex, len(edges)))
    for e, (u, v) in enumerate(edges):
        B[u, e] = -1
        B[v, e] = 1
    return B, edges


def formula(b, k, t):
    root = math.sqrt(k)
    S = expm(-t*np.array([[1., -root], [-root, k+1.]]))
    G = expm(-t*np.array([[b+1., -root], [-root, k+1.]]))
    z = math.exp(-t)
    s11,s12,s22=S[0,0],S[0,1],S[1,1]
    g11,g12,g22=G[0,0],G[0,1],G[1,1]
    I = (abs((b-1)*s11+g11)+(b-1)*abs(g11-s11))/b
    I += root*(abs((b-1)*s12+g12)+(b-1)*abs(g12-s12))/b
    U = ((b-1)*s22+g22)/b
    O = (abs((b-1)*s12+g12)+(b-1)*abs(g12-s12))/(b*root)
    O += (abs(U+(k-1)*z)+(k-1)*abs(U-z))/k
    O += (b-1)*abs(g22-s22)/b
    return I,O


def signed_tree_transport(mass, edges, vertices):
    """Unique-flow W1 formula, computed by descendant masses."""
    ch = [[] for _ in range(vertices)]
    for u, v in edges:
        ch[u].append(v)
    sub = np.array(mass, dtype=float)
    for v in reversed(range(vertices)):
        for w in ch[v]:
            sub[v] += sub[w]
    return sum(abs(sub[v]) for _, v in edges)


def test_formula():
    tests=0
    for b in range(2,7):
        for k in range(2,7):
            B,edges=tree_incidence(b,k)
            E=B.T@B
            L=B@B.T
            for t in [0.0,0.001,0.02,0.2,0.5,1.0,2.0,5.0,10.0]:
                full=expm(-t*E)
                I,O=formula(b,k,t)
                row=np.abs(full).sum(axis=1)
                assert np.max(np.abs(row[::(k+1)]-I))<4e-12, (b,k,t,I,row[0])
                for j in range(b):
                    st=j*(k+1)
                    assert np.max(np.abs(row[st+1:st+k+1]-O))<4e-12,(b,k,t,O)
                assert abs(max(I,O)-max(row))<4e-12
                assert max(I,O)<=4+2e-12
                assert I>=0 and O>=0
                if b<=4 and k<=4 and t in [0.0,0.2,1.0,5.0]:
                    Pt=expm(-t*L)
                    for e in [0,1,k+1]:
                        u,v=edges[e]
                        val=signed_tree_transport(Pt[:,v]-Pt[:,u],edges,len(Pt))
                        assert abs(val-row[e])<3e-12,(b,k,t,e,val,row[e])
                        tests+=1
                tests+=3
    return tests


def test_primal():
    tests=0
    for b,k,t,e in [(2,2,0.25,0),(2,3,0.45,1),(3,2,0.3,0),(3,3,0.8,1),(4,3,0.75,0)]:
        B,edges=tree_incidence(b,k)
        L=B@B.T
        n=len(L)
        Pt=expm(-t*L)
        u,v=edges[e]
        mu=Pt[:,v]
        nu=Pt[:,u]
        # All-pairs graph distances on this tree.
        from scipy.sparse.csgraph import shortest_path
        A=np.zeros((n,n))
        for a,c in edges: A[a,c]=A[c,a]=1
        D=shortest_path(A,directed=False,unweighted=True)
        c=D.reshape(n*n)
        mat=[]
        rhs=[]
        # Transportation plan x_{i,j} with prescribed row/column sums.
        for i in range(n):
            row=np.zeros(n*n);row[i*n:(i+1)*n]=1
            mat.append(row);rhs.append(mu[i])
        for j in range(n):
            col=np.zeros(n*n);col[j::n]=1
            mat.append(col);rhs.append(nu[j])
        result=linprog(c,A_eq=mat,b_eq=rhs,bounds=(0,None),method='highs')
        assert result.success
        val=signed_tree_transport(mu-nu,edges,n)
        assert abs(result.fun-val)<2e-9,(b,k,t,e,val,result.fun)
        tests+=1
    return tests


def test_large_branching():
    previous=0
    tests=0
    for n in [8,16,32,64,128,256,512,1024]:
        t=n**(-0.5)
        I,O=formula(n,n,t)
        assert 1<I<4+1e-10 and 0<=O<4+1e-10
        assert I>previous
        previous=I
        tests+=1
    assert previous>3.98
    return tests


if __name__=='__main__':
    counts=(test_formula(),test_primal(),test_large_branching())
    print('PASS: matrix/flow comparisons = %d; transport LPs = %d; large-branching tests = %d' % counts)
