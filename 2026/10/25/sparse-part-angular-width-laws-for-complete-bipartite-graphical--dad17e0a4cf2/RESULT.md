# Sparse-part angular-width laws for complete-bipartite graphical zonotopes

## Finding

The width distribution of a complete-bipartite graphical zonotope undergoes a genuine change of type according to whether its smaller bipartition class remains finite or grows. The fixed-class law has an exact, part-size-dependent lower-edge exponent; when both classes grow, the laws become Gaussian after the proper normalization, with a particularly small but positive variance at balance.

For integers \(p,q\ge1\) with \(n=p+q\ge3\), put \(d=n-1\), let \(H=\{u\in\mathbb R^n:\sum_i u_i=0\}\), and define the centered graphical zonotope
\[
Z_{p,q}=\sum_{1\le i\le p,\ 1\le j\le q}\left[-\frac{e_i-e_{p+j}}2,\frac{e_i-e_{p+j}}2\right]\subset H.
\]
For \(U\) uniformly distributed on the intrinsic Euclidean unit sphere of \(H\), let \(W_{p,q}\) be its directional width and normalize it by
\[
A_{p,q}=\frac{\sqrt{d}}{pq}W_{p,q}.
\]
Set
\[
\mu=\frac2{\sqrt\pi},\qquad b=\sqrt{\frac2\pi},\qquad
v=\frac13+\frac{2\sqrt3-4}{\pi}>0,
\]
and
\[
f(x)=\mathbb E|x-G|=b e^{-x^2/2}+x\operatorname{erf}(x/\sqrt2),\qquad G\sim N(0,1).
\]
The following conclusions hold.

**Finite-small-part law and angular boundary exponent.** For each fixed integer \(p\ge1\), as \(q\to\infty\),
\[
A_{p,q}\Longrightarrow L_p=\frac1p\sum_{i=1}^p f(G_i),
\]
where the \(G_i\) are independent standard Gaussians. This nondegenerate distribution has mean \(\mu\), variance \(v/p\), support \([b,\infty)\), and is not Gaussian. Its exact lower-edge asymptotic is
\[
\boxed{\ \mathbb P\{L_p\le b+t\}\sim
\frac{(pt/b)^{p/2}}{\Gamma(p/2+1)}\quad(t\downarrow0).\ }
\]
Thus the exponent of the probability near the smallest limiting normalized width records the finite part size \(p\).

**Two growing parts.** If \(p,q\to\infty\) and \(p/n\to\alpha\in(0,1)\), then
\[
\boxed{\ \sqrt n(A_{p,q}-\mu)\Longrightarrow
N\!\left(0,\ \frac{v}{\alpha(1-\alpha)}-\frac2\pi\right).\ }
\]
The variance is strictly positive for every \(\alpha\in(0,1)\); it has its unique minimum at \(\alpha=1/2\), where its exact value is
\[
\boxed{\ \sigma_{\mathrm{bal}}^2=\frac43+\frac{8\sqrt3-18}{\pi}
=0.0143865453994\ldots>0.\ }
\]
The negative \(2/\pi\) term is essential: it comes from using a *uniform Euclidean unit direction* rather than an unnormalized Gaussian direction. At equal part sizes it cancels most of the raw pair-difference fluctuation.

**Growing but negligible small part.** If \(p\to\infty\) and \(p/q\to0\), then
\[
\boxed{\ \sqrt p(A_{p,q}-\mu)\Longrightarrow N(0,v).\ }
\]
Interchanging \(p,q\) gives the complementary unbalanced regime. More generally, without assuming any limit for the aspect ratio, if \(\min(p,q)\to\infty\), let
\[
s_{p,q}^2=v\left(\frac1p+\frac1q\right)-\frac{2}{\pi n}>0.
\]
Then the unified angular central limit theorem is
\[
\boxed{\ \frac{A_{p,q}-\mu}{s_{p,q}}\Longrightarrow N(0,1).\ }
\]
The fixed-small-part directions instead have a non-Gaussian law. Thus the difference between a bounded and an unbounded smaller part persists for arbitrary relative growth rates.

## Assumptions and scope

