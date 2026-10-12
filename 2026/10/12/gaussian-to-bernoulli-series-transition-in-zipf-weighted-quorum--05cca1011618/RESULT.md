# Gaussian-to-Bernoulli-series transition in Zipf-weighted quorum times

## Finding

For every fixed exponent \(0\le s<1\), rate \(\lambda>0\), and finite collection of levels \(0<\theta_1<\cdots<\theta_m<1\), consider the weighted quorum collection process defined below. Put \(R_N(\theta)=\lambda\tau_{N,\theta}/N\) and \(c(\theta)=-\log(1-\theta)\). The following joint finite-dimensional limits hold as \(N\to\infty\).

**Diffuse Gaussian region \(0\le s<1/2\).**
\[
\bigl(\sqrt N\,[R_N(\theta_j)-c(\theta_j)]\bigr)_{j=1}^m
\ \Longrightarrow\ (G_s(\theta_j))_{j=1}^m,
\]
where the centered Gaussian vector has covariance
\[
\operatorname{Cov}(G_s(\theta),G_s(\eta))=
\frac{(1-s)^2}{1-2s}\,
\frac{\min(\theta,\eta)-\theta\eta}{(1-\theta)(1-\eta)}.
\]

**Logarithmic boundary \(s=1/2\).**
\[
\bigl(\sqrt{N/\log N}\,[R_N(\theta_j)-c(\theta_j)]\bigr)_{j=1}^m
\ \Longrightarrow\ (G_{1/2}(\theta_j))_{j=1}^m,
\]
with covariance
\[
\operatorname{Cov}(G_{1/2}(\theta),G_{1/2}(\eta))=
\frac{1}{4}\frac{\min(\theta,\eta)-\theta\eta}{(1-\theta)(1-\eta)}.
\]

**Persistent-weight region \(1/2<s<1\).** Let \((U_i)_{i\ge1}\) be independent uniform random variables on \([0,1]\). Then
\[
\bigl(N^{1-s}[R_N(\theta_j)-c(\theta_j)]\bigr)_{j=1}^m
\ \Longrightarrow\ (L_s(\theta_j))_{j=1}^m,
\quad
L_s(\theta)=-\frac{1-s}{1-\theta}
\sum_{i=1}^{\infty}i^{-s}\bigl(\mathbf1_{\{U_i\le\theta\}}-\theta\bigr).
\]
Each series converges in \(L^2\). For every fixed \(\theta\in(0,1)\), the limit \(L_s(\theta)\) is nondegenerate and **non-Gaussian**. Its variance is \((1-s)^2\zeta(2s)\theta/(1-\theta)\). Thus the same family of weights that gives deterministic first-order quorum times for all \(s<1\) exhibits a sharp **second-order transition at \(s=1/2\)**.

## Assumptions and scope

For each integer \(N\ge1\), type \(i\in\{1,\dots,N\}\) has independent Poisson arrivals with common rate \(\lambda/N\). Its first arrival time is \(T_{i,N}\). Give this type weight
\[
w_{i,N}=\frac{i^{-s}}{H_N^{(s)}},\qquad H_N^{(s)}=\sum_{k=1}^N k^{-s}.
\]
The accumulated distinct-type weight is \(M_N(t)=\sum_{i=1}^Nw_{i,N}\mathbf1_{\{T_{i,N}\le t\}}\), and the quorum time is
\[
\tau_{N,\theta}=\inf\{t\ge0:M_N(t)>\theta\}.
\]
All limits take \(s,\lambda,m,\theta_1,\dots,\theta_m\) fixed, with \(0\le s<1\) and all levels strictly between zero and one. The Poisson clocks are **homogeneous**; the weights, not the arrival rates, follow the Zipf law. The strict threshold is part of the definition. A joint finite collection of levels is asserted, not convergence of the entire quantile process.

## Proof

