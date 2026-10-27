# First GUE pivot: a sharp norm-exponent phase diagram and Hilbert-window crossover

## Finding
For each integer \(n\ge2\), let \(A\) be an \(n\)-by-\(n\) Gaussian unitary ensemble matrix under the entry normalization \(A_{11}\sim N(0,1)\) and \(A_{j1}=(Y_{j1}+iY_{j2})/\sqrt2\), with all \(Y_{jk}\) and \(A_{11}\) independent standard real Gaussians. In the first step of Gaussian elimination with partial pivoting, measure a complex entry by the real-coordinate \(\ell^p\)-norm, where \(1\le p\le\infty\); a real entry has its usual absolute value. Let \(P_n(p)\) be the probability that row 1 is retained in the first pivot.

**Sharp fixed-exponent law.** For fixed \(1\le p<2\), set
\[
\lambda_p=2^{1-2/p},\qquad \alpha_p=\frac1{2\lambda_p}=2^{2/p-2},\qquad
K_p=\frac{\Gamma(\alpha_p)}{\sqrt{2\pi\lambda_p}}\left(\frac{\sqrt{\pi(2-p)}}2\right)^{\alpha_p}.
\]
Then
\[
P_n(p)\sim K_p\,n^{-\alpha_p}(\log n)^{(\alpha_p-1)/2}.
\]
At \(p=2\),
\[
P_n(2)\sim\frac1{\sqrt{2n\log n}}.
\]
For every fixed \(2<p\le\infty\), the asymptotic is instead universal in \(p\):
\[
P_n(p)\sim\frac{\pi^{1/4}}2\,n^{-1/2}(\log n)^{-1/4}.
\]
The known endpoint \(P_n(1)=1/(2n-1)\) is recovered from the first formula, and the known \(p=2\) result is quoted for comparison. The results for fixed \(1<p<2\), fixed \(p>2\), and the crossover below are the new statements.

**Critical logarithmic window.** Define the binary entropy \(H(u)=-u\log u-(1-u)\log(1-u)\), with \(0\log0=0\), and
\[
M(\beta)=\frac1{2\pi}\int_0^{2\pi}\exp\left[-\frac\beta2 H(\cos^2\theta)\right]d\theta.
\]
For each fixed real \(\beta\), take \(p_n=2+\beta/\log n\) for sufficiently large \(n\). Then
\[
\lim_{n\to\infty}\sqrt{2n\log n}\,P_n(p_n)=M(\beta)^{-1/2}.
\]
The crossover is nonconstant: \(M(0)=1\) and \(M\) is smooth and strictly decreasing. Thus the Hilbert exponent \(p=2\) has a different logarithmic power than every nearby but fixed \(p\ne2\). In addition, for every fixed \(p>1\), \(nP_n(p)\to\infty\), whereas \(nP_n(1)\to1/2\).

## Assumptions and scope
The complex \(\ell^p\)-norm is \((|\Re z|^p+|\Im z|^p)^{1/p}\) for finite \(p\), and \(\max(|\Re z|,|\Im z|)\) for \(p=\infty\). This definition is deliberately tied to the real/imaginary coordinate axes; except at \(p=2\), it is not invariant under multiplication by a unit-modulus complex number. The probability concerns only the initial column pivot, not the full elimination permutation or backward stability. All asymptotic statements are for \(n\to\infty\) with \(p\) fixed except in the explicitly stated critical window. There are no restrictions on the remaining matrix entries beyond the GUE law, since the first pivot depends only on column 1. The class is a probabilistic random-matrix question (MSC2020 60B20).

## Proof
**1. Angular reduction.** Let \(X,Y_1,Y_2\) be independent standard real Gaussians and write \(W_p=\|(Y_1,Y_2)\|_p/\sqrt2\). The first-column representation and continuity give
\[
P_n(p)=\Pr\bigl\{|X|\ge\max_{1\le j\le n-1}W_{p,j}\bigr\}=\mathbb E\left[(1-\overline F_p(|X|))^{n-1}\right],
\]
where \(\overline F_p(t)=\Pr(W_p>t)\). Put
\[
a_p(\theta)=(|\cos\theta|^p+|\sin\theta|^p)^{1/p},\qquad
h_p(\theta)=a_p(\theta)^{-2},
\]
with \(a_\infty(\theta)=\max(|\cos\theta|,|\sin\theta|)\). Polar coordinates in the independent planar standard normal, whose radius has survival probability \(e^{-r^2/2}\), yield the exact identity
\[
\overline F_p(t)=\frac1{2\pi}\int_0^{2\pi}e^{-t^2h_p(\theta)}\,d\theta\qquad(t\ge0).
\]

