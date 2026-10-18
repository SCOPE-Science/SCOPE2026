# Uniform strictness of the Mahler–flag bound for three-dimensional zonotopes and their polars

## Finding
For an origin-symmetric three-dimensional convex polytope \(P\), write \(\mathcal F(P)\) for its number of complete flags and \(\mathcal M(P)=\operatorname{vol}_3(P)\operatorname{vol}_3(P^\circ)\) for its centered Mahler product. Define the deficit in Winter's flag inequality by
\[
\Delta(P)=\frac{2}{9}\mathcal F(P)-\mathcal M(P).
\]
For every full-dimensional three-dimensional zonotope \(Z\), and also for its polar \(Z^\circ\), the following classification and quantitative gap hold:
\[
\Delta(Z)=0\ \Longleftrightarrow\ Z\text{ is a parallelotope},
\]
\[
\Delta(Z^\circ)=0\ \Longleftrightarrow\ Z^\circ\text{ is a cross-polytope}.
\]
If \(Z\) is **not** a parallelotope, then both deficits satisfy the uniform positive lower bound
\[
\boxed{\Delta(Z)=\Delta(Z^\circ)\geq 16-\frac{4\pi^2}{3}>0.}
\]
More precisely, let \(E(Z)\) denote the edge count. Exactly one of the following alternatives occurs:

1. \(E(Z)=12\) and \(Z\) is a parallelotope, with \(\Delta(Z)=0\).
2. \(E(Z)=18\) and \(Z\) is an affine hexagonal prism, with \(\Delta(Z)\geq16-4\pi^2/3\).
3. \(E(Z)\geq24\), with the stronger edge-sensitive bound
\[
\Delta(Z)\geq\frac{8E(Z)}9-\frac{16\pi^2}{9}\geq\frac{192-16\pi^2}{9}.
\]
The stated uniform positive constant is explicit, not asserted to be optimal.

## Assumptions and scope
The zonotope \(Z\) is a finite Minkowski sum of nondegenerate line segments in \(\mathbb R^3\), with nonempty interior. Translate to its unique center and merge parallel generating segments to write
\[
Z=\sum_{i=1}^m[-g_i,g_i],\qquad m\geq3,
\]
where the nonzero generators \(g_i\) have pairwise distinct unoriented directions and span \(\mathbb R^3\). The polar \(Z^\circ=\{y:\langle x,y\rangle\leq1\text{ for all }x\in Z\}\) is taken about the origin. Affine prism means a nonsingular linear image of a Cartesian product of a centrally symmetric hexagon with a segment. No regularity, integrality, or general-position condition is imposed.

## Proof
**1. Edge families of a zonotope.** For each generator define
\[
k_i=\#\{\operatorname{span}(g_i,g_j):j\ne i\},
\]
counting distinct two-planes containing \(g_i\). The polytope has exactly
\[
E(Z)=2\sum_{i=1}^{m}k_i.\tag{1}
\]
To see this, choose a supporting functional perpendicular to \(g_i\), but not to any other generator. Its exposed face is an edge in direction \(g_i\), and the signs of the other pairings determine its position. Restricting the normal to the two-dimensional plane \(g_i^\perp\), the other generators cut out \(k_i\) distinct lines through the origin, making exactly \(2k_i\) sectors. Their exposed edges are distinct; conversely every edge of \(Z\) comes from one such sector and has a unique generator direction because parallel generators were merged. This proves (1). Since the generators span three dimensions, \(k_i\geq2\) for every \(i\).

For \(m=3\), the three generators are independent, \(k_i=2\), and \(E=12\). This is a parallelotope.

For \(m=4\), either no three generators lie in a plane, in which case every \(k_i=3\) and \(E=24\), or three lie in a plane \(L\) and the fourth lies outside \(L\). In the latter case the first three \(k_i\) are \(2\), the fourth is \(3\), and \(E=18\); the resulting body is a prism over a genuine centrally symmetric hexagon.

For \(m\geq5\), select four generators spanning \(\mathbb R^3\). If none of their triples is coplanar, these four already contribute \(12\) to \(\sum k_i\), so (1) gives \(E\geq24\). Otherwise relabel three coplanar generators as \(a,b,c\in L\) and a fourth as \(u\notin L\). Take a fifth distinct-direction generator \(v\). If \(v\in L\), then \(u\) determines at least four distinct planes with the four directions in \(L\), while each of those four planar generators has at least two planes; hence \(\sum k_i\geq4+4\cdot2=12\). If \(v\notin L\), the plane \(\operatorname{span}(u,v)\) meets \(L\) in one line. At least two of \(a,b,c\) avoid that line, and those two together with \(u,v\) have no coplanar triple. Again four generators each contribute at least three planes, giving \(E\geq24\). Further generators cannot decrease \(E\). Therefore the three alternatives above exhaust all zonotopes.

