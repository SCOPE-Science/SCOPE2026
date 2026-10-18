# Renewal-arrival moments and positive aging correlations in a discrete fractional Poisson process

## Finding
Let \(0<q<1\), \(0<\lambda<1\), and let \(T_1,T_2,\ldots\) be independent positive-integer waiting times with probability generating function
\[
G(z)=\mathbb E z^{T_1}=\frac{\lambda z}{\lambda+(1-z)^q}.
\]
Put \(S_0=0\), \(S_k=\sum_{j=1}^kT_j\), \(I_n=\mathbf1_{\{n=S_k\text{ for some }k\ge1\}}\), and \(u_n=\mathbb P(I_n=1)\) for \(n\ge1\), with \(u_0=1\).

Define, for \(x>0\),
\[
w_{q,\lambda}(x)=\frac{\lambda\sin(\pi q)}{\pi}\,
\frac{x^{-q}}{1-2\lambda x^{1-q}\cos(\pi q)+\lambda^2x^{2(1-q)}}.
\]
Then \(w_{q,\lambda}\) is a strictly positive probability density on \((0,\infty)\), and for **every integer** \(n\ge0\),
\[
\boxed{u_n=\int_0^\infty(1+x)^{-n}w_{q,\lambda}(x)\,dx.}
\]
Hence the renewal mass sequence is strictly completely monotone: for all integers \(n\ge0\) and \(k\ge1\),
\[
\boxed{(-1)^k\Delta^k u_n>0.}
\]
For integers \(t,h\ge1\), the arrival indicators satisfy the exact strictly positive covariance identity
\[
\boxed{\operatorname{Cov}(I_t,I_{t+h})=u_t(u_h-u_{t+h})>0.}
\]
Moreover,
\[
u_n\sim\frac{\lambda}{\Gamma(q)}n^{q-1},\qquad
\boxed{\lim_{t\to\infty}\operatorname{Corr}(I_t,I_{t+h})=u_h}\quad(h\ge1),
\]
and \(\sum_{h\ge1}u_h=\infty\). Thus the nonstationary arrival process has a **strictly positive, nonsummable limiting aging-correlation profile**. This is not an assertion that the arrival indicators are stationary. At the boundary \(q=1\), the waiting time becomes geometric and the arrival indicators at distinct positive integers are independent, so all their covariances vanish.

## Assumptions and scope
The parameter restrictions and probability space are as stated above. Each interarrival time is a positive integer; \(I_n\) indicates an arrival *exactly* at positive integer time \(n\). The initial renewal at time zero is excluded from \(I_n\) but gives \(u_0=1\) by convention. The covariance and correlation formulas concern distinct positive times; the limiting correlation fixes the positive lag before sending the observation time to infinity. The law with \(0<\lambda<1\) is the renewal model considered in [1].

## Proof
The renewal equation gives the formal power-series identity
\[
\sum_{n\ge1}u_n z^n=\frac{G(z)}{1-G(z)}
=\frac{\lambda z}{(1-z)^q+\lambda(1-z)}.
\]
Set \(F(s)=\lambda/(s^q+\lambda s)\), taking the principal fractional power on the plane slit along the nonpositive real axis. Then the generating function above is \(zF(1-z)\). For \(0<q<1\), \(F\) is analytic on the slit plane and has decay \(O(|s|^{-1})\) at infinity and growth \(O(|s|^{-q})\) at the origin in sectors bounded away from the cut. The small and large circular contributions therefore vanish in the Cauchy keyhole contour calculation. Its jump across the negative real axis is
\[
-\frac1\pi\operatorname{Im}F(-x+i0)
=\frac{\lambda\sin(\pi q)}\pi
\frac{x^{-q}}{1-2\lambda x^{1-q}\cos(\pi q)+\lambda^2x^{2(1-q)}}=w_{q,\lambda}(x).
\]
The denominator is \((\lambda x^{1-q}-\cos(\pi q))^2+\sin^2(\pi q)>0\), so the density is strictly positive. Cauchy's formula yields the Stieltjes representation
\[
F(s)=\int_0^\infty\frac{w_{q,\lambda}(x)}{s+x}\,dx\qquad(s>0).
\]
As \(s\to\infty\), \(sF(s)\to1\). Monotone convergence applied to \(s/(s+x)\) shows that \(\int w_{q,\lambda}=1\), including the absence of missing atoms in the representation.

