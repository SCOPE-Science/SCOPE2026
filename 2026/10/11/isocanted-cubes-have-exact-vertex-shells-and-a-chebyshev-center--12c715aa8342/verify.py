#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
import sympy as sp

def source_vertices(d, L, a):
    out=[]
    for k in range(1,d+1):
        for Wt in combinations(range(d),k):
            W=set(Wt)
            v=tuple(Fraction(L,2) if i in W else Fraction(a)-Fraction(L,2) for i in range(d))
            out.append((k,v))
            out.append((k,tuple(-x for x in v)))
    return out

checks=0
for d in range(2,9):
    for L,a in [(4,1),(5,2),(7,6),(9,4)]:
        assert 0<a<L
        V=source_vertices(d,L,a)
        assert len(V)==2**(d+1)-2
        assert len({v for _,v in V})==len(V)

        counts={k:0 for k in range(1,d+1)}
        shell_values={}
        coord_tight={(i,s):False for i in range(d) for s in (-1,1)}
        diff_tight={(i,j,s):False for i in range(d) for j in range(i+1,d) for s in (-1,1)}

        for k,v in V:
            counts[k]+=1
            for i,x in enumerate(v):
                assert abs(x)<=Fraction(L,2)
                if x==Fraction(L,2):
                    coord_tight[(i,1)]=True
                if x==-Fraction(L,2):
                    coord_tight[(i,-1)]=True
            for i in range(d):
                for j in range(i+1,d):
                    diff=v[i]-v[j]
                    assert abs(diff)<=L-a
                    if diff==L-a:
                        diff_tight[(i,j,1)]=True
                    if diff==-(L-a):
                        diff_tight[(i,j,-1)]=True

            n2=sum(x*x for x in v)
            closed=Fraction(k*L*L,4)+(d-k)*(Fraction(L,2)-a)**2
            assert n2==closed
            shell_values[k]=closed
            checks+=1

        for k in range(1,d+1):
            assert counts[k]==2*sp.binomial(d,k)
        assert all(coord_tight.values())
        assert all(diff_tight.values())
        for k in range(1,d):
            assert shell_values[k+1]-shell_values[k]==a*(L-a)>0
        assert shell_values[d]==Fraction(d*L*L,4)

# Exact radical phase checks.
ell=sp.symbols("ell", positive=True)
a=sp.symbols("a", positive=True)
sqrt2=sp.sqrt(2)
astar=sp.simplify(ell*(1-1/sqrt2))
rcoord=ell/2
rdiff=(ell-a)/sqrt2
assert sp.simplify(rdiff.subs(a,astar)-rcoord)==0

# Representative exact points on the two sides.
for q,side in [(sp.Rational(1,4),"below"),(sp.Rational(1,2),"above")]:
    expr=sp.simplify((ell*q-astar)/ell)
    if side=="below":
        assert bool(expr<0)
        assert bool(sp.simplify((rdiff-rcoord).subs(a,ell*q))>0)
    else:
        assert bool(expr>0)
        assert bool(sp.simplify((rcoord-rdiff).subs(a,ell*q))>0)
        halfwidth=sp.simplify(rcoord-rdiff.subs(a,ell*q))
        assert bool(halfwidth>0)

print(f"VERIFY_OK isocanted-cube-shell-center-phase vertex_checks={checks} d=2..8 exact=yes")
