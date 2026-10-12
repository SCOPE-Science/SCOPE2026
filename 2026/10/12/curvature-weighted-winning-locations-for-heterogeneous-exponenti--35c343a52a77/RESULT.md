# Curvature-weighted winning locations for heterogeneous exponential extremes

## Finding
Let a continuously twice differentiable rate profile \(r:[0,1]\to(0,\infty)\) attain its global minimum \(r_*\) at exactly the distinct interior points \(t_1,\ldots,t_m\), where \(m\ge1\) is finite and \(r''(t_j)>0\) for every \(j\). For each integer \(n\ge2\), take independent \(X_{n,i}\sim\operatorname{Exp}(r(i/n))\), with the rate rather than the mean parameterization, and write \(M_n=\max_{1\le i\le n}X_{n,i}\) and \(I_n=\operatorname{argmax}_{1\le i\le n}X_{n,i}\). Let \(J_n\) be the index of the nearest minimum \(t_j\) to \(I_n/n\), breaking midpoint ties toward the smaller index. Put
\[
K_j=\sqrt{\frac{2\pi r_*}{r''(t_j)}},\qquad K=\sum_{j=1}^mK_j,\qquad b_n=\frac{\log n-\frac12\log\log n+\log K}{r_*}.
\]
Then, jointly,
\[
\left(r_*(M_n-b_n),J_n,\sqrt{\log n}\,(I_n/n-t_{J_n})\right)
\;\Longrightarrow\;(G,J,Z_J).
\]
Here \(\Pr(G\le y)=\exp(-e^{-y})\), \(\Pr(J=j)=K_j/K\), and conditionally on \(J=j\), \(Z_J\sim N(0,r_*/r''(t_j))\). The Gumbel variable \(G\) is independent of the pair \((J,Z_J)\). Thus two equally low rate valleys are selected in inverse proportion to the square roots of their curvatures; the height and rescaled location of the winning observation are asymptotically independent.

## Assumptions and scope
All limits hold as integer \(n\to\infty\). Each row contains \(n\) independent, continuous, nonnegative observations. The rate profile is fixed, positive and \(C^2\) on the closed interval. All global rate minima are interior, finitely many and nondegenerate (strictly positive second derivative). Covariances between different rows are immaterial. No strict convexity or global monotonicity is assumed between the minimizing points. The label convention makes \(J_n\) well defined even away from the minimum neighborhoods; that part has vanishing probability. Write \(J(i)\) for the nearest-minimum label associated with the grid location \(i/n\), using the same tie convention.

## Proof
**1. Uniform localization of exceedance intensity.** Set \(L=\log n\) and \(x_n(y)=b_n+y/r_*\). For any fixed \(y\in\mathbb R\), the rate minima admit the expansions
\[
r(t_j+z/\sqrt L)=r_*+\frac{r''(t_j)}{2L}z^2+o(L^{-1})
\]
uniformly over bounded \(z\). Since \(x_n(y)/L\to1/r_*\),
\[
e^{-r(t_j+z/\sqrt L)x_n(y)}=
\frac{\sqrt L}{nK}e^{-y}
\exp\!\left(-\frac{r''(t_j)}{2r_*}z^2\right)(1+o(1))
\]
uniformly on compact \(z\)-sets. The mesh of rescaled coordinates is \(\sqrt L/n\to0\). Because the global minima are finite and nondegenerate, a compactness argument supplies strictly larger rates away from their neighborhoods and quadratic lower bounds inside sufficiently small neighborhoods. The resulting Gaussian majorants justify passing to the entire rescaled real line. Consequently, for any Borel \(B\subset\mathbb R\) with Lebesgue-null boundary and each \(j\),
\[
\sum_{\substack{1\le i\le n:\ J(i)=j\\\sqrt L\,(i/n-t_j)\in B}}
 e^{-r(i/n)x_n(y)}
\longrightarrow\frac{e^{-y}}K\int_B\exp\!\left(-\frac{r''(t_j)}{2r_*}z^2\right)\,dz.
\]
In particular, adding over all valleys and taking \(B=\mathbb R\) yields \(\sum_i e^{-r(i/n)x_n(y)}\to e^{-y}\), because the Gaussian integrals equal \(K_j\). Also \(\max_i e^{-r(i/n)x_n(y)}=O(\sqrt L/n)\to0\).

**2. The maximum.** The exact exponential survival probabilities give
\[
\Pr(M_n\le x_n(y))=\prod_{i=1}^n\left(1-e^{-r(i/n)x_n(y)}\right).
\]
For any fixed \(y\), the difference between the logarithm of this product and minus its first-order tail sum is bounded by a constant times \(\sum_i e^{-2r(i/n)x_n(y)}\), which vanishes by the preceding maximum-tail bound. Hence \(r_*(M_n-b_n)\) converges to the standard Gumbel law.

