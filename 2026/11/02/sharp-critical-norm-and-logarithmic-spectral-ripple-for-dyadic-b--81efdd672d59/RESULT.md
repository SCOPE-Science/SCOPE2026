# Sharp critical norm and logarithmic spectral ripple for dyadic Bergman line sampling

## Finding
Let \(\Pi=\{z\in\mathbb C:\operatorname{Im}z>0\}\), with the unweighted analytic Bergman norm \(\|f\|_{A^2(\Pi)}^2=\int_0^\infty\int_{\mathbb R}|f(x+iy)|^2\,dx\,dy\). For every real \(\beta>0\) define
\[
Q_\beta(f)=\sum_{j=0}^\infty 2^{-\beta j}\int_{\mathbb R}|f(x+i2^{-j})|^2\,dx.
\]
Its optimal Bergman embedding constant is finite **if and only if** \(\beta\ge1\). At the critical exponent \(\beta=1\), put
\[
P(\theta)=\sum_{k\in\mathbb Z}2^{k+\theta}e^{-2^{k+\theta}},\qquad
K=\max_{0\le\theta\le1}P(\theta).
\]
Then the exact sharp inequality is
\[
Q_1(f)\le K\|f\|_{A^2(\Pi)}^2,
\]
with **strict inequality for every nonzero** \(f\). The 1-periodic function \(P\) has exactly one maximum and one minimum modulo 1, and
\[
P(\theta)=\frac1{\log2}\sum_{\ell\in\mathbb Z}
\Gamma\left(1-\frac{2\pi i\ell}{\log2}\right)e^{2\pi i\ell\theta}.
\]
In particular, \(K>1/\log2\); numerical evaluation gives \(K\approx1.4427093011329494542\) and its maximizing phase \(\theta_*\approx0.8611035250777802693\). The **two-sided** dyadic sampling form obtained by extending the line index to every \(j\in\mathbb Z\), with coefficient \(2^{-j}\), also has exact norm \(K\). Thus removing every coarse line at heights \(2,4,8,\ldots\) leaves the sharp trace norm unchanged, although it strictly decreases the quadratic form on each nonzero function.

More generally, for every \(\beta>0\), set
\[
P_\beta(\theta)=\sum_{k\in\mathbb Z}2^{\beta(k+\theta)}e^{-2^{k+\theta}},\qquad
R_\beta(u)=\sum_{k=1}^\infty(2^ku)^\beta e^{-2^ku}.
\]
Under the unitary Bergman--Laplace transform, the trace-form operator is the multiplier
\[
m_\beta(t)=2t\sum_{j=0}^\infty 2^{-\beta j}e^{-2t2^{-j}},\quad
m_\beta(u/2)=u^{1-\beta}\{P_\beta(\log_2u)-R_\beta(u)\}.
\]
The periodic factor has the absolutely convergent expansion
\[
P_\beta(\theta)=\frac1{\log2}\sum_{\ell\in\mathbb Z}
\Gamma\left(\beta-\frac{2\pi i\ell}{\log2}\right)e^{2\pi i\ell\theta}.
\]
It is strictly positive and nonconstant for all \(\beta>0\). Consequently \(m_\beta(t)\) grows without bound along large frequencies when \(0<\beta<1\), has a nonconstant log-periodic high-frequency profile when \(\beta=1\), and tends to zero when \(\beta>1\). All bounded operators in this family are noncompact, have no eigenvalues, and have spectrum the closed interval from zero to their operator norm.

## Assumptions and scope
All line integrals use ordinary one-dimensional Lebesgue measure \(dx\); the Bergman measure is ordinary two-dimensional \(dx\,dy\), with no hidden \(\pi\)-normalization. The line stack consists of precisely the heights \(2^{-j}\), \(j\ge0\), with coefficients \(2^{-\beta j}\). The corresponding positive Borel measure is locally finite in \(\Pi\). The asserted optimal constant, extremal-phase uniqueness, and nonattainment refer to the Hilbert-space norm on the **analytic**, unweighted Bergman space; neither polyanalytic orders nor arbitrary line locations are covered.

