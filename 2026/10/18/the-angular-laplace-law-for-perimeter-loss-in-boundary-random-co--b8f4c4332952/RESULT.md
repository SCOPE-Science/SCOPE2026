# The angular Laplace law for perimeter loss in boundary-random convex polygons

## Finding

Let \(P\subset\mathbb R^2\) be a convex polygon with \(m\ge3\) genuine vertices, Euclidean perimeter \(L>0\), and interior angles \(\alpha_j\in(0,\pi)\). Independently select \(N\ge3\) arclength-uniform boundary points, and let \(H_N\) be their convex hull. Define the perimeter deficit \(D_N=L-\operatorname{per}(H_N)\), with ordinary Euclidean perimeter (a segment has twice its length).

For each \(\alpha\in(0,\pi)\), take independent mean-one exponentials \(E,F\) and set
\[
Q_\alpha=E+F-\sqrt{E^2+F^2-2EF\cos\alpha}.
\]
Let \(Q_{\alpha_1},\ldots,Q_{\alpha_m}\) be independent. Then
\[
\boxed{\quad \frac NL D_N\ \Longrightarrow\ Z_P:=\sum_{j=1}^m Q_{\alpha_j}.\quad}
\]
Convergence holds also for every positive integer moment. Writing
\[
c_\alpha(u)=1-\sqrt{1-2(1+\cos\alpha)u(1-u)},\quad 0\le u\le1,
\]
the **complete angular Laplace law** is
\[
\boxed{\quad \mathbb E e^{-t Z_P}=\prod_{j=1}^m \int_0^1(1+t c_{\alpha_j}(u))^{-2}\,du,\quad t\ge0.\quad}
\]
In particular, put
\[
\mu(\alpha)=1-\frac{\sin^2(\alpha/2)}{\cos(\alpha/2)}\log\cot(\alpha/4).
\]
Then
\[
\lim_{N\to\infty}\frac NL\mathbb ED_N=\sum_{j=1}^m\mu(\alpha_j),
\]
\[
\lim_{N\to\infty}\frac{N^2}{L^2}\operatorname{Var}(D_N)
=\sum_{j=1}^m\left[6\mu(\alpha_j)-2(1+\cos\alpha_j)-\mu(\alpha_j)^2\right].
\]
The normalized limiting distribution is therefore **independent of individual edge lengths** for fixed interior angles. If \(0<\alpha<\beta<\pi\), the natural coupling with the same \(E,F\) satisfies \(Q_\alpha>Q_\beta\) almost surely. The angular dependence is strict.

## Assumptions and scope

The polygon is fixed while \(N\to\infty\); every corner has angle strictly between zero and \(\pi\), and every edge has positive length. Points are independent and uniformly distributed relative to the **full boundary's arclength**, not uniformly from the interior, not one-per-edge, and not sampled independently conditional on edge counts. Scaling \(N/L\) is part of the theorem. This statement addresses the perimeter deficit, not the Hausdorff distance or missing area. No limit is asserted when the polygon itself changes with \(N\).

## Proof

**1. An exact finite-sample vertex decomposition.** Label vertices cyclically as \(v_1,\ldots,v_m\) and their edges as \(e_j=[v_j,v_{j+1}]\). On the event \(G_N\) that each edge contains at least one sampled point, the convex hull has as boundary vertices precisely the first and last sampled point along every edge (only one point if its occupancy is one). The original polygonal sides contribute the portions between those extreme sampled points; the remaining hull edges bridge the two samples nearest each original corner. This follows because the supporting line of an original edge exposes exactly its selected extremal points, and the cyclic boundary order of extreme points of a convex set agrees with the boundary order of \(P\).

At corner \(v_j\), let \(S_{j,N},T_{j,N}\ge0\) be the distances along its two incident edges to the nearest sampled point on each respective edge. By the cosine rule, the bridging chord has length
\[
B_{j,N}=\sqrt{S_{j,N}^2+T_{j,N}^2-2S_{j,N}T_{j,N}\cos\alpha_j}.
\]
Consequently the exact identity on \(G_N\) is
\[
\boxed{\quad D_N=\sum_{j=1}^m(S_{j,N}+T_{j,N}-B_{j,N}).\quad}\tag{1}
\]
It remains correct when an edge has exactly one sampled point: in that case its two endpoint gaps add to the full edge length and its own retained boundary interval has length zero.

**2. Joint exponential endpoint gaps.** There are \(2m\) endpoint gaps. For any fixed nonnegative thresholds \(s_1,\ldots,s_{2m}\), sufficiently large \(N\) makes all the disjoint forbidden boundary intervals of lengths \(Ls_k/N\) fit inside their corresponding half-edges. The probability that none of the \(N\) independent points falls in any forbidden interval is exactly
\[
\left(1-\frac1N\sum_{k=1}^{2m}s_k\right)^N
\longrightarrow\exp\left(-\sum_{k=1}^{2m}s_k\right).
\]
This is the joint upper-orthant survival law of \(2m\) independent unit exponentials. Hence all \(N S_{j,N}/L\) and \(N T_{j,N}/L\) converge jointly to independent unit exponentials. Moreover \(\Pr(G_N^c)\le\sum_j(1-|e_j|/L)^N\to0\). Since the expression in (1) is continuous and homogeneous of degree one in each gap pair, the continuous-mapping theorem gives the asserted limit in distribution.

