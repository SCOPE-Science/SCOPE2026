"""Exact-rational verification of categorical-complete-graph cut/cycle projection formulas.
Run: python verify_categorical.py ; requires sympy. Finite tests supplement, not replace, the paper proof.
"""
from fractions import Fraction as F
from itertools import combinations
import sympy as sp

def formulas(a,b):
    a,b=F(a),F(b)
    base=2*(a*a*b*b-a*a-b*b-6*a*b+5*a+5*b-3)/(a*b*(a-1)*(b-1))
    imbalance=2*abs(a-b)*(2*a*b-4*a-4*b+9)/(a*b*(a-1)*(b-1)*(a*b-a-b))
    cut=base+imbalance
    cycle=cut+1-4*(a*b-1)/(a*b*(a-1)*(b-1))
    return cut,cycle

def graph(a,b):
    vertices=[(i,j) for i in range(a) for j in range(b)]
    edges=[(u,v) for u,v in combinations(range(len(vertices)),2)
           if vertices[u][0]!=vertices[v][0] and vertices[u][1]!=vertices[v][1]]
    return vertices,edges

def potential(a,b,vertices,u,v):
    (i0,j0),(i1,j1)=vertices[u],vertices[v]
    assert i0!=i1 and j0!=j1
    d=a*b-a-b
    p=F(1,a*(b-1));q=F(1,b*(a-1))
    return [F((i==i0 and j==j0)-(i==i1 and j==j1),d)
            -F((i==i0)-(i==i1),d)*p
            -F((j==j0)-(j==j1),d)*q for (i,j) in vertices]

def test_case(a,b):
    V,E=graph(a,b); n=len(V)
    u,v=V.index((0,0)),V.index((1,1))
    f=potential(a,b,V,u,v)
    lap=[F(0) for _ in V]
    for x,y in E:
        lap[x]+=f[x]-f[y]
        lap[y]+=f[y]-f[x]
    assert all(lap[k]==(1 if k==u else -1 if k==v else 0) for k in range(n))
    col=sum(abs(f[x]-f[y]) for x,y in E)
    diag=f[u]-f[v]
    cut,cycle=formulas(a,b)
    assert col==cut
    assert col+1-2*diag==cycle
    assert diag==F(2*(a*b-1),a*b*(a-1)*(b-1))
    return len(E)

def test_grounded_all(a,b):
    V,E=graph(a,b);n=len(V)
    L=sp.zeros(n,n)
    for u,v in E:
       L[u,u]+=1;L[v,v]+=1;L[u,v]-=1;L[v,u]-=1
    H=L[1:,1:].inv()
    normQ,normP=formulas(a,b)
    for u,v in E:
       source=sp.zeros(n-1,1)
       if u:source[u-1]+=1
       if v:source[v-1]-=1
       z=[F(0)]+[F(x.p,x.q) for x in H*source]
       qcolumn=[z[x]-z[y] for x,y in E]
       csum=sum(map(abs,qcolumn))
       assert csum==normQ
       pcolsum=sum(abs((1 if (x,y)==(u,v) else 0)-c)
                   for (x,y),c in zip(E,qcolumn))
       assert pcolsum==normP
    return len(E)

def symbolic_proof_checks():
    a,b=sp.symbols('a b',positive=True)
    d=(a-1)*(b-1);D=a*b-a-b
    p=1/(a*(b-1));q=1/(b*(a-1))
    c1=d
    c2=(b-1)*d-2*(b-2)
    c3=(a+b-3)*d-2*D
    c4=(a+b-2)*d-2*(D+a-2)
    coarea=2*((1-2*p-q)*c1+(p-q)*c2+(2*q-p)*c3+(p-q)*c4)/D
    base=2*(a*a*b*b-a*a-b*b-6*a*b+5*a+5*b-3)/(a*b*(a-1)*(b-1))
    corr=2*(a-b)*(2*a*b-4*a-4*b+9)/(a*b*(a-1)*(b-1)*D)
    assert sp.factor(coarea-base-corr)==0
    assert sp.factor((2/D)*(1-p-q)-2*(a*b-1)/(a*b*(a-1)*(b-1)))==0
    u,v=sp.symbols('u v',nonnegative=True)
    aa=u+3;bb=aa+v
    expression=sp.factor(sp.Rational(8,3)-(base-corr))
    polynomial_den=3*(u+2)*(u+3)*(u+v+2)*(u+v+3)*(u*u+u*v+4*u+2*v+3)
    H0=u**6+8*u**5+29*u**4+82*u**3+186*u**2+234*u+108
    H1=3*u**5+20*u**4+58*u**3+117*u**2+174*u+108
    H2=3*u**4+16*u**3+33*u**2+35*u+24
    H3=u*(u+2)**2
    assert sp.factor(expression.subs({a:aa,b:bb})-2*(H0+v*H1+v**2*H2+v**3*H3)/polynomial_den)==0
    assert all(x>0 for x in sp.Poly(H0,u).all_coeffs())
    assert all(x>0 for x in sp.Poly(H1,u).all_coeffs())
    assert all(x>0 for x in sp.Poly(H2,u).all_coeffs())
    assert sp.expand(H3)==u**3+4*u*u+4*u

if __name__=='__main__':
    symbolic_proof_checks()
    checks=0
    for a in range(3,13):
        for b in range(3,13):
            checks+=test_case(a,b)
    allcols=0
    for a,b in [(3,3),(3,4),(4,4)]:
        allcols+=test_grounded_all(a,b)
    print(f'CATEGORICAL_COMPLETE_GRAPH_EXACT_OK configurations=100 edge_current_checks={checks} grounded_projection_columns={allcols} symbolic_identities=PASS')