## Proof
**1. Exact diagonalization and the boundedness threshold.** The normalized Bergman--Laplace representation is the unitary map
\[
(Ug)(z)=\frac1{\sqrt{2\pi}}\int_0^\infty\sqrt{2t}\,g(t)e^{itz}\,dt,
\qquad U:L^2(0,\infty)\longrightarrow A^2(\Pi).
\]
Initially take \(g\in C_c^\infty(0,\infty)\). Plancherel on horizontal lines yields
\[
\int_{\mathbb R}|Ug(x+iy)|^2dx
=\int_0^\infty2t e^{-2ty}|g(t)|^2dt.
\]
Integrating \(y>0\) confirms the isometry; the analytic Bergman Paley--Wiener representation establishes onto-ness. Tonelli therefore gives \(Q_\beta(Ug)=\int m_\beta(t)|g(t)|^2dt\) on the dense test domain, with the displayed multiplier \(m_\beta\). Its essential supremum is the optimal form constant whenever finite.

**2. Multiplicative periodization.** Put \(u=2t\), and add the missing indices \(j<0\) to the series after extracting \(u^{1-\beta}\). This gives exactly
\(m_\beta(u/2)=u^{1-\beta}(P_\beta(\log_2u)-R_\beta(u))\).
On compact \(\theta\)-intervals both ends of the bilateral series converge geometrically or superexponentially. Its mean-period Fourier coefficient is, by substituting \(s=2^{k+\theta}\),
\[
\int_0^1P_\beta(\theta)e^{-2\pi i\ell\theta}d\theta
=\frac1{\log2}\int_0^\infty s^{\beta-1-2\pi i\ell/\log2}e^{-s}ds
=\frac{\Gamma(\beta-2\pi i\ell/\log2)}{\log2}.
\]
Stirling's bound on vertical lines gives absolute convergence even after any finite number of differentiations. Gamma has no zeros, hence the nonzero first coefficient proves that \(P_\beta\) is nonconstant. It is positive on the compact period and has a positive minimum.

As \(u\to\infty\), the omitted tail obeys \(R_\beta(u)=O_\beta(u^\beta e^{-2u})\); as \(u\downarrow0\), dominated convergence directly gives \(m_\beta(u/2)/u\to(1-2^{-\beta})^{-1}\). Accordingly \(m_\beta\) is bounded exactly when \(\beta\ge1\), diverges for \(0<\beta<1\) because \(P_\beta\) has positive minimum, and decays for \(\beta>1\). At \(\beta=1\), \(m_1(u/2)=P(\log_2u)-R_1(u)<K\) for every finite \(u>0\), while choosing \(u_n=2^{n+\theta_*}\) makes \(m_1(u_n/2)\to K\). This proves the exact sharp norm and its nonattainment by any nonzero \(L^2\) vector, hence by any nonzero Bergman function. Extending the original sum to all \(j\in\mathbb Z\) yields precisely the multiplier \(P(\log_2u)\), so the full two-sided stack has the same norm \(K\) even though its omitted-tail form is strictly positive on every nonzero input. It also shows that \(\limsup_{t\to\infty}m_1(t)=K\) and \(\liminf_{t\to\infty}m_1(t)=\min P\).

**3. Uniqueness of the critical logarithmic phase.** Write \(c_\ell=\Gamma(1-2\pi i\ell/\log2)/(\log2)\) and \(\theta_0=-\arg(c_1)/(2\pi)\) modulo 1. The dominant harmonic is \(c_0+2|c_1|\cos(2\pi(\theta-\theta_0))\). The exact gamma modulus identity gives
\[
\frac{|c_\ell|}{|c_1|}
=\sqrt{\frac{\ell\sinh(2\pi^2/\log2)}{\sinh(2\pi^2\ell/\log2)}}
\le\sqrt\ell\,q^{\ell-1},\qquad
q=e^{-\pi^2/\log2}<10^{-6}\quad(\ell\ge2).
\]
Thus both the normalized first-derivative and second-derivative Fourier tails are bounded by
\[
\sum_{\ell=2}^\infty\ell^2\frac{|c_\ell|}{|c_1|}
\le\sum_{\ell=2}^\infty\ell^3q^{\ell-1}
=\frac{1+4q+q^2}{(1-q)^4}-1<9\cdot10^{-6}<\frac1{\sqrt2}.
\]
Outside the two radius-\(1/8\) arcs about \(\theta_0\) and \(\theta_0+1/2\), the first harmonic has derivative of absolute size at least \(4\pi|c_1|/\sqrt2\), and the tail cannot cancel it. Inside either arc, the first harmonic has second derivative of absolute size at least \(8\pi^2|c_1|/\sqrt2\), so the full derivative is strictly monotone. Its endpoint signs are opposite. Hence exactly one critical point lies in each arc; curvature distinguishes the unique maximum and minimum. Since the mean is \(c_0=1/\log2\) and \(P\) is nonconstant, its maximum strictly exceeds the mean.

