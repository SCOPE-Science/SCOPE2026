# An exponentially accurate perimeter–angle mean law for random boundary hulls

## Finding

Let \(K\) be any fixed convex polygon with no collinear consecutive edges (all interior angles strictly between zero and \(\pi\)) with \(m\ge3\) vertices, perimeter \(P\), consecutive edge lengths \(\ell_1,\ldots,\ell_m>0\), and interior angles \(\alpha_1,\ldots,\alpha_m\). For each integer \(N\ge1\), choose \(N\) independent points uniformly by arclength on \(\partial K\), let \(H_N\) be their convex hull (area zero if fewer than three distinct noncollinear points occur), and put
\[
\Delta_N=\operatorname{Area}(K)-\operatorname{Area}(H_N),\qquad
C_K=\frac{P^2}{2}\sum_{i=1}^m\sin\alpha_i.
\]
Then there is a constant \(c_K>0\), depending only on the fixed polygon, such that
\[
\boxed{\ \mathbb E\Delta_N=\frac{C_K}{(N+1)(N+2)}+O_K(e^{-c_KN}).\ }
\]
Thus all algebraic finite-sample corrections to the mean are encoded in the single rational denominator: the individual edge lengths enter only through an exponentially small remainder when the perimeter and angles are fixed.

Let \(E_i,F_i\) (\(1\le i\le m\)) be \(2m\) independent exponential random variables of rate one, and write \(w_i=P^2\sin\alpha_i/2\). Then
\[
\boxed{\ N^2\Delta_N\ \xrightarrow[N\to\infty]{\mathrm d}\ W_K
:=\sum_{i=1}^m w_iE_iF_i,\ }
\]
and the convergence holds for *every fixed positive moment*. In particular,
\[
\lim_{N\to\infty}N^4\operatorname{Var}(\Delta_N)
=3\sum_{i=1}^m w_i^2
=\frac{3P^4}{4}\sum_{i=1}^m\sin^2\alpha_i.
\]
The limit is nondegenerate and non-Gaussian for every polygon in this class. Its Laplace transform is the explicit product
\[
\mathbb E e^{-sW_K}
=\prod_{i=1}^m \frac{e^{1/(sw_i)}E_1(1/(sw_i))}{sw_i},\quad s>0,
\]
where \(E_1(z)=\int_z^\infty e^{-t}\,dt/t\) is the exponential integral. In particular, the entire limiting law depends only on perimeter and the multiset of interior-angle sines, even though finite-sample sampling is along edges of unequal lengths.

## Assumptions and scope

The vertices of \(K\) are listed counterclockwise, with indices interpreted cyclically. Fixed \(m\) and fixed positive side lengths are essential; no simultaneous limit in polygon complexity is asserted. Uniform sampling is with respect to normalized boundary arclength and samples are independent. Angles satisfy \(0<\alpha_i<\pi\); the exterior angle is \(\pi-\alpha_i\), so its sine equals \(\sin\alpha_i\). The random hull may be degenerate at small \(N\); its area is interpreted as zero then. The positive constant in the exponentially small error may be any sufficiently small number below \(-\log(1-\min_i\ell_i/P)\). A different symbol \(C_K\) is used for the leading geometric coefficient.

## Proof

**1. Exact geometry on the high-probability event.** Let \(G_N\) be the event that every edge contains at least one sampled point. On an edge \(e_i=[v_i,v_{i+1}]\), let \(L_{i,N}\) and \(R_{i,N}\) be distances along the edge from its two endpoints to its nearest sampled points; if the edge is empty, assign both distances its full length \(\ell_i\). Put \(X_{i,N}=R_{i-1,N}\) and \(Y_{i,N}=L_{i,N}\). On \(G_N\), the hull follows the supporting portions of each sampled edge, and between neighboring edges it replaces the original vertex by the chord joining the nearest points. Consequently the missing regions are disjoint corner triangles, exactly giving
\[
\Delta_N=\frac12\sum_{i=1}^m\sin\alpha_i\,X_{i,N}Y_{i,N}\qquad\text{on }G_N.
\]
Because the sampling distribution is continuous, endpoint coincidences have probability zero. The identity also covers an edge containing a single sampled point, for which the two nearest points on that edge coincide. It follows directly from the supporting-line property of each side of a convex polygon, not from an approximation by small triangles.

