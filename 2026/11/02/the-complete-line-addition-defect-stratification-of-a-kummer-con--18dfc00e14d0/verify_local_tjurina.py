"""Exact symbolic checks of the local Tjurina lemma for k=2,...,14.
The general all-k proof is in RESULT.md; finite runs are corroboration.
Requires sympy.
"""
import sympy as sp
u,v,t = sp.symbols('u v t')

def standard_monomial_length(G):
    leads=[P.monoms()[0] for P in G.polys]
    a=min((i for i,j in leads if j==0), default=None)
    b=min((j for i,j in leads if i==0), default=None)
    assert a is not None and b is not None
    return sum(not any(x<=i and y<=j for x,y in leads)
               for i in range(a) for j in range(b))

for k in range(2,15):
    h=u**k+v**(2*k)
    g=(u+v)*h
    s=v**k+(-1)**k # vanishes at the k nonzero crossing nodes
    sat=sp.groebner([g,sp.diff(g,u),sp.diff(g,v),1-t*s],t,u,v,order='lex')
    no_t=[P.as_expr() for P in sat.polys if not P.as_expr().has(t)]
    local=sp.groebner(no_t,u,v,order='lex')
    length=standard_monomial_length(local)
    expected=2*k*k-2*k+2
    assert length == expected, (k,length,expected)
    if k>=3:
        A=u**k+2*k*u*v**(2*k-1)+(2*k+1)*v**(2*k)
        B=u**(k-1)*v-(2*k+2)*u*v**(2*k-1)-(2*k+3)*v**(2*k)
        C=v**(2*k-1)*(u**2-v**2)
        D=v**(2*k)*(u+v)
        E=v**(3*k-2)
        universal=sp.groebner([A,B,C,D,E],u,v,order='lex')
        assert all(local.reduce(Q)[1]==0 for Q in [A,B,C,D,E])
        assert all(universal.reduce(Q)[1]==0 for Q in no_t)
        assert standard_monomial_length(universal)==expected
    print(f'k={k} tau_local={length} expected={expected}')
print('LOCAL_TJURINA_ALL_CHECKS_OK')
