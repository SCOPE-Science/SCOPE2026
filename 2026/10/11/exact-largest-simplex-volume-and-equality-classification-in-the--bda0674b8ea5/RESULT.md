# Exact largest-simplex volume and equality classification in the regular 24-cell

## Finding

Let \(e_1,\ldots,e_4\) be the standard basis of \(\mathbb R^4\), and let the regular root-system 24-cell be
\[
C=\operatorname{conv}\{\sigma e_i+\tau e_j:1\le i<j\le4,\quad\sigma,\tau\in\{-1,1\}\}.
\]
For every 4-simplex \(T\subseteq C\), including simplices whose vertices are arbitrary points of \(C\),
\[
\operatorname{vol}_4(T)\le\frac12
=\frac1{16}\operatorname{vol}_4(C).
\]
Equality holds for precisely 48 simplices. Every equality simplex has all five vertices among the 24 vertices of \(C\), and all 48 form one orbit under signed permutations of the four ambient coordinates. A representative unordered vertex set is
\[
\{(-1,-1,0,0),(-1,1,0,0),(0,0,-1,-1),(0,0,-1,1),(1,0,1,0)\}.
\]
Equivalently, the ten squared edge lengths of every equality simplex are six copies of \(4\) and four copies of \(6\). No two distinct equality simplices share a tetrahedral vertex face (four vertices).

## Assumptions and scope

All volumes are Euclidean intrinsic four-dimensional volumes. A 4-simplex means the convex hull of five affinely independent points. The classification counts *unoriented geometric simplices*, not orderings of their vertices. There is no assumption that a candidate's vertices lie at vertices of the containing polytope; this is a conclusion for every maximizer.

The 24-cell is affinely fixed in the indicated root realization; the normalized volume ratio and equality-orbit statement transfer to invertible affine images, with the symmetry action transported by conjugation. No claim is made about arbitrary other four-polytopes.

## Proof

**The container volume.** Directly from the root-vertex description,
\[
C=[-1,1]^4\cap\left\{x:\sum_{i=1}^4|x_i|\le2\right\}.
\]
Indeed, each root satisfies the right-hand inequalities. Conversely, in each closed coordinate orthant, the latter polytope is represented by \(0\le y_i\le1\) and \(\sum_i y_i\le2\); its extreme points have at most two nonzero coordinates, each equal to \(1\). The origin and single-coordinate unit vectors belong to the root convex hull, whereas its two-coordinate extreme points are roots. Thus the two bodies agree.

The 24 facets are the eight hyperplanes \(x_i=\pm1\) and the 16 hyperplanes \(\varepsilon\cdot x=2\), with \(\varepsilon\in\{-1,1\}^4\). Each intersects \(C\) in six vertices forming a regular Euclidean octahedron of edge length \(\sqrt2\), hence of three-dimensional volume \(4/3\). Each supporting facet hyperplane is at distance \(1\) from the origin. Coning the facets to the origin partitions \(C\) (up to null boundaries) into pyramids of four-volume \((1/4)(4/3)(1)=1/3\). Therefore
\[
\operatorname{vol}_4(C)=24\cdot\frac13=8.
\]

**Sphere bound with a lattice parity gap.** Write the 24 vertices as \(\mathcal R\), all of squared norm \(2\). First restrict to five vertices \(v_0,\ldots,v_4\in\mathcal R\), and let \(\bar v=\tfrac15\sum_i v_i\), \(y_i=v_i-\bar v\), and \(G=\sum_i y_i y_i^{\mathsf T}\). If \(D\) denotes the determinant of the four edge vectors based at \(v_0\), the augmented-vertex-matrix Gram identity gives
\[
D^2=5\det G.
\]
One way to check this identity is to form the square matrix with top row \((1,1,1,1,1)\) and lower rows \(y_0,\ldots,y_4\); its Gram matrix is block diagonal with blocks \(5\) and \(G\), while elementary column subtraction gives determinant \(\pm D\).

Moreover,
\[
\operatorname{tr}G=\sum_i\|v_i\|^2-5\|\bar v\|^2\le10.
\]
Applying the arithmetic-geometric-mean inequality to the four nonnegative eigenvalues of \(G\) shows
\[
|D|\le\sqrt5\left(\frac{10}{4}\right)^2
=\frac{25\sqrt5}{4}<14.
\]
Every root belongs to the even-coordinate-sum lattice
\[
D_4=\{z\in\mathbb Z^4:\sum_j z_j\equiv0\pmod2\}.
\]
Hence every edge difference also lies in \(D_4\); modulo \(2\), all four edge vectors lie in the three-dimensional kernel of the nonzero linear form summing coordinates. Their integer determinant \(D\) is consequently even. Combining this integrality gap with \(|D|<14\) gives the sharp discrete upper bound \(|D|\le12\).

For the five displayed vertices, direct determinant evaluation gives \(|D|=12\), so their simplex has volume \(12/4!=1/2\). For any five points of \(C\), successive affine linearity of the signed simplex determinant in each vertex (and the triangle inequality for its absolute value) allows one to replace each point by a vertex of \(C\) without decreasing volume. Consequently, the exact upper bound \(1/2\) holds for *all* inscribed simplices, not just vertex simplices.

