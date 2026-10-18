# Angular product-exponential law for missed area of boundary-sampled polygons

## Finding
Let \(K\) be a fixed, full-dimensional convex Euclidean polygon with \(m\ge3\) genuine vertices, perimeter \(L\), and interior angles \(\theta_1,\ldots,\theta_m\in(0,\pi)\). Let \(H_N\) be the convex hull of \(N\) independent points uniformly sampled in arclength from \(\partial K\). Define the dimensionless missed area
\[
Y_N=\frac{N^2}{L^2}\bigl(\operatorname{area}(K)-\operatorname{area}(H_N)\bigr).
\]
Then, as \(N\to\infty\),
\[
Y_N\ \xrightarrow{\ d\ }\ Y_K:=\frac12\sum_{i=1}^m\sin\theta_i\,E_{i,-}E_{i,+},
\]
where the \(2m\) variables \(E_{i,-},E_{i,+}\) are independent unit-rate exponential random variables. Convergence holds for every positive integer moment. For every \(t\ge0\), the complete limiting Laplace transform is
\[
\mathbb E[e^{-tY_K}]=\prod_{i=1}^m\int_0^\infty\frac{e^{-x}}{1+(t\sin\theta_i/2)x}\,dx.
\]
In particular,
\[
\mathbb E[Y_K]=\frac12\sum_{i=1}^m\sin\theta_i,\qquad
\operatorname{Var}(Y_K)=\frac34\sum_{i=1}^m\sin^2\theta_i.
\]
For each integer \(k\ge0\), writing \(c_i=\sin\theta_i/2\), an explicit complete moment formula is
\[
\mathbb E[Y_K^k]=k!\sum_{j_1+\cdots+j_m=k}\prod_{i=1}^m j_i!\,c_i^{j_i},\qquad j_i\in\{0,1,2,\ldots\}.
\]
Hence the entire limiting law depends on the corner angles alone, not the individual edge lengths. For a prescribed number \(m\) of genuine vertices, the limiting normalized mean satisfies the sharp inequality
\[
\mathbb E[Y_K]\le\frac m2\sin\frac{2\pi}{m},
\]
with equality precisely when all interior angles are equal. Thus equiangular polygons, including the regular polygon, and no others maximize that normalized mean.

## Assumptions and scope
The polygon is fixed as \(N\to\infty\); all its sides have strictly positive length and adjacent sides are noncollinear. The sampling distribution is normalized Euclidean arclength over the *entire* polygon boundary. Repeated samples have probability zero. The theorem does not assert a uniform approximation over families whose side lengths or angles vary with \(N\), nor any statement in dimensions greater than two.

## Proof
Index the sides and vertices cyclically, with side \(S_i\) running from vertex \(v_i\) to \(v_{i+1}\), and side length \(\ell_i>0\). Let \(U_{i,-}\) and \(U_{i,+}\) be the distances from the two respective endpoints of \(S_i\) to the nearest sampled point on \(S_i\). If a side is empty, temporarily set both distances to \(\ell_i\). Let \(G_N\) be the event that every side contains a sampled point. The complement has exponentially small probability:
\[
\Pr(G_N^c)\le\sum_{i=1}^m(1-\ell_i/L)^N.
\]
On \(G_N\), the extreme sampled points on each straight side are precisely the nonredundant endpoints of the collinear sampled segment. In cyclic boundary order they form the vertices of \(H_N\). The polygonal region \(K\setminus H_N\) is, up to shared edges, the disjoint union of the corner triangles cut out at its original vertices. The two legs of the triangle at \(v_i\) have lengths \(U_{i-1,+}\) and \(U_{i,-}\), meeting at angle \(\theta_i\). Therefore the following finite-sample identity holds *exactly* on \(G_N\):
\[
\operatorname{area}(K)-\operatorname{area}(H_N)
=\frac12\sum_{i=1}^m\sin\theta_i\,U_{i-1,+}U_{i,-}.
\tag{1}
\]
For any fixed nonnegative thresholds \(t_1,\dots,t_{2m}\), the \(2m\) short endpoint arcs, each of length \(Lt_j/N\), become mutually disjoint when \(N\) is sufficiently large. Thus the joint survival probability for the corresponding rescaled endpoint distances is exactly
\[
\Pr\{NU_j/L>t_j\text{ for all }j\}
=\left(1-\frac{\sum_jt_j}{N}\right)^N
\longrightarrow e^{-\sum_jt_j}.
\]
It follows (including by the standard joint-survival characterization) that the full rescaled endpoint-gap vector converges in distribution to \(2m\) independent unit exponential variables. Since \(\Pr(G_N^c)\to0\), the continuous-mapping theorem applied to (1) proves convergence in distribution of \(Y_N\).