**3. Moment convergence.** If \(R_N\) is any one endpoint gap, then \(\Pr(NR_N/L>t)=(1-t/N)^N\le e^{-t}\) for every feasible \(t\ge0\), and the tail is zero above the corresponding edge-length bound. Thus all positive fixed moments of \(NR_N/L\) are uniformly bounded. On \(G_N\), each summand in (1) lies between zero and \(S_{j,N}+T_{j,N}\). By the elementary inequality bounding a finite sum's fixed power by a constant times the sum of its members' powers, the normalized deficit restricted to \(G_N\) has uniformly bounded moments of arbitrarily high order. On \(G_N^c\), \(0\le D_N\le L\), so \(\mathbb E[(ND_N/L)^k\mathbf1_{G_N^c}]\le N^k\Pr(G_N^c)\to0\) for every fixed integer \(k\). Uniform integrability, using a moment order strictly greater than the desired one, proves convergence of every positive integer moment.

**4. Exact Laplace transform.** For independent unit exponentials, \(S=E+F\) is Gamma with shape two and rate one, and \(U=E/(E+F)\) is independent and uniform on \([0,1]\). A direct substitution gives \(Q_\alpha=S c_\alpha(U)\). Since \(\mathbb E[e^{-zS}]=(1+z)^{-2}\), conditioning on \(U\) proves
\[
\mathbb E[e^{-tQ_\alpha}]=\int_0^1(1+t c_\alpha(u))^{-2}\,du.
\]
Independence across corners produces the product.

**5. Mean and variance.** Gamma moments give \(\mathbb E Q_\alpha=2\int_0^1c_\alpha(u)\,du\) and \(\mathbb E Q_\alpha^2=6\int_0^1c_\alpha(u)^2\,du\). Put \(a=\cos(\alpha/2)\), \(b=\sin(\alpha/2)\) and change variables \(z=2u-1\). Then
\[
\int_0^1\sqrt{1-2(1+\cos\alpha)u(1-u)}\,du
=\int_0^1\sqrt{b^2+a^2z^2}\,dz
=\frac12+\frac{b^2}{2a}\operatorname{arsinh}(a/b).
\]
Since \(\operatorname{arsinh}(\cot(\alpha/2))=\log\cot(\alpha/4)\), this yields the displayed expression for \(\mu(\alpha)\). Also \(\int_0^1c_\alpha(u)^2\,du=\mu(\alpha)-(1+\cos\alpha)/3\), proving the second-moment and variance formulas. Monotone dependence on \(\alpha\) follows directly because the bridging chord length increases strictly as its included angle increases for positive gaps.

## Verification

A standalone Python 3 checker reproduces the exact deficit decomposition by directly computing convex hull perimeters for 70 independent arclength samples of each of three convex polygons (triangle, rectangle, and pentagon), conditioned only on each side containing a sample. It verifies the closed mean and second-moment formulas against Simpson quadrature at five angles; evaluates the Laplace integrals at three positive parameters; and compares the derived mean with 60,000 independent exponential corner samples at three angles. All tests passed at the specified numerical tolerances. The proof above, not the finite tests, establishes the infinite-sample convergence and all-angle identities.

## Relationship to prior work

Prochno, Schütt, Sonnleitner and Werner (first publicly available April 3, 2024) derive a sharp asymptotic **Hausdorff-distance** law for convex polygons sampled on their boundary, with angular dependence and exponential local gaps. Their subject and local-gap technique motivate this separate perimeter question, but their Theorem 1 and associated remarks concern the maximum of the corner distances, not the additive chord-shortening observable, its complete Laplace product, or its mean and variance. Reitzner, Schütt and Werner (first publicly available November 14, 2019) study vertex/facet counts and volume deficits for boundary-random simple polytopes; these are different observables. Nikitin and Polevaya (2020) compute mean perimeter for points chosen on the **smooth unit circle**, not the asymptotic boundary-random polygon corner regime. A related mathematical record on regular-polygon Hausdorff fluctuations likewise concerns a maximum-distance statistic, not perimeter loss. These comparisons identify a distinct gap but do not guarantee exhaustive novelty against every unindexed source.

## Limitations

The theorem applies only to fixed planar convex polygons with positive edge lengths and genuine corners; it does not assert a uniform limit over degenerating angles, polygons whose side count grows, or smoother bodies. Only integer-moment convergence is claimed. Its originality remains contingent on complete bibliographic coverage, and no independent mathematical audit has been performed.

## References

1. J. Prochno, C. Schütt, M. Sonnleitner, E. M. Werner, *Random approximation of convex bodies in Hausdorff metric*, arXiv:2404.02870 (first submitted 2024-04-03), https://arxiv.org/abs/2404.02870 ; published *Mathematische Annalen* (2025), https://doi.org/10.1007/s00208-025-03186-7 .
2. M. Reitzner, C. Schütt, E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917 (first submitted 2019-11-14), https://arxiv.org/abs/1911.05917 ; *Discrete & Computational Geometry* 69 (2023), https://doi.org/10.1007/s00454-022-00460-2 .
3. Ya. Yu. Nikitin and T. A. Polevaya, *On the average perimeter of the inscribed random polygon*, *Vestnik of Saint Petersburg University. Mathematics. Mechanics. Astronomy* 7 (2020), 77–84, https://doi.org/10.21638/11701/spbu01.2020.108 .
