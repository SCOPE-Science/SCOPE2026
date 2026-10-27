# Sharp simultaneous Lipschitz extension to every facet centroid of a regular cross-polytope

## Finding
For every integer \(d\ge3\), let \(V_d=\{\pm e_i:1\le i\le d\}\subset\mathbb R^d\), and let \(F_d=\{d^{-1}(s_1,\ldots,s_d):s_i\in\{-1,1\}\}\) be the centroids of all facets of their Euclidean convex hull. Give \(V_d\cup F_d\) the inherited Euclidean distance. Among **all** real-linear operators extending scalar Lipschitz functions on \(V_d\) to \(V_d\cup F_d\) and preserving the original values, the exact least Lipschitz seminorm is
\[
\boxed{\Lambda_d=\sqrt{\frac d2}\,\frac{1+\sqrt2(d-1)}{1+d\sqrt{(d-1)/2}}.}
\]
The minimizer is an explicit positive, symmetry-equivariant operator which assigns **positive weight to all \(2d\) original vertices** at every facet centroid, not merely to the \(d\) vertices of that facet. The constant satisfies \(\Lambda_d>1\) and \(\Lambda_d\to\sqrt2\) as \(d\to\infty\). It is strictly less than the norm \(\sqrt{d/2}\) of naive interpolation averaging only vertices of the corresponding facet.

## Assumptions and scope
The vertices are the signed coordinate vectors \(\pm e_i\) in Euclidean \(\mathbb R^d\), not the unit sphere of the \(\ell_1\) metric; distances between distinct nonopposite vertices equal \(\sqrt2\) and between opposites equal \(2\). Every facet of the cross-polytope has exactly one vertex \(s_i e_i\) from each coordinate pair, with centroid \(f_s=d^{-1}\sum_i s_i e_i\). The distance between \(f_s\) and an incident signed vertex is \(r=\sqrt{(d-1)/d}\), and between \(f_s\) and an opposite signed vertex is \(h=\sqrt{1+3/d}\); \(\|f_s-f_t\|_2=(2/d)\sqrt{k}\) if the signs differ in exactly \(k\) coordinates.

The Banach spaces are real Lipschitz functions modulo constants equipped with the Lipschitz seminorm. Admissible real-linear extensions necessarily send constants to constants, since their induced operator seminorm is finite and the values on original vertices are fixed. Write \(\lambda\) for the infimum of their operator norms, with no positivity or equivariance assumed at the outset.

## Proof
**1. Symmetric reduction.** The full signed-coordinate-permutation group acts transitively on facet centroids and by Euclidean isometries on the complete configuration. Averaging any bounded real-linear extension over that finite group cannot increase its Lipschitz operator norm and preserves the extension property. The stabilizer of a facet centroid \(f_s\) partitions \(V_d\) into the incident set \(\{s_i e_i\}\) and the opposite set \(\{-s_i e_i\}\). Thus the symmetrized extension at any centroid has the form
\[
(Et)(f_s)=a\sum_{i=1}^d t(s_i e_i)+b\sum_{i=1}^d t(-s_i e_i),\qquad d(a+b)=1,
\]
for real \(a,b\). The normalization follows by applying the operator to a constant function. Symmetrizing is valid even for initially signed, nonsymmetric operators.

**2. Two universal sharp lower witnesses.** For the incident vertex \(v=s_1e_1\), restrict the Euclidean distance function \(t(x)=\|x-v\|_2\) to \(V_d\); it has Lipschitz constant one and \(t(v)=0\). Directly counting the \(d-1\) other incident vertices and the \(d\) opposites yields
\[
\frac{|(Et)(f_s)-t(v)|}{\|f_s-v\|_2}
=\left|\sqrt{\frac{2(d-1)}d}+\frac{2b}{r}\right|.
\]
Consequently the extension norm is at least \(A(b)=\sqrt{2(d-1)/d}+2b/r\), whether or not \(a,b\) are positive.

For opposite centroids \(f_s\) and \(f_{-s}\), their output difference is \((a-b)\sum_i(t(s_ie_i)-t(-s_ie_i))\). The normalized vertex function taking value \(\sqrt2\) on the incident signed vertices and zero on their opposites is one-Lipschitz: each nonopposite source--sink distance is \(\sqrt2\), each opposite distance is \(2\). This gives the lower bound
\[
F(b)=\sqrt{\frac d2}\,|1-2db|.
\]
These are two genuine one-Lipschitz test functions, not finite experiments. Set \(u=\sqrt{2(d-1)/d}\) and \(v=\sqrt{d/2}\). For \(d\ge3\), \(v>u\). The increasing affine function \(A(b)=u+2b/r\) and decreasing branch \(v(1-2db)\) meet at
\[
b_* =\frac{v-u}{2/r+2dv},\qquad a_*=\frac1d-b_*.
\]
Since \(0<b_*<1/(2d)\), \(a_*>b_*>0\). For every real \(b\le b_*\), the bound \(F(b)\ge v(1-2db)\ge F(b_*)\); for \(b\ge b_*\), \(A(b)\ge A(b_*)\). Therefore every possible extension has norm at least \(\Lambda_d=A(b_*)=F(b_*)\), algebraically identical to the boxed expression.

