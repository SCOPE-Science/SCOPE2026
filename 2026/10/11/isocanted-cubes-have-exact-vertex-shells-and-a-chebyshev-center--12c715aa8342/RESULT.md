# Isocanted cubes have exact vertex shells and a Chebyshev-center phase transition
## Finding
Let
\[
d\ge2,\qquad \ell>0,\qquad 0<a<\ell,
\]
and let
\[
\mathcal I_d(\ell,a)\subset\mathbb R^d
\]
be the centered isocanted cube of de la Puente and Clavería, equivalently their symmetric cubic isocanted alcoved polytope.

Its vertices lie on exactly \(d\) centered Euclidean shells. For
\[
1\le k\le d,
\]
the \(k\)-th shell has squared radius
\[
\boxed{
R_k^2
=
\frac{k\ell^2}{4}
+
(d-k)\left(\frac{\ell}{2}-a\right)^2
}
\tag{1}
\]
and contains exactly
\[
\boxed{
2\binom dk
}
\tag{2}
\]
vertices. The shell radii are strictly increasing with \(k\).

Consequently the unique minimum enclosing sphere is centered at the origin and has radius
\[
\boxed{
R\bigl(\mathcal I_d(\ell,a)\bigr)
=
\frac{\ell\sqrt d}{2},
}
\tag{3}
\]
which is independent of the cant parameter. Its contact set consists exactly of the two pole vertices
\[
\boxed{
\pm\frac{\ell}{2}\mathbf1.
}
\tag{4}
\]

The exact Euclidean inradius is
\[
\boxed{
r_{\mathrm{in}}\bigl(\mathcal I_d(\ell,a)\bigr)
=
\min\left\{
\frac{\ell}{2},
\frac{\ell-a}{\sqrt2}
\right\}.
}
\tag{5}
\]
Set
\[
a_*=\ell\left(1-\frac1{\sqrt2}\right).
\tag{6}
\]
The full Chebyshev-center set is
\[
\boxed{
\operatorname{Cent}\bigl(\mathcal I_d(\ell,a)\bigr)
=
\begin{cases}
\{0\},&0<a\le a_*,\\[2mm]
\left\{
t\mathbf1:
|t|
\le
\frac{\ell}{2}
-
\frac{\ell-a}{\sqrt2}
\right\},
&a_*<a<\ell.
\end{cases}
}
\tag{7}
\]

Thus canting produces a genuine metric phase transition. Before the threshold, only the coordinate facets control the inball and the center is unique. At the threshold, coordinate and difference facets become simultaneously active. Beyond the threshold, all difference facets control the radius and the set of optimal centers becomes a nontrivial segment parallel to the long diagonal.

## Assumptions and scope
The realization is the centered symmetric cubic isocanted alcoved polytope, also called the isocanted cube in the later paper by the same authors.

The metric is the standard Euclidean metric of the coordinates used in the defining inequalities.

The parameters satisfy
\[
d\ge2,\qquad \ell>0,\qquad 0<a<\ell.
\]
The endpoint \(a=0\) is the cube limit and is excluded from the strict shell statement because the shells coalesce there. The endpoint \(a=\ell\) is excluded because the source realization loses full dimension.

## Proof
The source defines an alcoved polytope from a normal idempotent matrix by inequalities
\[
a_{ij}\le x_i-x_j\le-a_{ji}
\]
and
\[
a_{i,d+1}\le x_i\le-a_{d+1,i}.
\]
For the symmetric cubic isocanted matrix
\[
I^{\mathrm{SNI}}(d+1;\ell,a)
=
Q^{\mathrm{SNI}}(d+1;\ell)-E,
\]
the cube matrix has coordinate entries \(-\ell/2\) and off-diagonal entries \(-\ell\), while the constant perturbation has off-diagonal entries \(-a\). Hence
\[
\boxed{
\mathcal I_d(\ell,a)
=
\left\{
x\in\mathbb R^d:
|x_i|\le\frac{\ell}{2},
\quad
|x_i-x_j|\le\ell-a
\ \text{for all }i<j
\right\}.
}
\tag{8}
\]
The later volume paper states the same centered inequality description explicitly.

