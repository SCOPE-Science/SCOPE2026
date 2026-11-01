# All generic central-section side counts of the regular truncated icosahedron

## Finding
Let \(P\) be the regular truncated icosahedron centered at the origin, obtained by truncating the twelve vertices of a regular icosahedron one third of the way along every incident edge. For a nonzero direction \(u\in\mathbb R^3\), write \(H_u=\{x:u\cdot x=0\}\). Call \(u\) **generic** if \(H_u\) contains no vertex of \(P\), and let \(N(u)\) be the number of sides of the polygon \(P\cap H_u\).

Then the complete set of generic section side counts is
\[
\boxed{\{N(u):u\ne0\text{ generic}\}=\{10,12,14,16,18\}.}
\]
Every count occurs for an open, positive-solid-angle set of directions. In particular, there are no generic central sections with more than 18 sides, and none with fewer than 10 or with an odd number of sides.

The 30 antipodal vertex pairs yield 30 distinct vertex-normal great circles on the sphere of orientations. They are in general position, with 435 distinct pairwise projective intersection points, and determine exactly 872 oriented open chambers. The respective numbers of such chambers for \(N=10,12,14,16,18\) are
\[
\boxed{132,\ 420,\ 180,\ 120,\ 20.}
\]
These **chamber counts are not probabilities**: the chambers generally have different spherical areas. As a separate exact Haar expectation,
\[
\mathbb E N(U)=\frac{90}{\pi}\arccos\!\left(1-\frac2{10+9\varphi}\right)
\approx11.6407231368,\qquad
\varphi=\frac{1+\sqrt5}{2},
\]
for a uniformly oriented central plane.

## Assumptions and scope
The regular icosahedron is the convex hull of the twelve vectors
\[
(0,\pm1,\pm\varphi),\quad(\pm1,\pm\varphi,0),\quad(\pm\varphi,0,\pm1).
\]
Its edges are precisely the 30 unordered pairs of vertices at distance \(2\). For every oriented original edge \((a,b)\), define the truncated vertex \(w_{ab}=(2a+b)/3\). Its 60 vertices are all distinct and lie on a sphere. The truncated polyhedron has 90 edges: 30 short edges \([w_{ab},w_{ba}]\) on original edges, and 60 edges \([w_{ab},w_{ac}]\) whenever the original vertices \(a,b,c\) span a triangular face.

A generic central plane intersects no truncated vertex, so every intersection with a polyhedral edge is transverse and contributes one distinct polygon vertex. Thus \(N(u)\) equals the number of the 90 edges with endpoints on opposite sides of \(H_u\). The excluded directions form a finite union of great circles and have Haar measure zero. No claim is made for nongeneric planes or off-center sections.

## Proof
**1. Exact edge model.** All coordinates belong to \(\mathbb Q(\varphi)\), with \(\varphi^2=\varphi+1\). Taking all directed original icosahedral edges constructs 60 vertices, and the standard one-third truncation constructs the 90 edges described above. The supplied exact checker reconstructs the original edge graph from the equation \(\|a-b\|^2=4\), confirms all truncated vertices are distinct, verifies that every truncated edge has the same squared length, and verifies degree three at all 60 truncated vertices. The geometric identification follows directly from truncation: each old triangular face becomes a hexagon, and the five endpoints cut from the edges incident to each old vertex form a new pentagonal face.

**2. The finite chamber arrangement.** Since the polyhedron is centrally symmetric, its 60 vertices consist of 30 antipodal pairs. Choose one representative \(v_i\) from each pair. Their 30 great circles are \(C_i=\{u\in S^2:v_i\cdot u=0\}\). For generic \(u\), the signs of all vertex dot products, and therefore all edge-crossing indicators, are constant on each connected chamber of \(S^2\setminus\bigcup_i C_i\).

For each of the \(\binom{30}{2}=435\) normal pairs, the checker forms the exact cross product \(q=v_i\times v_j\). A third circle meets their intersection point precisely if \(v_k\cdot q=0\). Exact arithmetic finds 435 distinct projective intersections, each incident to exactly two circles. Thus all great circles are in general position and have
\[
2+30(30-1)=872
\]
oriented chambers. This is the standard great-circle arrangement count (adding the \(k\)-th circle divides \(2(k-1)\) existing regions, for \(k\ge2\)).