For convergence of *all* positive integer moments, note that every endpoint gap \(U\) obeys, for all \(t\ge0\),
\[
\Pr(NU/L>t)\le e^{-t},
\]
with the event empty once \(t>N\ell_i/L\). This follows directly by forbidding all samples from the associated boundary arc, taking account of the prescribed cap on gaps from an empty side. Consequently each \(NU/L\) has all moments bounded uniformly in \(N\). Hölder's inequality and the finite sum in (1) give uniformly bounded moments of arbitrary order for \(Y_N\) on \(G_N\). On \(G_N^c\) the actual missed area is at most \(\operatorname{area}(K)\), so its contribution to any fixed power moment of \(Y_N\) is bounded by a polynomial in \(N\) times \(\Pr(G_N^c)\), and tends to zero. This proves uniform integrability of every required power and hence convergence of all positive integer moments.

The summands in \(Y_K\) are independent. Conditioning on one unit exponential in each product gives the displayed Laplace integral; \(\mathbb E[(EF)^k]=(k!)^2\) yields the multinomial moment formula. In particular \(\mathbb E[EF]=1\) and \(\operatorname{Var}(EF)=4-1=3\), proving the mean and variance. Finally the exterior turning angles \(\varphi_i=\pi-\theta_i\in(0,\pi)\) sum to \(2\pi\). Since sine is strictly concave on \((0,\pi)\), Jensen's inequality yields
\[
\sum_i\sin\theta_i=\sum_i\sin\varphi_i\le m\sin(2\pi/m),
\]
with equality exactly for equal exterior—and therefore interior—angles.

## Verification
The accompanying `checker.py` uses only the Python standard library. It tests the *exact* finite-sample area decomposition against independently constructed planar convex hulls, tests scaled empirical means for three polygons with four or five vertices, and checks the first two moments against independently sampled product-exponential variables. Run `python checker.py`. In its recorded seeded run it passed 300 exact geometric identity tests, three large-sample scaled-mean comparisons, and two product-exponential moment comparisons. Such finite tests are corroboration, not proofs of asymptotic convergence or bibliographic novelty.

## Relationship to prior work
Reitzner, Schütt and Werner, first publicly available in November 2019, study uniform random points on the boundary of a simple polytope and derive expected volume-deficit asymptotics; their Theorem 1.2 concerns an *expectation*. The present result treats the entire weak law of the normalized missed area for every fixed planar convex polygon, gives its Laplace transform and every integer moment, and isolates angular universality. A known exact expected-area formula for boundary-sampled parallelograms, and an exact expected-area formula for boundary-sampled triangles, concern first moments rather than the full law. Results for interior-uniform sampling have fundamentally different endpoint point processes. Prior work on boundary-perimeter fluctuations concerns a different observable: an additive corner length defect rather than a product-of-gaps area defect.

## Limitations
The proof is asymptotic in the sample count with a fixed polygon. It does not provide a quantitative convergence rate, a finite-\(N\) distribution, a multivariate coupling with other hull observables, or a higher-dimensional law. Full independent validation has not occurred. Relevant indexed literature was compared, but a previously unindexed equivalent derivation cannot be ruled out solely by search.

## References
1. M. Reitzner, C. Schütt, E. M. Werner, *The Convex Hull of Random Points on the Boundary of a Simple Polytope*, arXiv:1911.05917 (first public posting 2019-11-14), *Discrete & Computational Geometry* **69** (2023), 453–504, https://doi.org/10.1007/s00454-022-00460-2.
2. P. Groeneboom, *Convex hulls of uniform samples from a convex polygon*, arXiv:1109.3118 (2011). This concerns interior-uniform sampling, not sampling from the boundary.
