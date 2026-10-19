"""Exact finite checks of the reciprocal-polynomial derivative numerators.
All unrestricted statements require the independent algebraic proof.
"""
import sympy as sp

z=sp.symbols('z')
cases=[(0,1),(0,2,5),(-3,0,2,7),(0,1,2,3,4)]
checks=0
for nodes in cases:
    n=len(nodes)-1
    P=sp.prod((z-sp.Integer(a)) for a in nodes)
    Q=sp.Integer(1)
    for m in range(0,7):
        if m:
            Q=sp.expand(sp.diff(P,z)*Q-P*sp.diff(Q,z)/m)
        poly=sp.Poly(Q,z)
        assert poly.degree()==n*m, (nodes,m,'degree')
        for a in nodes:
            assert Q.subs(z,a)==sp.diff(P,z).subs(z,a)**m, (nodes,m,'pole')
        totalreal=poly.count_roots(-sp.oo,sp.oo)
        assert totalreal==(n if m%2 else 0), (nodes,m,'real roots',totalreal)
        if m%2:
            for a,b in zip(nodes[:-1],nodes[1:]):
                assert poly.count_roots(a,b)==1, (nodes,m,'gap',a,b)
        assert (poly.degree()-totalreal)//2 == n*(m//2)
        checks+=1
    print(f'OK knots={nodes}, n={n}, m=0..6')
print(f'PASS {checks} exact polynomial zero-count test cases; these are not an infinite proof.')