The graph is the simple, unweighted complete bipartite graph; the zonotope uses unit root generators \(e_i-e_j\) of Euclidean length \(\sqrt2\), with symmetric segments of half-length. Every width, sphere, and normalizing factor is intrinsic to \(H\), with the inherited Euclidean metric; widths do not depend on translating the zonotope. Parameters \(p,q\) are deterministic positive integers. The distributional assertions are taken along arbitrary integer sequences satisfying the stated hypotheses. All Gaussians in the formulas are standard and mutually independent when separately indexed. No independence is claimed for width values at distinct directions.

## Proof

**1. Exact Gaussian representation.** Support functions of Minkowski sums add. For every unit \(u\in H\),
\[
W_{p,q}(u)=\sum_{i=1}^p\sum_{j=1}^q |u_i-u_{p+j}|.
\tag{1}
\]
Let \(X_1,\ldots,X_p,Y_1,\ldots,Y_q\) be independent \(N(0,1)\) variables. Center their concatenation by subtracting its arithmetic mean and write the resulting vector as \(RU\), where \(R^2\sim\chi_d^2\); \(R\) and \(U\) are independent and \(U\) is uniform on the intrinsic unit sphere. Since differences cancel the common mean,
\[
A_{p,q}=\frac{B_{p,q}}{R/\sqrt d},\qquad
B_{p,q}=\frac1{pq}\sum_{i=1}^p\sum_{j=1}^q|X_i-Y_j|.
\tag{2}
\]
This equality is on a common probability space, not merely an equality of expectations. The unconditional mean of the pair kernel is \(\mu=\mathbb E|X-Y|=2/\sqrt\pi\).

**2. Exact moment check and the two Gaussian contractions.** Put \(h(x)=f(x)-\mu\). The joint normal variables \(X-Y\) and \(X-Y'\) have variances \(2\) and correlation \(1/2\) for independent \(Y,Y'\). The standard bivariate absolute-Gaussian identity
\[
\mathbb E|N_1N_2|=\frac2\pi\left(\sqrt{1-\rho^2}+\rho\arcsin\rho\right)
\tag{3}
\]
for unit-variance normals of correlation \(\rho\) gives
\[
\operatorname{Var}(h(X))=\mathbb Ef(X)^2-\mu^2
=\frac13+\frac{2\sqrt3-4}\pi=v.
\tag{4}
\]
Conditioning on \(X-Y\) gives \(\mathbb E[X^2-1\mid X-Y]=((X-Y)^2-2)/4\), so
\[
\operatorname{Cov}(h(X),X^2-1)
=\frac{\mathbb E|X-Y|^3-2\mathbb E|X-Y|}{4}=\frac\mu2.
\tag{5}
\]
For comparison with existing moment results, let \(\eta_d=\sqrt2\Gamma((d+1)/2)/\Gamma(d/2)=\mathbb ER\). The independent radial decomposition in (2), together with pairwise absolute-Gaussian moments, yields the **previously available general graphical-zonotope moment specialization**
\[
\mathbb EA_{p,q}=\mu\frac{\sqrt d}{\eta_d},\qquad
\mathbb EA_{p,q}^2
=\mu^2+\frac{2-\mu^2+v(n-2)}{pq}.
\tag{6}
\]
Indeed, the \(pq\) edge pairs contain exactly \(pq(n-2)/2\) unordered pairs of adjacent edges. Formula (6) is used here as a consistency check, **not** claimed as an independently new width-moment formula. It also verifies that the limiting variance for fixed \(p\) is \(v/p\), and that the coefficient in the balanced central limit is consistent with the exact second moment.

**3. Fixed \(p\) and its boundary behavior.** For fixed \(p\), conditional on \((X_1,\ldots,X_p)\), the strong law of large numbers applied to the independent \(Y_j\) gives
\[
B_{p,q}\longrightarrow \frac1p\sum_i\mathbb E_Y|X_i-Y|=L_p
\quad\text{almost surely}.
\]
Moreover \(R/\sqrt d\to1\) in probability, proving the stated weak limit by Slutsky's theorem. The function \(f\) is even and strictly increasing on \([0,\infty)\), because \(f'(x)=\operatorname{erf}(x/\sqrt2)\), and has its unique minimum \(b=f(0)\). It is unbounded, so the support of the average \(L_p\) is precisely \([b,\infty)\); the variance in (4) shows nondegeneracy. Any nondegenerate Gaussian has full real support, so \(L_p\) is not Gaussian.

