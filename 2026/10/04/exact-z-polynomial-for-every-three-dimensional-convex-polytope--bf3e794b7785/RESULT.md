# Exact Z-polynomial for every three-dimensional convex polytope
## Finding
Let \(\mathcal P\) be any three-dimensional convex polytope with \(v\) vertices, \(e\) edges, and \(f\) facets, and let \(P\) be its face lattice. For the Eulerian-kernel \(Z\)-polynomial of Ferroni--Riccardi,
\[
Z_P(x)=1+(v+f-4)x+(2v+2f-10)x^2+(v+f-4)x^3+x^4.
\]
Equivalently,
\[
Z_P(x)=(1+x)^2\bigl(x^2+(v+f-6)x+1\bigr)
=(1+x)^4+(v+f-8)x(1+x)^2.
\]
Thus in dimension three the entire \(Z\)-polynomial depends only on \(v+f\), its \(\gamma\)-vector is \((1,v+f-8,0)\), and it is \(\gamma\)-positive and real-rooted. The tetrahedron is the unique case with \(v+f=8\), where \(Z_P(x)=(1+x)^4\); otherwise the two non-\(-1\) roots are distinct, negative, and reciprocal.

## Assumptions and scope
The face lattice includes the minimum face \(\widehat 0\) and maximum face \(\widehat 1\), so it has rank four. The \(Z\)-polynomial is the one attached to the Eulerian kernel. No rationality, simplicity, simpliciality, or smoothness assumption is imposed on \(\mathcal P\).

The input theorem used from Ferroni--Riccardi is that for every Eulerian poset \(P\), \(Z_P(x)\) equals the toric \(h\)-polynomial of the poset \(\widehat P\) of all closed intervals of \(P\), together with a formal empty interval, ordered by reverse inclusion. Their rank formula makes \(\widehat P\) a rank-five Eulerian poset when \(P\) is the face lattice of a three-dimensional polytope.

## Proof
Write \(Q=\widehat P\). For an interval \([s,t]\) of \(P\), its rank above the minimum interval \([\widehat 0,\widehat 1]\) is
\[
\rho_Q([s,t])=\rho_P(s)+\rho_P(\widehat 1)-\rho_P(t).
\]
Hence the rank-one elements of \(Q\) are exactly \([v,\widehat 1]\) for vertices \(v\) and \([\widehat 0,F]\) for facets \(F\). Their number is
\[
a_1=v+f.
\]
The rank-two elements are \([E,\widehat 1]\), \([\widehat 0,E]\), and \([v,F]\) with \(v\subset F\). The first two families contribute \(2e\). The number of vertex--facet incidences is \(2e\), because each polygonal facet has equally many vertices and edges and every edge lies in two facets. Therefore
\[
a_2=4e.
\]

For a rank-three lower interval \([Q_{\min},q]\), if it has \(a\) atoms then its toric \(g\)-polynomial is \(1+(a-3)x\). The rank-three elements \(q\) of \(Q\) fall into four families:
\[
[F,\widehat 1],\qquad [\widehat 0,v],\qquad [E,F],\qquad [v,E].
\]
For \([F,\widehat 1]\), the lower interval has as many atoms as \(F\) has vertices; for \([\widehat 0,v]\), it has \(\deg(v)\) atoms. Each interval of the other two types has exactly three atoms and hence contributes zero to the linear coefficient of its local toric \(g\)-polynomial. Consequently the sum of these local linear coefficients is
\[
\sum_F\bigl(|V(F)|-3\bigr)+\sum_v\bigl(\deg(v)-3\bigr)
=4e-3(v+f).
\]

Use the defining toric \(h\)-recursion for the rank-five Eulerian poset \(Q\):
\[
h_Q(x)=\sum_{q<\widehat 1_Q}g_{[\widehat 0_Q,q]}(x)(x-1)^{4-\rho_Q(q)}.
\]
Only the minimum and rank-one terms can contribute to the coefficient of \(x^3\), so that coefficient is
\[
(v+f)-4.
\]
For the coefficient of \(x^2\), the minimum contributes \(6\), rank one contributes \(-3(v+f)\), rank two contributes \(4e\), and the linear terms of the rank-three local \(g\)-polynomials contribute \(4e-3(v+f)\). Thus
\[
[x^2]h_Q(x)=6+8e-6(v+f).
\]
Euler's relation \(v-e+f=2\) gives \(e=v+f-2\), hence
\[
[x^2]h_Q(x)=2(v+f)-10.
\]
Toric \(h\)-symmetry supplies the remaining coefficient, proving the displayed formula for \(h_Q\), and Ferroni--Riccardi's theorem gives \(Z_P=h_Q\).

Finally,
\[
Z_P(x)=(1+x)^4+(v+f-8)x(1+x)^2.
\]
Every three-dimensional convex polytope has \(v\ge4\) and \(f\ge4\), so \(v+f-8\ge0\), proving \(\gamma\)-positivity. The second factor has discriminant
\[
(v+f-6)^2-4=(v+f-8)(v+f-4)\ge0,
\]
and all its coefficients are positive, so both of its roots are negative; together with the double root \(-1\), this proves real-rootedness.

## Verification
The accompanying `verify.py` replays the coefficient reduction using the rank counts above, checks the Euler simplification, the \(\gamma\)-vector, and the factor discriminant on the tetrahedron, cube, octahedron, dodecahedron, and icosahedron. It returns `VERIFY_OK`. These finite examples are consistency checks only; the universal statement is proved by the rank-count argument and Euler relation above.

## Relationship to prior work
Ferroni and Riccardi prove the structural identity \(Z_P=h_{\widehat P}\) for every Eulerian poset and explicitly ask whether \(Z\)-polynomials of Gorenstein* lattices are \(\gamma\)-positive. They also emphasize that explicit \(Z\)-polynomial computation is difficult even for small-dimensional polytopes. Their article does not state the dimension-three coefficient formula, the collapse to the single parameter \(v+f\), or the real-rooted factorization proved here.

The present result uses their interval-poset representation but adds a complete rank-by-rank evaluation for every three-dimensional convex polytope. It therefore gives an affirmative answer to their \(\gamma\)-positivity question on the full three-dimensional polytopal subclass and strengthens it there to real-rootedness.

## Limitations
This result concerns face lattices of convex three-dimensional polytopes. It does not settle \(\gamma\)-positivity for arbitrary Gorenstein* lattices of rank four or higher, and it does not assert that \(v+f\) determines the face lattice. The derivation uses only the Eulerian-kernel \(Z\)-polynomial and should not be conflated with unrelated zeta or Ehrhart polynomials.

## References
1. Luis Ferroni and Roberto Riccardi, *Eulerian posets and Z-polynomials*, arXiv:2510.17679v1, first posted 2025-10-20; Forum of Mathematics, Sigma 14 (2026), e120, DOI 10.1017/fms.2026.10270.
2. The toric \(g\)- and \(h\)-polynomial recursion used above is the standard recursion recalled by Ferroni--Riccardi from Bayer--Ehrenborg and Stanley.