**2. The exponentially accurate expectation.** For \(0\le x<\ell_{i-1}\) and \(0\le y<\ell_i\), the two boundary intervals adjacent to vertex \(v_i\) are disjoint except at a point of zero arclength. Hence
\[
\Pr(X_{i,N}>x,\ Y_{i,N}>y)
=\left(1-\frac{x+y}{P}\right)^N.
\]
Integration of this joint survival function (the standard identity for a product of nonnegative bounded variables) gives
\[
\begin{split}
\mathbb E[X_{i,N}Y_{i,N}]={P^2\over(N+1)(N+2)}\bigg[1
&-\left(1-\frac{\ell_{i-1}}P\right)^{N+2}
-\left(1-\frac{\ell_i}P\right)^{N+2}\\
&+\left(1-\frac{\ell_{i-1}+\ell_i}P\right)^{N+2}\bigg].
\end{split}
\]
All bases are nonnegative since the polygon has at least three positive-length edges. Moreover,
\[
\Pr(G_N^c)\le\sum_{i=1}^m\left(1-\frac{\ell_i}P\right)^N.
\]
On any outcome \(0\le\Delta_N\le\operatorname{Area}(K)\) and \(0\le X_{i,N}\le\ell_{i-1}\), \(0\le Y_{i,N}\le\ell_i\). Therefore the difference between \(\Delta_N\) and the corner-triangle sum is bounded by a fixed geometric constant on \(G_N^c\), and vanishes on \(G_N\). Summing the exact product expectations proves the displayed rational formula with an exponentially small error. An explicit valid error bound is
\[
\left|\mathbb E\Delta_N-\frac12\sum_i\sin\alpha_i\,\mathbb E[X_{i,N}Y_{i,N}]\right|
\le\left(\operatorname{Area}(K)+\frac12\sum_i\ell_{i-1}\ell_i\sin\alpha_i\right)\sum_j(1-\ell_j/P)^N.
\]

**3. Independent corner Poisson limits.** Scale the \(2m\) endpoint distances by \(N/P\). For any fixed nonnegative thresholds on these distances, their corresponding small boundary intervals are eventually mutually disjoint, because each edge has fixed positive length. The probability that none of \(N\) independently sampled points lies in their union is exactly \((1-T/N)^N\), where \(T\) is the sum of those thresholds, for all sufficiently large \(N\). It converges to \(e^{-T}\), the joint survival function of \(2m\) independent unit exponentials. Hence all scaled endpoint distances converge jointly in law to \((E_1,F_1,\ldots,E_m,F_m)\). Since \(\Pr(G_N^c)\to0\), the corner-area identity and the continuous mapping theorem imply the asserted weighted-product distributional limit.

**4. Convergence of all moments.** For any single capped endpoint distance \(D_{N}\),
\[
\Pr(ND_N/P>t)\le e^{-t}\quad(t\ge0),
\]
by the exact binomial void probability \((1-t/N)^N\) below the edge-length cutoff (and zero beyond it). Thus every scaled endpoint distance has uniformly bounded moments of all positive orders. Hölder's inequality supplies uniformly bounded moments of the scaled corner-area sum of every order. The residual contribution from \(G_N^c\) to a positive moment of \(N^2\Delta_N\) is bounded by a polynomial in \(N\) times \(\Pr(G_N^c)\), hence vanishes. Applying convergence in distribution with uniform integrability at the required order proves convergence of all fixed positive moments. Since \(\mathbb E(E_iF_i)=1\) and \(\operatorname{Var}(E_iF_i)=4-1=3\), the displayed limiting mean and variance follow. More generally, for each integer \(k\ge0\),
\[
\mathbb E W_K^k
=k!\sum_{r_1+\cdots+r_m=k}\prod_{i=1}^m(r_i!\,w_i^{r_i}).
\]

**5. Distribution, transform and non-Gaussianity.** Conditioning on one unit exponential gives \(\mathbb E[e^{-tEF}]=\int_0^\infty e^{-x}(1+tx)^{-1}\,dx=e^{1/t}E_1(1/t)/t\) for \(t>0\). Independence over vertices proves the claimed product transform. Each weight \(w_i\) is strictly positive. Therefore \(W_K>0\) almost surely, is unbounded above, and has positive variance; it cannot have a nondegenerate Gaussian distribution, which assigns positive mass to negative values.

