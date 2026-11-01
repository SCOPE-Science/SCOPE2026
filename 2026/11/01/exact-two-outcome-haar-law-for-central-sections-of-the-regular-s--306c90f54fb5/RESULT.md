# Exact two-outcome Haar law for central sections of the regular square antiprism

## Finding
Let \(P\subset\mathbb R^3\) be the regular square antiprism (eight vertices, sixteen edges), centered midway between its square faces. Choose a plane through the origin with Haar-uniform unoriented normal. For a generic plane, let \(N\) be the number of sides of its intersection with \(P\). Then
\[
\Pr(N=8)=\frac8\pi\arccos\!\left(\frac{2\sqrt2-1}{7}\right)-3\approx0.3270440971384683,
\]
\[
\Pr(N=6)=4-\frac8\pi\arccos\!\left(\frac{2\sqrt2-1}{7}\right)\approx0.6729559028615317.
\]
No generic central section has any other number of sides; in particular a seven-sided central section is impossible. The normal sphere has exactly 58 maximal sign chambers: 24 six-side chambers and 34 eight-side chambers. The mean number of sides is \(16\arccos((2\sqrt2-1)/7)/\pi\).

## Assumptions and scope
Scale so the circumradius of the square bases is one. Put \(s=1/\sqrt2\), \(h=2^{-3/4}\), and take the ordered vertices
\[
\begin{aligned}
&v_0=(1,0,h),\ v_1=(0,1,h),\ v_2=(-1,0,h),\ v_3=(0,-1,h),\\
&v_4=(s,s,-h),\ v_5=(-s,s,-h),\ v_6=(-s,-s,-h),\ v_7=(s,-s,-h).
\end{aligned}
\]
The sixteen edges consist of the two square boundary cycles and the eight joining pairs \((0,4),(0,7),(1,4),(1,5),(2,5),(2,6),(3,6),(3,7)\). The choice of handedness is immaterial. Generic means the normal \(u\) satisfies \(u\cdot v_i\neq0\) for all eight vertices; the exceptional orientations have Haar measure zero. Every generic central plane intersects the antiprism interior, because the origin is interior.

## Proof
**Geometry and edge count.** Every vertex has squared norm \(1+h^2\), and every listed edge has squared length two: for a lateral edge the squared length is \(2-\sqrt2+4h^2=2\). Thus these vertices realize the regular square antiprism. For a generic normal \(u\), an edge meets \(u^\perp\) precisely when its two endpoints have opposite dot-product signs. Since the section polygon is transverse to the edges, its number of sides equals the number of cut edges.

**Exhaustive chamber classification.** The signs of the eight numbers \(u\cdot v_i\) are constant on each chamber cut out by the eight vertex-normal great circles. A positive change of vertical scale turns the vertices into
\[
(1,0,1),(0,1,1),(-1,0,1),(0,-1,1),
(s,s,-1),(-s,s,-1),(-s,-s,-1),(s,-s,-1).
\]
This does not change any possible sign pattern. The signs of the 56 ordered triple determinants are computed exactly in the quadratic field \(\mathbb Q(\sqrt2)\); none vanishes, so no three great circles meet at a point and no two coincide. At each intersection of circles indexed by \(i<j\), take the two antipodal normals \(\pm(v_i\times v_j)\). For each of the remaining six indices \(k\), the limiting dot-product sign equals the sign of \(\pm\det(v_i,v_j,v_k)\). Locally, each of the four combinations of the two undecided signs for \(i,j\) occurs in one adjacent open chamber. Enumerate all 28 index pairs, both antipodes, and these four local choices, and deduplicate the resulting eight-component sign strings. The exact certificate `verify.py` implements these finite operations without floating-point tests and obtains 58 strings. Evaluating the sixteen-edge cut count for each string gives exactly 24 strings with six cut edges and 34 with eight.

This is exhaustive, not a sample: eight great circles with no triple crossings have exactly \(8\cdot7+2=58\) regions by the spherical great-circle arrangement formula. The constructed 58 distinct locally realized sign strings therefore represent every chamber. In particular, \(N\in\{6,8\}\) almost surely. As a structural check, the graph is four-regular, hence every edge cut has even cardinality; the chamber classification rules out even counts other than six and eight.

**Haar probabilities.** If nonzero vectors \(a,b\) form angle \(\alpha\), the measure of unit normals for which \((u\cdot a)(u\cdot b)<0\) is \(\alpha/\pi\). This follows by taking a great-circle section in their span, where the two opposite-sign angular arcs have combined measure \(2\alpha\) out of \(2\pi\). For either endpoint pair of any edge,
\[
\cos\alpha=\frac{(1+h^2)-1}{1+h^2}=\frac{h^2}{1+h^2}=\frac{2\sqrt2-1}{7}.
\]
Linearity of expectation over the sixteen edges therefore gives \(\mathbb E[N]=16\alpha/\pi\). Since \(N\) only equals six or eight, \(\mathbb E[N]=6+2\Pr(N=8)\). Solving establishes both stated probabilities. Every chamber is open and of positive spherical area, so both probabilities are strictly positive.

## Verification
Run `python verify.py` from the folder containing this document. Its exact symbolic component checks all 56 nonzero triple determinants in \(\mathbb Q(\sqrt2)\), constructs every chamber sign string from local great-circle crossings, asserts exactly 58 chambers with counts \(24\) and \(34\), and checks the regularity and edge-angle algebra. A separate 250,000-normal Gaussian simulation confirms that only six and eight cuts are observed and reproduces the octagon probability to sampling precision. Numerical simulation is diagnostic; the proof uses the exhaustive symbolic chamber certificate and exact spherical sign probability.

## Relationship to prior work
Brandenburg, De Loera, and Meroni (2023), *The Best Ways to Slice a Polytope*, prove general slicing-chamber decompositions for polytopes and compute extremal sections for selected examples. Their Theorem 1.1 supplies a broad combinatorial framework but neither the 58-chamber classification for this square antiprism nor its exact Haar probabilities. Berlow, Brandenburg, Meroni, and Shankar (2021), *Intersection Bodies of Polytopes*, study intersection bodies and algorithms, a related but distinct invariant. Standard descriptions of the square antiprism give its vertices, regularity and edge angle; these geometric premises are not claimed as new. The result here concerns the exact two-outcome probability law and exclusion of all other central-section side counts. A fully exhaustive historical-priority review has not been performed.

## Limitations
Only **central**, generic, planar sections of the **regular** square antiprism are covered. Affine off-center sections can have other polygon types. The result does not determine section area, perimeter, or conditional shape distributions. The 58-chamber enumeration is a reproducible finite symbolic proof, not a claimed conceptual classification for all antiprisms. No independent mathematical audit has been performed.

## References
- M.-C. Brandenburg, J. A. De Loera, C. Meroni, *The Best Ways to Slice a Polytope*, arXiv:2304.14239, first posted 2023-04-27, especially Theorem 1.1 and §5.
- K. Berlow, M.-C. Brandenburg, C. Meroni, I. Shankar, *Intersection Bodies of Polytopes*, arXiv:2110.05996, first posted 2021-10-12.
- D. McCooey, *Square Antiprism*, https://dmccooey.com/polyhedra/SquareAntiprism.html (geometric coordinate and radius comparison).
