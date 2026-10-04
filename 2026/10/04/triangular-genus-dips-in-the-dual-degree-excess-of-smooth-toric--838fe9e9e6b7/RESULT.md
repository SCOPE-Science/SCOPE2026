# Triangular-genus dips in the dual-degree excess of smooth toric surfaces
## Finding
Let \(P\subset\mathbb R^2\) be a smooth lattice polygon, and let \(X_P\) be the smooth projective toric surface embedded by the complete linear series associated with \(P\). Assume that the projective dual \(X_P^\vee\) is a hypersurface. Write
\[
g=g(P)
\]
for the sectional genus and \(v(P)\) for the number of vertices. Then
\[
\deg X_P^\vee-\deg X_P=4g+v(P)-4.
\]
Therefore, if
\[
m(g)=\min\{\deg X_P^\vee-\deg X_P: X_P\text{ smooth toric, nondefective, sectional genus }g\},
\]
then
\[
m(g)=
\begin{cases}
4g-1,&g=\binom{d-1}{2}\text{ for some integer }d\ge2,\\
4g,&\text{otherwise}.
\end{cases}
\]
When \(g=\binom{d-1}{2}\), the minimizer is unique up to integral affine equivalence: it is the smooth triangle \(d\Delta\), so \(X_P\) is the \(d\)-uple Veronese surface. For a nontriangular genus, the minimum \(4g\) is attained by the smooth rectangle
\[
[0,2]\times[0,g+1].
\]
Thus the lower envelope has arithmetic dips of exactly one at the triangular genera
\[
0,1,3,6,10,15,\ldots.
\]
For instance, the quadratic Veronese has excess \(-1\), the cubic Veronese has excess \(3\), genus \(2\) has minimum excess \(8\), and the quartic Veronese has excess \(11\).

## Assumptions and scope
The ground field is \(\mathbb C\). The polygon is smooth in the Delzant sense, so the associated projective toric surface is nonsingular. The embedding is the complete toric embedding determined by all lattice points of \(P\). The dual-degree excess is considered only when \(X_P^\vee\) is a hypersurface. This excludes the linearly embedded projective plane arising from the unimodular simplex \(\Delta\), whose dual has codimension greater than one.

The sectional genus means the genus of a general hyperplane section. For a smooth toric surface polarized by \(P\), it equals the number of interior lattice points of \(P\).

## Proof
Let
\[
A=\operatorname{Vol}_{\mathbb Z}(P),\qquad
B=|\partial P\cap\mathbb Z^2|,\qquad
V=v(P),\qquad
I=|\operatorname{int}(P)\cap\mathbb Z^2|.
\]
Here \(A\) is normalized area, so \(A=2\operatorname{Area}(P)\). The degree of the toric surface is
\[
\deg X_P=A.
\]
For a smooth lattice polygon, the general discriminant-degree formula of Gelfand--Kapranov--Zelevinsky, in the smooth form recorded by Matsui--Takeuchi and Dickenstein--Nill--Vergne, specializes to
\[
c(P)=3A-2B+V.
\]
When the dual is a hypersurface, \(c(P)=\deg X_P^\vee\); in the dual-defective case the same top Chern number vanishes.

Pick's theorem gives
\[
A=2I+B-2.
\]
The toric adjunction formula gives
\[
g=1+\frac{L^2+L\cdot K_{X_P}}2
  =1+\frac{A-B}{2}=I.
\]
Hence, in the nondefective case,
\[
\deg X_P^\vee-\deg X_P
=(3A-2B+V)-A
=2A-2B+V
=4I+V-4
=4g+V-4.
\]
For \(g\ge1\), the quantity \(c(P)=A+4g+V-4\) is positive, so such a smooth toric surface is automatically nondefective. At \(g=0\), the quadratic Veronese considered below also has positive \(c(P)\).

