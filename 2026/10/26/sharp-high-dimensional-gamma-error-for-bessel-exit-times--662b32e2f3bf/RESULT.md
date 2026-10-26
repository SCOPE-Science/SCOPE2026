# Sharp high-dimensional Gamma error for Bessel exit times

## Finding

Let \(T_a\) be the first hitting time of radius one for a Bessel process of index \(a-1\) started at zero, with \(a\geq4\); equivalently it is the exit time of standard Brownian motion from the unit ball in integer dimension \(2a\). Let \(G_a\) have the Gamma law with shape \(a+1\) and scale \(1/[2a(a+1)]\), which matches the mean and variance of \(T_a\). Define
\[
\mu_a=\frac1{2a},\quad \sigma_a=\frac1{2a\sqrt{a+1}},\quad
H_2(z)=z^2-1,\quad \varphi(z)=\frac{e^{-z^2/2}}{\sqrt{2\pi}}.
\]
As \(a\to\infty\) through arbitrary real values,
\[
\boxed{\sup_{z\in\mathbb R}\left|
\mathbb P(G_a\leq \mu_a+\sigma_a z)-
\mathbb P(T_a\leq\mu_a+\sigma_a z)-
\frac{a}{3(a+2)\sqrt{a+1}}H_2(z)\varphi(z)
\right|=O(a^{-1}).}
\]
In particular, the sharp Kolmogorov error is
\[
\boxed{d_{\rm K}(\mathcal L(G_a),\mathcal L(T_a))
=\frac{1}{3\sqrt{2\pi a}}+O(a^{-1}),\qquad
\lim_{a\to\infty}\sqrt a\,d_{\rm K}=\frac1{3\sqrt{2\pi}}.}
\]
The signed profile, and not merely a rate, is uniform over the entire real line. Its largest absolute first-order deviation is at the mean; the other stationary points are at standardized locations \(\pm\sqrt3\).

## Assumptions and scope

Take \(a\geq4\), Bessel index \(\nu=a-1\), and the standard Bessel normalization \(d(R_t^2)=2a\,dt+2\sqrt{R_t^2}\,dB_t\), starting with \(R_0=0\). The first hitting time is \(T_a=\inf\{t:R_t=1\}\). The Gamma convention is shape and **scale**, not rate. Brownian motion uses generator \(\frac12\Delta\). Both \(T_a\) and \(G_a\) have mean \(\mu_a\) and standard deviation \(\sigma_a\). The conclusion concerns fixed one-factor Gamma matching with increasing Bessel index; it is **not** convergence of the number of Gamma factors, nor a relative-tail bound.

## Proof

**1. Exact independent-exponential representation and cumulants.** Write \(j_{a-1,k}\) for the positive zeros of the Bessel function \(J_{a-1}\). The classical Kent/Ciesielski–Taylor formula, reproduced as equations (1)–(4) in Clark [1], states
\[
T_a\overset d=\sum_{k\ge1}c_{a,k}E_k,\qquad
c_{a,k}=\frac{2}{j_{a-1,k}^2},\qquad E_k\sim\mathrm{Exp}(1)\ \text{independently},
\]
with Laplace transform \(\mathbb Ee^{-sT_a}=1/{}_0F_1(;a;s/2)\). Expansion of \(\log{}_0F_1(;a;s/2)\) at the origin, or the exact Rayleigh recursion in [1, Proposition 2.3], gives
\[
\kappa_1(T_a)=\frac1{2a},\quad
\kappa_2(T_a)=\frac1{4a^2(a+1)},\quad
\kappa_3(T_a)=\frac1{2a^3(a+1)(a+2)}.
\]
The Gamma variable has the same first two cumulants, and the standardized variables
\[
X_a=(T_a-\mu_a)/\sigma_a,\qquad Y_a=(G_a-\mu_a)/\sigma_a
\]
have third cumulants
\[
\kappa_3(X_a)=\frac{4\sqrt{a+1}}{a+2},\qquad
\kappa_3(Y_a)=\frac2{\sqrt{a+1}},\qquad
\delta_a:=\frac{\kappa_3(Y_a)-\kappa_3(X_a)}6
=-\frac{a}{3(a+2)\sqrt{a+1}}.
\]

