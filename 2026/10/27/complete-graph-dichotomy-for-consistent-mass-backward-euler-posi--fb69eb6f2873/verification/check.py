"""Reproduce exact and numerical checks for equilateral-network diffusion positivity.

Requires Python 3, NumPy, SymPy, NetworkX.
"""
from fractions import Fraction
import numpy as np
import networkx as nx
import sympy as sp

LOW = [Fraction(1,1000), Fraction(1,100), Fraction(1,20), Fraction(1,10), Fraction(3,20), Fraction(1,6)-Fraction(1,1000)]
HIGH = [Fraction(1,6), Fraction(1,6)+Fraction(1,1000), Fraction(1,5), Fraction(1,2), Fraction(2)]


def graph_step(A, h, exact=False):
    n=A.rows if isinstance(A,sp.MatrixBase) else len(A)
    if exact:
        A=sp.Matrix(A)
        D=sp.diag(*[sum(A[i,j] for j in range(n)) for i in range(n)])
        return ((2+6*h)*D + (1-6*h)*A).inv() * (2*D+A)
    A=np.asarray(A, dtype=float)
    D=np.diag(A.sum(axis=0))
    h=float(h)
    return np.linalg.solve((2+6*h)*D+(1-6*h)*A,2*D+A)


def verify():
    exact_graphs=0
    numeric_graphs=0
    cases_exact=0
    cases_numeric=0
    for graph in nx.graph_atlas_g():
        n=len(graph)
        if not 2<=n<=7 or not nx.is_connected(graph):
            continue
        full = graph.number_of_edges()==n*(n-1)//2
        A=nx.to_numpy_array(graph, nodelist=sorted(graph.nodes()), dtype=int)
        for h in LOW+HIGH:
            P=graph_step(A,h,False)
            assert np.max(np.abs(P.sum(axis=1)-1))<1e-10, (n,h,"mass conservation")
            if full or h in HIGH:
                assert np.min(P)>-2e-11, (n,h,full,np.min(P))
            else:
                assert np.min(P)<-1e-11, (n,h,full,np.min(P))
            cases_numeric+=1
        numeric_graphs+=1
        if n<=5:
            exA=sp.Matrix([[int(x) for x in row] for row in A])
            for h in LOW+HIGH:
                P=graph_step(exA,sp.Rational(h.numerator,h.denominator),True)
                vals=[P[i,j] for i in range(n) for j in range(n)]
                assert (min(vals)>=0)==(full or h in HIGH),(n,h,full,vals)
                assert all(sum(P[i,j] for j in range(n))==1 for i in range(n))
                cases_exact+=1
            exact_graphs+=1
    # direct symbolic complete-graph eigenvalue formula
    z=sp.symbols('z',positive=True)
    for n in range(2,6):
        A=sp.ones(n,n)-sp.eye(n)
        R=(2*n-3)/(2*n-3+6*n*z)
        assert sp.simplify(graph_step(A,z,True)[0,0]-(R+(1-R)/n))==0
        assert sp.simplify(graph_step(A,z,True)[0,n-1]-(1-R)/n)==0
    print('PASS: %d connected atlas graphs, %d float sign/mass checks; %d exact graphs, %d exact rational sign/mass checks; 4 symbolic complete-graph cases.'%(numeric_graphs,cases_numeric,exact_graphs,cases_exact))

if __name__ == '__main__':
    verify()