**2. Sharp Gaussian norm tails.** For \(1\le p<2\), the four minima of \(h_p\) occur at the diagonal angles \(\pi/4+j\pi/2\). Their common value is \(\lambda_p=2^{1-2/p}\) and their second derivative is \(2\lambda_p(2-p)>0\). Classical one-dimensional Laplace expansion at all four nondegenerate minima (the function is smooth in their neighborhoods even at \(p=1\)) gives
\[
\overline F_p(t)\sim C_p\,t^{-1}e^{-\lambda_p t^2},\qquad
C_p=\frac2{\sqrt{\pi\lambda_p(2-p)}}.
\]
For fixed \(2<p<\infty\), the four minima instead occur at the coordinate-axis angles. There \(h_p(\theta)=1+(\theta-\theta_0)^2+o((\theta-\theta_0)^2)\), hence
\[
\overline F_p(t)\sim\frac2{\sqrt\pi}\,t^{-1}e^{-t^2}.
\]
Exactly the same local expansion holds for \(p=\infty\): although its angular norm is nonsmooth at diagonal directions, its minima are at the smooth axis directions. At \(p=2\), by contrast, \(h_2\equiv1\) and \(\overline F_2(t)=e^{-t^2}\) exactly. The change from four isolated minima to a continuum of minimizers explains the exceptional logarithmic power.

