# A unique dispersion peak and sharp endpoint laws for Brownian coverage occupation

## Finding
Let \(B\) be standard Brownian motion, let \(z>0\), and put
\[
Z_z=\int_0^1\mathbf1\{|B_t|\le z\sqrt t\}\,dt,
\qquad V(z)=\operatorname{Var}(Z_z).
\]
Write \(\Phi\) and \(\phi\) for the standard normal distribution and density. Then
\[\mathbb E Z_z=2\Phi(z)-1.\]
The variance has the exact one-dimensional representation
\[
\boxed{V(z)=\frac1\pi\int_0^1\sqrt{1-r^2}
\left(e^{-z^2/(1+r)}-e^{-z^2/(1-r)}\right)\,dr.}
\tag{1}
\]
It is strictly increasing until a *unique* global maximum and strictly decreasing thereafter. Specifically, let \(k_*>0\) denote the unique solution to
\[
\boxed{\int_0^1\frac{t^2e^{-k(1+t^2)}}{(1+t^2)^2}\,dt
=\int_0^1\frac{e^{-k(1+t^{-2})}}{(1+t^2)^2}\,dt.}
\tag{2}
\]
Then \(z_*=\sqrt{2k_*}\) is the sole maximizer. Numerical quadrature gives
\[
k_*\approx0.344054851601734,\qquad z_*\approx0.829523780975246,
\]
\[
2\Phi(z_*)-1\approx0.593191914154019,\qquad
V(z_*)\approx0.081356561855204.
\]
Thus the most variable limiting conventional-confidence-interval coverage fraction occurs at a nominal coverage of approximately \(59.3192\%\), not at either extreme of the coverage range.

The small-band and high-confidence endpoint laws have sharp constants:
\[
\boxed{V(z)=\frac2\pi z^2-\frac43\sqrt{\frac2\pi}\,z^3+o(z^3),\qquad z\downarrow0,}
\tag{3}
\]
\[
\boxed{V(z)\sim\frac{8\phi(z)}{z^3}\sim\frac{4\delta(z)}{z^2},
\qquad z\to\infty,\quad\delta(z)=2(1-\Phi(z)).}
\tag{4}
\]
In particular, \(V(z)/(\mathbb EZ_z)^2\to1\) at vanishing nominal coverage, whereas the high-confidence variance is of order \(\delta/\log(1/\delta)\), not of order \(\delta\). These are variance statements, not distributional or quantile asymptotics.

## Assumptions and scope
Brownian motion starts at zero, has unit variance per unit time, and the interval is \([0,1]\). The integrand at \(t=0\) is immaterial. All statements hold for every real \(z>0\); no other distributional assumptions enter. The statistical interpretation uses the limiting coverage functional from Fischer and Glynn (arXiv:2610.24668v1), under the invariance-principle hypotheses of their Theorem 1. No finite-sample confidence-interval variance formula is asserted.

## Proof
**Covariance reduction.** For \(0<s<t\), the pair \((B_s/\sqrt s,B_t/\sqrt t)\) is standard bivariate normal with correlation \(r=\sqrt{s/t}\). Define
\[
G_z(r)=\Pr\{|X|\le z,|Y|\le z\},
\]
where \((X,Y)\) is this bivariate normal pair with correlation \(r\in[0,1)\). Since \(G_z(0)=[2\Phi(z)-1]^2\), using \(s=ut\) on the time triangle gives
\[
\operatorname{Var}(Z_z)
=\int_0^1\bigl(G_z(\sqrt u)-G_z(0)\bigr)\,du
=2\int_0^1r\bigl(G_z(r)-G_z(0)\bigr)\,dr.
\tag{5}
\]
The bivariate normal density is
\[
g_r(x,y)=\frac{\exp\!\left[-(x^2-2rxy+y^2)/(2(1-r^2))\right]}{2\pi\sqrt{1-r^2}}.
\]
Direct differentiation gives \(\partial_rg_r=\partial_x\partial_yg_r\) for \(|r|<1\). Integrating the right side over the square \([-z,z]^2\) proves the classical Gaussian-corner identity
\[
G_z'(r)=2g_r(z,z)-2g_r(z,-z)
=\frac{e^{-z^2/(1+r)}-e^{-z^2/(1-r)}}{\pi\sqrt{1-r^2}}.
\tag{6}
\]
Both \(G_z(r)\) and \(G_z(0)\) are bounded as \(r\uparrow1\), so integration by parts in (5) yields
\[
V(z)=\int_0^1(1-r^2)G_z'(r)\,dr,
\]
which is (1). It also proves \(V(z)>0\) for \(z>0\).

