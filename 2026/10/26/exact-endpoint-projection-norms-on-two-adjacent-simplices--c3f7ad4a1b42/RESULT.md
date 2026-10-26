# Exact endpoint projection norms on two adjacent simplices

## Finding
Let \(d\ge2\) be an integer. Let \(S_+\) and \(S_-\) be nondegenerate \(d\)-simplices in \(\mathbb R^d\) having exactly one common \((d-1)\)-dimensional facet and disjoint interiors. On \(\Omega=S_+\cup S_-\), let \(P\) denote the \(L^2\)-orthogonal projection, for normalized Lebesgue volume, onto continuous functions that are affine on each simplex, without imposed boundary conditions. Define the smaller volume fraction
\[
r=\frac{\min\{|S_+|,|S_-|\}}{|S_+|+|S_-|}\in(0,1/2].
\]
Then the exact sharp endpoint operator norm is
\[
\boxed{\|P\|_{L^\infty\to L^\infty}=N_d(r)}
\]
where
\[
N_d(r)=-1+(d+2)\left[(1+r)\left(1-\frac{2r}{(d+2)(1+r)}\right)^{d+1}+(1-r)\left(\frac{d}{d+2}\right)^{d+1}\right].
\]
The function \(N_d\) is strictly decreasing on \((0,1)\). Consequently, among all such two-simplex meshes, the norm is minimized exactly when their volumes are equal, with sharp minimum
\[
N_d(1/2)=-1+(d+2)\left[\frac32\left(1-\frac{2}{3(d+2)}\right)^{d+1}+\frac12\left(\frac d{d+2}\right)^{d+1}\right],
\]
and its sharp, nonattained universal supremum is
\[
\boxed{\sup\|P\|=d+1+(d+2)\left(\frac d{d+2}\right)^{d+1}.}
\]
The norm depends only on the volume ratio, not on the individual shapes or aspect ratios. For the planar two-triangle mesh, the balanced value is \(49/18\), and the unrestricted sharp supremum is \(7/2\). The maximizing evaluation nodes are precisely the tip or tips opposite the shared facet that lie in a simplex of minimum volume; for equal volumes, both tips maximize.

## Assumptions and scope
Volumes \(|S_\pm|\) are positive; common-facet vertices are distinct; tips lie in opposite open half-spaces determined by the facet. The two elements form a conforming simplicial complex with \(d+2\) distinct vertices. Normalization divides Lebesgue volume by \(|S_+|+|S_-|\). The projection acts on real or complex \(L^\infty(\Omega)\), and the identical operator norm holds on continuous functions with the supremum norm. Every assertion is uniform over all permitted geometric shapes and volume ratios at each fixed \(d\).

## Proof
Label the \(d\) vertices of the common facet by \(v_1,\ldots,v_d\), and the opposite tips by \(u_+\) and \(u_-\). Write \(q=|S_+|/(|S_+|+|S_-|)\), and let \(\phi_j\) be the usual globally continuous nodal affine hat functions. On any \(d\)-simplex, a barycentric coordinate \(U\) of a uniformly selected point has density \(d(1-t)^{d-1}\) on \(0\le t\le1\), and two coordinates satisfy
\[
\mathbb E\lambda_i=\frac1{d+1},\qquad
\mathbb E(\lambda_i\lambda_j)=\frac{1+\mathbf1_{i=j}}{(d+1)(d+2)}.
\]
These identities determine the global Gram matrix and its inverse. A direct inversion-free way to exhibit the rows of the inverse is to construct the nodal reproducing functions \(K_v\in\operatorname{ran}(P)\), satisfying \(\int_\Omega K_v\phi_w\,d\mu=\mathbf1_{v=w}\). For a shared-facet node \(v_i\), on either simplex let
\[
K_{v_i}(y)=(d+1)\big((d+2)\lambda_{v_i}(y)-1\big).
\]
For the positive tip, the restrictions are
\[
K_{u_+}(y)=\begin{cases}
-(d+1)+\dfrac{(d+1)(d+2)(1+q)}{2q}\lambda_{u_+}(y),&y\in S_+,\\[4pt]
-(d+1)+\dfrac{(d+1)(d+2)}2\lambda_{u_-}(y),&y\in S_-.
\end{cases}
\]
The negative-tip formula is obtained by exchanging \(+\) and \(-\) and replacing \(q\) by \(1-q\). Each function takes the same value \(-(d+1)\) along the shared facet, except that \(K_{v_i}\) varies there consistently; hence these are continuous finite-element functions. Integrating against every global hat using the two barycentric moments gives the Kronecker identities above. For example, integration of \(K_{u_+}\) against \(\phi_{u_+}\), \(\phi_{u_-}\), and any \(\phi_{v_i}\) gives respectively \(1,0,0\). Thus the displayed functions really are all nodal kernel rows; no unverified matrix-inversion lemma is needed.

