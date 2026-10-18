# Exact Haar central-section polygon law for the regular dodecahedron

## Finding

Let \(P\) be a regular Euclidean dodecahedron centered at the origin. Choose \(U\) uniformly from the unit sphere \(S^2\), and let \(N(U)\) be the number of vertices of the planar polygon \(P\cap U^\perp\). Put
\[
\alpha=\arccos(1/3),\qquad \beta=\arccos(\sqrt5/3).
\]
Then the complete law, with exact probabilities, is
\[
\begin{aligned}
\Pr\{N=6\}&=\frac5\pi\bigl(2\pi-3\alpha-3\beta\bigr)=0.6384088115593409\ldots,\\
\Pr\{N=8\}&=\frac{15}\pi\bigl(2\alpha+\beta-\pi\bigr)=0.2389894688997701\ldots,\\
\Pr\{N=10\}&=\frac3\pi\bigl(2\pi-5\alpha\bigr)=0.1226017195408904\ldots.
\end{aligned}
\]
All other values have probability zero. The normal sphere is partitioned, up to a null set, into exactly \(20\) hexagonal chambers producing six-sided sections, \(60\) triangular chambers producing eight-sided sections, and \(12\) pentagonal chambers producing ten-sided sections. Their respective areas on the *unit normal sphere* are
\[
A_6=2\pi-3(\alpha+\beta),\qquad A_8=2\alpha+\beta-\pi,\qquad A_{10}=2\pi-5\alpha.
\]
An independent expectation identity is
\[
\mathbb E N(U)=\frac{30\beta}{\pi}=6.96838581596310\ldots.
\]
This is a statement about **section side counts**, not about the numbers of sides of the spherical chambers, which are respectively \(6,3,5\).

## Assumptions and scope

The shape is a nondegenerate regular dodecahedron, with its center at the origin. The uniform normal \(U\) gives the rotation-invariant distribution of central, unoriented cutting planes, since \(U\) and \(-U\) determine the same plane. A *generic* normal is one for which the cutting plane contains none of the dodecahedron's vertices. Nongeneric normals form a finite union of great circles and have probability zero. No result is asserted about noncentral or directionally biased sections, nor about arbitrary dodecahedra.

## Proof

**Step 1: exact dodecahedral coordinates and section vertices.** Let \(\varphi=(1+\sqrt5)/2\), and let \(P\) be the convex hull of the twenty points
\[
(\pm1,\pm1,\pm1),\quad
(0,\pm\varphi^{-1},\pm\varphi),\quad
(\pm\varphi^{-1},\pm\varphi,0),\quad
(\pm\varphi,0,\pm\varphi^{-1}),
\]
with independent displayed signs. These are the vertices of a regular dodecahedron: all have Euclidean squared norm \(3\), and nearest-neighbor pairs (edge length \(2/\varphi\)) comprise exactly thirty segments with degree three at each vertex. The included exact checker reconstructs every one of these identities in the ordered integer ring \(\mathbb Z[\sqrt5]\), after doubling all coordinates.

There are ten antipodal vertex pairs; choose one representative \(w_i\) from each, \(0\le i<10\). For a generic normal \(U\), the section vertices are precisely the intersections with dodecahedral edges whose endpoints have opposite signs of the scalar product with \(U\). Therefore
\[
N(U)=\#\{\{v,v'\}\in E(P):\langle v,U\rangle\langle v',U\rangle<0\}.
\]
The signs depend only on the chamber of the arrangement of ten great circles \(\langle w_i,U\rangle=0\) in \(S^2\).

**Step 2: complete finite chamber classification.** For each of the \(\binom{10}{2}=45\) unordered pairs \(i<j\), form the two oriented intersection directions \(\pm(w_i\times w_j)\). Exact quadratic-integer arithmetic verifies that the ten circles are distinct, no three have a common point, and these give exactly ninety distinct spherical vertices. At each intersection direction all eight other scalar-product signs are strictly determined, while the two zero coordinates independently take either sign in the four adjacent open chambers. Conversely, every chamber is an intersection of hemispheres and has at least one such corner; the four local sign choices thus exhaust all chambers without using random samples.

The checker enumerates the resulting sign masks, their incident corners, and sign-changing dodecahedral edges. The complete exact classification is

| Number of normal chambers | Corners of each chamber | Sides of each central section | Cosines of chamber interior angles |
| ---: | ---: | ---: | --- |
| \(20\) | \(6\) | \(6\) | \(3\) occurrences each of \(-1/3\) and \(-\sqrt5/3\) |
| \(60\) | \(3\) | \(8\) | \(2\) occurrences of \(1/3\), \(1\) of \(\sqrt5/3\) |
| \(12\) | \(5\) | \(10\) | \(5\) occurrences of \(-1/3\) |

This is a complete finite theorem rather than partial enumeration. For an intersection of circles indexed by \(i,j\), if \(s_i,s_j\in\{-1,1\}\) are the selected interior hemisphere signs, the chamber's interior angle has cosine
\[
-\frac{s_is_j\langle w_i,w_j\rangle}{\|w_i\|\,\|w_j\|}.
\]
All representatives have norm \(\sqrt3\). The table's angle cosines follow from exact pairings in \(\mathbb Q(\sqrt5)\). No approximation is used to decide the sign patterns, corner incidences, or section types.