For the quantitative edge law, Taylor expansion at the unique minimum gives
\[
f(x)=b+\frac b2x^2+O(x^4)\qquad(x\to0).
\tag{7}
\]
If \(L_p\le b+t\), each \(f(G_i)-b\le pt\), forcing all \(G_i=O(\sqrt t)\). Thus the event is, up to a relative \(1+o(1)\) error in its radial boundary, the Euclidean Gaussian small ball
\[
\sum_iG_i^2\le\frac{2pt}{b}(1+o(1)).
\]
The \(\chi_p^2\) density near zero has distribution function \(\mathbb P\{\chi_p^2\le z\}\sim z^{p/2}/[2^{p/2}\Gamma(p/2+1)]\). Substitution yields the announced sharp coefficient and exponent.

**4. Two-sample projection and the growing-part limits.** Define the canonical degenerate kernel
\[
k(x,y)=|x-y|-f(x)-f(y)+\mu.
\]
Its conditional means given either argument are zero. The exact Hoeffding decomposition is
\[
B_{p,q}-\mu
=\frac1p\sum_{i=1}^p h(X_i)
+\frac1q\sum_{j=1}^q h(Y_j)
+D_{p,q},\qquad
D_{p,q}=\frac1{pq}\sum_{ij}k(X_i,Y_j).
\tag{8}
\]
By degeneracy and independence, \(\mathbb E D_{p,q}^2=\mathbb Ek(X,Y)^2/(pq)\), with finite numerator. Hence \(\sqrt nD_{p,q}\to0\) in probability if both parts have a positive asymptotic proportion, and \(\sqrt pD_{p,q}\to0\) if \(p/q\to0\) with \(p\to\infty\).

Put \(Q_n=\sum_i(X_i^2-1)+\sum_j(Y_j^2-1)\). The centered Gaussian radius satisfies
\[
\frac{R^2}{d}=1+\frac{Q_n}{n}+O_{\mathbb P}(n^{-1}),
\qquad
\frac{\sqrt d}{R}=1-\frac{Q_n}{2n}+o_{\mathbb P}(n^{-1/2}).
\tag{9}
\]
The first equality follows by expanding \(R^2=\sum X_i^2+\sum Y_j^2-(\sum X_i+\sum Y_j)^2/n\). Combining (2), (8), and (9) for proportional parts gives
\[
A_{p,q}-\mu
=\frac1p\sum_i h(X_i)+\frac1q\sum_jh(Y_j)
-\frac\mu{2n}Q_n+o_{\mathbb P}(n^{-1/2}).
\tag{10}
\]
The multivariate i.i.d. central limit theorem, (4), (5), and \(\operatorname{Var}(X^2-1)=2\) give the Gaussian variance
\[
\begin{split}
\sigma^2(\alpha)
&=v\left(\frac1\alpha+\frac1{1-\alpha}\right)
+\frac{\mu^2}{2}-2\mu\frac\mu2\\
&=\frac{v}{\alpha(1-\alpha)}-\frac{\mu^2}{2}
=\frac{v}{\alpha(1-\alpha)}-\frac2\pi.
\end{split}
\tag{11}
\]
If \(p\to\infty\) and \(p/q\to0\), the \(p\)-group term in (8) alone survives after multiplication by \(\sqrt p\); the \(q\)-group, degenerate kernel, and radial correction are all \(o_{\mathbb P}(p^{-1/2})\). The ordinary i.i.d. central limit theorem gives variance \(v\), as asserted.

Finally, \(\alpha(1-\alpha)\le1/4\), with equality only at balance. Thus the proportional-limit variance is uniquely minimized at balance. Positivity there follows from the explicit inequality \(\pi>27/2-6\sqrt3\), yielding \(4v-2/\pi>0\). Numerically the balanced coefficient is \(0.0143865453994\ldots\). For the unified statement, note that \(s_{p,q}^2>0\) follows from \(n(1/p+1/q)\ge4\) and \(4v>2/\pi\). The sequence of ratios \(p/n\) has a convergent subsequence along every subsequence. If the limit lies in \((0,1)\), the proportional limit above divided by \(\sqrt n\,s_{p,q}\) is standard normal; if it is \(0\) or \(1\), use the unbalanced limit divided by \(\sqrt{\min(p,q)}\,s_{p,q}\), whose denominator tends to \(\sqrt v\). The subsequence principle proves the unified statement for arbitrary oscillating ratios. This completes the proof.

