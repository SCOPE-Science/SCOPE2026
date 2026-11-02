# Every generic central section of the icosidodecahedron is a dodecagon

## Finding

Let \(\varphi=(1+\sqrt5)/2\), and consider the regular icosahedron
\[
I=\operatorname{conv}\{(0,\pm1,\pm\varphi),(\pm1,\pm\varphi,0),(\pm\varphi,0,\pm1)\}.
\]
Let \(P\) be the convex hull of the midpoints of the edges of \(I\); this is the **regular icosidodecahedron**. For any nonzero \(u\in\mathbb R^3\) such that no vertex of \(P\) lies in the plane \(u^\perp\), the polygon \(P\cap u^\perp\) has **exactly twelve sides**:
\[
\boxed{f_0(P\cap u^\perp)=12.}
\]
The condition excludes finitely many great circles of normal directions. In particular, with the rotation-invariant uniform distribution on central planes, the section side-count variable \(N\) satisfies
\[
\boxed{\Pr(N=12)=1,\quad \mathbb E[N]=12,\quad\operatorname{Var}(N)=0.}
\]
Thus, although the solid has triangular and pentagonal facets and is not a zonotope, the number of sides of a generic central section is **completely rigid** under orientation changes.

## Assumptions and scope

All geometry is in Euclidean three-space. The solid is exactly the rectification of the displayed icosahedron, with no affine distortion. A **generic** central plane is one through the origin that contains none of the thirty polyhedron vertices. No probabilistic qualification is required for the pointwise statement: it holds for every such plane. The Haar law samples the unoriented normal uniformly from the quotient of the unit sphere by antipodal identification. Nongeneric planes, including special equatorial sections, may have fewer sides.

## Proof

**1. Section vertices are transverse edge crossings.** If \(Q\) is a convex three-polytope, \(u\) is generic, and \(0\) lies in the interior of \(Q\), then each vertex of \(Q\cap u^\perp\) comes from exactly one edge of \(Q\) with endpoints on opposite sides of the plane, and conversely. Hence
\[
N_Q(u)=\sum_{\{v,w\}\in E(Q)}\mathbf1_{\{(u\cdot v)(u\cdot w)<0\}}.
\]

**2. Radial-neighbor-pairing lemma.** Suppose a convex polyhedron has four edges at each nonzero vertex \(v\), and the four neighbors can be labeled \(w_1,w_2,w_3,w_4\) so that \(w_1+w_2\) and \(w_3+w_4\) are each collinear with \(v\). On the great circle \(u\cdot v=0\), the two members of each pair have opposite normal projections, provided the crossing is away from the finitely many other vertex great circles. Therefore exactly two of the four incident edges cross \(u^\perp\) on either side of this wall: when \(u\cdot v\) changes sign, the number of incident crossing edges remains two. When antipodal vertices share the same wall, the argument applies to both. Any two generic normals can be joined by a piecewise-smooth path crossing the finite collection of vertex great circles transversely one at a time, avoiding their intersection points. The total number of crossed edges does not change. It follows that \(N_Q(u)\) is constant over the entire set of generic directions.

**3. Exact geometry and radial pairing.** The regular icosahedron \(I\) has thirty edges, precisely its pairs of vertices at squared Euclidean distance \(4\). Taking their midpoints gives thirty distinct rectification vertices, all on the sphere of radius \(\varphi\). The twenty triangular faces inherited from original icosahedron faces and the twelve pentagonal faces inherited from original icosahedron vertices are supporting facets. Together they determine exactly sixty edges, all of length \(1\); the resulting graph has degree four at each vertex. These assertions can be checked using the listed coordinates and arithmetic in \(\mathbb Q(\sqrt5)\), as done in the accompanying standalone checker. At each of the thirty vertices \(v\), the four neighbors admit one pairing into two pairs with both vector sums parallel to \(v\). The checker verifies all \(30\) instances by vanishing exact cross products; no floating-point tolerance is used for this finite identity. The lemma therefore proves that \(N_P(u)\) is constant for generic \(u\).