**Step 3: exact area and probability.** The spherical polygon area formula gives the sum of the interior angles minus \((r-2)\pi\) for a geodesic \(r\)-gon. Hence the six-corner, three-corner and five-corner chambers have areas \(A_6,A_8,A_{10}\) displayed above. They are positive and satisfy the exact identity
\[
20A_6+60A_8+12A_{10}=4\pi.
\]
The normal has uniform area measure, so dividing the corresponding total chamber areas by \(4\pi\) proves all three probabilities and exhaustiveness.

**Step 4: independent first-moment check.** Every dodecahedral edge subtends the same angle \(\beta\) at the origin, since the endpoints lie on radius \(\sqrt3\) and their dot product divided by \(3\) equals \(\sqrt5/3\). For a uniformly oriented normal, two fixed vertex vectors enclosing angle \(\beta\) have opposite signs with probability \(\beta/\pi\). Sum these indicators over the thirty edges. Thus \(\mathbb E N=30\beta/\pi\), which also follows by substituting the three probabilities. This second derivation does not rely on spherical chamber areas.

## Verification

Run `python3 verify_dodecahedron.py` using Python 3 standard library only. The program represents \(a+b\sqrt5\) exactly as an integer pair and determines its sign by integer comparisons, with no floating-point threshold. It verifies the twenty vertices and thirty degree-three edges; all ten antipodal axes; every one of the ninety double intersections and the absence of triple intersections; the entire ninety-two-chamber list; every chamber's corner count, section-edge count and angle-cosine multiset; all three exact class multiplicities; and the probability normalization. Its final line is `All exact ring and combinatorial checks passed.` The final displayed decimal probabilities are supplementary evaluations, not inputs to the finite proof.

A separate simulation of 200,000 independent random normals gave approximately \(0.639\), \(0.238\), \(0.123\) for the respective classes, consistent with the exact formulas. That simulation is not part of the proof.

## Relationship to prior work

Kabluchko and Seidel, *Convex cones spanned by regular polytopes* (2020), establish expected face counts of Haar-random central sections for the simplex, cube, and cross-polytope families using conic intrinsic volumes; they neither treat the dodecahedron nor its complete section-type law. Montejano, *Convex bodies all whose sections (projections) are equal* (2021), studies rigidity of families of central sections, not their random combinatorial distribution. De Loera, Lopez-Campos and Torres, *On the Number of Vertices in Hyperplane Cross-Sections of Convex Polytopes* (2024), give general enumeration methods and attainable count questions, but not rotation-invariant probabilities for central dodecahedron sections.

A separately published exact law for **central icosahedron sections** gives only ten- and twelve-sided sections, with a different normal arrangement (six great circles rather than ten). Polarity exchanges sections of one body with projections of its polar and does **not** turn that icosahedron section law into the present dodecahedron section law.

The older MathPages article *N Points On Sphere all in One Hemisphere* already describes the **same ten-circle normal arrangement** and its \(60\) triangular, \(20\) hexagonal, and \(12\) pentagonal spherical chambers. Those chamber counts are prior art, not claimed new. The article does not establish which chamber family gives which **planar dodecahedron section side count**, nor the exact closed distribution displayed here. It lists decimal chamber-area fractions that disagree with the exact angle computations here, a discrepancy that should not be silently interpreted as evidence of novelty. The new claim is the fully verified mapping between chamber classes and section types, together with its correct exact angular probability law.

## Limitations

The conclusion is almost sure and does not classify nongeneric vertex-containing cuts. It addresses the regular dodecahedron only, rather than arbitrary three-dimensional convex bodies or arbitrary offsets. The ten-circle chamber *counts* were already known, and the angle calculations are classical spherical geometry; those components are not independent novel theorems. Despite targeted searches, an equivalent earlier dodecahedron section-type law could exist in stereological or polyhedral-geometric literature. The numerical discrepancy with the older spherical-area table requires separate source-side reconciliation; the conclusion here rests instead on reproducible exact geometry. Independent mathematical validation has not yet been performed.

## References

1. Z. Kabluchko and H. Seidel, *Convex cones spanned by regular polytopes*, arXiv:2006.09492 (first public 2020-06-16), https://arxiv.org/html/2006.09492v2.
2. L. Montejano, *Convex bodies all whose sections (projections) are equal*, arXiv:2108.08917 (first public 2021-08-19), https://arxiv.org/html/2108.08917v2.
3. J. A. De Loera, G. Lopez-Campos and A. J. Torres, *On the Number of Vertices in Hyperplane Cross-Sections of Convex Polytopes*, arXiv:2412.12419 (first public 2024-12-17), https://arxiv.org/html/2412.12419v3.
4. *N Points On Sphere all in One Hemisphere*, MathPages, https://www.mathpages.com/home/kmath327/kmath327.htm (date of original publication not established).
5. *Exact Haar polygon-type law for central icosahedron sections*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-haar-polygon-type-law-for-central-icosahedron-sections--65970a533c4f (public comparison work).