## Verification

The standalone `verify.py` is executable with Python 3 and the standard library only (`python3 verify.py`). It directly enumerates all segment-sign supports in forty small deterministic cases and compares them to (1); independently numerically integrates the three Gaussian moment contractions \(\mathbb Ef(X)\), \(\mathbb Ef(X)^2\), and \(\mathbb Ef(X)(X^2-1)\); compares Monte Carlo first and second spherical width moments for three graph sizes with (6); checks convergence of the exact second-moment coefficient to (11) for three part ratios; and verifies the sharp \(p=1\) lower-edge asymptotic by independent scalar inversion. Observed output:

`VERIFY_OK support_cases= 40 quadratures=3 spherical_cases=3 asymptotic_ratios=3 edge_cdf=3`

These finite and numerical checks are diagnostics. The all-dimensional distributional statements and boundary coefficient follow from the analytical proof, and the code is not an infinite proof.

## Relationship to prior work

Padrol, Pilaud, and Poullot study graphical zonotopes and their deformation cones, including the Minkowski-sum realization and normal arrangements, not spherical width distributions [1]. Chapoton and Pilaud identify the graphical zonotope of a complete bipartite graph as the shuffle of two point polytopes and study its combinatorial and Minkowski structure [2]. An earlier published geometric calculation gives the first two spherical width moments for **every** connected graphical zonotope, and in particular subsumes formula (6) and its finite-dimensional variance-balancing corollaries [3]. The present distributional claims are distinct: a non-Gaussian finite-small-part law with a sharp lower-edge exponent, a full growing-part Gaussian crossover, and its explicit angular normalization correction.

The Hoeffding decomposition and multivariate central limit theorem are standard probability tools; the new statement is their specialization to a geometrically natural width observable together with the exact boundary exponent and variance cancellation. General literature on Gini mean differences and normalized two-sample statistics provides related probabilistic techniques [4] but was not found to state this intrinsic spherical graphical-zonotope law.

## Limitations

Only complete-bipartite unweighted graphical zonotopes in the standard root-vector Euclidean realization are covered. The result is not a classification of arbitrary graph sequences, edge weights, joint directions, higher-dimensional projections, or exact finite-sample width densities. The finite-dimensional mean and variance are credited to earlier work; neither an independent novelty certification nor an independent mathematical audit has been performed. A more general unindexed theorem on normalized two-sample Gaussian absolute differences could imply the limit statements; this remains a bibliographic uncertainty despite the documented comparisons.

## References

1. A. Padrol, V. Pilaud, G. Poullot, *Deformed graphical zonotopes*, arXiv:2111.12422, initial public submission 2021-11-24, https://arxiv.org/abs/2111.12422. Introduction and Sections 1.3 and 2.
2. F. Chapoton, V. Pilaud, *Shuffles of deformed permutahedra, multiplihedra, constrainahedra, and biassociahedra*, arXiv:2201.06896, initial public submission 2022-01-18, https://arxiv.org/abs/2201.06896. Sections 1.4 and 2.4, especially Proposition 98.
3. *Sharp width-variance extremizers among tree graphical zonotopes*, published mathematical record `2026/10/11/SCOPE-sharp-width-variance-extremizers-among-tree-graphical-zonotopes--482983ab9269`, https://github.com/published-finding corpus/2026/blob/main/2026/10/11/SCOPE-sharp-width-variance-extremizers-among-tree-graphical-zonotopes--482983ab9269/RESULT.md. Finding and proof of universal first and second moments.
4. C. Gerstenberger and D. Vogel, *On the efficiency of Gini's mean difference*, Statistical Methods & Applications 24 (2015), 569–596, DOI:10.1007/s10260-015-0315-x, https://arxiv.org/abs/1405.5027 (statistical context, not a geometric prior-result assertion).