**Unique maximum.** Put \(k=z^2/2\). Under \(r=(1-u)/(1+u)\), followed by \(u=t^2\), (1) becomes
\[
V(\sqrt{2k})=\frac8\pi\int_0^1\frac{t^2}{(1+t^2)^3}
\left[e^{-k(1+t^2)}-e^{-k(1+t^{-2})}\right]dt.
\tag{7}
\]
Define the positive functions
\[
A(k)=\int_0^1\frac{t^2e^{-k(1+t^2)}}{(1+t^2)^2}dt,
\qquad
C(k)=\int_0^1\frac{e^{-k(1+t^{-2})}}{(1+t^2)^2}dt.
\]
For every \(k>0\) differentiation under the integral in (7) gives
\[
\frac{d}{dk}V(\sqrt{2k})=\frac8\pi\bigl(C(k)-A(k)\bigr).
\tag{8}
\]
Direct elementary integration gives \(A(0)=\pi/8-1/4\) and \(C(0)=\pi/8+1/4\), so \(C(0)>A(0)\). The ratio \(A(k)/C(k)\) is strictly increasing: its logarithmic derivative is
\[
\frac{d}{dk}\log\frac{A(k)}{C(k)}
=\mathbb E_{C,k}[1+t^{-2}]-\mathbb E_{A,k}[1+t^2]>0.
\tag{9}
\]
Here the two expectations are with respect to the normalized positive integrands defining \(C(k)\) and \(A(k)\). The strict inequality holds because \(1+t^{-2}>2>1+t^2\) for every \(0<t<1\). Moreover \(C(k)\le C(0)e^{-2k}\), whereas restricting \(A(k)\) to any fixed \(0<t<a<1\) gives \(A(k)\ge c_ae^{-(1+a^2)k}\) with \(c_a>0\). Therefore \(A(k)/C(k)\to\infty\). By continuity and strict monotonicity there is precisely one positive root of (2), and (8) switches from positive to negative exactly once. Since \(z\mapsto z^2/2\) is strictly increasing, that root gives the sole strict global maximizer in the stated range. Formula (7), whose integrands are smooth at \(t=0\) for \(k>0\), supplies stable one-variable numerical evaluation.