**Exhaustive equality classification and interior-point rigidity.** The completely specified integer enumeration in `verify.py` forms all \(\binom{24}{5}=42{,}504\) unordered sets of five roots, computes their determinant twice by independent exact integer formulas, and finds the following determinant-magnitude spectrum:
\[
\begin{array}{c|rrrrrrr}
|D|&0&2&4&6&8&10&12\\\hline
\text{number of sets}&12168&11328&13776&3936&1152&96&48.
\end{array}
\]
The same exhaustive calculation certifies that no two of the 48 top-volume sets share four vertices. It also verifies that the signed-coordinate-permutation orbit of the displayed witness has size 48 and is exactly the entire maximizing family, and verifies the squared-edge multiset asserted above.

It remains to exclude other equality cases having nonvertex points of \(C\). Suppose a maximum-volume simplex has a vertex \(p\) that is not a vertex of \(C\). Holding \(p\) fixed, push its other four vertices successively to vertices \(a_1,\ldots,a_4\in\mathcal R\), preserving the already maximal volume by affine linearity. Express \(p\) as a convex combination of at least two distinct vertices of \(C\) with positive coefficients. With \(a_1,\ldots,a_4\) held fixed, the *signed* determinant is affine in \(p\). Its absolute value is maximal at \(p\), so every root appearing with positive weight in the convex representation of \(p\) must realize the same maximal signed determinant (the weighted-average equality case). Such roots are distinct from the held four vertices because their determinants are nonzero. We would obtain at least two distinct maximizing five-root sets sharing \(a_1,\ldots,a_4\), contradicting the exact exhaustive certificate. Hence every geometric equality simplex uses five vertices of \(C\), and the 48-set classification is complete.

## Verification

Run `python3 verify.py` with the Python standard library. It enumerates exactly \(42{,}504\) five-root subsets, compares two integer determinant implementations for every subset, verifies the entire count spectrum, the absence of a shared four-vertex face among maximizers, the 48-member signed-permutation orbit, and each maximizing simplex's edge-length spectrum. Its expected terminal line is

`VERIFY_OK D4_24cell vertex_sets=42504 max_det=12 maximizers=48 B4_orbit=48 shared_four=0`

The universal determinant bound, parity argument, container-volume computation, and exclusion of nonvertex optimizers are analytic proofs independent of a numerical experiment. The finite enumeration is exhaustive for the explicitly finite set of unordered five-root subsets; no enumeration of continuously many simplices is claimed.

## Relationship to prior work

Koca, Koca and Al-Barwani (2011) give the \(D_4\) quaternionic 24-cell setting, its root-system and symmetry machinery, and constructions of the snub 24-cell. The relevant complete accessible article does not study the largest simplex contained in the root 24-cell, its normalized volume, or its 48 equality configurations.

Horváth and Lángi (2014) study maximum-volume polytopes whose vertices lie on a Euclidean sphere. They establish the universal regular-simplex maximizing principle among five arbitrary points on a four-dimensional sphere. This is a *continuous-sphere* result; its regular-simplex equality is not available among the 24 lattice roots. The bound together with the root-lattice parity gap supplies a short upper-bound argument here, but does not identify the attained discrete optimum, classify 48 root configurations, or exclude all other nonvertex optimizers.

The separately published result “The \(D_4\) 24-cell is lattice reduced and complete” concerns Voronoi duality and lattice width/diameter extremality for the same 24-cell, not volumes of contained simplices. General largest-inscribed-simplex complexity and vertex-reduction principles likewise do not provide the present numerical value or equality classification. Targeted searches under 24-cell, root-system \(D_4\), inscribed pentachoron, determinant, orbit, and volume-ratio formulations did not locate a stronger covering published statement.

## Limitations

This is an exact classification for the regular root 24-cell in four dimensions and its affine images. It is not a classification for general 24-vertex polytopes, higher-dimensional \(D_d\) root polytopes, or arbitrary bodies. Its assertion of historical originality has residual uncertainty: older Coxeter/regular-polytope tables or an unindexed equivalent root-determinant census might already encode part of the conclusion. The exact finite equality count depends on replaying the included standard-library checker; the analytic upper bound and example alone do not establish the count 48.

## References

M. Koca, N. O. Koca, and M. Al-Barwani, “Snub 24-Cell Derived from the Coxeter–Weyl Group \(W(D_4)\),” arXiv:1106.3433, version 1 made public 2011-06-17; full accessible text at https://arxiv.org/html/1106.3433v2.

Á. G. Horváth and Z. Lángi, “Maximum volume polytopes inscribed in the unit sphere,” arXiv:1402.6496, version 1 made public 2014-02-26; full accessible text at https://arxiv.org/html/1402.6496v3.

“The \(D_4\) 24-cell is lattice reduced and complete,” published comparison record with source text at https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-the-d-4-24-cell-is-lattice-reduced-and-complete--f8198b1d9a8f/RESULT.md. Only its scientific Voronoi and lattice statements are used in the comparison.

AProPo, “Largest/Smallest \(j\)-Simplex,” https://www2.mathematik.tu-darmstadt.de/~pfetsch/apropo/largest_smallest_j_simplex.html, general vertex-reduction and algorithmic-complexity context.
