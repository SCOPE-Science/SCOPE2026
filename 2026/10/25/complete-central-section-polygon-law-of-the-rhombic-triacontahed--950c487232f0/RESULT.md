# Complete central-section polygon law of the rhombic triacontahedron

## Finding

Let \(\varphi=(1+\sqrt5)/2\) and let \(Z\subset\mathbb R^3\) be the golden zonohedron
\[
Z=\sum_{i=1}^{6}[-v_i,v_i],\qquad
(v_1,\ldots,v_6)=((0,1,\varphi),(0,-1,\varphi),(1,\varphi,0),(-1,\varphi,0),(\varphi,0,1),(\varphi,0,-1)).
\]
This is a rhombic triacontahedron, with thirty congruent golden rhombic facets. For a Haar-uniform normal \(U\in S^2\), write \(N(U)\) for the number of sides of the central polygon \(Z\cap U^\perp\). Then \(N(U)\in\{10,12,14\}\) almost surely and all three types occur with strictly positive probability.

Here is an exact closed form for the *complete* law. For any nonzero vectors \(X,Y,T\) in a common open hemisphere define
\[
\Omega(X,Y,T)=2\arctan\!\left(\frac{|\det(X,Y,T)|}{\lVert X\rVert\lVert Y\rVert\lVert T\rVert+(X\cdot Y)\lVert T\rVert+(Y\cdot T)\lVert X\rVert+(T\cdot X)\lVert Y\rVert}\right).
\]
This is the area of their minor geodesic spherical triangle. Put
\[
\begin{aligned}
F&=(0,1,\varphi),&G&=(1,1,1),&H&=(1,\varphi^2,\varphi),\\
P&=(1,1+3\varphi,2+3\varphi),&Q&=(1,\varphi^2,2+\varphi),&R&=(1,3-\varphi,\varphi).
\end{aligned}
\]
Then
\[
\boxed{\begin{aligned}
\mathbb P\{N=10\}&=\frac{30}{\pi}\Omega(F,P,Q)=0.1226017195408909474\ldots,\\
\mathbb P\{N=14\}&=\frac{30}{\pi}\Omega(Q,R,H)=0.3521630763158402212\ldots,\\
\mathbb P\{N=12\}&=1-\mathbb P\{N=10\}-\mathbb P\{N=14\}=0.5252352041432688313\ldots.
\end{aligned}}
\]
Independently, the exact expected side count is
\[
\boxed{\mathbb E[N]=\frac{60}{\pi}\arccos\left(\frac{\varphi^3}{\sqrt{(1+\varphi^2)(1+\varphi^4)}}\right)=12.45912271354989855\ldots.}
\]

## Assumptions and scope

The section plane passes through the symmetry center and its unoriented normal is Haar-uniform. An oriented uniform normal gives the same law. The exceptional normals perpendicular to some vertex constitute sixteen great circles and have spherical measure zero. Generic section vertices are precisely the intersections with original edges whose endpoints have opposite scalar-product signs. All probability statements are for this generic full-measure set. The scaling of the generators does not change the side-count law.

## Proof

**1. Exact zonotope combinatorics.** All six generators have squared length \(2+\varphi\) and any two have absolute inner product \(\varphi\). Every triple is independent over \(\mathbb Q(\sqrt5)\). For each generator \(v_i\), the ten signed cross-products \(\pm(v_i\times v_j)\), with \(j\ne i\), determine ten angular chambers of its normal circle. In each chamber, the choice of maximizers of the other five segments is fixed. Each resulting exposed edge has endpoints
\[
\sum_{j\ne i}\operatorname{sgn}(w\cdot v_j)v_j-v_i,
\quad
\sum_{j\ne i}\operatorname{sgn}(w\cdot v_j)v_j+v_i,
\]
where \(w\perp v_i\) lies in that chamber. These are all exposed edges, since any supporting direction exposing an edge must be orthogonal to exactly one generator in the generic rank-three arrangement. Exact golden-field enumeration yields sixty distinct edges and thirty rhombic facets, with thirty-two distinct vertices in antipodal pairs, split into a twelve-point and a twenty-point radius shell; every edge joins opposite shells and has the same normalized endpoint dot product.

**2. Fundamental spherical chamber.** The spherical triangle with corner rays \(F,G,H\) has interior angles \(\pi/5,\pi/3,\pi/2\), hence area \(\pi/30\). Its three edge reflections preserve the signed six-generator set, as can be checked exactly using \(x\mapsto x-2(n\cdot x)n/(n\cdot n)\) at each edge normal. Those reflections generate the full icosahedral Coxeter group of order 120, so its images of the triangle tile the sphere up to measure-zero edges. The central section side count is invariant under these reflections.

