# The four-class viewing atlas of the regular icosidodecahedron

## Finding
For the regular icosidodecahedron \(P\), the orthographic viewing sphere has an exact **152-chamber** subdivision by sixteen great circles. The four spherical chamber classes, with multiplicities, interior angles, and generic silhouette polygon sizes, are as follows:

| Chambers | Spherical chamber | Interior angles | Shadow vertices |
| ---: | --- | --- | ---: |
| 12 | pentagon | five \(\pi-\theta\) | 10 |
| 20 | equilateral triangle | three \(\eta\) | 12 |
| 60 | isosceles triangle | \(\theta,\theta,\beta\) | 12 |
| 60 | isosceles triangle | \(\pi-\theta,\gamma,\gamma\) | 14 |

Here \(\theta=\arccos(1/3)\), \(\eta=\arccos(1/\sqrt5)\), \(\beta=\arccos(\sqrt5/3)\), and \(\gamma=\arctan(3-\sqrt5)\). The sixteen circles intersect in 90 distinct points of the sphere: sixty points where precisely two circles cross and thirty points where precisely four circles cross. Their chamber borders are 240 arcs, with **exactly 60** bordering ten- and twelve-shadow chambers and **exactly 180** bordering twelve- and fourteen-shadow chambers. The finer classes of adjacent chambers have counts 60 (pentagon, isosceles-twelve), 60 (equilateral-twelve, isosceles-fourteen), and 120 (isosceles-twelve, isosceles-fourteen). There is no same-size transition and no direct ten-to-fourteen transition.

The exact Haar-uniform silhouette law follows by spherical excess:
\[
\Pr(N=10)=6-\frac{15\theta}{\pi},\quad
\Pr(N=12)=\frac{30(\theta-\gamma)}{\pi}-5,\quad
\Pr(N=14)=\frac{15(2\gamma-\theta)}{\pi}.
\]
The values are approximately \(0.1226017195409\), \(0.5252352041433\), and \(0.3521630763158\), respectively. **Novelty is attributed to the complete four-class viewing atlas and its adjacency profile, not to the probabilities as standalone consequences.**

## Assumptions and scope
Let \(\varphi=(1+\sqrt5)/2\), and let \(I\) have the twelve vertices obtained by independently signing the nonzero entries of \((0,1,\varphi)\), \((1,\varphi,0)\), and \((\varphi,0,1)\). All its edges have length two. Put \(P=\operatorname{conv}\{(v+w)/2:\{v,w\}\text{ is an edge of }I\}\). The sixty edges, thirty vertices, and thirty-two facets of \(P\) are those of the rectified icosahedron, with twenty triangular faces and twelve pentagonal faces.

The viewing direction \(u\) is a unit normal to an orthogonal projection plane. A generic direction is one with nonzero inner product with every facet normal. Its silhouette is the boundary polygon of the orthogonal projection of \(P\) to \(u^\perp\). The chamber atlas records *labelled face-sign data*, not merely polygon homeomorphism. Directions on the sixteen great circles form a zero-area excluded set; nongeneric degeneracies are not classified.

## Proof
**1. Exact normals and silhouette incidence.** The twelve normals of the pentagonal facets are parallel to the twelve vertices of \(I\). The twenty triangular-facet normals are proportional to sums of triples of vertices forming an icosahedral face. Opposite facets yield the same unoriented great circle. Exhaustive exact vertex-distance checks in the quadratic integer ring \(\mathbb Z[\varphi]\), using \(\varphi^2=\varphi+1\), establish the twelve vertices, thirty edges and twenty triangular faces and show that their 32 normals produce exactly sixteen distinct great circles. Every edge of \(P\) is incident to one triangular and one pentagonal face; the sixty such incidences are explicitly reconstructed from the twenty icosahedral faces. For a generic \(u\), an edge projects to an edge of the boundary silhouette if and only if its two adjacent outward facet normals have opposite signs when dotted with \(u\). Thus its projected silhouette has exactly the number of sign-discordant incidences. Signs are constant on every open chamber of the great-circle arrangement.

**2. Exact exhaustive cell classification.** The checker `checker.py` constructs the sixteen circle normals over \(\mathbb Z[\varphi]\), forms pairwise cross products, and deduplicates oriented intersection rays using exact positive-collinearity decisions. There are exactly ninety rays, sixty on two circle planes and thirty on four. For each of the \(2^{16}\) possible strict sign words, it finds all rays satisfying the corresponding closed hemispherical constraints. A feasible cell cone is pointed, because the sixteen normal vectors span three-space; every extreme ray is the intersection of two of its defining planes. Summing all eligible nonzero rays produces an interior point precisely for each full-dimensional feasible sign cone; the checker verifies all sixteen signs of this sum exactly. The algorithm therefore exhausts **every** open chamber and excludes every infeasible sign word. It finds 152 chambers with spherical side counts five (twelve chambers) or three (140 chambers).