**2. Flags and the universal volume estimate.** Every three-dimensional edge lies on two facets and contains two vertices. Thus every edge belongs to exactly four complete flags, so \(\mathcal F(Z)=4E(Z)\) and
\[
\frac29\mathcal F(Z)=\frac89E(Z).\tag{2}
\]
The symmetric Blaschke–Santaló inequality, credited to the existing literature, states
\[
\mathcal M(Z)\leq\operatorname{vol}_3(B_2^3)^2=\frac{16\pi^2}{9}.\tag{3}
\]
Consequently, whenever \(E\geq24\), (2)–(3) give the stronger edge-sensitive estimate in the statement.

**3. The exceptional hexagonal prism.** In the remaining nonparallelotope case, nonsingular linear invariance of the volume product identifies \(Z\) with \(H\times[-1,1]\), for a centrally symmetric planar hexagon \(H\) containing the origin. Its polar is
\[
(H\times[-1,1])^\circ=\{(y,s):h_H(y)+|s|\leq1\},
\]
where \(h_H\) is the support function. Integrating the fibers gives
\[
\begin{aligned}
\operatorname{vol}_3((H\times[-1,1])^\circ)
&=2\int_{H^\circ}(1-h_H(y))\,dy\\
&=\frac23\operatorname{area}(H^\circ).
\end{aligned}
\]
The final identity follows from radial homogeneity of \(h_H\): the mean of this function over \(H^\circ\) is \(2/3\). Hence
\[
\mathcal M(Z)=\frac43\operatorname{area}(H)\operatorname{area}(H^\circ)
\leq\frac43\pi^2,\tag{4}
\]
by the planar symmetric Blaschke–Santaló inequality. Since \(E=18\), (2) and (4) yield \(\Delta(Z)\geq16-4\pi^2/3>0\).

**4. Equality and polar duality.** A three-dimensional parallelotope has \(12\) edges and Mahler product \(32/3\); thus its flag bound \((8/9)12=32/3\) is attained. For every other zonotope, Steps 2–3 give strictness. Since polar duality reverses every complete flag and preserves the Mahler product, \(\Delta(Z^\circ)=\Delta(Z)\); the polar of a parallelotope is a cross-polytope. The nonprism lower bound exceeds the prism lower bound because \(12-\pi^2>0\), completing the proof.

## Verification
The independent finite-example program `verify.py` enumerates distinct generator-pair planes exactly, calculates the resulting edges a second way using convex-hull facets and Euler's formula, and compares the two calculations for a parallelotope, hexagonal prism, generic four-generator zonotope, octagonal prism, and generic five-generator zonotope. It also computes the polar area of an affine-regular hexagon using exact rational vertex coordinates, checking that the corresponding prism has Mahler product \(12\). The universal edge and volume-product assertions above follow from the analytical proof, not the finite tests.

## Relationship to prior work
Winter's October 7, 2026 result establishes \(\mathcal M(P)\leq 2^3\mathcal F(P)/(3!)^2\) for all centrally symmetric three-dimensional polytopes, and explicitly leaves equality classification conjectural. The present result verifies that conjectured equality classification for the infinite subclass of three-dimensional zonotopes and, by polarity, for their duals, while supplying a positive geometry-independent deficit away from the equality class. It **does not reprove** Winter's general inequality. The Blaschke–Santaló inequality supplies the known external upper bound for the volume product; its use is attributed. Existing reverse Blaschke–Santaló stability results for zonoids control proximity to parallelotopes when the *lower* Mahler bound is nearly attained, whereas the quantity considered here measures deficit in a different, flag-dependent *upper* bound. The explicit elementary edge threshold and two-case comparison establish the stated result.

## Limitations
The constant \(16-4\pi^2/3\) is a universal positive gap but need not be sharp. The proof does not settle Winter's conjectured equality classification for arbitrary centrally symmetric polytopes or in dimensions greater than three. It is a deduction using known Winter and Blaschke–Santaló inequalities; no new volume-product inequality for general convex bodies is asserted. Previously unindexed statements about equality in the flag-dependent inequality could overlap with this result and require independent bibliographic validation. No independent audit is claimed.

## References
1. M. Winter, *A relation between Mahler volume and flag number for convex polytopes*, arXiv:2610.09990v1 (public October 7, 2026), https://arxiv.org/html/2610.09990v1. Theorem 1, Corollary 2, Conjecture 3.
2. G. Bianchi and M. Kelly, *The Blaschke-Santaló Inequality*, arXiv:1312.0244 (2013), https://arxiv.org/abs/1312.0244. Theorem in Section 1.
3. K. J. Böröczky and D. Hug, *Stability of the reverse Blaschke–Santaló inequality for zonoids and applications*, Advances in Applied Mathematics 44 (2010), 309–328, DOI:10.1016/j.aam.2009.09.002. Related but distinct lower-product stability.
4. G. M. Ziegler, *Lectures on Polytopes*, Springer, 1995. Background on zonotopes and hyperplane arrangements.
