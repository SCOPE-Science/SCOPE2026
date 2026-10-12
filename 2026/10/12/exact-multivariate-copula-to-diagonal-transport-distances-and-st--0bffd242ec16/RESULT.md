# Exact multivariate copula-to-diagonal transport distances and strict dimension convexity

## Finding
Let \(d\ge1\) be an integer. Let \(\Pi_d\) be Lebesgue-uniform probability on \([0,1]^d\), and \(M_d\) be the law of \((V,\ldots,V)\) for \(V\sim\operatorname{Unif}[0,1]\). Write \(Q_d=W_2^2(\Pi_d,M_d)\) for squared quadratic Wasserstein distance with ordinary Euclidean squared cost. Then
\[
Q_d=\frac d6-\frac1{(2d+1)!}\sum_{k=0}^{d}(-1)^k\binom{2d}{k}(d-k)^{2d+1}.
\]
The optimal coupling is uniquely induced, up to \(\Pi_d\)-null sets, by the map
\[
(x_1,\ldots,x_d)\longmapsto(F_d(s),\ldots,F_d(s)),\qquad s=\sum_{i=1}^d x_i,
\]
where \(F_d\) is the continuous distribution function of a sum of \(d\) independent \(\operatorname{Unif}[0,1]\) variables. Moreover \((Q_d)_{d\ge1}\) is strictly increasing and strictly convex: for every \(d\ge1\), \(Q_{d+1}>Q_d\) and \(Q_{d+2}-2Q_{d+1}+Q_d>0\). Finally,
\[
Q_d=\frac d6-\sqrt{\frac d{12\pi}}\left(1+\frac1{40d}+O(d^{-2})\right)
\qquad(d\to\infty).
\]
In particular \(Q_1=0\), \(Q_2=1/10\), and \(Q_3=181/840\).

## Assumptions and scope
Both copulas have uniform one-coordinate marginals. The quadratic transport metric is defined on the corresponding probability measures in \(\mathbb R^d\), not on copula distribution-function graphs. All transports may be measurable couplings; the source measure is absolutely continuous. The integer dimension \(d\) is unrestricted. Strict convexity concerns this one canonical benchmark sequence, **not** arbitrary copulas. It does not imply that \(M_d\) is farthest from \(\Pi_d\) among all \(d\)-copulas for \(d\ge3\).

## Proof
**1. Reduction to a scalar optimal coupling and uniqueness.** Let \(X=(X_1,\ldots,X_d)\sim\Pi_d\), \(V\sim\operatorname{Unif}[0,1]\), and \(S=\sum_iX_i\). Every coupling of \(\Pi_d\) and \(M_d\) may be represented by such a pair \((X,V)\), with cost
\[
\mathbb E\sum_i(X_i-V)^2=\frac{2d}{3}-2\mathbb E[SV].
\]
The one-dimensional rearrangement inequality maximizes \(\mathbb E[SV]\) at the comonotone coupling of the continuous law of \(S\) and the uniform law, namely \(V=F_d(S)\). The law of \(S\) is absolutely continuous and has a positive density in \((0,d)\), hence this coupling is unique almost surely. It is realizable with the original \(X\), so it uniquely minimizes the multidimensional cost. Alternatively the map is the gradient of the convex potential \(x\mapsto\int_0^{\sum_i x_i}F_d(t)\,dt\). In particular its pushforward is \(M_d\).