**2. Uniform control of every exponential weight, and many nonvanishing weights.** Set
\[
b_{a,k}=c_{a,k}/\sigma_a=\frac{4a\sqrt{a+1}}{j_{a-1,k}^2}.
\]
Then \(\sum_{k\ge1}b_{a,k}^2=1\). In the Schrödinger form of the Bessel Dirichlet eigenproblem, \(j_{a-1,k}^2\) is the \(k\)-th eigenvalue of
\[
-u''(r)+\frac{(a-1)^2-1/4}{r^2}u(r),\quad 0<r<1,
\]
with the Friedrichs condition at zero and Dirichlet condition at one. Its potential is bounded below by \((a-1)^2-1/4\ge a^2/2\) for \(a\ge4\). The min–max principle gives
\[
j_{a-1,k}^2\ge a^2/2\quad(k\ge1).
\]
For \(1\le k\le\lfloor a\rfloor\), take as a trial subspace the first \(k\) Dirichlet sine eigenfunctions on \([1/2,1]\), extended by zero. On this interval the potential is at most \(4(a-1)^2\), and the Dirichlet Laplacian's \(k\)-th eigenvalue is \(4\pi^2 k^2\). Thus
\[
j_{a-1,k}^2\le4\pi^2k^2+4(a-1)^2\le(4\pi^2+4)a^2.
\]
Consequently, for constants independent of \(a\),
\[
0<b_{a,k}\le C a^{-1/2}\quad(k\ge1),\qquad
b_{a,k}\ge c a^{-1/2}\quad(1\le k\le\lfloor a\rfloor).
\]
In particular \(\sum b_{a,k}^4\le (\max b_{a,k})^2\sum b_{a,k}^2=O(a^{-1})\). These estimates establish the essential high-frequency integrability rather than assuming a generic central limit theorem has a sharp uniform error remainder.

**3. Characteristic functions and their uniform Fourier remainder.** For real \(u\), let \(\psi_a(u)=\mathbb Ee^{iuX_a}\), \(\chi_a(u)=\mathbb Ee^{iuY_a}\). They are exactly
\[
\psi_a(u)=\prod_{k\ge1}\frac{e^{-iu b_{a,k}}}{1-iu b_{a,k}},\qquad
\chi_a(u)=e^{-iu\sqrt{a+1}}(1-iu/\sqrt{a+1})^{-(a+1)}.
\]
For \(|u|\le a^{1/16}\), Taylor's formula \(\log(e^{-ix}/(1-ix))=-x^2/2+(ix)^3/3+O(x^4)\) and the bounds in step 2 imply
\[
\log\psi_a(u)=-u^2/2+\frac{\kappa_3(X_a)}6(iu)^3+O(u^4/a),\qquad
\log\chi_a(u)=-u^2/2+\frac{\kappa_3(Y_a)}6(iu)^3+O(u^4/a).
\]
Exponentiation and \(\kappa_3(X_a),\kappa_3(Y_a)=O(a^{-1/2})\) give the **integrable**, pointwise remainder
\[
\left|\chi_a(u)-\psi_a(u)-\delta_a(iu)^3e^{-u^2/2}\right|
\le\frac C a (|u|^4+|u|^6)e^{-u^2/4}.
\]
For the complementary frequencies, \(\log(1+x)\ge x/(1+x)\) implies, with a numerical \(C\),
\[
|\psi_a(u)|\le\exp\left(-\frac{u^2}{2(1+C u^2/a)}\right),\quad
|\chi_a(u)|=(1+u^2/(a+1))^{-(a+1)/2}.
\]
Thus \(a^{1/16}\le|u|\le a\) contributes an exponentially small integral against \(du/|u|\). For \(|u|\ge a\), use the first \(\lfloor a\rfloor\) weights from step 2 to obtain
\[
|\psi_a(u)|\le(1+c^2u^2/a)^{-\lfloor a\rfloor/2},
\]
whose \(du/|u|\) tail is likewise exponentially small; the Gamma characteristic function enjoys the same bound with an exponent \(a+1\). The Gaussian correction is integrable on this range. Combining all three frequency ranges proves
\[
\int_{\mathbb R}\frac{|\chi_a(u)-\psi_a(u)-\delta_a(iu)^3e^{-u^2/2}|}{|u|}\,du=O(a^{-1}).
\]