**3. A Gaussian-maxima transfer calculation.** Suppose a continuous nonnegative law satisfies \(\Pr(W>\sqrt u)\sim C u^{-1/2}e^{-\lambda u}\) with \(C,\lambda>0\). For independent copies \(W_1,\ldots,W_{n-1}\) and \(X\sim N(0,1)\), set \(Q_n=\Pr(|X|\ge\max_jW_j)\). The density of \(X^2\) gives
\[
Q_n=\frac1{\sqrt{2\pi}}\int_0^\infty u^{-1/2}e^{-u/2}\bigl(1-\Pr(W>\sqrt u)\bigr)^{n-1}\,du.
\]
Define the centering
\[
b_n=\lambda^{-1}\{\log n-\tfrac12\log\log n+\log(C\sqrt\lambda)\}.
\]
For fixed real \(v\), at \(u=b_n+v/\lambda\) one has \(n\Pr(W>\sqrt u)\to e^{-v}\). Consequently the integral localized to this window yields
\[
Q_n\sim\frac{e^{-b_n/2}}{\lambda\sqrt{2\pi b_n}}
\int_{-\infty}^\infty e^{-v/(2\lambda)}e^{-e^{-v}}\,dv
=\frac{\Gamma(1/(2\lambda))}{\lambda\sqrt{2\pi b_n}}e^{-b_n/2}.
\]
For completeness, passage under the integral is justified by splitting at \(u=b_n/2\) and at a fixed multiple above \(b_n\). The lower piece is at most \(e^{-c\sqrt n/\operatorname{polylog}(n)}\) by monotonicity of the survival function, the centered lower tail is dominated by \(e^{c|v|}e^{-c'e^{|v|}}\), and the upper tail by a constant multiple of \(e^{-v/(2\lambda)}\); these are integrable. Expanding \(b_n\) gives the exact transfer formula, with \(\alpha=1/(2\lambda)\),
\[
Q_n\sim\frac{\Gamma(\alpha)}{\sqrt{2\pi\lambda}}
(C\sqrt\lambda)^{-\alpha}\,n^{-\alpha}(\log n)^{(\alpha-1)/2}.
\]
Substituting the constants in Step 2 proves the two fixed-exponent regimes. For \(p=1\), the known identity follows independently by the \(45^\circ\) rotation \(\| (Y_1,Y_2)\|_1/\sqrt2\stackrel d=\max(|Z_1|,|Z_2|)\), with \(Z_1,Z_2\) independent standard Gaussians, so \(P_n(1)=1/(2n-1)\). For \(p=2\), replacing Step 2's tail by \(e^{-u}\) in the same integral and centering at \(u=\log n\) gives \(P_n(2)\sim(2n\log n)^{-1/2}\).

**4. Critical crossover.** Let \(p_n=2+\beta/\log n\). Uniformly for \(\theta\in[0,2\pi]\), Taylor expansion at \(p=2\) gives
\[
\log h_{p_n}(\theta)=\frac\beta{2\log n}H(\cos^2\theta)
+O_\beta((\log n)^{-2}).
\]
This expansion is uniform even at the axes since \(u^p(\log u)^j\) remains bounded for \(u\in[0,1]\) and fixed \(j\). For each fixed real \(v\), at \(u=\log n+v\), the angular formula in Step 1 implies
\[
n\overline F_{p_n}(\sqrt u)\longrightarrow M(\beta)e^{-v}.
\]
Using the \(X^2\)-density integral with this centering, bounded convergence on compact \(v\)-windows plus the same exponential/superexponential tail bounds as in Step 3 shows
\[
\sqrt{n\log n}\,P_n(p_n)
\longrightarrow\frac1{\sqrt{2\pi}}
\int_{-\infty}^\infty e^{-v/2}e^{-M(\beta)e^{-v}}dv
=\frac1{\sqrt{2M(\beta)}}.
\]
The stated limit follows. Since \(H(\cos^2\theta)>0\) except at finitely many axes, differentiating under the bounded angular integral shows \(M'(\beta)<0\) for all finite \(\beta\). The formula also gives \(M(0)=1\), completing the proof.

## Verification
The standalone `verify_pivot_phase.py` evaluates the exact angular integral and the independent diagonal Gaussian integral by deterministic quadrature. It checks the published exact \(p=1\) law, the finite-\(n\) \(p=2\) binomial expression, angular norm-tail constants, and large-\(n\) asymptotic ratios for interior and extreme exponents, as well as the critical-window function. The check is reproducible using `requirements.txt`. Deterministic finite quadrature does not establish the asymptotics; Steps 1–4 do. The script reports the numerical tolerances it uses.

## Relationship to prior work
Gunawan, Peca-Medlin and Zhong (2026, arXiv:2610.10481v1), Proposition 6 and Section 4.1, derive the exact \(\ell^1\) no-swap probability \(1/(2n-1)\), the asymptotic \(\ell^2\) probability \((2n\log n)^{-1/2}\), and their numerical-algorithm interpretation. Those two cases and Gaussian norm extreme-value tools are prior knowledge, not new contributions here. The present result computes the intervening and super-Hilbert parameter regimes and their constants, identifies the universal \(p>2\) regime, and proves the logarithmic critical-window profile. Peca-Medlin (2023/2024, arXiv:2301.13452) treats distributions of pivot counts for other random-matrix ensembles; the accessible abstract alone cannot certify noncoverage of every norm variant. Huang and Tikhomirov (2022/2024, arXiv:2206.01726) concern Gaussian GEPP growth factors, not the precise first-pivot norm comparison seen here. Existing Gaussian angular Laplace and extreme-value principles explain the method; an implicit equivalent consequence in such general literature is a residual novelty risk.

## Limitations
This is a first-pivot law for a particular GUE normalization and fixed real/imaginary coordinate convention. It is not a statement about the entire GEPP permutation, numerical backward error, or unitary-invariant complex pivot rules for \(p\ne2\). The fixed-exponent asymptotics are not uniform as \(p\to2\); the separate window theorem handles only deviations of order \(1/\log n\) with a fixed window parameter. No assertion of external certification or exhaustive historical novelty is made.

## References
1. K. Gunawan, J. Peca-Medlin and C. Zhong, *Random permutations using GEPP*, arXiv:2610.10481v1, first posted 2026-10-07; especially Proposition 6 and Section 4.1. https://arxiv.org/html/2610.10481
2. J. Peca-Medlin, *Distribution of the number of pivots needed using Gaussian elimination with partial pivoting on random matrices*, arXiv:2301.13452, 2023; subsequently *Annals of Applied Probability* 34 (2024), 2294–2325. https://arxiv.org/abs/2301.13452
3. H. Huang and K. Tikhomirov, *Average-case analysis of the Gaussian elimination with partial pivoting*, arXiv:2206.01726, 2022. https://arxiv.org/abs/2206.01726