Every polygon has at least three vertices, so
\[
\deg X_P^\vee-\deg X_P\ge4g-1.
\]
It remains to determine exactly which genera admit a smooth lattice triangle. Translate one vertex to the origin. Because the two primitive edge directions there form a lattice basis, an integral linear change of coordinates puts the other vertices at
\[
(a,0),\qquad(0,b)
\]
with positive integers \(a,b\). Put \(q=\gcd(a,b)\). At \((a,0)\), the primitive outgoing directions are
\[
(-1,0),\qquad(-a/q,b/q).
\]
Smoothness forces their determinant to have absolute value one, hence \(b/q=1\). The same argument at \((0,b)\) gives \(a/q=1\). Thus \(a=b=d\), and every smooth lattice triangle is integrally affinely equivalent to
\[
d\Delta=\operatorname{conv}\{(0,0),(d,0),(0,d)\}.
\]
Its number of interior lattice points is
\[
I=\frac{(d-1)(d-2)}2=\binom{d-1}{2}.
\]
Therefore a genus supports a three-vertex smooth polygon if and only if it is triangular in this sense. For \(d\ge2\), \(d\Delta\) is nondefective and gives
\[
\deg X_{d\Delta}^\vee-\deg X_{d\Delta}=4g-1.
\]
The preceding triangle classification also proves uniqueness of this minimizer up to integral affine equivalence.

If \(g\) is not triangular, no smooth polygon of genus \(g\) can have three vertices, hence \(V\ge4\) and the excess is at least \(4g\). This bound is attained by
\[
P_g=[0,2]\times[0,g+1],
\]
which is smooth, has four vertices, and has
\[
|\operatorname{int}(P_g)\cap\mathbb Z^2|=(2-1)((g+1)-1)=g.
\]
For every nontriangular genus this gives the required nondefective surface and proves the second line of the formula for \(m(g)\).

## Verification
The bundled exact-integer checker performs three finite regression tests. It verifies the triangle formulas and excess identity for \(2\le d\le200\), checks directly for \(1\le a,b\le200\) that a right lattice triangle \(\operatorname{conv}\{(0,0),(a,0),(0,b)\}\) is smooth exactly when \(a=b\), and verifies the rectangle realization and predicted lower envelope for \(0\le g\le1000\).

These computations are not used as an infinite proof. The classification of smooth triangles and the four-vertex lower bound are proved symbolically above.

## Relationship to prior work
Matsui and Takeuchi give general formulas for dimensions and degrees of \(A\)-discriminants and explicitly note that, for smooth toric varieties, their formula coincides with the classical Gelfand--Kapranov--Zelevinsky formula. Dickenstein, Nill, and Vergne record for a smooth lattice polytope the alternating face-volume expression
\[
c(P)=\sum_{p=0}^n(-1)^{n-p}(p+1)\sum_{F\in\mathcal F_p(P)}\operatorname{Vol}_{\mathbb Z}(F),
\]
whose surface specialization is \(3A-2B+V\), and explain that it is the top Chern class of the first jet bundle and equals the dual degree in the hypersurface case.

The new point here is the fixed-sectional-genus extremal classification. Exact-formula and semantic searches for smooth toric surfaces, dual-degree excess, fixed sectional genus, triangular genera, and Veronese minimizers did not locate a source stating either
\[
\deg X_P^\vee-\deg X_P=4g+v(P)-4
\]
as an extremal organizing identity or the resulting lower envelope with one-unit dips exactly at triangular genera. The closest inspected sources supply the discriminant-degree machinery, not this minimization theorem.

## Limitations
The theorem is restricted to smooth projective toric surfaces with their complete toric embeddings. It does not address singular toric surfaces, incomplete linear systems, or higher-dimensional toric varieties. At genus zero the linearly embedded projective plane is dual defective and is excluded by definition of \(m(g)\); the quadratic Veronese is the first nondefective triangular case.

The literature search cannot exclude an unindexed or differently phrased classical observation deriving the same fixed-genus envelope from the standard toric discriminant formula and Pick's theorem. The theorem is elementary once those ingredients are assembled; its content is the sharp all-genus classification and the characterization of the arithmetic equality cases.

## References
Yutaka Matsui and Kiyoshi Takeuchi, *A geometric degree formula for A-discriminants and Euler obstructions of toric varieties*, arXiv:0807.3163, first submitted 20 July 2008; later published in Advances in Mathematics 226 (2011), 2040--2064. The preprint lists Mathematics Subject Classification 14M25, 14N05, 32S60, 33C70, 35A27.

Alicia Dickenstein, Benjamin Nill, and Michèle Vergne, *A relation between number of integral points, volumes of faces and degree of the discriminant of smooth lattice polytopes*, Comptes Rendus Mathématique 350 (2012), 229--233, DOI: 10.1016/j.crma.2012.02.001; arXiv:1111.2880.