For \(|z|<1\), expand \((1+x-z)^{-1}\) geometrically and use positivity to interchange sum and integral. Thus \(zF(1-z)=\sum_{n\ge1}z^n\int(1+x)^{-n}w(x)\,dx\). Coefficient comparison proves the integral formula for positive \(n\); normalization gives \(n=0\). The \(k\)-th forward finite difference of \((1+x)^{-n}\) is \((-1)^k(1+x)^{-n}[x/(1+x)]^k\), strictly signed for all \(x>0\), proving complete monotonicity.

By independent post-renewal increments, for \(t,h\ge1\),
\[
\mathbb E(I_tI_{t+h})=\mathbb P(I_t=1)\mathbb P(I_h=1)=u_tu_h.
\]
Subtracting \(u_tu_{t+h}\) gives the covariance formula; strict positivity follows from strict decrease of \(u_n\).

At the origin \(w(x)\sim\lambda\sin(\pi q)x^{-q}/\pi\). The integral formula and a standard Laplace scaling \(x=y/n\), with domination using the integrable tail of \(w\), imply
\[
u_n\sim\frac{\lambda\sin(\pi q)}\pi\Gamma(1-q)n^{q-1}
=\frac\lambda{\Gamma(q)}n^{q-1}.
\]
For fixed \(h\), \(u_t\to0\) and \(u_{t+h}/u_t\to1\). Consequently
\[
\operatorname{Corr}(I_t,I_{t+h})=
\frac{u_t(u_h-u_{t+h})}{\sqrt{u_t(1-u_t)u_{t+h}(1-u_{t+h})}}
\longrightarrow u_h.
\]
The harmonic power exponent \(q-1\in(-1,0)\) makes the sum of \(u_h\) diverge. If \(q=1\), the waiting PGF is that of a geometric law with success probability \(\lambda/(1+\lambda)\). The renewal indicators are then independent Bernoulli trials on the positive integers.

## Verification
Run `python verification.py` with Python 3 and `mpmath`. The program computes renewal coefficients recursively from their generating function and independently integrates the Stieltjes density after removing its endpoint singularity. It verifies the first eight coefficients across four parameter pairs, selected positive finite differences, and the exact regeneration covariance expression, giving 436 finite checks. The script does not certify the infinite-dimensional results: analyticity, contour deformation, coefficient comparison, and the asymptotic argument establish those.

## Relationship to prior work
[1] defines the discrete renewal model, proves the interarrival generating function, and identifies investigating its autocorrelation structure as a future direction. Its count-distribution formulas do not state a positive spectral mixing law for the renewal-epoch indicators or their aging-correlation limit. [2] studies two discrete fractional Bernoulli renewal constructions and correlations of *inverse Sibuya counts* and subordinated walks. Those are distinct observables from the arrival indicators here. [3] establishes general complete-monotonicity results for discrete fractional Volterra equations and related waiting distributions; this supplies a nearby method and possible implicit general coverage but does not explicitly identify the displayed renewal-epoch Stieltjes density and subsequent covariance/aging profile. General renewal-regeneration identities are classical [4], and are used here rather than claimed as new on their own. The combined model-specific spectral law and nonstationary correlation consequence are the contribution.

## Limitations
The result concerns renewal arrival indicators, **not** the covariance of the accumulated counting process or stationary long-range dependence in the usual spectral-density sense. The parameter range \(0<\lambda<1\) follows the source model. The finite verifier cannot prove contour deformation or infinite asymptotics. Complete uniqueness relative to differently formulated earlier discrete-renewal results is not certified; related general complete-monotonicity theory could imply parts of the spectral law. No independent assessment has been performed.

## References
[1] N. Yoshida, *An alternative formulation of the discrete-time fractional Poisson process* (2026), arXiv:2605.03664, https://arxiv.org/html/2605.03664v1.

[2] A. Pachon, F. Polito and C. Ricciuti, *On discrete-time semi-Markov processes* (2020), https://pure.southwales.ac.uk/ws/files/4229033/1531_3492_2017_11_631_4_.pdf.

[3] R. A. C. Ferreira, *Complete monotonicity of discrete equations and related results*, https://www.cmup.pt/sites/default/files/2025-03/CM_Discrete_M_L_Function.pdf.

[4] R. G. Gallager, *Discrete Stochastic Processes*, Chapter 4: Renewal Processes, MIT OpenCourseWare, https://ocw.mit.edu/courses/6-262-discrete-stochastic-processes-spring-2011/931ffa0940899c27f34b71ad64fd2bb0_MIT6_262S11_chap04.pdf.
