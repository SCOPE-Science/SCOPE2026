# Power-law hub condensation in clique-windmill fractional stable-set polytopes

## Finding

Fix an integer \(r\ge2\). For every integer \(m\ge1\), form the clique windmill \(G_{m,r}=K_1\vee(mK_r)\): one hub is adjacent to all vertices in \(m\) disjoint cliques of size \(r\). In \(\mathbb R^{1+mr}\), let \(F_{m,r}=\operatorname{FRAC}(G_{m,r})\) be the nonnegative edge-inequality relaxation and let \(S_{m,r}=\operatorname{STAB}(G_{m,r})\) be the convex hull of independent-set indicator vectors. All volumes here are ordinary Euclidean coordinate volumes, not lattice-normalized volumes. Set \(c_r=2^{1-r}\).

The exact volumes are
\[
\operatorname{vol}(F_{m,r})=
\int_0^{1/2}(c_r-t^r)^m\,dt+
\frac{2^{-(rm+1)}}{rm+1},
\qquad
\operatorname{vol}(S_{m,r})=
\frac{1}{(r!)^m(rm+1)}.
\]
For a point chosen uniformly from either full-dimensional polytope, let \(T^F_{m,r}\) or \(T^S_{m,r}\) denote its hub coordinate. As \(m\to\infty\) with \(r\) fixed,
\[
m^{1/r}T^F_{m,r}\ \Longrightarrow\ X_r,
\quad
(rm+1)T^S_{m,r}\ \Longrightarrow\ E,
\]
where \(E\) is exponential with mean one and \(X_r\) has the probability density
\[
f_r(s)=\frac{e^{-s^r/c_r}}{c_r^{1/r}\Gamma(1+1/r)}\mathbf1_{\{s\ge0\}}.
\]
The relaxation-to-integral volume ratio has the sharp equivalent
\[
\frac{\operatorname{vol}(F_{m,r})}{\operatorname{vol}(S_{m,r})}
\sim(r!c_r)^m\,r\,c_r^{1/r}\Gamma(1+1/r)\,m^{1-1/r}.
\]
In the friendship-graph case \(r=2\), the local exponential factor equals one; nonetheless
\[
\frac{\operatorname{vol}(F_{m,2})}{\operatorname{vol}(S_{m,2})}
\sim\sqrt{\frac{\pi m}{2}}.
\]
Thus an unbounded polynomial relaxation-volume gap can arise solely from the shared hub, even though each individual non-hub block is an edge, whose edge relaxation is integral. The hub coordinate concentrates on scale \(m^{-1/r}\) in the relaxation but scale \(m^{-1}\) in the integral polytope. At \(r=2\), \(X_2\) is half-normal with underlying normal standard deviation \(1/2\); for larger fixed \(r\), it has a stretched-exponential density.

## Assumptions and scope

The vertex set consists of a hub labeled \(0\) and leaves \((j,a)\) with \(1\le j\le m\) and \(1\le a\le r\). The graph edges are all hub-to-leaf pairs and all leaf pairs belonging to the same block \(j\), with no edges between distinct leaf blocks. In \(F_{m,r}\), every coordinate is nonnegative and each graph edge \(\{u,v\}\) imposes \(x_u+x_v\le1\). Every vertex is incident to an edge, so these inequalities imply each coordinate lies in \([0,1]\). The integral polytope \(S_{m,r}\) is the convex hull of the indicator vectors of stable sets. These two polytopes are full-dimensional in the same coordinate Euclidean space.

For comparison with poset geometry, let \(P_{m,r}\) have one minimal element and \(m\) otherwise disjoint chains, each of length \(r\), all lying above the minimum. Its comparability graph is precisely \(G_{m,r}\), and the ordinary chain polytope \(\mathcal C(P_{m,r})\) is \(S_{m,r}\). The theorem is about the edge relaxation of this chain polytope, not about an enriched poset polytope. No assertion is made for a block size growing with \(m\), weighted inequalities, or a different metric normalization.

## Proof