**4. Determine the constant without enumerating orientations.** Let \(e=\{v,w\}\) be an edge. Both endpoints have length \(\varphi\) and \(\lVert v-w\rVert=1\); hence the angle \(\theta_e\in(0,\pi)\) between them satisfies
\[
\cos\theta_e=1-\frac{1}{2\varphi^2}=\frac{\varphi}{2}=\cos\frac\pi5.
\]
Thus \(\theta_e=\pi/5\). For a Haar-uniform normal \(u\), the probability that \(u\cdot v\) and \(u\cdot w\) have opposite signs is exactly \(\theta_e/\pi\); this follows by rotation invariance and the fact that the two separating great semicircles delimit spherical lunes of total angular fraction \(\theta_e/\pi\). Linearity of expectation, without assuming the individual edge-crossing indicators independent, gives
\[
\mathbb E[N_P]=\sum_{e\in E(P)}\frac{\theta_e}{\pi}=60\cdot\frac15=12.
\]
Since step 3 shows \(N_P\) is a constant on the full-measure set of generic directions, that constant is twelve. This completes the proof.

## Verification

The bundled standard-library program `verify_icosidodecahedron.py` constructs the exact field \(\mathbb Q(\sqrt5)\), reconstructs all twelve original icosahedron vertices and thirty original edges, and checks the twenty supporting triangular facets, twelve supporting pentagonal facets, thirty rectification vertices, sixty actual edges and their four-regular adjacency. It then tests all thirty radial-pairing identities with exact cross products, independently verifies the Crofton angle identity, checks four rationally specified generic directions, and performs an additional finite random-direction diagnostic. Run:

```text
python3 verify_icosidodecahedron.py
```

The universal statement follows from the written geometric argument and exact local pairing, not from the finite Monte Carlo diagnostic. The exact checker is provided so that the key nonstandard finite lemma can be replayed in the same directory as this document.

## Relationship to prior work

Brandenburg, De Loera and Meroni (2023), *The Best Ways to Slice a Polytope*, prove that the set of crossed edges is fixed within a slicing chamber and study optimal and combinatorial polytope sections. Their general chamber theorem does not assert that **the number** of edge crossings remains unchanged when moving across **different chambers** for the icosidodecahedron. That cross-chamber invariance is established here by the radial-neighbor-pairing lemma.

Reid (2016), *Rectifications of Convex Polyhedra*, describes the rectified icosahedron and its face vector \((30,60,32)\); this classical geometry is acknowledged rather than claimed new. The inspected article addresses rectification sequences and surface and volume computations, not the number of vertices of every generic central plane section.

Separate published geometric section results cover central sections of an icosahedron, and the cuboctahedron has an analogous but distinct eight-sided section rigidity. Neither statement alone implies the present twelve-sided classification for the different icosidodecahedral edge structure. A direct proof and exact reconstruction are provided to make the specific contribution independently checkable.

## Limitations

The result says nothing about the number of sides in a nongeneric central plane passing through a vertex (some special equatorial sections are decagonal); it does not classify section lengths, angles or areas, nor off-center sections, affinely distorted solids or other Archimedean solids. The identical local-balance condition need not hold in those settings. Priority with respect to older stereological and recreational-polyhedron literature remains provisional; no claim of independent audit is made.

## References

1. M.-C. Brandenburg, J. A. De Loera, C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239v1 (first publicly posted 2023-04-27), especially Theorem 1.1 and Section 5; https://arxiv.org/abs/2304.14239 .
2. S. Reid, *Rectifications of Convex Polyhedra*, arXiv:1604.00580v1 (first publicly posted 2016-04-03), especially Section 2; https://arxiv.org/abs/1604.00580 .
3. Wolfram MathWorld, *Archimedean Solid*, classical face-number reference; https://mathworld.wolfram.com/ArchimedeanSolid.html .
4. Published geometric section records: *Exact Haar polygon-type law for central icosahedron sections*; *Exact Haar hexagon law and cubic rigidity for central sections of rectangular boxes* (published-finding corpus, 2026-10).
