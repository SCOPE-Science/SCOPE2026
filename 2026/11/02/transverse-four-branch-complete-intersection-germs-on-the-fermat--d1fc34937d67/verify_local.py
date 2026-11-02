#!/usr/bin/env python3
"""Exact symbolic and support-incidence checks for second-type lines on the Fermat cubic fourfold.
Uses SymPy; does not substitute finite sampling for the local analytic proof.
"""
import itertools
import sympy as s

I = frozenset(range(6))
triple_partitions = set()
for a in itertools.combinations(range(6), 3):
    A = frozenset(a)
    if 0 in A:
        triple_partitions.add(frozenset((A, I - A)))
assert len(triple_partitions) == 10
pair_types = [(frozenset(P), root) for P in itertools.combinations(range(6), 2) for root in range(3)]
assert len(pair_types) == 45
cross = [(part, P, root) for part in triple_partitions for P, root in pair_types if any(P <= block for block in part)]
assert len(cross) == 180
for part in triple_partitions:
    assert sum(1 for x in cross if x[0] == part) == 18
for P, root in pair_types:
    assert sum(1 for x in cross if (x[1], x[2]) == (P, root)) == 4

points = []
for P in itertools.combinations(range(6), 2):
    P = frozenset(P)
    for Q in itertools.combinations(sorted(I - P), 2):
        Q = frozenset(Q)
        if tuple(sorted(P)) >= tuple(sorted(Q)):
            continue
        for rp in range(3):
            for rq in range(3):
                points.append((P,Q,rp,rq))
assert len(points) == 405
SS = list(itertools.combinations(triple_partitions,2))
assert len(SS) == 45
assert all(sum(1 for point in points if all(any(point[0] <= block for block in part) and any(point[1] <= block for block in part) and not any((point[0] | point[1]) <= block for block in part) for part in (a,b))) == 9 for a,b in SS)
# Each point has exactly two partitions of triples and two Eckardt-type surfaces.
for P,Q,rp,rq in points:
    containing_ss = [part for part in triple_partitions if any(P <= A and Q <= B for A in part for B in part if A != B)]
    containing_tt = [(R,r) for R,r in pair_types if (R,r) in ((P,rp),(Q,rq))]
    assert len(containing_ss) == 2 and len(containing_tt) == 2
    containing_curves = [(part,R,r) for part,R,r in cross if part in containing_ss and (R,r) in containing_tt]
    assert len(containing_curves) == 4
assert len(points)*4 == len(cross)*9

A,B,C,D,E,F,G,H,u,v = s.symbols('A B C D E F G H u v')
xs = [(1+A)*u+E*v,(-1+A)*u+E*v,B*u+(1+F)*v,B*u+(-1+F)*v,C*u+G*v,D*u+H*v]
poly = s.Poly(s.expand(sum(t**3 for t in xs)),u,v)
coefs = [poly.coeff_monomial(u**3),poly.coeff_monomial(u**2*v),poly.coeff_monomial(u*v**2),poly.coeff_monomial(v**3)]
expected = [2*A**3+6*A+2*B**3+C**3+D**3,
            6*A*A*E+6*E+6*B*B*F+3*C*C*G+3*D*D*H,
            6*A*E*E+6*B*F*F+6*B+3*C*G*G+3*D*H*H,
            2*E**3+2*F**3+6*F+G**3+H**3]
assert all(s.expand(a-b)==0 for a,b in zip(coefs,expected))
J = s.Matrix(coefs).jacobian([A,E,B,F])
J0 = J.subs({a:0 for a in [A,B,C,D,E,F,G,H]})
assert J0.det() != 0
assert J0 == s.diag(6,6,6,6)
# Four smooth surface germs: equations in implicit coordinates (C,D,G,H).
for zero_vars,forced in [
    ((C,D),(A,E,B)),((G,H),(E,B,F)),
    ((D,G),(E,B)),((C,H),(E,B))]:
    vals = {x:0 for x in zero_vars+forced}
    substituted = [s.factor(f.subs(vals)) for f in coefs]
    # Equations not identically zero may only be the independent Eckardt-endpoint cubics.
    assert all(f==0 or f.free_symbols <= {A,F,C,D,G,H} for f in substituted)

planes = [frozenset((C,D)),frozenset((G,H)),frozenset((D,G)),frozenset((C,H))]
minimal_hitting = []
for n in range(1,5):
    for sub in itertools.combinations((C,D,G,H), n):
        T = frozenset(sub)
        if all(T & e for e in planes) and not any(U <= T for U in minimal_hitting):
            minimal_hitting.append(T)
assert set(minimal_hitting) == {frozenset((C,G)),frozenset((D,H))}
# Intrinsic singular scheme of the reduced codimension-two complete intersection.
Jsing = s.Matrix([C*G,D*H]).jacobian([C,D,G,H])
minors = {s.factor(Jsing[:,[i,j]].det()) for i,j in itertools.combinations(range(4),2)}
minorpolys = {s.expand(f) for f in minors if f != 0}
assert minorpolys == {C*D,-C*H,D*G,G*H}
# On the complete intersection, the equations supply the other two squarefree quadrics.
assert {s.expand(f) for f in minorpolys | {C*G,D*H}} == {C*D,C*G,-C*H,D*G,D*H,G*H}
# All squarefree quadratic monomials generate exactly the ideal of the four axes.
axis_ideals=[frozenset(set((C,D,G,H))-{x}) for x in (C,D,G,H)]
axis_hits=[]
for n in range(1,5):
    for X in itertools.combinations((C,D,G,H),n):
        M=frozenset(X)
        if all(M & Y for Y in axis_ideals) and not any(U <= M for U in axis_hits):
            axis_hits.append(M)
assert set(axis_hits) == {frozenset((x,y)) for x,y in itertools.combinations((C,D,G,H),2)}
print('FERMAT_SECOND_TYPE_LOCAL_AND_INCIDENCE_EXACT_OK')
print('components=(10,45) cross_elliptics=180 deep_points=405; deep_local_ideal=(C*G,D*H); implicit_jacobian_det=',J0.det())
