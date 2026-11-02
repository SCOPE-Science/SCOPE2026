# Rigidity of maximal simple critical-point sets for planar polynomials

## Finding
Let \(d\ge3\) and \(f\in\mathbb C[x,y]\) have degree \(d\). Assume the affine critical scheme \(V(f_x,f_y)\) consists of exactly \((d-1)^2\) distinct, reduced points. Then the following conditions are equivalent.

1. Some polynomial \(g\in\mathbb C[x,y]\) of degree at most \(d\), not of the form \(cf+c_0\), has each of those points as a critical point.
2. After an invertible affine change of coordinates \((x,y)\mapsto(u,v)\), one has \(f=F(u)+G(v)\), with \(\deg F=\deg G=d\) and with both \(F'\) and \(G'\) squarefree.

In that case the critical scheme is the Cartesian product of the two derivative root sets in the new coordinates. Every degree-bounded companion is, up to a constant, a linear combination of \(F(u)\) and \(G(v)\). In particular the companion \(F(u)-G(v)\) has precisely the same reduced critical scheme.

## Assumptions and scope
The ground field is \(\mathbb C\); the characteristic-zero assumption is used to integrate partial derivatives and classify constant-coefficient second-order equations. The number \((d-1)^2\) is the maximal possible number of reduced affine intersections of the two derivatives, by Bézout. The theorem concerns **reduced, nondegenerate** critical points, not multiple critical schemes or configurations with fewer than \((d-1)^2\) points. The companion \(g\) need not itself have only isolated critical points; one can choose it with exactly the same critical scheme.

## Proof
Put \(m=d-1\), \(P=f_x\), and \(Q=f_y\). By hypothesis, the two derivatives meet transversely at exactly \(m^2\) distinct affine points. Bézout forces \(P,Q\) both to have degree \(m\), to have no common component, and to have no common point at infinity when homogenized to degree \(m\). Their homogeneous complete intersection is precisely the reduced degree-\(m^2\) critical scheme.

**Degree-\(m\) interpolation.** If \(h\) has degree at most \(m\) and vanishes at all the critical points, its degree-\(m\) homogenization belongs to the saturated complete-intersection ideal \((P^h,Q^h)\). As a homogeneous element of degree \(m\), it is a constant linear combination of these two degree-\(m\) generators. Consequently
\[
 g_x=aP+bQ,\qquad g_y=cP+eQ
\]
for a constant matrix \(A=\begin{pmatrix}a&b\\c&e\end{pmatrix}\). If \(A\) is scalar, then \(g\in\mathbb Cf+\mathbb C\); hence in the case of interest \(A\) is not scalar.

**Integrability and canonical forms.** Equality of mixed derivatives of \(g\) yields
\[
 c f_{xx}+(e-a)f_{xy}-b f_{yy}=0.
\]
This is a nonzero constant-coefficient homogeneous second-order differential operator. Over \(\mathbb C\), its binary quadratic symbol factors into linear forms. An invertible linear coordinate change reduces the equation to either \(f_{uv}=0\) (distinct factors) or \(f_{uu}=0\) (repeated factor). The polynomial solutions respectively have the forms
\[
 f=F(u)+G(v),\qquad\text{or}\qquad f=uH(v)+G(v).
\]

**Excluding the repeated characteristic.** In the repeated-factor case the critical equations are \(H(v)=0\) and \(uH'(v)+G'(v)=0\). A critical point is isolated and nondegenerate only if its coordinate \(v\) is a simple root of \(H\); for any such root there is exactly one critical point. Since \(\deg H\le d-1=m\), there can be at most \(m\) nondegenerate critical points, strictly fewer than \(m^2\) for \(d\ge3\). This case is impossible.

**Distinct characteristic and converse.** Thus \(f=F(u)+G(v)\). Its critical locus is exactly \(V(F'(u),G'(v))\). Having \(m^2\) reduced points and \(\deg F',\deg G'\le m\) forces each derivative to have exactly \(m\) distinct roots, so \(F,G\) both have degree \(d\). Conversely, for such \(F,G\), the polynomial \(g=F(u)-G(v)\) has the same critical points and does not lie in \(\mathbb Cf+\mathbb C\), because both derivatives are nonzero in independent coordinates.

**All companions.** In coordinates \(u,v\), every degree-bounded companion satisfies \((g_u,g_v)=A'(F'(u),G'(v))\) for a constant matrix. Integrability implies that the off-diagonal entries vanish, since \(F''(u)\) and \(G''(v)\) are nonzero polynomials in independent variables (and \(d\ge3\)). Thus \(g=\alpha F(u)+\beta G(v)+c_0\), as asserted. \(\square\)

## Verification
The key algebraic input is the degree-\(m\) part of the homogeneous complete-intersection ideal of two degree-\(m\) forms with no shared projective zero at infinity. Its Koszul resolution gives exactly two independent degree-\(m\) generators. The remaining argument is an explicit classification of a factorable constant-coefficient quadratic differential operator and of the resulting critical equations. For a checkable example, take \(F(u)=u^d-du\) and \(G(v)=v^d-dv\); over \(\mathbb C\), each derivative has \(d-1\) simple roots. No finite sampling is invoked in the proof.

## Relationship to prior work
Arredondo and Muciño-Raymundo explicitly ask whether Cartesian grids are the only source of nonessentially determined Morse polynomials in their study of planar critical-point interpolation. Their main concrete results classify the cubic case and exhibit grids as examples; the statement here addresses precisely the **maximal reduced affine intersection** hypothesis uniformly in all degrees. The earlier paper does not state this general rigidity implication. Work of Campillo and Olivares concerns singular schemes determining projective foliations; it is related but does not state this degree-bounded affine-potential grid classification. The theorem does not resolve arbitrary non-maximal Morse configurations.

## Limitations
Only maximal reduced affine critical sets over \(\mathbb C\) are covered. It is not asserted that every nonessentially determined Morse polynomial with fewer than \((d-1)^2\) critical points is separated. The comparison to earlier results is based on the cited accessible texts; unknown equivalent literature remains a priority risk. This is an algebraic proof, not an independent formal verification.

## References
1. J. A. Arredondo and J. Muciño-Raymundo, *Plane polynomials and Hamiltonian vector fields determined by their singular points*, arXiv:2206.05569, first submitted 2022-06-11. https://arxiv.org/abs/2206.05569
2. A. Campillo and J. Olivares, *Foliations by curves uniquely determined by minimal subschemes of its singularities*, Journal of Singularities **18** (2018), 105–113, DOI 10.5427/jsing.2018.18g. https://www.journalofsingularities.com/volume18/article7.html
