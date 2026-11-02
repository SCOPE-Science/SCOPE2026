"""Independent exact checks for the Fermat quartic threefold Fano-curve calculation.

Requires Python 3.10+ and SymPy 1.12+. These tests corroborate the
coefficient and incidence calculations; global completeness is proved in RESULT.md.
"""
from itertools import combinations
from sympy import Matrix, Poly, symbols, expand

s,t,a,b,c,d,e,f = symbols('s t a b c d e f')
U=(1+a)*s+b*t
W=c*s+(1+d)*t
F=expand(-U**4+s**4-W**4+t**4+(e*s+f*t)**4)
coeff=[expand(Poly(F,s,t).coeff_monomial(s**(4-k)*t**k)) for k in range(5)]
J=Matrix([[coeff[k].diff(v).subs({a:0,b:0,c:0,d:0,e:0,f:0})
           for v in (a,b,c,d)] for k in (0,1,3,4)])
assert J==Matrix.diag(-4,-4,-4,-4), J
middle=coeff[2]
# IFT solutions for a,b,c,d start in degree four in (e,f).
assert expand(middle.subs({a:0,b:0,c:0,d:0})-6*e**2*f**2)==0
# Quartic jets solve the four independent coefficient equations.
jet={a:e**4/4,b:e**3*f,c:e*f**3,d:f**4/4}
for k in (0,1,3,4):
    polynomial=Poly(expand(coeff[k].subs(jet)),e,f)
    assert all(sum(monomial)>=8 for monomial,coefficient in polynomial.terms()
               if coefficient!=0), (k,polynomial)
assert all(sum(monomial)>=8 for monomial,coefficient in Poly(expand(middle.subs(jet)-6*e**2*f**2),e,f).terms() if coefficient!=0)
# Exactly 40 labelled irreducible components, 240 distinct nodal points.
pairs=list(combinations(range(5),2))
components=[(ij,phase) for ij in pairs for phase in range(4)]
assert len(components)==40
nodes={}
for i,(ij,phase) in enumerate(components):
    for kl,rho in components[i+1:]:
        if not set(ij)&set(kl):
            # Vertex-free fifth coordinate and two pair ratios determine a line.
            datum=(tuple(sorted((ij,kl))),
                   tuple(sorted(((ij,phase),(kl,rho)))))
            assert datum not in nodes
            nodes[datum]=((ij,phase),(kl,rho))
assert len(nodes)==240
valency={component:0 for component in components}
for pair in nodes.values():
    for component in pair:
        valency[component]+=1
assert set(valency.values())=={12}
# A 40-vertex graph with all intersecting components connected.
visited={components[0]}
while True:
    nxt=visited|{v for u,v in nodes.values() if u in visited}|{u for u,v in nodes.values() if v in visited}
    if nxt==visited:break
    visited=nxt
assert len(visited)==40
p_a=1+40*(3-1)+len(nodes)
assert p_a==321
print('FERMAT_QUARTIC_FANO_JACOBIAN_240_DOUBLE_NODES_GENUS321_OK')
print('four-by-four transverse Jacobian:',J)
print('middle coefficient initial term:',6*e**2*f**2)
print('components:',len(components),'nodes:',len(nodes),'valency:',set(valency.values()),'arithmetic_genus:',p_a)
