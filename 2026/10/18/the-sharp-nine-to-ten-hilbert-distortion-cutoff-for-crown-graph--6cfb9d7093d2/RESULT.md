# The sharp nine-to-ten Hilbert distortion cutoff for crown-graph transportation spaces

## Finding
Let \(\mathrm{Cr}_n\), \(n\ge3\), be the bipartite graph with vertices \(A_i,B_i\), \(1\le i\le n\), and unit edges \(A_iB_j\) exactly when \(i\ne j\). Equip its vertex set with shortest-path distance, and let \(X_n\) be the real \((2n-1)\)-dimensional Lipschitz-free (transportation-cost) space. The exact sharp maximal-distortion classification is
\[
 d_{\mathrm{BM}}(X_n,\ell_2^{2n-1})=\sqrt{2n-1}\quad\Longleftrightarrow\quad 3\le n\le9.
\]
For every \(n\ge10\) the distance is strictly below \(\sqrt{2n-1}\). Moreover, writing \(s_n=2\lfloor n^2/4\rfloor/n\), its squared value for every \(n\ge3\) is the following exact, two-variable variational expression:
\[
 \inf_{b,c>0}\left(\frac2n+\frac1b+\frac{n-2}{nc}\right)
 \max\left\{\frac n2,\frac n2+s_n(b+c-1),\frac{(n-4)^2}{2n}+\frac{8(n-1)}n c\right\}.
\]
In particular the loss of dimension-maximal Euclidean distortion occurs already when a perfect matching is deleted from the complete bipartite graph, and the first failure is at \(n=10\).

## Assumptions and scope
All scalars and Banach spaces are real. The Banach–Mazur distance is the infimum over all invertible linear changes of Euclidean coordinates, not merely graph-canonical quadratic forms. The graph is connected for every integer \(n\ge3\); the \(n=3\) case is the six-cycle. Distance uses unit graph edges and graph geodesics. No statement about maximality for non-bipartite graphs or other scalar fields is made.

## Proof
Write the dual unit ball as the potential polytope
\[
 K_n=\{f\in\mathbb R^{2n}/\langle\mathbf1\rangle: |f(A_i)-f(B_j)|\le1\text{ for all }i\ne j\}.
\]
The dual Banach–Mazur distance equals the primal distance. An ellipsoid may be described by a positive definite quadratic form \(Q\) on the zero-sum representatives. Its squared radial distortion is
\[
 \Big(\max_{i\ne j}\langle d_{ij},Q^{-1}d_{ij}\rangle\Big)
 \Big(\max_{f\in K_n}\langle f,Qf\rangle\Big),
 \qquad d_{ij}=e_{A_i}-e_{B_j}.
\]
Averaging \(Q\) over simultaneous index permutations and the interchange \(A_i\leftrightarrow B_i\) cannot increase either factor: the second factor is convex linear in \(Q\) under maximization, and the first is convex in \(Q\) by operator convexity of inversion. Consequently an optimal form may be assumed invariant. The zero-sum representation splits orthogonally into the one-dimensional constant-between-parts space \(P_0\) and the centered, paired-symmetric and paired-antisymmetric spaces \(P_+,P_-\), each of dimension \(n-1\). Thus \(Q=\alpha P_0+\beta P_++\gamma P_-\), where all eigenvalues are positive. Scaling to \(\alpha=1\), write \(b=\beta\), \(c=\gamma\). Every edge difference has squared projections \(2/n,1,(n-2)/n\), so the first factor is \(2/n+1/b+(n-2)/(nc)\).

We classify all vertices of \(K_n\). A vertex has a connected spanning graph of tight constraints: otherwise a component may be shifted infinitesimally, contradicting extremality; conversely a tight spanning tree fixes all potentials modulo constants. Because the tight graph is bipartite, all its vertices carry integer heights with parity determined by their part. Hence every cross-part height difference is an odd integer, and the Lipschitz constraints force every original edge to be tight. Each pair of \(A\)-vertices shares a \(B\)-neighbor for \(n\ge3\); their heights therefore differ by zero or two. This gives (up to shift and sign) ordinary two-level potentials with \(k\) of the \(A\)-coordinates at \(+1\) and \(n-k\) at \(-1\), while every \(B\)-coordinate is zero, together with their part-swapped analogues. There is one additional orbit: when one \(A\) height is exceptional, its matched \(B\)-height may differ by two from the other \(B\)-heights. One representative has \(A_i=0\), all other \(A\)'s \(-2\), \(B_i=-3\) and other \(B\)'s \(-1\). These are all possibilities.

