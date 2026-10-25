"""Exact check of three-leader inverse traces on complete-bipartite-minus-matching graphs.

Standard-library-free computation except for SymPy; public reproducibility artifact.
"""
from itertools import combinations
from math import comb
import sympy as s

x = s.symbols('n', integer=True, positive=True)
d = x - 1
A = (8*x**3-31*x**2+38*x-24)/(3*x*(x-2)*(x-1))
M = (8*x**3-31*x**2+38*x-18)/(3*x*(x-2)*(x-1))
U = (8*x**4-35*x**3+56*x**2-43*x+12)/(x*(x-1)*(3*x**2-8*x+3))
Ablock = 3/d+2*d*((x-4)/(d**2-1)+1/(d**2-(x**2-5*x+7)))
Mblock = 1/d+2*d*((x-3)/(d**2-1)+1/(d**2-(x**2-5*x+7)))
T=x**2-5*x+9
Ublock = 1/d+2*d*((x-4)/(d**2-1)+(2*d**2-T)/(d**4-T*d**2+2))
for left,right in ((A,Ablock),(M,Mblock),(U,Ublock)):
    assert s.cancel(left-right)==0
assert s.factor(M-A)==2/(x*(x-2)*(x-1))
assert s.cancel(U-M-2*(x-1)*(2*x**2-9)/(3*x*(x-2)*(3*x**2-8*x+3)))==0


def graph_laplacian(n):
    L=s.zeros(2*n)
    for a in range(n):
        for b in range(n):
            if a!=b:
                i,j=a,n+b
                L[i,i]+=1
                L[j,j]+=1
                L[i,j]-=1
                L[j,i]-=1
    return L


def typ(n,S):
    a=[j for j in S if j<n]
    b=[j-n for j in S if j>=n]
    if not a or not b: return 'A'
    if len(a)==2: return 'M' if b[0] in a else 'U'
    return 'M' if a[0] in b else 'U'


classes={}
exact_inverse_cases=0
all_triples=0
for n in range(3,9):
    L=graph_laplacian(n)
    wanted={'A':s.factor(A.subs(x,n)), 'M':s.factor(M.subs(x,n)), 'U':s.factor(U.subs(x,n))}
    observed={'A':set(),'M':set(),'U':set()}
    for S in combinations(range(2*n),3):
        F=[v for v in range(2*n) if v not in S]
        val=s.trace(L.extract(F,F).inv())
        key=typ(n,S)
        assert val==wanted[key], (n,S,key,val,wanted[key])
        observed[key].add(tuple(S))
        exact_inverse_cases+=1
        all_triples+=1
    assert len(observed['A'])==2*comb(n,3)
    assert wanted['A']<wanted['M']<wanted['U']
    classes[n]={k:len(v) for k,v in observed.items()}
for n in range(9,16):
    assert (M-A).subs(x,n)>0
    assert (U-M).subs(x,n)>0
print('VERIFY_OK', 'symbolic_identities=5', 'exact_inverse_cases='+str(exact_inverse_cases),
      'three_leader_sets='+str(all_triples), 'orders=3..8',
      'counts='+str(classes))
