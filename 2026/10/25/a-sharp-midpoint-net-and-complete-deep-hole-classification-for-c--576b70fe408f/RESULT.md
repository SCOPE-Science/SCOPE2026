# A sharp midpoint net and complete deep-hole classification for cross-polytopes

## Finding
For every integer \(d\ge2\), put
\[
V_d=\{\pm e_i:1\le i\le d\},\qquad
P_d=\operatorname{conv}(V_d)=\{x\in\mathbb R^d:\|x\|_1\le1\},\qquad
M_d=(V_d+V_d)/2.
\]
Then the Euclidean Hausdorff gaps satisfy
\[
d_H(P_d,V_d)=1,\qquad d_H(P_d,M_d)=\frac12.
\]
The complete locus of the farthest points of \(P_d\) from \(M_d\) is
\[
E_d=\bigl\{\pm\tfrac12 e_i:1\le i\le d\bigr\}
\ \cup\
\bigl\{\tfrac14\sum_{i\in I}\sigma_i e_i:
I\subseteq\{1,\ldots,d\},\ |I|=4,\ \sigma_i\in\{\pm1\}\bigr\}.
\]
There are exactly \(2d+16\binom d4\) farthest points (using \(\binom d4=0\) for \(d<4\)). Thus a second symmetry orbit of Euclidean deep holes first occurs at \(d=4\), although the covering radius stays independent of dimension.

## Assumptions and scope
Distances are Euclidean. A midpoint may use the same vertex twice, and all signs and pairs in \(M_d\) are included. The Hausdorff distance reduces to \(\max_{x\in P_d}\min_{m\in M_d}\|x-m\|_2\) because \(M_d\subset P_d\). No result is claimed for general asymmetric polytopes, non-Euclidean metrics, or higher Minkowski averaging orders.

## Proof
Write \(y=2x\), so \(\sum_i|y_i|\le2\). The doubled midpoint set \(2M_d=V_d+V_d\) consists of \(0\), all \(\pm2e_i\), and all \(\pm e_i\pm e_j\) for distinct indices. Signed-coordinate permutations preserve both the domain and the sites; assume \(y_1=a\ge y_2=b\ge y_3\ge\cdots\ge0\).

Let \(R=\|y\|_2^2\). Since \(y_i^2\le b y_i\) for \(i\ge2\),
\[
R\le a^2+b(2-a)=:B.
\]
The squared distances to the available sites \(0\), \(2e_1\), and \(e_1+e_2\), respectively, are
\[
R,\qquad R+4-4a,\qquad R+2-2(a+b).
\]
We prove that at least one is at most \(1\), and identify when every site has distance at least \(1\).

If \(a\le\tfrac12\), then \(R\le a\sum_i y_i\le2a\le1\). Equality requires \(a=1/2\), \(\sum_i y_i=2\), and each coordinate to be either \(0\) or \(1/2\); these are exactly four entries equal to \(1/2\).

Suppose \(1/2<a<1\) and put \(t=(1-a)^2/a\). If \(b\ge t\), then
\[
R+2-2(a+b)\le1+(a-1)^2-ab\le1.
\]
If \(b<t\), then
\[
R\le a^2+b(2-a)<a^2+t(2-a)<1.
\]
The last strict inequality is equivalent to \(a>1/2\). When \(b=t\), this same strict bound on \(R\) rules out equality. Therefore the distance is strictly less than one throughout this regime.

For \(a=1\), if \(b>0\) the pair site gives squared distance at most \(1-b<1\). If \(b=0\), the point is \(y=e_1\).

For \(1<a<2\), again write \(t=(a-1)^2/a\). When \(b>t\), the pair-site bound is strictly less than one; when \(b\le t\), the axial-site bound gives
\[
R+4-4a\le(2-a)^2+b(2-a)
\le(2-a)^2+t(2-a)<1.
\]
The last inequality follows from
\[
\frac{(a-1)^2}{a}<\frac{(a-1)(3-a)}{2-a}
\qquad(1<a<2).
\]
Finally, \(a=2\) forces \(y=2e_1\), itself a site. We have proved that all \(x\in P_d\) are within \(1/2\) of \(M_d\), and that equality can occur only at a signed axis point or a signed four-half-coordinate point in the scaled variables.

At \(y=e_i\), its distance to \(V_d+V_d\) is exactly \(1\): the origin and several two-vertex sums are at distance \(1\), and no site is closer. At \(y=\frac12\sum_{i\in I}\sigma_i e_i\) with \(|I|=4\), both the origin and a site supported on two of those coordinates have squared distance \(1\); sites of type \(\pm2e_i\) or supported outside \(I\) are farther, and no pair site is closer. Thus every listed point attains the bound. The two families do not overlap and contain respectively \(2d\) and \(16\binom d4\) points.

Finally, at \(x=0\) every vertex is exactly unit distance away. For nonzero \(x\in P_d\), choose \(j\) with \(|x_j|=a=\max_i|x_i|>0\). Since \(\|x\|_2^2\le a\|x\|_1\le a\), the vertex \(\operatorname{sgn}(x_j)e_j\) is at squared distance \(1+\|x\|_2^2-2a\le1\), while the origin is at distance exactly \(1\) from every vertex. Hence \(d_H(P_d,V_d)=1\).

## Verification
The bundled `crosspoly_midpoint_check.py` is standalone, uses only the Python standard library and exact rational arithmetic, and independently lists all doubled midpoint sites. It verifies the unit-ball covering inequality on rational grids in dimensions \(2\) through \(8\), and checks that the equality grid points match the two claimed orbits. Run `python crosspoly_midpoint_check.py`. Those finite checks corroborate—but do not replace—the proof for arbitrary dimensions and real coordinates.

## Relationship to prior work
Van Hintum studies the Hausdorff gap under repeated Minkowski averaging for general compact sets, including a construction with no improvement before dimension many averages and a general eventual-improvement theorem. These results motivate measuring the opposite, rapid-improvement behavior of the canonical centrally symmetric vertex set considered here, but do not compute its twofold gap or classify its extremal points. Earlier work on midpoints of polytope vertices emphasizes additive cardinality bounds, a different metric question. The familiar parity-lattice viewpoint explains the available doubled sites; the relevant claim additionally imposes the bounded cross-polytope domain and classifies its extremal finite-stage holes.

## Limitations
The theorem is restricted to the first midpoint average of the standard Euclidean cross-polytope. The inspected midpoint-cardinality article was accessible as an abstract, not a full manuscript; unindexed or inaccessible prior results on bounded parity-lattice coverings could overlap the conclusion. No independent validation has been performed.

## References
- Peter van Hintum, *The sharp threshold for Hausdorff convexification under Minkowski addition*, arXiv:2606.10815v1 (first posted 2026-06-09), https://arxiv.org/abs/2606.10815 .
- Mario Huicochea and Brien Navarro, *Midpoints of Vertex Pairs of Convex Polytopes*, SIAM Journal on Discrete Mathematics 39 (2025), 1806–1825, DOI:10.1137/24M1714496, https://doi.org/10.1137/24M1714496 .
