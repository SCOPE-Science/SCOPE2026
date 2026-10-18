# A single-hump time-arrow profile and a golden-ratio lag for two common-driven Gaussian probes

## Finding
Consider two stationary Gaussian probes driven by one independent Ornstein–Uhlenbeck latent source. Their signed time-reversal cross-covariance has one fixed sign for **every** positive lag and its absolute value has **exactly one** positive-lag maximizer whenever the probe relaxation rates differ. The best lag depends only on the three relaxation rates, not on the probe thermal noises or the coupling amplitudes. In a triple-rate coalescence limit, the maximizing lag, rescaled by the common damping, converges to the golden ratio.

More precisely, with the normalization given below, define for positive rates \(a,d,b\) and \(t\geq0\)
\[
 F_{a,d,b}(t)=\frac{2}{\pi}\int_0^\infty\frac{\omega\sin(\omega t)}{(\omega^2+a^2)(\omega^2+d^2)(\omega^2+b^2)}\,d\omega.
\]
For \(t>0\), this kernel is strictly positive, tends to zero as \(t\to\infty\), and has a single, strict global maximum at a finite \(t_*(a,d,b)>0\). The maximum is nondegenerate; in particular, its derivative has exactly one positive zero.

For the probes described below, let \(\Delta(t)=\mathbb E[X_1(s+t)X_2(s)]-\mathbb E[X_2(s+t)X_1(s)]\), which is independent of \(s\). Then, for all \(t\geq0\),
\[
 \boxed{\Delta(t)=2D_f c_1c_2(d-a)F_{a,d,b}(t).}
\]
For \(c_1c_2\ne0\), the stationary two-probe process is time-reversible if and only if \(a=d\); otherwise the direction of the lag asymmetry does not reverse and its absolute magnitude is maximized at the single lag \(t_*\). At the origin,
\[
 \boxed{\Delta'(0+)=\frac{2D_f c_1c_2(d-a)}{(a+d)(a+b)(d+b)}.}
\]
All of these statements are valid even when two or three relaxation rates coincide.

Let \(\varphi=(1+\sqrt5)/2\). As \((a,d,b)\to(\kappa,\kappa,\kappa)\) with \(\kappa>0\),
\[
 \boxed{\kappa\,t_*(a,d,b)\longrightarrow\varphi.}
\]
At exact triple equality the normalized kernel has the explicit profile
\[
 \boxed{F_{\kappa,\kappa,\kappa}(t)=\frac{e^{-\kappa t}(\kappa t)(1+\kappa t)}{8\kappa^4},}
\]
whose unique maximum is at \(t=\varphi/\kappa\). This is a *first-order mismatch sensitivity*: for exactly equal probe rates the physical asymmetry \(\Delta\) is identically zero, so no nonzero optimal irreversibility signal is asserted there.

## Assumptions and scope
For real nonzero couplings \(c_1,c_2\), positive damping rates \(a,d,b>0\) and strictly positive independent diffusion coefficients \(D_1,D_2,D_f\), let the three-dimensional stationary process solve
\[
\begin{aligned}
 dX_1&=(-aX_1+c_1F)\,dt+\sqrt{2D_1}\,dW_1,\\
 dX_2&=(-dX_2+c_2F)\,dt+\sqrt{2D_2}\,dW_2,\\
 dF&=-bF\,dt+\sqrt{2D_f}\,dW_f,
\end{aligned}
\]
with mutually independent standard Brownian motions. The drift has strictly negative eigenvalues, hence a unique centered stationary Gaussian state. Both probe positions are observed without further filtering. The probe noises are independent of each other and of the latent noise. The observation is the stationary two-component process, not the three-component Markov process.

The kernel \(F_{a,d,b}\) has units of inverse damping to the fourth power, and the asymmetry formula includes the source diffusion normalization \(2D_f\). The lag \(t\) is physical time, not discrete sample number. The statement on a preferred sampling lag means maximizing the *population absolute cross-covariance difference*, not maximizing statistical power with finitely many noisy samples.

## Proof
**1. Spectral representation and all-time identity.** The independent stationary source has two-sided power spectrum \(2D_f/(b^2+\omega^2)\). The transfer functions of the two probes are \(c_1/(a+i\omega)\) and \(c_2/(d+i\omega)\). For the convention in which \(C_{12}(t)=\mathbb E[X_1(s+t)X_2(s)]\), the cross spectrum is
\[
 S_{12}(\omega)=\frac{2D_fc_1c_2}{(b^2+\omega^2)(a+i\omega)(d-i\omega)}.
\]
The two independent probe noises contribute no cross spectrum. Subtracting \(S_{21}(\omega)=\overline{S_{12}(\omega)}\) and Fourier inverting gives
\[
 \Delta(t)=\frac{4D_fc_1c_2(d-a)}{\pi}\int_0^\infty
 \frac{\omega\sin(\omega t)}{(\omega^2+a^2)(\omega^2+d^2)(\omega^2+b^2)}\,d\omega,
\]
which is the claimed formula and remains valid without distinctness assumptions.

**2. Strict positivity.** Put \(\ell_r(t)=e^{-r|t|}/(2r)\) for every \(r>0\), and \(G=\ell_a*\ell_d*\ell_b\) on the real line. By Fourier inversion,
\[
 G(t)=\frac1{2\pi}\int_{-\infty}^{\infty}\frac{e^{i\omega t}}{(\omega^2+a^2)(\omega^2+d^2)(\omega^2+b^2)}\,d\omega,
 \qquad F_{a,d,b}(t)=-2G'(t)\quad(t>0).
\]
Each \(\ell_r\) is positive, even and strictly decreasing away from zero. To check strictness under convolution, let \(h\) be an even absolutely continuous function with \(h'(s)<0\) for \(s>0\). For \(t>0\),
\[
 (\ell_r*h)'(t)=\int_0^\infty h'(s)\{\ell_r(t-s)-\ell_r(t+s)\}\,ds<0,
\]
since \(|t-s|<t+s\). Apply this argument successively to the exponential kernels (with the derivative interpreted almost everywhere at the cusp). Consequently \(G'(t)<0\) for every \(t>0\), so \(F_{a,d,b}(t)>0\). Fourier integrability also gives \(F(0)=0\), continuity and decay to zero at infinity. Differentiating at the origin, or evaluating a rational spectral integral, yields
\[
 F'_{a,d,b}(0+)=\frac1{(a+d)(a+b)(d+b)}>0.
\]
This also yields the small-lag formula for \(\Delta\).

**3. Uniqueness of the preferred lag.** When \(a,d,b\) are distinct, partial fractions give the explicit entire positive-lag profile
\[
 F_{a,d,b}(t)=\sum_{r\in\{a,d,b\}}
 \frac{e^{-rt}}{\prod_{s\in\{a,d,b\}\setminus\{r\}}(s^2-r^2)},\qquad t>0.
\]
For repeated rates the continuous limits of this formula give exponential polynomials, in which the sum of the multiplicities of distinct exponential rates is still three. Therefore \(F'\) belongs to a three-dimensional exponential-polynomial Chebyshev space. A direct generalized Rolle argument shows that any nonzero function in that space has at most two real zeros counted with multiplicity: multiply by the exponential of the slowest rate, differentiate (reducing the total polynomial multiplicity by one), and apply Rolle inductively. This also applies to repeated rates because polynomial factors arise through confluent limits and the differentiation argument remains valid.

As \(F'(0+)>0\), while \(F(t)>0\) and \(F(t)\to0\), its derivative must become negative; indeed the slowest exponential term with nonzero polynomial coefficient is eventually positive and decreasing. Thus a positive zero of \(F'\) exists and changes sign from positive to negative. Two sign-changing zeros would force at least three zeros to end with negative sign; any additional tangent zero would count with multiplicity at least two and also violate the two-zero bound. Hence there is **exactly one** positive zero, it is simple, and it is the unique strict global maximum.

**4. Gaussian time-reversal criterion.** A centered stationary Gaussian vector process is reversible exactly when every covariance matrix at lag \(t\) is symmetric. The two diagonal covariances are automatically even in time, and the only potentially asymmetric pair is \(C_{12}(t),C_{21}(t)\). The identity in step 1, together with strict positivity in step 2, says that these agree at every lag if and only if \(c_1c_2(d-a)=0\). Under the nonzero-coupling hypothesis this is equivalent to \(a=d\). The full three-dimensional process can still dissipate when the observed pair is reversible; no equivalence of observed and full entropy production is asserted.

**5. Triple coalescence.** Fourier inversion or repeated-pole residues give
\[
 G_{\kappa,\kappa,\kappa}(t)=\frac{e^{-\kappa |t|}}{16\kappa^5}
 \bigl((\kappa |t|)^2+3\kappa |t|+3\bigr).
\]
Taking \(-2G'\) gives the displayed kernel. Its derivative on \(t>0\) has the sign of \(1+z-z^2\), with \(z=\kappa t\), hence the unique maximizer is \(z=\varphi\). The defining spectral integral is jointly smooth in positive \(a,d,b\) and \(t>0\), and this stationary point is simple. The implicit function theorem, together with the proved global uniqueness, therefore yields continuous convergence of the unique maximizing lag as all three rates approach \(\kappa\).

## Verification
Run `python verification.py` with NumPy and SciPy. The standalone check constructs an independently defined drift matrix and stationary covariance using the continuous-time Lyapunov equation, computes exact-lag covariance via a matrix exponential, and compares it against the oscillatory-integral formula, including coincident rates and signed couplings. It also compares distinct-rate partial fractions, checks numerical positivity and the shape over bounded grids, and tests the triple-rate golden-ratio formula. The shipped program passed 459 finite assertions. These are reproducibility checks and are not a proof of the universal sign, uniqueness or limit; those are established above.

## Relationship to prior work
Bi and Calhoun (2026) establish the channel-separable cross-spectral structure, exact coherence witness, and positive full-system entropy production of the same one-way coupled Ornstein–Uhlenbeck benchmark. Their full joint spectrum (especially their Sec. II and Appendix K) already *implies* the frequency-domain cross-spectrum used in step 1; neither that model nor the spectral factorization is claimed to be new. The new mathematical content assessed here is the **global single-hump theorem** for the time-domain antisymmetric cross-covariance, its unique noise-independent optimizing lag for arbitrary positive and coincident rates, and its exact golden-ratio triple-coalescence limit.

Godrèche and Luck (2018) derive general matrix formulas for stationary Ornstein–Uhlenbeck correlations and entropy production. These formulas likewise allow computation of the cross-covariance for a specified drift, but they do not in themselves give the fixed-sign single-hump characterization of the three-rate scalar kernel. Lucente and coauthors (2022) study observational loss of irreversibility, while Ohga, Ito and Kolchinsky (2023) prove general bounds on cross-correlation asymmetry; these motivate the diagnostic meaning of the observable without specifying this three-rate optimization. Standard exponential-polynomial zero-counting is used in the proof and is not independently claimed as a new lemma.

## Limitations
The result requires a single autonomous Ornstein–Uhlenbeck hidden driver with independent Gaussian probe noise, linear one-way couplings and positive relaxation rates. Additional latent modes or oscillatory/colored forcing can create different lag shapes and are outside the theorem. A nonzero coherence witness need not mean the two-probe observed path law is irreversible: exactly matched probe dampings make it reversible even though the full system can dissipate. The model-specific full cross spectrum is prior work, and broader filter-response mathematics might implicitly cover the optimizing-lag phenomenon; an independent originality assessment has not been performed. Population-optimal lag is not asserted to be statistically optimal under finite-sample uncertainty. No inference of unknown parameters from sampled data is proved.

## References
1. Y. Bi and V. D. Calhoun, *Cross-Spectral Witness for Hidden Nonequilibrium Beyond the Scalar Ceiling*, arXiv:2604.03775v3 (initial public posting 2026-04-04), especially Secs. II–IV and Appendix K. https://arxiv.org/html/2604.03775
2. C. Godrèche and J.-M. Luck, *Characterising the nonequilibrium stationary states of Ornstein–Uhlenbeck processes*, arXiv:1807.00694 (2018), especially Sec. 2.6. https://arxiv.org/abs/1807.00694
3. D. Lucente, A. Baldassarri, A. Puglisi, A. Vulpiani, and M. Viale, *Inference of time irreversibility from incomplete information: Linear systems and its pitfalls*, Physical Review Research 4, 043103 (2022), DOI:10.1103/PhysRevResearch.4.043103.
4. N. Ohga, S. Ito, and A. Kolchinsky, *Thermodynamic Bound on the Asymmetry of Cross-Correlations*, Physical Review Letters 131, 077101 (2023), DOI:10.1103/PhysRevLett.131.077101.
