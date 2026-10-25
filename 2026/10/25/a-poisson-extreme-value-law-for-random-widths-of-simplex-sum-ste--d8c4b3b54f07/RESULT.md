# A Poisson extreme-value law for random widths of simplex-sum stellohedra

## Finding
For an integer \(m\ge3\), let \(G_m=K_{1,m}\) be the star on hub \(0\) and leaves \(1,\ldots,m\). Its *unit-weight simplex-sum graph associahedron* is the intrinsic \(m\)-dimensional polytope
\[
 P_m=\sum_{S\subseteq\{0,1,\ldots,m\}:\,G_m[S]\text{ connected},\,S\ne\varnothing}\operatorname{conv}\{e_i:i\in S\}\subset\mathbb R^{m+1}.
\]
All summands occur with coefficient one. Let \(U_m\) be uniform on the unit sphere in \(\mathbf1^\perp\), and let \(W_m=h_{P_m}(U_m)+h_{P_m}(-U_m)\) be its Euclidean directional width. Define \(b_m=\Phi^{-1}(1-1/m)>0\) using the standard normal CDF \(\Phi\).

Let \(E_1,E_2,\ldots\) be independent mean-one exponential variables, let \(\gamma\) be Euler's constant, and define the almost surely and \(L^2\)-convergent random series
\[
 Z=\gamma-\log2+\sum_{k=1}^\infty\frac{1-2^{-k}}{k}(E_k-1).
\]
For an independent copy \(Z'\), the **complete non-Gaussian fluctuation limit** is
\[
 \boxed{\quad b_m\left(\frac{\sqrt m}{2^m}W_m-2b_m\right)\ \Longrightarrow\ Z+Z'.\quad}
\]
In particular, the limit has mean \(2(\gamma-\log2)\), variance
\[
 \boxed{2\left((\log2)^2+\operatorname{Li}_2(1/4)\right),}
\]
and positive third cumulant. More generally, its cumulants of every integer order \(r\ge2\) are
\[
 \boxed{\kappa_r(Z+Z')=2(r-1)!\sum_{k=1}^\infty\frac{(1-2^{-k})^r}{k^r}.}
\]
The exact *finite-dimensional* mean, not just its limit, is
\[
 \boxed{\mathbb EW_m=\frac{2}{\sqrt2\,\Gamma((m+1)/2)/\Gamma(m/2)}\sum_{j=0}^m\binom mj\mu_{j+1},\qquad \mu_k=\mathbb E\max_{1\le i\le k}G_i,}
\]
with independent standard normal \(G_i\). Consequently
\[
 \frac{\sqrt m}{2^m}\mathbb EW_m
 =2b_m+\frac{2(\gamma-\log2)}{b_m}+o(b_m^{-1}).
\]
The limit is distributional; no claim of a finite-dimensional exact exponential-series law is made.

## Assumptions and scope
The metric is the ordinary Euclidean metric induced on the hyperplane parallel to \(\mathbf1^\perp\), not a coordinate projection or an arbitrary affine realization. The random direction is Haar-uniform on the corresponding \((m-1)\)-sphere. The polytope is specifically the unit-weight Minkowski sum of all nonempty connected-subset coordinate simplices; other realizations with the same normal fan need not obey these formulas. All limits have \(m\to\infty\), with no additional parameters.

## Proof
**1. Exact support decomposition.** In \(G_m\), the nonempty connected vertex sets are the \(m\) leaf singletons and the \(2^m\) subsets \(\{0\}\cup A\), \(A\subseteq[m]\). Singleton summands have zero width. Consequently, for every deterministic \(g=(g_0,g_1,\ldots,g_m)\),
\[
 W_{P_m}(g)=\sum_{A\subseteq[m]}\left(\max_{i\in\{0\}\cup A}g_i-\min_{i\in\{0\}\cup A}g_i\right).
\]
Let \(Y_{m,1}\ge\cdots\ge Y_{m,m}\) be the leaves sorted in decreasing order, and put \(t_+=\#\{i:g_i>g_0,\ i\ge1\}\). Counting subsets whose highest included leaf has rank \(j\) gives the *exact*, finite identity
\[
 2^{-m}\sum_A\max_{i\in\{0\}\cup A}g_i
 =\sum_{j=1}^{t_+}2^{-j}Y_{m,j}+2^{-t_+}g_0.
\]
Similarly, writing \(Y^-_{m,j}\) for the leaves in increasing order and \(t_-=\#\{i:g_i<g_0,\ i\ge1\}\),
\[
 2^{-m}\sum_A\min_{i\in\{0\}\cup A}g_i
 =\sum_{j=1}^{t_-}2^{-j}Y^-_{m,j}+2^{-t_-}g_0.
\]
These identities require no probabilistic approximation.

**2. The hub disappears at the extreme-value scale.** Take independent standard normal coordinates \(g_i\). Conditional on the finite value of \(g_0\), the strong law shows that both \(t_+\) and \(t_-\) are positive fixed proportions of \(m\) with probability tending to one. Gaussian maximal inequalities give \(\max_{0\le i\le m}|g_i|=O_{\mathsf P}(\sqrt{\log m})\). Thus extending both geometric sums in Step 1 to all \(m\) leaf ranks incurs an error bounded in absolute value by
\[
 4\,\max_{0\le i\le m}|g_i|\,\big(2^{-t_+}+2^{-t_-}\big)=o_{\mathsf P}(b_m^{-1}).
\]
(The factor four is a harmless uniform bound.) Hence
\[
 b_m\left(2^{-m}W_{P_m}(g)-2b_m\right)
 =\sum_{j=1}^{m}2^{-j}b_m(Y_{m,j}-b_m)
 +\sum_{j=1}^{m}2^{-j}b_m(-Y^-_{m,j}-b_m)+o_{\mathsf P}(1).
\]
There is also a vanishing \(-2^{-m}b_m^2\) centering correction in each sum, absorbed by the remainder.

**3. Weighted Gaussian extremes.** Let \(T_j=E_1+\cdots+E_j\), where the \(E_i\) are independent mean-one exponentials. The ordered variables \(\Phi^{-1}(1-T_j/T_{m+1})\), \(1\le j\le m\), have exactly the distribution of the descending Gaussian sample. Mills' ratio and \(T_{m+1}/m\to1\) imply, for each fixed \(j\),
\[
 b_m\left[\Phi^{-1}\left(1-\frac{T_j}{T_{m+1}}\right)-b_m\right]\longrightarrow-\log T_j\quad\text{almost surely}.
\]
The geometric weighting permits extension from fixed ranks to the entire sum. Here are sufficient details for the required tail control: fix \(0<\delta<1\). Almost surely, the strong law yields \(T_j\asymp j\) uniformly over all sufficiently large \(j\), and \(T_{m+1}\asymp m\). Uniform Gaussian Mills-ratio bounds for tail probabilities between a constant multiple of \(1/m\) and \(m^{-1+\delta}\) give
\[
 \left|b_m\left[\Phi^{-1}(1-T_j/T_{m+1})-b_m\right]\right|
 \le C(\omega,\delta)(1+\log j),\qquad j\le m^\delta,
\]
for all sufficiently large \(m\); a finite initial set of ranks is covered by the fixed-rank convergence. The full sample extremes satisfy \(\max_i|g_i|=O_{\mathsf P}(b_m)\), and under this exponential-spacing coupling the same bound holds almost surely eventually (by the Gaussian quantile formula and \(T_1>0\), \(T_{m+1}-T_m=E_{m+1}\) with subpolynomial eventual bounds). The weighted part with \(j>m^\delta\) is thus \(O_{\mathsf P}(b_m^2 2^{-m^\delta})=o_{\mathsf P}(1)\). Dominated convergence for the small ranks proves
\[
 \sum_{j=1}^m 2^{-j}b_m(Y_{m,j}-b_m)
 \Longrightarrow Z_*= -\sum_{j=1}^\infty2^{-j}\log T_j.
\]
The series converges absolutely almost surely, since \(T_j/j\to1\) and \(\sum2^{-j}\log(j+1)<\infty\). The lower tail has the same limit. The upper and lower extreme point processes are asymptotically independent: using the exact uniform-spacing representation, their first \(K\) ranks depend on disjoint blocks of \(K\) exponential spacings at opposite endpoints; these converge jointly to independent exponential-arrival sequences. The geometric tail bound then lets \(K\to\infty\). Therefore the Gaussian-width fluctuation limit is \(Z_*+Z_*'\) with independent copies.

**4. Explicit independent-exponential law and cumulants.** For any integer \(M\ge2\), the beta-gamma algebra gives independent variables \(B_k=T_k/T_{k+1}\sim\operatorname{Beta}(k,1)\), \(1\le k<M\), independent also of \(T_M\). Thus \(-k\log B_k\) are independent mean-one exponentials. Summation by parts gives
\[
 -\sum_{j=1}^M 2^{-j}\log T_j
 =-(1-2^{-M})\log T_M
 +\sum_{k=1}^{M-1}(1-2^{-k})\frac{F_k}{k},
\]
where \(F_k\) are independent \(\operatorname{Exp}(1)\). Since \(\log T_M-\log M\to0\) and
\[
 \sum_{k=1}^{M-1}\frac{1-2^{-k}}{k}-\log M\longrightarrow\gamma-\log2,
\]
the centered exponential series converges almost surely and in \(L^2\), and \(Z_*\stackrel d=Z\) as stated. Independence of the summands gives \(\kappa_r(Z)=(r-1)!\sum_{k\ge1}(1-2^{-k})^r/k^r\) for \(r\ge2\). For \(r=2\), expansion of the square and \(\operatorname{Li}_2(x)=\sum_{k\ge1}x^k/k^2\) give
\[
 \operatorname{Var}(Z)=\frac{\pi^2}{6}-2\operatorname{Li}_2(1/2)+\operatorname{Li}_2(1/4)=(\log2)^2+\operatorname{Li}_2(1/4).
\]
The strictly positive third cumulant proves the limit is not Gaussian.

**5. Spherical normalization.** Write \(\Pi\) for orthogonal projection onto \(\mathbf1^\perp\). For Gaussian \(g\in\mathbb R^{m+1}\), \(R=\|\Pi g\|\sim\chi_m\), \(U=\Pi g/R\) is Haar-uniform, and the width of \(P_m\) in direction \(g\) is \(R W_m\). As \(R/\sqrt m=1+O_{\mathsf P}(m^{-1/2})\), and \(b_m^2=O(\log m)\), replacement of Gaussian widths by \(\sqrt m\) times spherical widths changes the centered fluctuations by \(O_{\mathsf P}(\log m/\sqrt m)=o_{\mathsf P}(1)\). This proves the boxed distributional limit.

**6. Exact expected width and its asymptotics.** The Gaussian width of a coordinate simplex on \(k\) indices has expectation \(2\mu_k\). There are \(\binom mj\) hub-containing tubes of cardinality \(j+1\). Thus \(\mathbb E(RW_m)=2\sum_{j=0}^m\binom mj\mu_{j+1}\); independence of \(R\) and \(U\) yields the exact mean. With \(J\sim\operatorname{Binomial}(m,1/2)\), the uniform Gaussian-maxima expansion \(\mu_k=b_k+\gamma/b_k+o(b_k^{-1})\), and \(J/m\to1/2\) exponentially fast, give \(\mathbb E\mu_{J+1}=b_m+(\gamma-\log2)/b_m+o(b_m^{-1})\). Finally \(\sqrt m/\mathbb E\chi_m=1+O(m^{-1})\), proving the stated mean expansion.

## Verification
The standalone standard-library script `CHECKER.py` verifies all finite subset-count identities with exact rational arithmetic for several star sizes and hub locations, and checks the limiting mean, variance, and third-cumulant series numerically. These finite checks are diagnostics, not a substitute for Steps 2–6. The analytic Gaussian-limit proof covers all dimensions as \(m\to\infty\).

## Relationship to prior work
The Minkowski-sum definition of graph associahedra is due to Postnikov; Padrol–Pilaud–Poullot give a modern complete deformation-cone treatment and explicitly reproduce the simplex-sum realization. They do not assert the spherical random-width distribution or its high-dimensional extreme-value asymptotics. The limiting Gaussian extreme point process and beta-gamma algebra are classical probabilistic inputs; the contribution here is their exact geometric weighting and the resulting explicit non-Gaussian stellohedral law. Prior results about the stellohedron's minimum enclosing ball and Minkowski asymmetry concern different extrema and do not determine random-direction fluctuations.

## Limitations
The theorem is specific to *unit-weight* simplex-sum stellohedra, not every combinatorially equivalent stellohedron or graph associahedron. Weak convergence does not yield finite-\(m\) total variation bounds or a full finite-\(m\) density. The limit's mean and cumulants describe the limit law, while the separate exact expectation formula and its asymptotic describe the finite-dimensional mean. No independent review has been performed. Unindexed probability literature about geometrically weighted order statistics may contain equivalent descriptions of the auxiliary limit law, though no source was found establishing the corresponding stellohedral width theorem.

## References
1. Arnau Padrol, Vincent Pilaud, Germain Poullot, *Deformation cones of graph associahedra and nestohedra*, arXiv:2109.09200, first public 2021-09-19, especially Theorem 2.2 and Sections 2–3.
2. Alexander Postnikov, *Permutohedra, associahedra, and beyond*, arXiv:math/0507163, first public 2005-07-07, especially the Minkowski sums of coordinate simplices and nested-complex constructions.
3. Jean Cardinal, Lionel Pournin, Mario Valencia-Pabon, *The rotation distance of brooms*, arXiv:2211.07984, first public 2022-11-15, especially Section 2 on stellohedra and graph associahedra.
4. Classical Gaussian maximum domain-of-attraction, uniform-order-statistic exponential-spacing representation, and beta-gamma independence identities, used with their elementary forms in the proof.