**3. A positive operator attaining the lower bound.** Choose \(a=a_*\), \(b=b_*\) in the displayed formula, and fix vertex values. Each centroid receives a convex combination of **all** vertex values. By Kantorovich--Rubinstein duality on the finite vertex metric, the Lipschitz operator norm is the maximum over pairs of target points of the transportation norm of the difference of their evaluation measures divided by their Euclidean distance.

For a centroid and an incident vertex, sending every positive coefficient to that single vertex costs exactly \(\sqrt2(d-1)/d+2b\), so the ratio is \(A(b)\). For a centroid and an opposite vertex, the same calculation gives
\[
B(b)=\frac{\sqrt2(d-1)/d+2a}{\sqrt{1+3/d}}.
\]
At \(b=0\), \(B(0)\le A(0)\) is equivalent to \(1\le(2-\sqrt2)(d-1)\), valid for all \(d\ge3\). As \(b\) increases with \(a=1/d-b\), \(B(b)\) decreases and \(A(b)\) increases, so \(B(b_*)\le A(b_*)\).

For two distinct facet centroids whose sign patterns differ on \(k\) coordinates, their signed evaluation-measure difference has precisely \(k\) positive masses and \(k\) negative masses, each of magnitude \(a-b\). If \(k=1\), transporting the one mass to its opposite vertex costs \(2(a-b)\), giving ratio \(d(a-b)\). If \(k\ge2\), each source-to-sink distance is at least \(\sqrt2\), and a derangement matches the \(k\) changed coordinate indices with no repeated coordinate, attaining precisely \(k\sqrt2(a-b)\). Dividing by \(2\sqrt{k}/d\) yields \(d\sqrt{k/2}(a-b)\), maximized at \(k=d\), where it equals \(v(1-2db_*)=\Lambda_d\). Vertex-to-vertex pairs are unchanged and contribute exactly one. Hence every target-point pair is bounded by \(\Lambda_d\), and equality occurs for an incident vertex--centroid pair and for opposite centroids. The lower bound is sharp.

**4. Strict improvement over ordinary facet averaging and the limit.** Ordinary facet averaging corresponds to \(b=0\), \(a=1/d\). Its opposite-centroid ratio is \(v\), which dominates its vertex--centroid ratios for \(d\ge3\), proving norm \(\sqrt{d/2}\). Because \(b_*>0\), its strict improvement is \(\Lambda_d=v(1-2db_*)<v\). Also \(\Lambda_d\ge u>1\). Dividing numerator and denominator of the closed formula by \(d^{3/2}\) gives \(\Lambda_d\to\sqrt2\).

## Verification
The standalone standard-library program `verify_crossfacet_stdlib.py` checks the analytic coefficients and enumerates all vertex--facet and facet--facet pairs for dimensions \(3\) through \(6\). The facet-pair transport is recomputed by explicitly minimizing over all source--sink matching permutations, independently of the derangement argument. It passed \(1,264\) vertex--facet and \(2,660\) facet--facet comparisons (including \(62,592\) assignment permutations in dimension six), with no counterexamples. An additional independent transportation linear-program calculation checked all pairs in dimensions \(3\), \(4\), and \(5\), with agreement. These are finite corroborations; the proof above covers every integer \(d\ge3\).

## Relationship to prior work
Bruè, Di Marino, and Stra (first posted 23 January 2018, arXiv:1801.07533), in their introduction, Section 3 and Theorem 4.1, construct linear Lipschitz extension operators via random projections and bound their norms on general doubling subsets; they do not give the exact norm of the specific cross-polytope-to-all-facets extension. Basso (first posted 29 April 2021, arXiv:2104.14238), in Sections 1 and 5, identifies finite linear Lipschitz extension moduli with finite projection constants and gives linear-programming methods; no exact cross-polytope facet-centroid formula or simultaneous positive optimizer is stated there.

The cross-polytope **edge-midpoint** problem has a different target point set, different face distances, and a different exact expression; the earlier cubical **facet-centroid** problem reverses which dual polytope supplies the original vertices. Neither implication follows merely by polar duality, which does not preserve the relevant finite Euclidean vertex--centroid distances or the Lipschitz extension operator domain. Related published results on cross-polytope nearest-point retractions concern nonlinear retractions in \(\ell_p\) geometry, not this exact finite interpolation invariant.

## Limitations
The result is for scalar real-linear Lipschitz extension under the specified ambient Euclidean metric. It does not determine every minimizing operator, target Banach-valued extension factors, arbitrary facet subdivisions, or other polytope metrics. An equivalent formulation in unpublished or less-indexed literature has not been excluded. The finite checks are corroboration rather than independent proof or independent mathematical audit.

## References
- E. Bruè, S. Di Marino, F. Stra, *Linear Lipschitz and C¹ extension operators through random projection*, arXiv:1801.07533 (first public 23 January 2018), https://arxiv.org/abs/1801.07533.
- G. Basso, *Absolute Lipschitz extendability and linear projection constants*, arXiv:2104.14238 (first public 29 April 2021), https://arxiv.org/abs/2104.14238.