**3. Exact chamber angles and shadow labels.** For each chamber vertex, the two adjacent boundary great circles are identified by their shared endpoint rays, and the cosine of the interior angle is obtained from the signed dot product of their normals. All angle tests compare squared inner products and norm products in \(\mathbb Z[\varphi]\), with a separate exact sign test; no floating-point threshold decides a class. The only angle cosines are the exact algebraic values corresponding to \(\pi-\theta\), \(\eta\), \(\theta\), \(\beta\), and \(\gamma\). Pairing these angles with the sixty sign-discordance incidence counts yields precisely the four multiplicity classes in the table. Three angles determine a spherical triangle up to isometry; the fivefold rotational symmetry identifies the twelve pentagonal cells. Their angles determine their areas by spherical excess. The four chamber areas are respectively \(2\pi-5\theta\), \(3\eta-\pi\), \(2\theta+\beta-\pi\), and \(2\gamma-\theta\). The identity \(\beta+\eta+2\gamma=\pi\) yields the total area \(4\pi\).

**4. Exact adjacency and Haar law.** Each chamber side is uniquely represented by the circle index and its two ray endpoints. The checker creates this key independently for every chamber and verifies that precisely two chamber records share each key. The resulting 240 keys split into the three stated finer transition classes. Each adjacency switches exactly one facet-sign condition and hence changes the shadow edge count by two. Dividing the total spherical areas of chambers of each silhouette size by \(4\pi\) gives the three probabilities in the Finding.

## Verification
Run `python3 checker.py` in the same directory as this file. It uses only the Python standard library and integer operations in \(\mathbb Z[\varphi]\). It prints `EXACT_CERTIFICATE_OK` and asserts all of the following: 12 icosahedron vertices, 30 edges, 20 faces, 32 facet normals, 16 distinct great circles, 90 sphere arrangement vertices with multiplicities 60/30, all \(65,536\) sign cases, 152 feasible open chambers, four chamber class populations, 240 shared border arcs, and the full transition counts. The finite test is **exhaustive** because every chamber is a full-dimensional polyhedral cone and every extreme ray arises from two of the known sixteen plane constraints; no claim of proof is drawn from sampling or numerical measurements. The displayed angular identities are independently checkable from their trigonometric definitions.

## Relationship to prior work
Classical viewing-direction aspect decompositions use great circles orthogonal to the facet normals of convex polyhedra. Glisse and Lazard [1] prove a general expected-size bound for silhouettes and recall the dihedral-angle formula for the expected silhouette count. Popko [2] describes the ten- and six-circle icosahedral families inside Fuller's classical 31-circle construction; **the sixteen circles themselves are not asserted as newly discovered**. The particular prior icosahedron central-section polygon-type law and the regular-dodecahedron decagonal-section probability concern different marginal measurements; the numerical ten-shadow probability here agrees with an existing decagonal-section value. When combined with the classical expected-shadow-size formula, that known marginal can already constrain the remaining marginal probabilities. Neither these marginal statements nor the inspected primary literature provide the complete four-class **face-labelled** arrangement, its ninety singular points, and its precise 240-edge adjacency graph. Those are the primary claims.

## Limitations
The claim concerns this one regular Archimedean polyhedron and generic orthographic views, not arbitrary affine deformations, perspective views, or nonconvex surfaces. Chamber equivalence is by spherical geometry, while their labelling records the visible facets rather than a topological aspect-graph quotient. Published constructions of the 31-circle icosahedral grid could conceal an equivalent presentation of some sixteen-circle combinatorics, and unindexed historical diagrams may contain the same chamber table; this remains a historical-priority risk. Independent mathematical audit has not been performed.

## References
[1] M. Glisse and S. Lazard, *An Upper Bound on the Average Size of Silhouettes*, first public arXiv version 14 February 2007, https://arxiv.org/abs/cs/0702087 . Relevant material: Section 2 and Section 3.2, especially the dihedral-angle expectation identity.

[2] E. Popko, *Divided Spheres: Geodesics and the Orderly Subdivision of the Sphere*, 2012, Chapter 2, Section 2.5 (the 10-plus-6 icosahedral great-circle families), and Chapter 10 (31-circle sphere). A readable edition: https://www.scribd.com/document/1015526853/Divided-Spheres-E-Popko-2012 .