**3. Exact winning-location density and independence.** Independence and the absence of ties give the *exact* joint density in the transformed height variable \(y\):
\[
\Pr\{I_n=i,\ r_*(M_n-b_n)\in dy\}/dy
=\frac{r(i/n)}{r_*}\,e^{-r(i/n)x_n(y)}
\prod_{k\ne i}\left(1-e^{-r(k/n)x_n(y)}\right).
\]
For fixed \(y\), the product tends to \(\exp(-e^{-y})\) uniformly in \(i\) whose rescaled location lies in any fixed bounded valley window: deleting one factor changes it by \(1+o(1)\). In such windows \(r(i/n)/r_*\to1\). Summing the exact density over these indices and using Step 1 yields the limiting joint density
\[
\frac{e^{-y-e^{-y}}}{K}
\exp\!\left(-\frac{r''(t_j)}{2r_*}z^2\right)\,dy\,dz
\]
for each discrete label \(j\). Integrating in \(y\) gives one, and integrating in \(z\) gives \(K_j/K\). The product form proves the claimed conditional normal law and independence from \(G\).

**4. No escaped mass.** For any fixed \(A>0\), the event that the winning location lies outside bounded rescaled windows is included in the union of \(\{M_n\le x_n(-A)\}\) and the event that some index outside those windows exceeds \(x_n(-A)\). By Step 2 the first probability tends to \(\exp(-e^A)\); by the union bound and Step 1 the second has limiting upper bound \(e^A\) times the Gaussian mixture mass outside the windows. First choose \(A\) large, then the windows large. This proves joint tightness and extends the compact-window density convergence to the claimed weak convergence.

## Verification
Run `python3 verify.py` using the Python standard library. The file checks an explicit two-valley rate profile, its curvatures, exact finite-row exponential exceedance sums, maximum distribution functions, and predicted winning-valley tail weights. Its finite tests support the calculations but do not replace the continuous Laplace and density arguments. The example \(r(t)=1+100(t-1/4)^2(t-3/4)^2(1+8t)\) has minima \(t_1=1/4\) and \(t_2=3/4\), curvatures \(150\) and \(350\), and exact limiting first-valley probability \(\sqrt7/(\sqrt7+\sqrt3)\).

## Relationship to prior work
Davydov and Rotar [1] consider heterogeneous argmax probabilities and obtain tail-factor asymptotics under a common proportional tail shape. That assumption is **not satisfied** by nonconstant exponential-rate profiles: ratios \(e^{-r(i/n)x}/e^{-r(k/n)x}\) generally diverge or vanish as \(x\to\infty\). Their winner limit therefore does not imply the present localization, Gaussian curvature mixture, logarithmic centering or joint independence. Malmberg's spatial-choice formulation [2] analyzes, among other cases, exponential disturbances with a varying **additive** location term, which preserves a common exponential tail rate and produces a fixed-scale spatial selection law. The varying-rate valleys here instead produce a shrinking \(1/\sqrt{\log n}\) spatial scale. Davydov and Rotar's subsequent point-process theorem [4] establishes a general limit for triangular arrays under a fixed-scale mark and a uniformly common normalized tail measure (their hypothesis H2). In the present problem, rates away from the global minima have distinct tail exponents and original-scale winners concentrate at finitely many points; the paper does not provide the shrinking-scale Laplace calculation needed for the Gaussian marks and curvature constants. General nonstationary extreme-value and rare-exceedance methods [3] furnish context, but neither inspected winner paper states the present curvature-weighted location and centering law.

## Limitations
The theorem does not cover minima on the boundary, degenerate or flat minima, a continuum of minima, dependent observations, random rate fields, or non-exponential upper tails. The proof is asymptotic and supplies no uniform finite-sample error bound. Generic nonstationary extreme-value and random-choice literature could contain an equivalent specialization not identified by the inspected materials; priority remains subject to independent bibliographic review.

## References
[1] Y. Davydov and V. Rotar, *The Distribution of Argmaximum or a Winner Problem*, arXiv:2305.05967, first posted 10 May 2023, revised 6 February 2024. https://arxiv.org/abs/2305.05967

[2] H. Malmberg, *Random Choice over a Continuous Set of Options*, Licentiate thesis, Stockholm University, 2013; section on exponential offers. https://paperzz.com/doc/7080685/random-choice-over-a-continuous-set-of-options

[3] J. Hüsler, *Extreme values of non-stationary random sequences*, Journal of Applied Probability 23 (1986), 937–950. DOI: 10.2307/3214467. The abstract and bibliographic context were inspected, not the complete article.

[4] Y. Davydov and V. Rotar, *Point Process Approach to the Winner Problem*, arXiv:2503.02473, first posted 4 March 2025; published in *Stochastics* (2026), DOI: 10.1080/17442508.2026.2635122. https://arxiv.org/pdf/2503.02473