## Verification

The accompanying standard-library-only script `verify.py` independently constructs Euclidean convex hulls by the monotone-chain algorithm and computes their areas by shoelace sums. On thousands of independently sampled configurations it checks the corner-triangle identity whenever every edge is occupied, including nonregular polygons. Its finite-sample Monte Carlo checks compare independently computed hull-area deficits with the rational expectation and the predicted rescaled variance. A separate simulation checks the first two moments of a product of independent exponentials. The script reports all checks and uses deterministic random seeds. The analytical argument, not the simulations, proves the infinite-dimensional convergence, transform, or exponential remainder.

For a unit square, \(P=4\) and all \(\sin\alpha_i=1\), so \(C_K=32\) and \(W_K=8\sum_{i=1}^4 E_iF_i\). The limiting variance is \(768\), and \(\mathbb E\Delta_N=32/((N+1)(N+2))+O(e^{-cN})\) for some positive \(c\). These values provide a directly reproducible specialization.

## Relationship to prior work

The classical random-polygon central-limit work of Pardon (arXiv:1003.4209, first available 22 March 2010) concerns uniform samples **inside** convex sets, not the present uniform boundary sampling. Schütt and Werner (2000) study boundary-sampled polytopes under regularity hypotheses on smooth convex bodies. Reitzner, Schütt and Werner (arXiv:1911.05917; journal 2023), in the same boundary-sampled polytope model, establish a general power law for the expected volume deficit with an unspecified geometric constant; their stated results do not supply the present explicit planar coefficient, all-algebraic-orders mean law, or random limit. Prochno, Schütt, Sonnleitner and Werner (arXiv:2404.02870) establish fixed-polygon **Hausdorff-distance** asymptotics and, as an intermediate result, joint local Poisson point-process convergence. The present weighted-product distribution follows from that existing process limit after the polygonal area-cap identity is supplied, so independent novelty is **not** asserted for the underlying asymptotic independence mechanism. Their results do not entail the new exponentially accurate finite-\(N\) rational mean identity. A public result on Gumbel Hausdorff error for randomly inscribed regular polygons (record `3fe000dbc9a1`) likewise concerns an extreme value in a different observable, not the finite-mean identity or the area-loss distribution. The principal claim of originality is the exponentially accurate, all-algebraic-orders finite-sample perimeter–angle mean identity. The explicit area-product law, moments, and Laplace transform complement and interpret that identity; the joint Poisson limit on which they rest is previously established.

## Limitations

Only fixed convex polygons with no collinear consecutive edges with positive side lengths and independent arclength-uniform sampling are covered. The claim does not extend automatically to smooth curved boundaries, a growing number of sides, sampling from the polygon interior, or nonuniform boundary densities. The finite-sample remainder is exponentially bounded but no best possible exponent is asserted. The limit need not determine side lengths or polygon congruence; at fixed perimeter it only sees the multiset of angle sines. Historical priority is assessed against inspected sources, not exhaustively proved. Finite checker outcomes are corroboration, not independent certification of the theorem.

## References

1. J. Pardon, *Central limit theorems for random polygons in an arbitrary convex set*, arXiv:1003.4209 (first public 22 March 2010), https://arxiv.org/abs/1003.4209 .
2. C. Schütt and E. M. Werner, *Random polytopes with vertices on the boundary of a convex body*, Comptes Rendus Acad. Sci. I Math. 331 (2000), 697–701, doi:10.1016/S0764-4442(00)01685-2 (smooth-boundary comparison).
3. M. Reitzner, C. Schütt and E. M. Werner, *The convex hull of random points on the boundary of a simple polytope*, arXiv:1911.05917; Discrete Comput. Geom. 69 (2023), 453–504, doi:10.1007/s00454-022-00460-2.
4. J. Prochno, C. Schütt, M. Sonnleitner and E. M. Werner, *Random approximation of convex bodies in Hausdorff metric*, arXiv:2404.02870 (first public 3 April 2024), https://arxiv.org/abs/2404.02870 .
5. *Gumbel transition and second-order Hausdorff error for randomly inscribed regular polygons*, publicly available geometric-probability research result, record `3fe000dbc9a1` (comparative source; distinct Hausdorff observable).