**4. Noncompactness and spectrum.** For \(\beta\ge1\), \(m_\beta\) is positive real analytic and nonconstant on \((0,\infty)\), and \(m_\beta(t)\to0\) as \(t\downarrow0\). A nonconstant real-analytic function has measure-zero level sets, so multiplication by \(m_\beta\) has no point eigenvalues. It is noncompact on the nonatomic \(L^2(0,\infty)\) because it is bounded below on some interval of positive measure. Its spectrum, the essential range, is the connected interval \([0,\sup m_\beta]\). This holds even though \(m_\beta(t)\to0\) for \(\beta>1\).

## Verification
The accompanying `verify_dyadic.py` checks direct line-spectrum sums against the exact omitted-tail decomposition and the Mellin Fourier series at multiple points and parameters, verifies a near-optimal geometric-frequency sequence, checks the specified numerical critical phase and norm, and checks the quantitative smallness of higher harmonics. These are supplementary finite numerical checks. The claims about all frequencies, all exponents, uniqueness, and exact optimality are proved analytically above, not inferred from the finite program.

## Relationship to prior work
Rozenblum and Vasilevski (2019, arXiv:1907.06878, Example 4.4) explicitly introduced the same dyadic horizontal lines and gave the sufficient condition \(W(j)=O(2^{-2j})\) in their measure class; they did not supply the sharp critical exponent \(\beta=1\) or the sharp norm for the borderline family. Rozenblum and Vasilevski (2022, arXiv:2203.04170, Section 4) diagonalize vertical-symbol Toeplitz operators and explicitly treat a single horizontal delta line. The present work applies that known spectral viewpoint to the infinite dyadic stack and solves its global critical norm extremal problem. The periodization and gamma-Fourier computation are instances of the classical Mellin harmonic-sum method surveyed by Flajolet, Gourdon and Dumas; those techniques are not claimed as new. The new claim is the exact combination of sharp analytic Bergman embedding, nonattainment, and unique log-frequency norm phase for the motivating line-stack operator.

## Limitations
No assertion of global historical priority is made. Classical Mellin-periodization machinery and known vertical-symbol Toeplitz spectral representations could enable independent rediscovery; an equivalent published sharp dyadic-stack norm formula not located in the inspected literature would subsume the proposed contribution. The numerical decimal figures are illustrative and are not interval-arithmetic certificates. The theorem does not address general irregular weights or nonhorizontal supports, and no independent mathematical audit has been carried out.

## References
1. G. Rozenblum and N. Vasilevski, *Toeplitz operators with singular symbols in polyanalytic Bergman spaces on the half-plane*, arXiv:1907.06878v1 (first publicly posted 2019-07-16), especially Example 4.4. https://arxiv.org/abs/1907.06878
2. G. Rozenblum and N. Vasilevski, *Commutative algebras of Toeplitz operators on the Bergman space revisited: Spectral theorem approach*, arXiv:2203.04170, especially Section 4 and its single-line delta-symbol example. https://arxiv.org/abs/2203.04170
3. P. Flajolet, X. Gourdon and P. Dumas, *Mellin transforms and asymptotics: harmonic sums*, Theoretical Computer Science 144 (1995), 3--58. https://algo.inria.fr/flajolet/Publications/mellin-harm.pdf