**3. Four exact regions.** There are precisely sixteen antipodal vertex axes in the sixty-edge reconstruction. A great circle perpendicular to one of these axes can cut the interior of the fundamental triangle only if its vertex-axis dot products with the three corner rays have both signs. Exact comparisons in \(\mathbb Z[\varphi]\) show that exactly three axes have this property; they are proportional to
\[
A=(\varphi^2,0,-\varphi),\qquad B=(1,1,-1),\qquad C=(\varphi^2,-1,0).
\]
The resulting three circles cut the closed fundamental triangle into four spherical triangles, \(FPQ\), \(PQH\), \(QRH\), and \(RGH\), whose interiors are disjoint. The asserted locations follow from the exact incidences \(B\cdot P=0\), \(B\cdot Q=C\cdot Q=0\), \(A\cdot R=0\), and the appropriate fundamental-triangle sides, as reproduced by the code. Thus no other section-type changes are possible in a fundamental chamber.

Each triangular cell has fixed signs of all thirty-two vertex scalar products. Evaluating the sign-changing-edge count at one exact interior ray per cell gives, in the same order,
\[
N=10,\quad 12,\quad14,\quad12.
\]
Because no original vertex lies on an open cell, the count is constant throughout that cell. This supplies an exhaustive classification rather than an inference from finitely sampled normals.

**4. Exact areas.** Spherical triangle excess gives
\[
\Omega(F,P,Q)+\Omega(P,Q,H)+\Omega(Q,R,H)+\Omega(R,G,H)=\pi/30.
\]
Every one of the 120 congruent fundamental triangles has the same partition and side counts. Dividing all 120 areas by the total sphere area \(4\pi\) yields the three displayed probabilities.

**5. Independent expectation.** A uniformly random plane through the origin separates two nonzero vectors making angle \(\theta\) with probability exactly \(\theta/\pi\). All sixty edges of the zonohedron have the same endpoint angle
\[
\theta=\arccos\left(\frac{\varphi^3}{\sqrt{(1+\varphi^2)(1+\varphi^4)}}\right).
\]
Summing the sixty edge-crossing indicator expectations gives the stated independent mean. Substitution of the three spherical-excess probabilities reproduces the same value, furnishing a nontrivial independent consistency identity.

## Verification

Run `python3 check_geometry.py` with Python, NumPy, and mpmath. All crucial combinatorial decisions use exact integer-pair arithmetic in the field \(\mathbb Q(\sqrt5)\), representing \(a+b\varphi\) by integer coefficients. The checker verifies all twenty generator triples, all sixty distinct edges and thirty-two vertices, the two vertex shells, the generating reflections, all sixteen vertex axes, the three and only three crossing great circles, the four cell interior edge-crossing counts, and the high-precision spherical-excess and expected-value identities. It independently samples 180,000 isotropic Gaussian normal directions and compares section-type frequencies with the proved law. The Monte Carlo calculation is supplementary; the infinite statement follows from the proved exhaustive chamber reduction and exact area calculations.

## Relationship to prior work

Koca, Koca, and Koc (arXiv:1403.2847, initially made public March 12, 2014) construct the rhombic triacontahedron via icosahedral projection of a six-dimensional cubic lattice. Their full paper supplies structural context for the same named solid but not the random central-section polygon law. Stinson, Gleich, and Constantine (arXiv:1602.06620, initial public version February 22, 2016) study zonotope vertex enumeration using Gaussian sampled *normal cones*, not the distribution of central plane section side counts. The published *Exact Haar polygon-type law for central icosahedron sections* (published-finding corpus, October 11, 2026) concerns the different icosahedron, which has decagonal or dodecagonal generic sections but no fourteen-sided ones; duality is not an equivalence of plane-section polygon counts. Its actual result and proof were read, including its great-circle chamber method. The structural great-circle technique is shared, but the sixteen-axis arrangement and three-atom law here are new objects and calculations. General cube-section expected counts cannot determine the law of a three-dimensional projected zonotope's central sections, since taking projections and sections do not commute.

## Limitations

The law concerns central planes and exact golden-ratio geometry, not translated planes or perturbed zonotopes. The only independence is that of the analytical edge-mean calculation from the chamber-area calculation; no independent mathematical audit has been performed. The full scholarly priority of this distribution is provisional: related older solid-geometry treatments are not all machine-readable. Absence of an indexed match is not a proof of uniqueness.

## References

1. M. Koca, N. O. Koca, and R. Koc, *Group Theoretical Analysis of Quasicrystallography from Projections of Higher Dimensional Lattices Bn*, arXiv:1403.2847v1, March 12, 2014, https://arxiv.org/abs/1403.2847 (full paper, especially geometry of the six-dimensional cube projection).
2. P. Stinson, D. Gleich, and P. Constantine, *A randomized algorithm for enumerating zonotope vertices*, arXiv:1602.06620v1, February 22, 2016, https://arxiv.org/abs/1602.06620 (full paper, zonotope support and normal-cone sampling).
3. *Exact Haar polygon-type law for central icosahedron sections*, published published-finding corpus research, October 11, 2026, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-haar-polygon-type-law-for-central-icosahedron-sections--65970a533c4f (full RESULT.md examined).
4. P. Bourke, *Rhombic Triacontahedron*, August 2002, https://www.paulbourke.net/geometry/Rhombic_triacontahedron/ (geometry and incidence data, no random-section probabilities).
5. Y. Lonke, *On random sections of the cube*, arXiv:math/9812123, December 21, 1998, https://arxiv.org/abs/math/9812123 (background on random-section face expectations of a different polytope).