**Small-band expansion.** Set \(a=z^2\) and \(W(a)=V(\sqrt a)\). Equation (1) gives, for \(a>0\),
\[
W'(a)=\frac1\pi\int_0^1\sqrt{1-r^2}
\left[\frac{e^{-a/(1-r)}}{1-r}-\frac{e^{-a/(1+r)}}{1+r}\right]dr.
\]
Its limit at zero is \(W'(0+)=2/\pi\): the integrand at \(a=0\) simplifies to \(2r/\sqrt{1-r^2}\), with finite integral. The change \(s=1-r\) decomposes the correction to this derivative into an analytic term \(O(a)\) from the denominator \(1+r\), and the singular term
\[
T(a)=\frac1\pi\int_0^1\sqrt{2-s}\,s^{-1/2}\bigl(e^{-a/s}-1\bigr)ds.
\]
Substituting \(s=au\) and applying dominated convergence gives
\[
\frac{T(a)}{\sqrt a}\longrightarrow\frac{\sqrt2}{\pi}
\int_0^\infty u^{-1/2}(e^{-1/u}-1)du
=-2\sqrt{\frac2\pi}.
\]
The domination is by a constant times \(u^{-1/2}\min\{1,u^{-1}\}\), which is integrable on \((0,\infty)\); the final integral follows from an integration by parts after \(v=1/u\). Hence
\[
W'(a)=\frac2\pi-2\sqrt{\frac2\pi}\sqrt a+o(\sqrt a).
\]
Integration from zero proves (3), including its nonanalytic cubic correction.

**High-confidence expansion.** In (1), the negative exponential integral is bounded by \(e^{-z^2}\int_0^1\sqrt{1-r^2}dr\), negligible compared with \(e^{-z^2/2}z^{-3}\). In the remaining term put \(y=z^2(1-r)\). Then
\[
z^3e^{z^2/2}\int_0^1\sqrt{1-r^2}e^{-z^2/(1+r)}dr
=\int_0^{z^2}\sqrt{2y-y^2/z^2}
\,e^{-z^2/(2-y/z^2)+z^2/2}\,dy.
\]
For each fixed \(y\ge0\), the integrand tends to \(\sqrt{2y}e^{-y/4}\). Since \(1/(2-v)\ge1/2+v/4\) for \(0\le v\le1\), it is bounded by \(\sqrt{2y}e^{-y/4}\), an integrable majorant. Dominated convergence and \(\int_0^\infty\sqrt{2y}e^{-y/4}dy=4\sqrt{2\pi}\) give
\[
V(z)\sim\frac{4\sqrt{2/\pi}}{z^3}e^{-z^2/2}
=\frac{8\phi(z)}{z^3}.
\]
The standard Gaussian Mills ratio \(2(1-\Phi(z))\sim2\phi(z)/z\) yields the second equivalent in (4). Also \(z^2\sim2\log(1/\delta(z))\), establishing the order statement about extreme nominal coverage. The two endpoint laws and the uniqueness proof are analytical and do not rely on numerical extrapolation.

## Verification
Run `python3 verify.py` in this directory (Python standard library only). It checks a bisection solution of (2), both independent one-dimensional quadrature representations (1) and (7), endpoint scaling at several inputs, and the signs of the derivative on either side of the computed maximizer. `verification_output.txt` records the actual run. The numerical output is approximate; the strict uniqueness and limiting claims are proved above, not inferred from a finite grid. An independent high-precision integral solve also gave \(k_*\approx0.34405485160173360883\) and \(V(z_*)\approx0.08135656185520381043\).

## Relationship to prior work
Fischer and Glynn, *On the Proportion of Time that a Conventional Confidence Interval Covers*, arXiv:2610.24668v1 (first public posting 2026-10-17), introduce exactly this Brownian coverage fraction, prove its invariance principle, and provide a nested-integral formula for its second moment (their equation (4)) and numerical variance values (their Table 1). Those results and the underlying functional are prior art. The additions here are the one-dimensional covariance integral (1), the analytical *uniqueness* and exact integral characterization of the maximally variable coverage level, and the two sharp endpoint expansions (3)–(4). A numerical table alone neither excludes additional maxima nor supplies the singular endpoint constants.

The Gaussian-corner derivative in (6) is the standard identity associated with Plackett's reduction formula; it is included with its derivation, not claimed as novel. Ehrhardt, Majumdar, and Bray (arXiv:cond-mat/0306101) treat occupation statistics of Gaussian stationary processes, including Ornstein–Uhlenbeck examples. Their setting motivates an equivalence check, but the abstract describes a different sampling and occupation setup, and its full text was not retrieved in this investigation. A hidden equivalent of these specific weighted two-sided-occupation conclusions remains a residual priority risk.

## Limitations
The theorem concerns the variance of a *limiting* Brownian occupation functional at fixed nominal threshold. It does not give the full law, density, median, quantiles, finite-sample coverage error, or convergence rates of any statistical procedure. The numerical maximizer values are computed approximations, while equation (2) is the exact characterization. The literature comparison cannot establish absolute priority, especially relative to older technical treatments of Ornstein–Uhlenbeck occupations. Independent validation has not been performed.

## References
1. M. Fischer and P. W. Glynn, *On the Proportion of Time that a Conventional Confidence Interval Covers*, arXiv:2610.24668v1 (posted 2026-10-17), https://arxiv.org/abs/2610.24668.
2. R. L. Plackett, *A Reduction Formula for Normal Multivariate Integrals*, Biometrika 41 (1954), 351–360, https://doi.org/10.1093/biomet/41.3-4.351.
3. G. C. M. A. Ehrhardt, S. N. Majumdar, A. J. Bray, *Persistence Exponents and the Statistics of Crossings and Occupation Times for Gaussian Stationary Processes*, arXiv:cond-mat/0306101 (2003), https://arxiv.org/abs/cond-mat/0306101.