The source \(f\)-vector gives
\[
f_{d-1}=d(d+1),
\]
while (8) has exactly
\[
2d+2\binom d2=d(d+1)
\]
distinct supporting hyperplanes. Thus every coordinate and difference inequality in (8) is facet-defining.

### Vertex shells
The original source labels the vertices by nonempty proper subsets of
\[
[d+1].
\]
In the visualized normalization, if
\[
\varnothing\ne W\subseteq[d],
\]
the vertex labeled by \(W\) has coordinate \(0\) on \(W\) and coordinate \(-\ell+a\) off \(W\). Translating by
\[
\frac{\ell}{2}\mathbf1
\]
to the centered symmetric normalization gives
\[
v_W(i)
=
\begin{cases}
\ell/2,&i\in W,\\
a-\ell/2,&i\notin W.
\end{cases}
\tag{9}
\]
The vertex labeled by the complementary subset
\[
[d+1]\setminus W
\]
is
\[
-v_W.
\]
This accounts for all
\[
2^{d+1}-2
\]
vertices.

If
\[
|W|=k,
\]
then
\[
\|v_W\|^2
=
\frac{k\ell^2}{4}
+
(d-k)\left(\frac{\ell}{2}-a\right)^2,
\]
which is (1). There are
\[
\binom dk
\]
such \(W\) not containing \(d+1\), and their antipodes provide the second copy, proving (2).

Moreover,
\[
R_{k+1}^2-R_k^2
=
\frac{\ell^2}{4}
-
\left(\frac{\ell}{2}-a\right)^2
=
a(\ell-a)>0.
\tag{10}
\]
Thus the \(d\) shell radii are pairwise distinct and increase strictly.

The outer shell is \(k=d\), consisting of the two antipodal poles
\[
\pm\frac{\ell}{2}\mathbf1,
\]
whose norm is
\[
\frac{\ell\sqrt d}{2}.
\]
Every other vertex has smaller norm, so the origin-centered ball of radius (3) contains the whole polytope.

Any ball containing the two poles must have radius at least half their mutual distance,
\[
\frac12\left\|
\frac{\ell}{2}\mathbf1
-
\left(-\frac{\ell}{2}\mathbf1\right)
\right\|
=
\frac{\ell\sqrt d}{2}.
\]
Equality for an antipodal pair forces the center to be their midpoint, namely the origin. This proves (3)--(4) and uniqueness of the minimum enclosing sphere.

### Inradius and the center phase
Let a Euclidean ball of radius \(\rho\) centered at
\[
z=(z_1,\ldots,z_d)
\]
be contained in (8).

The two coordinate facets in direction \(i\) give
\[
|z_i|+\rho\le\frac{\ell}{2}.
\tag{11}
\]
The two difference facets in directions
\[
e_i-e_j
\]
and
\[
e_j-e_i
\]
have normal norm \(\sqrt2\), so they give
\[
|z_i-z_j|+\rho\sqrt2\le\ell-a.
\tag{12}
\]

Conversely, (11)--(12) are sufficient because they are exactly the clearance conditions for all halfspaces in (8).

At
\[
z=0,
\]
the clearances are
\[
\frac{\ell}{2}
\quad\text{and}\quad
\frac{\ell-a}{\sqrt2}.
\]
Hence the centered ball with radius (5) is feasible.

For any center, (11) implies
\[
\rho\le\frac{\ell}{2},
\]
and (12), applied to any pair, implies
\[
\rho\le\frac{\ell-a}{\sqrt2}.
\]
Therefore no larger ball exists, proving (5).

The two bounds are equal exactly when
\[
a=a_*=\ell\left(1-\frac1{\sqrt2}\right).
\]

If
\[
0<a\le a_*,
\]
then an optimal ball has
\[
\rho=\frac{\ell}{2}.
\]
Equation (11) forces
\[
z_i=0
\]
for every \(i\), so the center is unique.