**2. Conversion to an absolute moment.** Let \(S'\) be an independent copy of \(S\). Continuous-law symmetrization gives
\[
\mathbb E|S-S'|=4\mathbb E[S F_d(S)]-2\mathbb ES
=4\mathbb E[S F_d(S)]-d.
\]
Indeed split \(|S-S'|\) into its two symmetric halves and condition on either variable. Thus
\[
Q_d=\frac d6-\frac12\mathbb E|S-S'|.
\]
Writing \(S'=\sum_iX_i'\), the centered sum \(S-S'\) has the same law as \(Y_{2d}-d\), where \(Y_{2d}\) is a sum of \(2d\) independent \(\operatorname{Unif}[0,1]\) variables. Symmetry about \(d\) and the integrated distribution-function identity imply
\[
\mathbb E|Y_{2d}-d|=2\int_0^d F_{Y_{2d}}(t)\,dt.
\]
The classical Irwin--Hall CDF on \([0,2d]\) is
\[
F_{Y_{2d}}(t)=\frac1{(2d)!}\sum_{k=0}^{2d}(-1)^k\binom{2d}{k}(t-k)_+^{2d},
\]
where \(z_+=\max(z,0)\). Integrating term by term from \(0\) to \(d\) gives the claimed exact integer sum. Substitution at \(d=1,2,3\) gives the stated values.

**3. Strict convexity in dimension.** Put \(Z_i=X_i-X_i'\) and \(H_d=\mathbb E|\sum_{i=1}^d Z_i|\), with \(H_0=0\). Every \(Z_i\) is symmetric, has finite first moment, and has nonnegative characteristic function
\[
a(t)=\left(\frac{\sin(t/2)}{t/2}\right)^2\in[0,1].
\]
Fourier's absolute-moment identity yields
\[
H_d=\frac2\pi\int_0^\infty\frac{1-a(t)^d}{t^2}\,dt.
\]
Consequently
\[
H_{d+1}-H_d=\frac2\pi\int_0^\infty\frac{a(t)^d(1-a(t))}{t^2}\,dt>0,
\]
and
\[
H_{d+2}-2H_{d+1}+H_d=-\frac2\pi\int_0^\infty\frac{a(t)^d(1-a(t))^2}{t^2}\,dt<0.
\]
The inequalities are strict because \(0<a(t)<1\) on an interval of positive measure, and the integrals converge at zero and infinity. Since \(Q_d=d/6-H_d/2\), strict discrete convexity follows. Also \(H_1=\mathbb E|X_1-X_1'|=1/3\), so \(Q_1=0\) and \(Q_2-Q_1>0\); strict convexity then gives strict increase for all dimensions.

**4. Large-dimensional expansion.** Put \(T_d=\sum_iZ_i/\sqrt{d/6}\). Its characteristic function is
\[
\varphi_d(t)=\left[\frac{\sin(t\sqrt{6/d}/2)}{t\sqrt{6/d}/2}\right]^{2d}.
\]
The elementary Taylor expansion \(\log(\sin z/z)=-z^2/6-z^4/180+O(z^6)\) gives, uniformly on \(|t|\le d^{1/10}\),
\[
\varphi_d(t)=e^{-t^2/2}\left(1-\frac{t^4}{40d}+O\left(\frac{t^6+t^8}{d^2}\right)\right),
\]
with the error integrable after division by \(t^2\) against a fixed Gaussian envelope. Outside that range, on \(d^{1/10}\le |t|\le c\sqrt d\), the standard bound \(|\sin z/z|\le e^{-c_0z^2}\) for bounded \(|z|\) gives exponentially small integrals; beyond \(c\sqrt d\) the sinc power is bounded by a geometric-in-\(d\) envelope, and the Gaussian tail is negligible. These observations justify termwise integration with overall \(O(d^{-2})\) error in the normalized first absolute moment. Fourier's identity and Gaussian integrals now give
\[
\mathbb E|T_d|=\sqrt{\frac2\pi}\left(1+\frac1{40d}+O(d^{-2})\right).
\]
Multiplication by \(\sqrt{d/6}\), then by \(1/2\), establishes the asymptotic formula for \(Q_d\).

## Verification
The accompanying self-contained `verify_exact.py` uses only the Python standard library. It independently evaluates \(Q_d\) for \(d=1,\ldots,8\) both via the closed \(2d\)-uniform truncated-power formula and by exact rational polynomial integration of the distinct expression \(2d/3-2\mathbb E[S F_d(S)]\). It also checks the first twelve exact finite formulas, the \(d=2,3\) benchmark constants, and the strict differences in those tested dimensions. These are finite consistency checks, not proofs of the universal or asymptotic statements; all unrestricted steps are analytic above.

## Relationship to prior work
Ansari (2026, arXiv:2609.23940v1, Proposition 3.1 and Corollary 1.4) proves the optimal diagonal transport and value \(1/10\) for **two** coordinates and proves a stronger global maximization result over bivariate copulas. The scalar rearrangement principle used in Step 1 is therefore not new. The present single claim concerns **all dimensions**, an explicit dimension-indexed exact distance, strict dimension convexity, and a two-term quantitative large-dimensional law; none is a statement of Ansari's bivariate theorems.

Abdellatif--Kuchling--Rüdiger--Ventura (2024), Theorem 3.7, gives a multivariate Wasserstein decomposition when **both probability laws have the same copula**. That hypothesis fails for \(\Pi_d\) and \(M_d\), whose dependence structures are independent and comonotone. The Irwin--Hall CDF and its integrated absolute moment are classical tools, not claimed as novel. A published 2026 calculation of the centered Irwin--Hall absolute moment in a simplex-projection problem is likewise acknowledged as covering that auxiliary formula, not this copula-distance sequence or its strict convexity. Published-source and mathematical-record searches found no stronger direct coverage of the full claim. This is not a priority guarantee.

## Limitations
The extremal property of \(M_d\) among *all* multivariate copulas is proved in the cited lead paper only in dimension two and is not asserted here in higher dimension. The cost is Euclidean squared cost; nothing is claimed about other Wasserstein orders, alternative norms, or non-uniform marginal laws. The characteristic-function expansion supplies an asymptotic remainder, not a finite-dimension uniform error constant. Independent external review has not taken place.

## References
1. J. Ansari, *Copulas farthest from independence in quadratic Wasserstein distance*, arXiv:2609.23940v1, first submitted 2026-09-20, Sections 1.2--1.3 and 3. https://arxiv.org/html/2609.23940v1 .
2. M. Abdellatif, P. Kuchling, B. Rüdiger, I. Ventura, *Wasserstein distance in terms of the comonotonicity copula*, 2024, DOI 10.1080/17442508.2024.2427734, especially Theorem 3.7. https://doi.org/10.1080/17442508.2024.2427734 .
3. M. Catalano and H. Lavenant, *Measures of Dependence based on Wasserstein distances*, arXiv:2510.06034, first submitted 2025-10-07 (survey and motivating conjecture). https://arxiv.org/abs/2510.06034 .
4. The classical Irwin--Hall distribution formula for sums of independent uniform random variables; the CDF formula is displayed in Step 2.
