# Equal-area three-slice centerpoints improve to \(8/27\)
## Finding
Let \(A_0,A_1,A_2\subset\mathbb{R}^2\) be planar convex bodies with common positive area \(a\), and assume
\[
\frac12(A_0+A_2)\subseteq A_1.
\]
For
\[
S=\bigcup_{i=0}^2(\{i\}\times A_i),
\]
let \(h_S(y)\) denote halfspace depth with respect to the sum of planar areas on the three slices. Then the centroid \(y\) of the middle slice satisfies
\[
h_S(y)\ge \frac{8a}{9}=\frac{8}{27}\,\mu(S).
\]
Moreover, the hypotheses force a rigid translation structure: there are a planar convex body \(K\) and a vector \(v\) such that \(A_i=K+i v\) for \(i=0,1,2\).

## Assumptions and scope
All three sets are full-dimensional compact convex bodies in the plane and have the same positive area. The midpoint inclusion is exactly the one used in Cheng--Basu's three-slice theorem. The conclusion concerns the specific point given by the centroid of \(A_1\). The constant \(8/27\) is a certified lower bound in the balanced equal-area regime; it is not asserted to be optimal.

## Proof
Write \(|A_i|=a\). Brunn--Minkowski in the plane gives
\[
\left|\frac12(A_0+A_2)\right|^{1/2}
\ge \frac12\bigl(|A_0|^{1/2}+|A_2|^{1/2}\bigr)=\sqrt a.
\]
The midpoint set lies in \(A_1\), whose area is \(a\), so equality holds throughout. Equality in Brunn--Minkowski for positive-area convex bodies implies that \(A_0\) and \(A_2\) are homothetic. Their equal areas force the homothety ratio to be one, hence they are translates. Writing \(A_2=A_0+2v\), the midpoint set is \(A_0+v\). Since it is contained in \(A_1\) and both have area \(a\), they coincide. Thus, with \(K=A_0\),
\[
A_i=K+i v\qquad(i=0,1,2).
\]

Apply the affine shear \(T(z,x)=(z,x-zv)\). It preserves each slice area and maps halfspaces to halfspaces, while sending the three slices to \(\{0,1,2\}\times K\). Therefore it suffices to prove the depth bound in this normalized configuration. Let \(g\) be the centroid of \(K\), and set \(y=(1,g)\).

Take any closed halfspace \(H\) containing \(y\). If its boundary is parallel to the slices, then \(H\) contains the entire middle slice and at least one outer slice, so
\[
\mu(S\cap H)\ge 2a>\frac{8a}{9}.
\]
Otherwise the three planar sections of \(H\) are parallel halfplanes
\[
G_i=\{x\in\mathbb{R}^2:\ell(x)\ge b-ci\},\qquad i=0,1,2,
\]
for some nonzero linear functional \(\ell\). Because \(y\in H\), the middle halfplane \(G_1\) contains \(g\). The planar Grünbaum--Winternitz inequality therefore gives
\[
|K\cap G_1|\ge \frac49 a.
\]
The three halfplanes are nested, and one of \(G_0,G_2\) contains \(G_1\). For that outer slice,
\[
|K\cap G_i|\ge |K\cap G_1|\ge \frac49 a.
\]
Adding the middle contribution and this outer contribution yields
\[
\mu(S\cap H)\ge \frac89 a.
\]
Since \(\mu(S)=3a\), every closed halfspace containing \(y\) has mass at least \((8/27)\mu(S)\), proving the claim.

## Verification
The proof uses two classical sharp ingredients only in their standard forms: equality in the planar Brunn--Minkowski inequality for positive-area convex bodies, and the planar Grünbaum--Winternitz centroid bound \(4/9\). The affine shear is invertible with determinant one and restricts on each integer slice to a translation, so it preserves the mixed slice-area measure exactly. The halfplane nesting follows directly from the affine equation of a non-horizontal halfspace.

The arithmetic is exact:
\[
2\cdot\frac49 a=\frac89a,
\qquad
\frac{(8/9)a}{3a}=\frac{8}{27}.
\]
No numerical experiment is used as proof.

## Relationship to prior work
Cheng and Basu, arXiv:2609.32953v1, prove the sharp universal lower bound \(2/9\) under the same midpoint inclusion when only the total area is normalized. Their sharpness construction is strongly unbalanced: one outer slice has area tending to zero while the other two carry almost all the mass. Their paper does not state an improved constant under equal slice areas.

The present result isolates the opposite balanced regime. Equal areas turn the midpoint inclusion into an equality case of Brunn--Minkowski, forcing all three slices to be translates. That rigidity lets the planar centroid inequality contribute on two nested slices simultaneously, giving \(8/27\). Targeted searches using the exact constant, equal-area, balanced-slice, translation-rigidity, and Brunn--Minkowski formulations did not locate a prior statement of this refinement.

## Limitations
The bound \(8/27\) is not proved optimal. The argument depends essentially on exact equality of the three slice areas; it does not provide a stability estimate when the areas are merely close. It also does not address four or more slices or higher-dimensional planar factors. Because the motivating preprint is very recent, a bibliographically equivalent observation could appear under terminology not reached by the searches.

## References
1. H. Cheng and A. Basu, *A centerpoint theorem for three planar convex bodies*, arXiv:2609.32953v1, 26 September 2026.
2. B. Grünbaum, *Partitions of mass-distributions and of convex bodies by hyperplanes*, Pacific Journal of Mathematics 10 (1960), 1257--1261.
3. A. Winternitz, classical planar centroid area theorem; see the historical discussion in Grünbaum's work and modern accounts of Winternitz's theorem.
4. Classical Brunn--Minkowski inequality and its equality characterization for full-dimensional convex bodies.