The full projection kernel is \(K(x,y)=\sum_v\phi_v(x)K_v(y)\). Consequently
\[
\|P\|_{\infty\to\infty}=\sup_{x\in\Omega}\int_\Omega|K(x,y)|\,d\mu(y).
\]
For \(x\) in either simplex, its local barycentric coordinates are nonnegative and sum to one. The triangle inequality shows that its kernel-row absolute integral does not exceed the largest nodal row integral. Hence a maximizing evaluation point can be chosen among the vertices. The kernel sign yields equality in the \(L^\infty\) dual bound; bounded continuous approximations give the same norm for \(C(\Omega)\).

For \(c>d+1\), put \(F_d(c)=\mathbb E|cU-(d+1)|\). Integrating the positive tail of the beta density at the unique zero \((d+1)/c\) gives
\[
\mathbb E(cU-(d+1))_+=\frac c{d+1}\left(1-\frac{d+1}{c}\right)^{d+1},
\]
so
\[
F_d(c)=d+1-\frac c{d+1}+\frac{2c}{d+1}\left(1-\frac{d+1}{c}\right)^{d+1}.
\]
The row integral at any shared node is
\[
S_d=F_d((d+1)(d+2))=-1+2(d+2)\left(\frac{d+1}{d+2}\right)^{d+1}.
\]
The positive-tip row integral, by integration over the two weighted simplices, equals
\[
qF_d\!\left(\frac{(d+1)(d+2)(1+q)}{2q}\right)
+(1-q)F_d\!\left(\frac{(d+1)(d+2)}2\right)=N_d(q).
\]
The negative-tip row gives \(N_d(1-q)\). All scalar parameters in these uses of \(F_d\) are strictly greater than \(d+1\), so its formula applies without endpoint exceptions.

Set \(m=d+1\) and \(b=d/(d+2)=(m-1)/(m+1)\). Then
\[
N_d(q)=-1+(m+1)\left[\frac{(1+bq)^m}{(1+q)^{m-1}}+(1-q)b^m\right],
\]
and direct differentiation yields
\[
N_d'(q)=(m+1)b\left[(q-1)\frac{(1+bq)^{m-1}}{(1+q)^m}-b^{m-1}\right]<0\qquad(0<q<1).
\]
Also \(N_d(1)=S_d\), so both exclusive-tip rows strictly exceed all shared-node rows for positive volumes. Since \(N_d\) decreases strictly, the norm is \(\max\{N_d(q),N_d(1-q)\}=N_d(\min\{q,1-q\})\). The balanced minimum, boundary supremum, nonattainment, node characterization, and geometric shape-independence follow. Finally, \(N_2(1/2)=49/18\) and \(\lim_{q\downarrow0}N_2(q)=7/2\) by substitution.

## Verification
A self-contained standard-library Python script, `check_exact.py`, constructs and inverts the global nodal mass matrix over exact rationals, independently evaluates each absolute affine row integral by polynomial integration of the beta density, and compares them with the closed formulas. Running `python check_exact.py` yields 432 exact row comparisons and 54 exact full-operator comparisons over dimensions \(2\) through \(10\) and six rational volume fractions. It additionally checks the planar special values. All tested equalities hold exactly as rational numbers. The unbounded family statement and strict optimization are established algebraically above, not inferred from finite experiments.

## Relationship to prior work
Crouzeix and Thomée (1987) investigate \(L^p\) and Sobolev stability of finite-element \(L^2\) projections under mesh regularity conditions. Karkulik, Pavlicek, and Praetorius (arXiv:1210.0367, publicly available 2012-10-01) prove \(H^1\) stability of the Courant projection on newest-vertex-bisection meshes; their full-text proof studies element mass matrices but does not give this sharp two-simplex \(L^\infty\) norm. The known single-simplex affine projector determines the common-facet row value \(S_d\), but does not determine the larger exclusive-tip rows. This theorem gives a distinct exact all-dimensions area-ratio profile, its optimal balancing, and sharp degeneration behavior. Bibliographic searches did not locate the same complete profile; absence from search results is not proof of priority.

## Limitations
The theorem applies to exactly two full-dimensional simplices with one common facet and to continuous degree-one elements, not to larger meshes, discontinuous finite elements, nonconstant integration weights, or \(H^1\) stability. It does not state that every evaluation point maximizing the row integral must be a vertex: only the nodal maximizers and existence of nodal extremizers are established. Earlier unindexed or inaccessible equivalent computations remain a residual originality risk. No independent audit is represented by the accompanying reproducibility calculations.

## References
1. M. Crouzeix and V. Thomée, *The Stability in Lp and Wp1 of the L2-Projection onto Finite Element Function Spaces*, Mathematics of Computation **48** (1987), 521–532, DOI: 10.2307/2007825.
2. M. Karkulik, D. Pavlicek, and D. Praetorius, *On 2D Newest Vertex Bisection: Optimality of Mesh-Closure and H1-Stability of L2-Projection*, arXiv:1210.0367v1 (2012-10-01), later Constructive Approximation **38** (2013), 213–234.
3. J. H. Bramble, J. E. Pasciak, and O. Steinbach, *On the Stability of the L2 Projection in H1*, Mathematics of Computation **71** (2002), 147–156, DOI: 10.1090/S0025-5718-01-01314-X.
