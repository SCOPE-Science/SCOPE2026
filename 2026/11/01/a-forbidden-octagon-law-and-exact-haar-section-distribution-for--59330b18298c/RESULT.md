# A forbidden-octagon law and exact Haar section distribution for the regular pentagonal antiprism

## Finding

Let \(P\subset\mathbb R^3\) be a regular pentagonal antiprism centered at the origin. Choose an unoriented plane \(H=\{x:\langle u,x\rangle=0\}\) with Haar-uniform normal direction \(u\in S^2/\{\pm1\}\). Outside the measure-zero directions for which \(H\) passes through a vertex, let \(N\) be the number of sides of \(P\cap H\). Then **\(N\in\{6,10\}\) almost surely**: in particular, no generic central octagon occurs. Both types have positive probability, and their complete law is

\[
\Pr(N=10)=\frac5\pi\arccos\frac1{\sqrt5}-\frac32
\approx0.26208191174783346,
\qquad
\Pr(N=6)=\frac52-\frac5\pi\arccos\frac1{\sqrt5}
\approx0.73791808825216654.
\]

The expected side count is
\[
\mathbb E N=\frac{20}{\pi}\arccos\frac1{\sqrt5}\approx7.048327646991334.
\]

The five vertex-normal great circles in antipodal pairs have exactly \(22\) open chambers: \(10\) are hexagon chambers and \(12\) are decagon chambers. Chamber *counts* here are not asserted to equal spherical *areas*; the exact probabilities follow instead from the crossing-angle formula and the two-point support.

## Assumptions and scope

Put \(\phi=(1+\sqrt5)/2\), so \(\phi^2=\phi+1\). The regular icosahedron has vertices
\[
(0,\pm1,\pm\phi),\quad(\pm1,\pm\phi,0),\quad(\pm\phi,0,\pm1).
\]
Delete \((0,1,\phi)\) and its negative. The convex hull \(P\) of the remaining ten points is a centered regular pentagonal antiprism, with two parallel regular pentagons and ten congruent equilateral triangular side faces. Every vertex has squared norm \(\phi+2\); the \(20\) edges have squared length \(4\). Scaling does not affect the theorem. The section normal is chosen from normalized spherical surface measure. Generic means that its scalar product with every vertex is nonzero.

## Proof

**1. Exact edge and sign setup.** For the above ten vertices \(v_1,\dots,v_{10}\), the \(20\) unordered pairs of squared distance \(4\) are exactly the antiprism edges. The graph is \(4\)-regular, with two pentagonal ring cycles and ten connectors. A generic central plane intersects an edge precisely when its endpoint scalar products have opposite signs. Thus its section vertex count, and hence its polygon side count, is
\[
N(u)=\#\{\{i,j\}\text{ an edge}:\operatorname{sgn}\langle u,v_i\rangle\ne\operatorname{sgn}\langle u,v_j\rangle\}.
\]

**2. Five great circles and twenty-two chambers.** Choose one representative from each antipodal vertex pair:
\[
r_1=(0,-1,\phi),\quad r_2=(-1,-\phi,0),\quad r_3=(-1,\phi,0),\quad
r_4=(-\phi,0,-1),\quad r_5=(-\phi,0,1).
\]
Direct expansion in \(\mathbb Z[\phi]\) gives nonzero determinants for all \(\binom53=10\) triples. Consequently the great circles \(\langle u,r_i\rangle=0\) have pairwise intersections but no triple intersections. Their number of spherical chambers is exactly
\[
2+2(1+2+3+4)=22.
\]

A chamber is uniquely identified by its five signs \((\operatorname{sgn}\langle u,r_1\rangle,\ldots,\operatorname{sgn}\langle u,r_5\rangle)\): intersections of the corresponding open half-spaces with the sphere are connected. The file `verify.py` contains **22 explicitly listed integer normal vectors**, each with a distinct strictly realizable sign vector. It recomputes all dot-product signs, all edges, and the crossed-edge count in exact \(\mathbb Z[\phi]\) arithmetic. The counts are \(10\) witnesses with \(N=6\) and \(12\) with \(N=10\). Since there are only \(22\) chambers, these strict witnesses exhaust all possible generic sections; in particular there is no octagon chamber. Both outcomes occur on open sets of positive spherical area.

The checker is an independently replayable finite certificate, not a random enumeration. Signs of nonzero \(a+b\phi\) are certified by rational enclosure of \(\phi\), with rational endpoint checks against \(z^2-z-1=0\); no floating-point decision is used in chamber classification.

**3. Exact probabilities.** All edges have endpoint dot product \(\phi\), and both endpoints have squared norm \(\phi+2\). Therefore their central angle \(\theta\) obeys
\[
\cos\theta=\frac{\phi}{\phi+2}=\frac1{\sqrt5}.
\]
For Haar-uniform \(u\), the probability that \(\langle u,v_i\rangle\) and \(\langle u,v_j\rangle\) have opposite signs equals \(\theta/\pi\). This follows by restricting the rotationally invariant normal to the two-dimensional span of the endpoints: the disagreement occupies total angular measure \(2\theta\) on a circle of circumference \(2\pi\). Summing the \(20\) edge-crossing indicators yields \(\mathbb E N=20\theta/\pi\). Since \(N\) takes only the values \(6\) and \(10\), solving \(\mathbb E N=6+4\Pr(N=10)\) proves the stated exact law.

## Verification

Run `python3 verify.py` using Python 3 with only the standard library. Its exact certificates check vertex lengths, the \(20\) edges and their degrees, all ten nonzero determinants, the \(22\) distinct strict chamber witnesses, all crossed-edge counts, and the algebraic cosine identity. Floating-point calculations occur **only after** the exact classification, to display decimal approximations and check consistency of the probability formulas. The final diagnostic is `ALL_EXACT_CERTIFICATE_CHECKS_PASSED`.

## Relationship to prior work

Brandenburg, De Loera, and Meroni give general finite slicing-chamber algorithms and combinatorial optimization methods for polytopes; their discussion of central slices explains the broad arrangement setting. Their inspected full text does not provide a Haar side-count distribution for the pentagonal antiprism. The exact novelty claimed here is the **specific forbidden-octagon classification and exact two-atom probability law** for that solid, not the chamber method or the angular-crossing identity. Existing exact central-section laws for the regular icosahedron and square antiprism concern different edge graphs. Neither law alone implies the present one: deleting the two icosahedral poles changes the crossed-edge count in a direction-dependent way.

## Limitations

The result applies only to planes through the center, with Haar-uniform orientation, and to the regular pentagonal antiprism. Planes through vertices are excluded from the generic classification and have probability zero. It does not determine section areas or perimeters, or distributions for off-center sections or distorted antiprisms. The literature comparison supports provisional novelty but does not establish definitive priority; no independent mathematical audit has been performed.

## References

- M.-C. Brandenburg, J. A. De Loera and C. Meroni, *The Best Ways to Slice a Polytope*, first public arXiv version April 27, 2023, arXiv:2304.14239v1, https://arxiv.org/abs/2304.14239.
- Related published research record, *Exact Haar polygon-type law for central icosahedron sections*, public result identifier `2026/10/11/SCOPE-exact-haar-polygon-type-law-for-central-icosahedron-sections--65970a533c4f` (different solid).