For the ordinary \(k\)-level orbit, the squared lengths of the three orthogonal projections are
\[
 \left(\frac{(2k-n)^2}{2n},\frac{2k(n-k)}n,\frac{2k(n-k)}n\right).
\]
For the exceptional orbit they are
\[
 \left(\frac{(n-4)^2}{2n},0,\frac{8(n-1)}n\right).
\]
The ordinary expression is affine in \(2k(n-k)/n\), so its maximum occurs either at \(k=0\) or at \(k=\lfloor n/2\rfloor\). This proves the stated two-variable formula, with no unverified symmetry assumption.

Set \(b_0=n/[2(n-1)]\) and \(c_0=(n-2)/[2(n-1)]\). All three displayed vertex values equal \(n/2\), and the product equals \(2n-1\). For \(s=s_n\), define
\[
 u_n=\frac{(n-1)^2}{(2n-1)s},\qquad
 v_n=\frac{n(n-1)}{4(n-2)(2n-1)},\qquad
 w_n=1-u_n-v_n.
\]
For \(3\le n\le9\), direct rational reduction gives \(w_n\ge0\). Consequently the convex mixture with weights \(w_n,u_n,v_n\) of the three vertex quadratic values is bounded above by their maximum and has positive coefficients in \(1,b,c\). Cauchy–Schwarz implies that the product of this mixture and \(2/n+1/b+(n-2)/(nc)\) is minimized when its three weighted coefficient ratios match the inverse-square coefficients. Precisely these conditions hold at \((b_0,c_0)\): writing \(R_0=2(2n-1)/n\),
\[
 R_0u_ns=\frac{n}{2b_0^2},\qquad
 R_0\left(u_ns+v_n\frac{8(n-1)}n\right)=\frac n2\frac{n-2}{nc_0^2}.
\]
The lower bound equals \(2n-1\), proving equality for all nine-or-fewer orders.

For \(n\ge10\), \(w_n<0\). Indeed for even \(n\),
\[
 w_n=-\frac{n^3-13n^2+32n-16}{4n(n-2)(2n-1)},
\]
and for odd \(n\),
\[
 w_n=-\frac{n^3-12n^2+27n-8}{4(n-2)(n+1)(2n-1)}.
\]
The two numerator polynomials are positive respectively from even \(n=10\) and odd \(n=11\) onward, by positive derivatives there. At \((b_0,c_0)\), each of the three smooth candidate products is active. If their maximum had a local minimum there, the origin would belong to the convex hull of their gradients (a necessary condition for a minimum of finitely many smooth functions). Solving the two gradient equations together with weights summing to one gives the *unique* weights \((w_n,u_n,v_n)\), with negative first coordinate. Thus a common strict descent direction exists, and a nearby positive \((b,c)\) has product strictly smaller than \(2n-1\). The general upper bound \(\sqrt{2n-1}\) is therefore strict precisely from order ten onward.

## Verification
The standalone Python 3 checker `crown_distortion_check.py` verifies the contact identities and sign cutoff in exact rational arithmetic for \(3\le n\le500\), and supplies a rational distortion improvement for \(n=10\). A separate exhaustive enumeration of vertex potentials for \(3\le n\le7\) corroborated the two types used above. Those finite computations are checks, not proofs of the all-order classification.

## Relationship to prior work
The graph-to-transportation-space quotient and Lipschitz duality are standard, and are set out in Dilworth–Kutzarova–Ostrovskii (2023, arXiv:2305.12582, sections 1.1–1.3). The sharp universal Euclidean bound and Ader contact characterization appear in Grundbacher–Kobos (2024, arXiv:2407.08829, sections 1–2). Neither inspected full-text source gives the crown-graph cutoff. The known complete-bipartite calculation covers the undeleted graph, while the published cycle calculation covers the crown boundary \(n=3\), not the split at \(n=10\).

## Limitations
The formula gives an exact two-variable variational characterization but does not solve its algebraic minimization in closed form for each \(n\ge10\). Originality is conditional on the inspected and searchable literature; an unindexed equivalent ellipsoid computation cannot be excluded. No independent audit has been conducted.

## References
1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582, first posted 2023-05-21.
2. F. Grundbacher, T. Kobos, *On certain extremal Banach–Mazur distances in small dimensions*, arXiv:2407.08829, first posted 2024-07-11.