If
\[
a>a_*,
\]
then an optimal ball has
\[
\rho=\frac{\ell-a}{\sqrt2}.
\]
Equation (12) becomes
\[
|z_i-z_j|\le0,
\]
hence
\[
z=t\mathbf1.
\]
Equation (11) is then equivalent to
\[
|t|
\le
\frac{\ell}{2}
-
\frac{\ell-a}{\sqrt2}.
\]
Every such \(t\) satisfies all clearance inequalities, proving (7).

For \(a<a_*\), the difference-facet clearance at the unique center is strictly larger than the inradius. At \(a=a_*\), both facet families are tangent. For \(a>a_*\), every optimal center has zero pairwise coordinate differences, so every difference facet is tangent. At an interior point of the center segment all coordinate facets are farther away; at the positive endpoint all upper coordinate facets are tangent, and at the negative endpoint all lower coordinate facets are tangent.

## Verification
The proof is symbolic for every admissible \(d,\ell,a\).

The source-dependent facts were checked in the primary full text: the alcoved inequality convention, the centered cube matrix, the constant-cant perturbation, the condition \(0<a<\ell\), the explicit visualized vertex formulas in the proof of the characterization theorem, the complement involution, and the total vertex count. The later same-object paper was also inspected; it independently states the centered inequalities (8) and the zonotope representation.

The accompanying `verify.py` uses exact rational arithmetic to enumerate all source-labeled vertices for
\[
2\le d\le8
\]
and several rational parameter pairs. It verifies every defining inequality, the exact shell formula and multiplicities, strict shell ordering, and tightness of every coordinate and difference facet. It also uses exact symbolic radicals to verify the Chebyshev threshold and the two center regimes. These finite checks are corroborative only.

## Relationship to prior work
The 2020 paper introduces isocanted alcoved polytopes, proves central symmetry, gives their vertices and face lattice, and shows that they are cubical zonotopes. It notes that the three-dimensional member is combinatorially a rhombic dodecahedron. It does not state Euclidean inradii, circumradii, vertex-shell radii, or Chebyshev centers.

The 2024 follow-up, under the shorter name *isocanted cube*, gives the centered inequality description directly, proves an explicit Minkowski-sum representation, computes the volume and the polar volume, and studies the Mahler product. Its full text does not state the shell spectrum, the minimum enclosing sphere, the inradius, or the Chebyshev-center transition.

A related quasi-Euclidean classification paper studies three-dimensional alcoved polyhedra under symmetries and small perturbations and explicitly treats Euclidean distances as invariants of its equivalence relation. It does not contain the all-dimensional isocanted family or a radius formula.

Targeted searches under “isocanted alcoved polytope”, “isocanted cube”, “inradius”, “circumradius”, “minimum enclosing sphere”, “Chebyshev center”, “vertex shells”, and “cant threshold” did not locate a theorem implying the complete statement above.

## Limitations
The result is realization-specific and assumes a cubic bounding box. General isocanted alcoved polytopes with unequal box edge lengths need not have the same shell structure or center phase.

The formulas do not determine the John or Löwner ellipsoids, mean width, or complete pairwise vertex-distance distribution.

The 2024 paper already supplies a particularly transparent halfspace and Minkowski-sum description, so the metric calculations are accessible once those formulas are combined with the earlier vertex labeling. A residual originality risk remains for an equivalent convex-geometric observation under the newer term “isocanted cube.”

## References
1. María Jesús de la Puente and Pedro Luis Clavería, *Isocanted alcoved polytopes*, arXiv:2009.13858, first public version 2020-09-29; Applications of Mathematics 65 (2020), 703--726, DOI 10.21136/AM.2020.0373-19.
2. María Jesús de la Puente and Pedro Luis Clavería, *The volume of an isocanted cube is a determinant*, arXiv:2406.01565, first public version 2024-06-03; Linear and Multilinear Algebra, DOI 10.1080/03081087.2024.2368240.
3. María Jesús de la Puente, *Quasi--Euclidean classification of alcoved convex polyhedra*, arXiv:2010.03818; Linear and Multilinear Algebra, DOI 10.1080/03081087.2019.1572065.