**4. Inversion and the sharp constant.** The signed difference between the two centered CDFs is the inverse Fourier transform of \((\chi_a-\psi_a)/( -iu)\) (equivalently, integrate the inverse density transform from \(-\infty\)). The absolutely integrable difference from step 3 permits a uniform error bound, at most \((2\pi)^{-1}\) times that integral. The inverse transform of \((iu)^3e^{-u^2/2}\) is \(H_3(z)\varphi(z)\), where \(H_3(z)=z^3-3z\). Since
\[
\int_{-\infty}^zH_3(x)\varphi(x)\,dx=-H_2(z)\varphi(z),
\]
we obtain uniformly in \(z\)
\[
F_{G_a}(\mu_a+\sigma_a z)-F_{T_a}(\mu_a+\sigma_a z)
=-\delta_a H_2(z)\varphi(z)+O(a^{-1}).
\]
The absolute maximum of \(H_2(z)\varphi(z)\) occurs at \(z=0\), where its magnitude is \(1/\sqrt{2\pi}\), while the off-center extrema at \(\pm\sqrt3\) have smaller magnitude. Taking the supremum and using \(-\delta_a=a/[3(a+2)\sqrt{a+1}]=1/(3\sqrt a)+O(a^{-3/2})\) proves both boxed statements.

## Verification

A self-contained `verification.py` independently checks the first three cumulants by formal hypergeometric expansion, the exact third-cumulant mismatch and its sign, the global extremum of the Hermite correction, the underlying Bessel eigenvalue weight inequalities on sample parameters, and the direction and size of the central CDF discrepancy through Laplace inversion at several large dimensions. Run `python verification.py` with the versions in `requirements.txt` or compatible libraries. Numerical tests corroborate finite values; the analytic Fourier estimates in the proof establish the infinite limiting result. The expression of the one-factor Gamma approximant is independently available in [1, Theorem 1.1].

## Relationship to prior work

Clark [1] constructs \(N\)-factor moment-optimal Gamma convolutions for Bessel exit times, establishes optimal first \(2N\) cumulants and a Kolmogorov error bound as **\(N\to\infty\) with Bessel index fixed**. Its explicit \(N=1\) distribution is exactly \(G_a\). The theorem here instead holds \(N=1\) and lets the Bessel index \(a-1\) tend to infinity; it determines a sharp, nonzero Kolmogorov constant and the signed uniform error profile. The first two cumulants and the third-cumulant difference follow from [1], but they alone do not entail a uniform CDF expansion or its sharp constant. Serafin [2] obtains exit-time density asymptotics for Bessel processes at fixed index, with index-dependent control. Deaconu–Herrmann [3] develop hitting-time simulation for noninteger Bessel dimension. Neither supplies this large-index comparison of the one-factor moment-matched Gamma law. General triangular-array Edgeworth theory may provide an alternative route once its hypotheses are verified for the Bessel eigenvalue array; no claim is made that the Fourier argument is the only possible proof.

## Limitations

The implicit \(O(a^{-1})\) bound is uniform in standardized threshold but is not given with an optimized numerical coefficient. This result does not establish relative tail approximation, a simultaneous limit in Gamma-factor count and index, or analogous constants for other domains, starting positions, or moment-matching families. It is a same-source-motivated new parameter regime, not a claim of having discovered the underlying exponential representation or the Gamma matching law. Bibliographic priority needs independent checking for results framed as general triangular-array Edgeworth expansions or high-dimensional exit-time asymptotics.

## References

[1] S. P. Clark, *Moment-optimal Gamma approximation of Bessel Process exit times*, arXiv:2610.19233v1 (first public 13 October 2026), https://arxiv.org/html/2610.19233v1. See Introduction, Theorems 1.1–1.2, Proposition 2.3, and Sections 3–5 and Appendix A.

[2] G. Serafin, *Exit times densities of Bessel process*, arXiv:1505.07551 (2015), https://arxiv.org/abs/1505.07551. See Introduction, density estimates, and Section 4.

[3] M. Deaconu and S. Herrmann, *Simulation of hitting times for Bessel processes with non integer dimension*, arXiv:1401.4843v1 (2014), https://arxiv.org/html/1401.4843v1. See Introduction and Sections 6–7.