**3. Exhaustive sign realization.** At each projective intersection point represented by \(q\), choose tangents \(q\times v_i\) and \(q\times v_j\) to the incident great circles, together with their negatives. For each sum \(t\) of two distinct tangent rays that has nonzero dot product with both incident normals, take the infinitesimal direction \(q+\varepsilon t\). Its complete 30-sign vector is determined *exactly*: a nonzero dot product \(v_k\cdot q\) determines the sign, and if it is zero, \(v_k\cdot t\) determines the sign. Each of the four local sectors has such a tangent-ray sum; the antipodal sign vectors give the sectors at \(-q\). Every spherical chamber has a vertex of this arrangement, so this construction encounters every chamber. As a check independent of the classification, it produces exactly 872 distinct sign vectors, equal to the count in Step 2.

Computing the endpoint signs of all 90 edges in these 872 sign vectors gives the following **exhaustive integer certificate**:

| Section sides \(N\) | Number of oriented chambers |
| ---: | ---: |
| 10 | 132 |
| 12 | 420 |
| 14 | 180 |
| 16 | 120 |
| 18 | 20 |

The counts sum to 872. Moreover, the five integer plane normals \((-1,-1,0)\), \((-2,-2,-1)\), \((-2,-1,0)\), \((-5,-4,-4)\), and \((-1,-1,-1)\) are generic and yield respectively \(10,12,14,16,18\) intersected edges. This establishes attainability on open sets and the exact five-value spectrum.

**4. Expected side count.** All 90 truncated edges have endpoints on one sphere of radius \(\sqrt{10+9\varphi}/3\) and Euclidean length \(2/3\). Their central angular separation is
\[
\alpha=\arccos\!\left(1-\frac2{10+9\varphi}\right).
\]
For two fixed nonzero vectors of angular separation \(\alpha\), a uniformly oriented plane separates them with probability \(\alpha/\pi\), by rotation symmetry of their two-dimensional span. Summing the 90 edge-crossing indicators gives the stated expectation.

## Verification
Run `python3 verify.py` with Python 3 and only its standard library. It builds all coordinates using pairs of integers representing \(a+b\varphi\), implements exact addition, multiplication, and sign comparisons, and enumerates every pairwise great-circle intersection and every local sector. It asserts the 60-vertex/90-edge graph, 30 antipodal pairs, 435 double intersections, 872 chambers, and the five exact chamber multiplicities. It also checks explicit integer witnesses and evaluates the independent expectation formula. Successful execution prints `ALL_CHECKS_PASSED`. No floating-point test is used for the finite classification; the sole floating-point evaluation reports the decimal Haar expectation. The certificate is a finite exhaustive proof of a discrete claim, not a sample of orientations.

## Relationship to prior work
Brandenburg, De Loera, and Meroni, *The Best Ways to Slice a Polytope* (first publicly posted 2023-04-27), prove a general decomposition of hyperplane space into slicing chambers and explain that edge-crossing sets determine section combinatorics (Theorem 1.1 and Lemma 2.1). That chamber framework is established prior work and is not claimed as new. Their full text includes examples on Platonic solids, a permutahedron, and cross-polytopes, but does not report the 30-circle arrangement or five-count central-section spectrum of the truncated icosahedron.

The MathWorld *Truncated Icosahedron* entry provides standard geometry and metric facts for the solid, not the orientation-dependent section count classification. The value here is the exact, checked special-object classification, not the generic principle that an arrangement exists. Results on the central sections of the untruncated icosahedron concern a different vertex and edge arrangement and do not imply the displayed spectrum without further work.

## Limitations
This classifies generic *central* sections only. The 132/420/180/120/20 chamber multiplicities do not specify the probabilities of the five counts under Haar orientation, whose computation requires chamber solid angles. The single numerical mean uses a separately proved first-moment identity. The result does not classify polygon congruence types, areas, perimeters, affine/off-center sections, or nonregular truncations. Historical priority remains provisional; independent mathematical verification has not been performed.

## References
1. M.-C. Brandenburg, J. A. De Loera and C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239v1, first posted 2023-04-27. https://arxiv.org/abs/2304.14239
2. E. W. Weisstein, *Truncated Icosahedron*, MathWorld, Wolfram Research. https://mathworld.wolfram.com/TruncatedIcosahedron.html