**1. A one-block relaxation section.** Fix the hub coordinate \(t\in[0,1]\). The feasible leaf coordinates for one clique form
\[
B_r(t)=\{x\in\mathbb R_{\ge0}^r:x_a\le1-t\ (1\le a\le r),\quad x_a+x_b\le1\ (a<b)\}.
\]
Put \(b_r(t)=\operatorname{vol}_r(B_r(t))\). For \(0\le t\le1/2\), the cube \([0,1/2]^r\) contributes volume \(2^{-r}\). Outside this cube, at most one coordinate can exceed \(1/2\), since any two such coordinates would violate a pair inequality. If coordinate \(a\) is the unique large one and equals \(u\in(1/2,1-t]\), every other coordinate ranges independently from zero to \(1-u\), contributing \((1-u)^{r-1}\,du\). The regions overlap only on measure-zero boundaries. Therefore
\[
b_r(t)=2^{-r}+r\int_{1/2}^{1-t}(1-u)^{r-1}\,du
=2^{1-r}-t^r=c_r-t^r.
\]
For \(1/2\le t\le1\), the hub inequalities force every leaf coordinate into \([0,1-t]\subseteq[0,1/2]\), so every leaf-to-leaf pair inequality is automatic. Consequently
\[
b_r(t)=\begin{cases}c_r-t^r,&0\le t\le1/2,\\(1-t)^r,&1/2\le t\le1.\end{cases}
\]
The two expressions agree at \(t=1/2\).

**2. Exact full-polytope sections and volumes.** Once \(t\) is fixed, the \(m\) leaf blocks in \(F_{m,r}\) are independent Cartesian factors. Thus its \(mr\)-dimensional fiber volume is \(b_r(t)^m\). Fubini's theorem gives the first volume formula; in particular,
\[
\int_{1/2}^1(1-t)^{rm}\,dt=\frac{2^{-(rm+1)}}{rm+1}.
\]
For the integral polytope, a stable set either consists of the hub alone, or contains at most one vertex from each leaf clique and does not contain the hub. Consequently
\[
S_{m,r}=\{(t,x):0\le t\le1,\quad x_{j,a}\ge0,
\quad\sum_{a=1}^r x_{j,a}\le1-t\quad(1\le j\le m)\}.
\]
To justify the reverse inclusion, for \(t<1\) write any such point as \(t(1,0)+(1-t)(0,x/(1-t))\); the leaf part lies in the Cartesian product of standard simplices and therefore is a convex combination of independent-set indicators. The case \(t=1\) is the hub vertex. A standard \(r\)-simplex scaled by \(1-t\) has volume \((1-t)^r/r!\), hence
\[
\operatorname{vol}(S_{m,r})=(r!)^{-m}\int_0^1(1-t)^{rm}\,dt
=\frac1{(r!)^m(rm+1)}.
\]

**3. Dominated-convergence asymptotics for fractional volumes.** Divide the fractional volume by \(c_r^m\) and denote the quotient by \(J_{m,r}\). The preceding exact formula becomes
\[
J_{m,r}=\int_0^{1/2}\left(1-\frac{t^r}{c_r}\right)^m\,dt
+\frac{2^{-m-1}}{rm+1}.
\]
The integrand is nonnegative on its interval because \((1/2)^r/c_r=1/2\). With \(u=m^{1/r}t\), its rescaled form converges pointwise to \(e^{-u^r/c_r}\), and is bounded by the same integrable function using \(1-z\le e^{-z}\). The rescaled second term tends to zero. Dominated convergence yields
\[
\lim_{m\to\infty}m^{1/r}J_{m,r}
=\int_0^\infty e^{-u^r/c_r}\,du
=c_r^{1/r}\Gamma(1+1/r).
\]
Hence
\[
\operatorname{vol}(F_{m,r})\sim c_r^m c_r^{1/r}
\Gamma(1+1/r)m^{-1/r}.
\]
Dividing this expression by the exact integral-polytope volume gives the displayed sharp gap, including its constant.