**1. Reduction to a weighted empirical quantile.** Set \(E_{i,N}=\lambda T_{i,N}/N\). These variables are independent standard exponential variables. Couple every \(N\) on one infinite sequence \((E_i)_{i\ge1}\), since their finite-dimensional laws agree, and write
\[
F_N(x)=\sum_{i=1}^Nw_{i,N}\mathbf1_{\{E_i\le x\}},\qquad \mu(x)=\mathbb EF_N(x)=1-e^{-x}.
\]
Then \(R_N(\theta)=\inf\{x:F_N(x)>\theta\}\), and \(\mu(c(\theta))=\theta\), \(\mu'(c(\theta))=1-\theta>0\).

Define the deterministic fluctuation scale
\[
a_N=\Big(\sum_{i=1}^Nw_{i,N}^2\Big)^{1/2}
=\frac{\sqrt{H_N^{(2s)}}}{H_N^{(s)}}.
\]
Since \(s<1\), \(H_N^{(s)}\to\infty\) and \(\max_iw_{i,N}\to0\); hence \(a_N\to0\). For each level put
\[
Z_N(\theta)=\frac{F_N(c(\theta))-\theta}{a_N}
=\sum_{i=1}^N \frac{i^{-s}}{\sqrt{H_N^{(2s)}}}
\bigl(\mathbf1_{\{E_i\le c(\theta)\}}-\theta\bigr).
\]
These variables are centered, uniformly bounded in second moment, and their joint covariances are exactly \(\min(\theta,\eta)-\theta\eta\).

**2. Inverting the random crossing.** We establish, simultaneously for every fixed finite set of levels,
\[
\frac{R_N(\theta)-c(\theta)}{a_N}
+\frac{Z_N(\theta)}{1-\theta}\xrightarrow{\mathbb P}0.\tag{1}
\]
For fixed real \(v\), subtracting the mean from the increment \(F_N(c+a_Nv)-F_N(c)\) gives a sum of independent centered terms. Its variance is at most
\[
\sum_i w_{i,N}^2\,\Pr\{E_i\text{ lies between }c\text{ and }c+a_Nv\}
\le |v|a_N^3,
\]
for sufficiently large \(N\) (the exponential density never exceeds one). Hence, after division by \(a_N\), this random centered increment converges to zero in \(L^2\). Taylor expansion of the deterministic mean yields
\[
\frac{F_N(c+a_Nv)-\theta}{a_N}
=Z_N(\theta)+(1-\theta)v+o_{\mathbb P}(1).\tag{2}
\]
In fact the error in (2) is uniform in \(v\) on each bounded interval in probability: take a finite grid, control each grid-point random increment by the displayed variance, and sandwich increments between neighboring grid points using monotonicity of \(F_N\); the corresponding deterministic mean increments divided by \(a_N\) are bounded by the mesh size. First let \(N\to\infty\), then the mesh tend to zero.

The sequence \(Z_N(\theta)\) is tight by its bounded variance. On the event \(|Z_N(\theta)|\le K\), (2) uniformly at all \(|v|\le 2K/(1-\theta)+2\) brackets the crossing \(\inf\{v:F_N(c+a_Nv)>\theta\}\) between \(-Z_N(\theta)/(1-\theta)\pm\varepsilon\) for any \(\varepsilon>0\), with probability tending to one. This uses only the monotonicity of \(F_N\), its right-continuity, and the strictly positive slope \(1-\theta\), so it remains valid when an individual jump is of order \(a_N\). Letting \(K\to\infty\) proves (1). Intersect the finitely many high-probability events for the joint assertion.

**3. Triangular-array limits.** Let \(U_i=1-e^{-E_i}\), iid uniform on \([0,1]\). The vector of indicators at levels \(c(\theta_j)\) equals the vector \((\mathbf1_{\{U_i\le\theta_j\}})_{j=1}^m\).

If \(s\le1/2\), then \(H_N^{(2s)}\to\infty\), so the largest coefficient \(1/\sqrt{H_N^{(2s)}}\to0\). The bounded-vector Lindeberg theorem, or Cramér–Wold plus Lindeberg, gives joint convergence of \((Z_N(\theta_j))\) to the centered Gaussian bridge vector with covariance \(\min(\theta,\eta)-\theta\eta\).

If \(1/2<s<1\), then \(H_N^{(2s)}\to\zeta(2s)<\infty\). Under the fixed infinite-uniform coupling, the coefficient vectors \((i^{-s}/\sqrt{H_N^{(2s)}})_{i\le N}\), extended by zero, converge in \(\ell^2\) to \((i^{-s}/\sqrt{\zeta(2s)})_{i\ge1}\). Independence and centering therefore give **joint \(L^2\) convergence** of the finitely many \(Z_N\) coordinates to the corresponding centered Bernoulli series.

Finally the elementary power-sum asymptotics yield
\[
\begin{aligned}
\sqrt N\,a_N&\longrightarrow\frac{1-s}{\sqrt{1-2s}}&& (0\le s<1/2),\\
\sqrt{N/\log N}\,a_N&\longrightarrow\frac12&&(s=1/2),\\
N^{1-s}a_N&\longrightarrow(1-s)\sqrt{\zeta(2s)}&&(1/2<s<1).
\end{aligned}
\]
Combine with (1) and Slutsky's theorem to obtain all three stated joint laws and their constants.

**4. Non-Gaussianity in the last region.** The limiting series has positive finite variance. For \(\theta\ne1/2\), its third cumulant is
\[
-\Big(\frac{1-s}{1-\theta}\Big)^3\theta(1-\theta)(1-2\theta)\zeta(3s)\ne0.
\]
When \(\theta=1/2\), the third cumulant vanishes, but its fourth cumulant equals
\[
-\frac18\Big(\frac{1-s}{1-\theta}\Big)^4\zeta(4s)\ne0.
\]
Convergence of these cumulants follows, for example, by independent-term moment-generating functions: square-summability of the coefficients gives a normally convergent centered log-moment-generating series near zero. Every Gaussian variable has vanishing cumulants of orders above two, proving the assertion.

## Verification

The accompanying standalone Python checker verifies, in exact rational arithmetic, the finite weighted-Bernoulli mean, covariance, and nested-level covariance identities used in the proof by exhaustive enumeration of all observation bins for several weight profiles and level pairs. It separately checks the same covariance formulas by their closed expressions and checks convergence of the three deterministic normalization factors numerically. Run `python3 verification/check.py` from the extracted package directory. These checks support finite algebra only; the uniform inversion argument, Lindeberg step, \(\ell^2\)-series limit, and cumulant non-Gaussianity are proved analytically above, not inferred from finite checks.

## Relationship to prior work

Müller and Šebek [1, Theorem 4.1, Section 4] obtain the first-order limit \(\lambda\tau_{N,\theta}/N\to-\log(1-\theta)\) in probability under homogeneous clocks and arbitrary diffuse weights. Their subsequent Zipf results [1, Sections 5–7] concern **aligned** rates and weights, a different model. The result above resolves second-order fluctuations for **homogeneous rates with Zipf weights**, detecting a new transition that the universal first-order limit does not distinguish.

Withers and Nadarajah [2] develop higher-order cumulant expansions of smooth functionals of weighted empirical distributions assuming, in particular, bounded rescaled sample weights in their Section 1. The rescaled Zipf sample weights \(Nw_{1,N}\asymp N^s\) are unbounded for \(s>0\), and the non-Gaussian series regime lies outside the normal/Edgeworth setting of those expansions. Necir [3] studies weighted approximation errors for ordinary **equal-observation-weight** empirical/quantile processes and is compatible with the uniform-weight Gaussian case, but does not supply these heterogeneous-weight regimes. Akinshin [4] develops weighted quantile estimators and smoothing, without the stated Zipf limit-law classification. Classical triangular-array Gaussian theorems are explicitly used here for \(s\le1/2\); the new model-specific conclusions are the complete constants, phase transition, and non-Gaussian regime.

## Limitations

This result applies to independent Poisson arrivals with homogeneous rate \(\lambda/N\), deterministic normalized Zipf quorum weights, fixed \(0\le s<1\), and fixed finite interior threshold sets. It does not cover aligned Zipf arrival rates, unequal arrival clocks, moving thresholds, parameters \(s\ge1\), local-limit rates, or full functional convergence as a process of threshold. The Gaussian portions use standard triangular-array theory; the originality claim concerns this precise quorum-time classification and the persistent-weight series, not the underlying central limit theorem. A more general previously published weighted empirical-quantile theorem could imply portions of these formulas.

## References

1. S. Müller and S. Šebek, *Weighted-threshold Coupon Collection*, arXiv:2607.08551v1 (first posted 9 July 2026), especially Theorem 4.1 and Sections 4–7. https://arxiv.org/abs/2607.08551
2. C. S. Withers and S. Nadarajah, *The distribution and quantiles of functionals of weighted empirical distributions when observations have different distributions*, arXiv:1002.4338v1 (2010), especially Section 1 assumptions on rescaled weights. https://arxiv.org/abs/1002.4338
3. A. Necir, *Weighted Gaussian Approximations for Increments of the Uniform Empirical and Quantile Processes*, arXiv:2606.28222v2 (2026), Sections 1–2. https://arxiv.org/abs/2606.28222
4. A. Akinshin, *Weighted quantile estimators*, arXiv:2304.07265v1 (2023), Sections 1–3. https://arxiv.org/abs/2304.07265
