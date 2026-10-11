# Three curvature-order directions are sharp for spherical rigidity

## Finding

Fix
\[
m\in\{1,2\}.
\]
Let \(M\subset\mathbb R^3\) be the \(C^2\) boundary of a convex body \(K\), and let \(\sigma_m\) denote the \(m\)-th mean curvature of \(M\). Consider the three unit directions
\[
e_1=(1,0,0),\qquad
e_2=\left(\frac35,\frac45,0\right),\qquad
e_3=\frac1{\sqrt2}(0,1,1).
\]
Assume that for each \(j\in\{1,2,3\}\),
\[
\sigma_m(p)\le \sigma_m(q)
\]
whenever
\[
p-q=\lambda e_j,\qquad \lambda\ge0,
\]
and the open segment joining \(p\) and \(q\) lies in \(\operatorname{int}K\). Then
\[
\boxed{M\text{ is a round sphere}.}
\]

The number of directions is optimal. For every pair of prescribed unit directions \(u,v\in S^2\), there is a nonround smooth strictly convex spheroid for which the same directional condition holds in both directions, in fact with equality. Hence the smallest cardinality of a finite prescribed direction set that can force a sphere through this curvature-order test is
\[
\boxed{3}.
\]

## Assumptions and scope

Ghomi's directional symmetry theorem is used with the same chord ordering as in the source: if \(p-q\) is a nonnegative multiple of a chosen direction and the open chord lies in the interior, the upper endpoint curvature does not exceed the lower endpoint curvature.

The result is three-dimensional. It applies separately to either \(m=1\), the first mean curvature, or \(m=2\), the Gauss curvature, with the normalization of \(\sigma_m\) inherited from the source. Since the proof uses only equality of curvature under Euclidean reflections after the first symmetry step, the normalization does not affect the argument.

No strict convexity is assumed for the rigidity implication. Strict convexity is used only to provide smooth nonround counterexamples showing that two prescribed directions can never suffice.

## Proof

Apply Ghomi's theorem in each of the three directions. For every \(j\), the assumed curvature ordering implies that \(K\) is invariant under reflection in some plane \(H_j\) orthogonal to \(e_j\).

Every Euclidean symmetry of a compact convex body fixes its centroid. Thus all three planes \(H_j\) contain the centroid of \(K\). Translate the centroid to the origin. The three symmetries are then the linear reflections
\[
R_jx=x-2\langle x,e_j\rangle e_j.
\]

Let \(\theta\in(0,\pi/2)\) be the angle between \(e_1\) and \(e_2\). Then
\[
\cos\theta=\frac35.
\]
The number \(\theta/\pi\) is irrational. Indeed, if it were rational, \(\zeta=e^{i\theta}\) would be a root of unity, so
\[
\zeta+\zeta^{-1}=2\cos\theta=\frac65
\]
would be a rational algebraic integer. Every rational algebraic integer is an integer, which \(6/5\) is not.

The product of the first two plane reflections is a rotation around the \(z\)-axis. Directly,
\[
R_2R_1=
\begin{pmatrix}
-7/25&-24/25&0\\
24/25&-7/25&0\\
0&0&1
\end{pmatrix},
\]
so its rotation angle is \(2\theta\). Because \(\theta/\pi\) is irrational, the powers of \(R_2R_1\) are dense in the full circle group of rotations about the \(z\)-axis. The symmetry group of a compact convex body is closed, hence \(K\) is invariant under every rotation about the \(z\)-axis.

The third reflection satisfies
\[
R_3(0,0,1)=(0,-1,0).
\]
Conjugating the full circle of \(z\)-axis rotations by \(R_3\) therefore gives the full circle of rotations about the \(y\)-axis. Rotations about the \(z\)- and \(y\)-axes generate \(SO(3)\), for example by the standard \(z\)-\(y\)-\(z\) Euler decomposition. Thus \(K\) is invariant under all rotations about the origin. A compact convex body with full rotational invariance is a Euclidean ball, and \(M\) is a round sphere.

