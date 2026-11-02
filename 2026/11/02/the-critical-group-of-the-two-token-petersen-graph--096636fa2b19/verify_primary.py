"""Exact arithmetic certificate for the critical group of the two-token Petersen graph.
Requires networkx and sympy. Execute: python verify_primary.py
"""
from collections import Counter
from itertools import combinations
from math import prod
import networkx as nx
import sympy as sp

EXPECTED_POLY = 'x*(x - 7)**6*(x - 6)**6*(x - 5)**4*(x - 3)**5*(x - 2)**5*(x**2 - 13*x + 32)**4*(x**2 - 13*x + 38)**5'
EXPECTED_SMITH = [1]*28+[2]*8+[4]*2+[28,1596,38304]+[191520]*3
PRIME_EXPONENT = {2:36,3:9,5:3,7:6,19:5}
PROFILE = {2:{0:28,1:8,2:4,5:4},3:{0:39,1:1,2:4},5:{0:41,1:3},7:{0:38,1:6},19:{0:39,1:5}}


def v_p(x,p,E):
    if x==0: return E
    k=0
    while x%p==0: x//=p;k+=1
    return k


def p_smith(A,p,E):
    """Diagonalize over Z/p^E via elementary row/column operations.
    At each step the least-valuation entry divides every active entry in Z/p^E.
    Its unit part is invertible, so both its column and row can be cleared.
    Result: the p-valuations of the Smith diagonal in nondecreasing order.
    """
    mod=p**E;n=len(A)
    M=[[u%mod for u in row] for row in A]
    valuations=[]
    for k in range(n):
        best=(E,None,None)
        for i in range(k,n):
            for j in range(k,n):
                e=v_p(M[i][j],p,E)
                if e<best[0]:best=(e,i,j)
                if best[0]==0:break
            if best[0]==0:break
        e,r,c=best
        assert r is not None, 'modular precision too small for nonzero determinant'
        M[k],M[r]=M[r],M[k]
        for row in M:row[k],row[c]=row[c],row[k]
        t=p**e; unit=M[k][k]//t
        modulus=mod//t
        inverse=pow(unit,-1,modulus)
        for i in range(k+1,n):
            coef=((M[i][k]//t)*inverse)%modulus
            if coef:
                for j in range(k,n):
                    M[i][j]=(M[i][j]-coef*M[k][j])%mod
            assert M[i][k]==0
        for j in range(k+1,n):
            coef=((M[k][j]//t)*inverse)%modulus
            if coef:
                for i in range(k,n):
                    M[i][j]=(M[i][j]-coef*M[i][k])%mod
            assert M[k][j]==0
        valuations.append(e)
    assert valuations==sorted(valuations)
    return valuations


def main():
    P=nx.petersen_graph()
    pairs=list(combinations(range(10),2))
    index={e:i for i,e in enumerate(pairs)}
    N=len(pairs)
    lap=[[0]*N for _ in range(N)]
    for i,(u,v) in enumerate(pairs):
        for occupied,stationary in ((u,v),(v,u)):
            for destination in P[occupied]:
                if destination==stationary:continue
                j=index[tuple(sorted((destination,stationary)))]
                lap[i][i]+=1;lap[i][j]-=1
    assert N==45 and sum(lap[i][i] for i in range(N))==240
    assert all(sum(row)==0 for row in lap)
    A=[row[:-1] for row in lap[:-1]]
    x=sp.symbols('x'); polynomial=sp.factor(sp.Matrix(lap).charpoly(x).as_expr())
    assert sp.expand(polynomial-sp.sympify(EXPECTED_POLY))==0
    positive_product=(7**6)*(6**6)*(5**4)*(3**5)*(2**5)*(32**4)*(38**5)
    tau=positive_product//45
    assert positive_product%45==0
    smith_profiles={}
    for p,e in PRIME_EXPONENT.items():
        vals=p_smith(A,p,e+1)
        assert dict(Counter(vals))==PROFILE[p]
        assert sum(vals)==e
        smith_profiles[p]=vals
    diagonal=[prod(p**smith_profiles[p][i] for p in PRIME_EXPONENT) for i in range(44)]
    assert diagonal==EXPECTED_SMITH
    assert prod(diagonal)==tau
    print('PRIMARY_EXACT_PASS', 'vertices',N,'edges',120,'tree_count',tau)
    print('PRIMARY_CHARACTERISTIC_POLYNOMIAL', polynomial)
    print('PRIMARY_SMITH',dict(Counter(diagonal)))
    for p in PRIME_EXPONENT:
        print('PRIMARY_P_ADIC',p,dict(Counter(smith_profiles[p])))

if __name__=='__main__':main()