**4. Hub-coordinate laws.** The density of \(T^F_{m,r}\) is \(b_r(t)^m/\operatorname{vol}(F_{m,r})\). The change of variables \(s=m^{1/r}t\), together with the dominated-convergence argument above, proves convergence of its distribution functions to the normalized integral of \(e^{-s^r/c_r}\) on \([0,\infty)\). The normalization constant is exactly \(c_r^{1/r}\Gamma(1+1/r)\), proving the first weak limit. Meanwhile \(T^S_{m,r}\) has density \((rm+1)(1-t)^{rm}\) on \([0,1]\). Its scaled survival probability, for fixed \(s\ge0\), is
\[
\Pr\{(rm+1)T^S_{m,r}>s\}
=\left(1-\frac{s}{rm+1}\right)^{rm+1}
\longrightarrow e^{-s},
\]
proving the second weak limit. For \(r=2\), substitute \(c_2=1/2\) and \(\Gamma(3/2)=\sqrt\pi/2\) to obtain the stated half-normal density and friendship-graph volume ratio. These statements establish all limits for fixed \(r\ge2\).

## Verification

The included standalone `check.py` uses exact rational binomial expansions and numerical integration to compare the finite volume formula for four clique sizes and six block counts. It also independently computes convex-hull volumes from half-integral feasible points for four small windmills, compares complete-graph relaxation hull volumes, and checks finite-size convergence of the normalized Laplace integrals and hub cumulative distributions. It requires Python with NumPy and SciPy; run `python3 check.py`. On the recorded run it passed 24 rational/integral volume comparisons, 8 convex-hull comparisons, 12 asymptotic comparisons and 9 hub-CDF comparisons. Numerical tests are finite corroborations; the proof of the asymptotic and distributional assertions is the preceding dominated-convergence argument, not any finite computation.

## Relationship to prior work

Okada and Tsuchiya's 2020 preprint on enriched poset polytopes recalls Stanley's ordinary chain-polytope construction, its antichain vertices, and its relationship to order polytopes; it does not treat fractional edge relaxations of clique-windmill chain polytopes or hub-coordinate limits. Hamano, Hibi and Ohsugi (2016) study Ehrhart series and Gorenstein properties for the fractional stable-set polytope of an arbitrary finite graph. Steingrímsson (1994) supplies a general finite-graph volume recursion for a dilation of the same edge relaxation, so the mere existence of a procedure to evaluate each finite volume is prior work. The specific limiting probability law for a uniformly sampled hub coordinate and the sharp \(m^{1-1/r}\) amplification relative to the integral polytope are not given by those results. The comparison concerns statements and their implications, not simply differing terminology; any literature that proves the same uniform-point marginal asymptotics would cover this theorem.

## Limitations

The clique size \(r\) is fixed while the number of blocks tends to infinity. The theorem gives weak limits and first-order asymptotics, not quantitative total-variation bounds or uniformity for varying \(r\). It does not claim uniqueness across all publications, and less-indexed literature on graph-packing volumes or uniform points in graph polytopes may contain equivalent formulas. General all-graph finite volume recurrences are acknowledged as prior work; the distinctive assertion is the localization and sharp power-law amplification. Independent mathematical validation has not been performed.

## References

1. S. Okada and A. Tsuchiya, *Two enriched poset polytopes*, arXiv:2003.12271v1, publicly posted 2020-03-27; MSC 52B12 primary. https://arxiv.org/abs/2003.12271
2. G. Hamano, T. Hibi and H. Ohsugi, *Ehrhart series of fractional stable set polytopes of finite graphs*, arXiv:1603.09613v1, publicly posted 2016-03-31. https://arxiv.org/abs/1603.09613
3. E. Steingrímsson, *A decomposition of 2-weak vertex-packing polytopes*, FPSAC 1994; *Discrete & Computational Geometry* 12 (1994), 465–479. https://fpsac-archive.github.io/FPSAC94/ARTICLES/48Steingrimsson.pdf
4. R. P. Stanley, *Two poset polytopes*, *Discrete & Computational Geometry* 1 (1986), 9–23; background on ordinary chain polytopes.