It remains to prove sharpness. Let \(u,v\in S^2\) be arbitrary. Choose a unit vector \(a\) orthogonal to both; such an \(a\) exists because \(\operatorname{span}\{u,v\}\) has dimension at most two. For any \(\rho>0\) with \(\rho\ne1\), set
\[
K_{a,\rho}
=
\left\{x\in\mathbb R^3:
\frac{\langle x,a\rangle^2}{\rho^2}
+
\left|x-\langle x,a\rangle a\right|^2
\le1
\right\}.
\]
This is a smooth strictly convex nonround spheroid of revolution about the axis \(\mathbb Ra\).

Every plane through the origin containing \(a\) is a reflection plane of \(K_{a,\rho}\). Since \(a\perp u\) and \(a\perp v\), both planes \(u^\perp\) and \(v^\perp\) contain the axis. Reflection in \(u^\perp\) exchanges the two endpoints of every chord parallel to \(u\), and reflection in \(v^\perp\) does the same for every chord parallel to \(v\). Euclidean reflection preserves principal curvatures, hence the corresponding endpoint values of \(\sigma_m\) are equal. Therefore the directional inequality holds in both prescribed directions although the spheroid is not a sphere.

So two directions never suffice, while the explicit three directions above do. The sharp minimum is three.

## Verification

The bundled checker reconstructs the three reflection matrices exactly. It verifies that \(R_2R_1\) fixes the \(z\)-axis and has planar cosine and sine
\[
\cos(2\theta)=-\frac7{25},\qquad
\sin(2\theta)=\frac{24}{25},
\]
consistent with \(\cos\theta=3/5\). It also verifies that \(R_3\) sends the \(z\)-axis to the negative \(y\)-axis.

The density step is analytic rather than computational: an irrational rotation has dense powers in the circle group. The irrationality proof is exact through the algebraic-integer argument above. The generation of \(SO(3)\) uses the standard Euler-angle decomposition and is not inferred from numerical samples.

For the lower bound on the number of directions, the proof gives a symbolic family of spheroids valid for every prescribed pair \(u,v\); no finite search over direction pairs is used.

## Relationship to prior work

Ghomi proves that a single directional ordering of any elementary mean curvature \(\sigma_m\) on a closed convex hypersurface forces one reflection hyperplane orthogonal to that direction. The source does not combine finitely many prescribed directional tests into a spherical rigidity criterion, and it does not determine the smallest number of such tests in dimension three.

Alfonseca-Cubero, Cordier, Morales-Amaya, and Verdusco Hernández study how collections of axes or hyperplanes of symmetry force bodies of revolution or spheres. Their 2026 article emphasizes infinite sequences of symmetry subspaces and gives sphere conclusions under corresponding spanning hypotheses. That symmetry theory is consistent with the dense-reflection mechanism used here, but the inspected statements do not give a three-direction curvature-order criterion or the sharp two-versus-three threshold.

The present result converts three one-direction curvature comparisons into a full rotational rigidity theorem and supplies a universal two-direction obstruction by nonround spheroids. Thus it identifies the exact finite test count for this directional curvature mechanism in \(\mathbb R^3\).

## Limitations

The theorem gives one explicit sufficient triple; it does not classify all triples of directions that force spherical rigidity. More generally, triples for which the generated reflection group is contained in a proper closed subgroup of \(O(3)\) may fail to force a sphere.

The sharpness statement concerns prescribed directional Ghomi tests. It does not say that two arbitrary pieces of other curvature data can never characterize a sphere.

No higher-dimensional minimum is claimed. In dimensions above three, the closed subgroup generated by a finite collection of hyperplane reflections has a richer structure and requires a separate analysis.

## References

1. Mohammad Ghomi, *Mean Curvatures and Symmetry of Convex Hypersurfaces*, arXiv:2608.28410v1, first submitted 28 August 2026.
2. Maria Alfonseca-Cubero, Michelle Cordier, Efrén Morales-Amaya, and Diana Verdusco Hernández, *Characterizations of generalized convex bodies of revolution*, Canadian Mathematical Bulletin, published online 15 July 2026, DOI:10.4153/S0008439526102215.
