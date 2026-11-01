# Exact rank-two Gaussian localization curvature at a disk

## Finding

Let \(t>0\) and let \(h:\mathbb R/(2\pi\mathbb Z)\to\mathbb R\) be a mean-zero \(C^3\) function. For sufficiently small real \(\varepsilon\), define the star-shaped domain
\[
\Omega_\varepsilon=\{re^{i\theta}:0\le r^2<t+\varepsilon h(\theta)\}.
\]
Its Euclidean area is exactly \(\pi t\) for every admissible \(\varepsilon\). Let \(T_\varepsilon\) denote analytic Bargmann–Fock localization with symbol \(\mathbf1_{\Omega_\varepsilon}\), and let \(L_2(\varepsilon)\) be the sum of its two largest eigenvalues (counted with multiplicity). Write
\[
\widehat h_k=\frac1{2\pi}\int_0^{2\pi}h(\theta)e^{-ik\theta}\,d\theta,
\qquad a_j(t)=\frac{t^j}{j!}.
\]
For each integer \(k\ge2\), put
\[
D_k(t)=t-\frac{a_k(t)}{\sum_{j=1}^{k}a_j(t)}-
\frac{t\,a_{k+1}(t)}{\sum_{j=2}^{k+1}a_j(t)}.
\]
**Theorem (exact rank-two shape Hessian).** For every fixed \(t>0\) and every real mean-zero \(h\in C^3\),
\[
\boxed{L_2(\varepsilon)=2-e^{-t}(2+t)-\varepsilon^2e^{-t}
\sum_{k=2}^{\infty}D_k(t)|\widehat h_k|^2
+O_{t,h}(|\varepsilon|^3).}
\]
The coefficients satisfy \(0<D_2(t)<D_3(t)<\cdots<t\), with
\[
\boxed{D_2(t)=\frac{t(3+2t)}{(t+2)(t+3)},\qquad
\lim_{k\to\infty}D_k(t)=t.}
\]
Consequently the exact sharp transverse quadratic deficit obeys
\[
\lim_{\varepsilon\to0}\frac{L_2(0)-L_2(\varepsilon)}{\varepsilon^2}
\ge e^{-t}\frac{t(3+2t)}{(t+2)(t+3)}
\sum_{k=2}^{\infty}|\widehat h_k|^2.
\]
Equality in this quadratic bound holds exactly when every Fourier coefficient of \(h\) of absolute order at least three vanishes; the first angular harmonic is a null direction (infinitesimal translation). A nonzero second harmonic attains the sharp positive transverse curvature. The theorem is a local statement along each fixed deformation, **not** a global isoperimetric inequality for all sets.

## Assumptions and scope

The analytic Fock Hilbert space is
\[
\mathcal F^2=\left\{f\text{ entire}:\|f\|^2=\frac1\pi\int_{\mathbb C}|f(z)|^2e^{-|z|^2}\,dA(z)<\infty\right\}.
\]
The Toeplitz localization operator is specified by
\[
\langle T_\varepsilon f,g\rangle=\frac1\pi\int_{\Omega_\varepsilon}f(z)\overline{g(z)}e^{-|z|^2}\,dA(z).
\]
It is positive trace class with \(\operatorname{Tr}T_\varepsilon=|\Omega_\varepsilon|/\pi=t\). For fixed \(t,h\), choose \(|\varepsilon|\|h\|_\infty<t\) so that each squared radial bound is strictly positive. The expansion is for \(\varepsilon\to0\), keeping \(t\) and \(h\) fixed; no uniformity in high Fourier frequency or large \(t\) is asserted. The orthonormal basis is \(e_n(z)=z^n/\sqrt{n!}\), indexed from \(n=0\). Fourier coefficients use the specified normalization, so a cosine \(h=\cos(k\theta)\) has \(|\widehat h_k|^2=1/4\) for \(k\ge1\).

## Proof

**1. Disk spectrum and spectral gap.** Polar integration gives the exact matrix elements
\[
\langle T_\varepsilon e_n,e_m\rangle=\frac1{2\pi\sqrt{m!n!}}
\int_0^{2\pi} e^{i(n-m)\theta}
\int_0^{t+\varepsilon h(\theta)}e^{-s}s^{(m+n)/2}\,ds\,d\theta.
\]
At \(\varepsilon=0\) this is diagonal, with strictly decreasing eigenvalues
\[
\lambda_n(t)=\frac1{n!}\int_0^t e^{-s}s^n\,ds
=1-e^{-t}\sum_{j=0}^n\frac{t^j}{j!},
\qquad\lambda_n-\lambda_{n+1}=e^{-t}a_{n+1}(t)>0.
\]
The top two eigenvectors are \(e_0,e_1\), and their sum is \(L_2(0)=2-e^{-t}(2+t)\). The occupied pair is separated from its complement by \(\lambda_1-\lambda_2=e^{-t}t^2/2>0\).

**2. Trace-norm differentiability.** The integrand in the matrix formula is a coherent-state rank-one projector density in the Hilbert space, analytic as a trace-class-valued function of the positive squared radius \(s\) near \(t>0\). On the compact angular circle, \(t+\varepsilon h(\theta)\) stays in a fixed positive compact interval. Differentiating the upper integration limit thus yields a genuine third-order Taylor remainder in trace norm for \(T_\varepsilon\). In particular, with \(P\) the projection onto \(\operatorname{span}\{e_0,e_1\}\), the isolated two-dimensional spectral cluster and its spectral sum have third-order perturbation expansions.

The first operator derivative has matrix elements
\[
\langle T'_0 e_n,e_m\rangle=e^{-t}\sqrt{a_m(t)a_n(t)}\,\widehat h_{m-n}.
\]
Its two occupied diagonal entries vanish because \(\widehat h_0=0\), so \(L_2'(0)=0\). The sum of second-order *direct* contributions (the coefficient of \(\varepsilon^2\), not the second derivative) is
\[
\operatorname{Tr}\bigl(P T''_0P/2\bigr)
=\frac{e^{-t}}2\bigl[-1+(1-t)\bigr]
\frac1{2\pi}\int_0^{2\pi}h(\theta)^2\,d\theta
=-te^{-t}\sum_{k\ge1}|\widehat h_k|^2.
\]
The last equality uses Parseval and reality of \(h\).

**3. Exact cross-cluster correction.** The standard isolated-cluster Rayleigh–Schrödinger identity gives the second-order coefficient of \(L_2\) as
\[
\operatorname{Tr}(PT''_0P/2)
+\sum_{n=0}^{1}\sum_{m=2}^{\infty}
\frac{|\langle T'_0e_n,e_m\rangle|^2}{\lambda_n-\lambda_m}.
\]
Mixing *within* the occupied two-plane cancels when its eigenvalues are summed. For \(m\ge2\), exact gaps are
\[
\lambda_0-\lambda_m=e^{-t}\sum_{j=1}^{m}a_j(t),\qquad
\lambda_1-\lambda_m=e^{-t}\sum_{j=2}^{m}a_j(t).
\]
Hence the cross-cluster term becomes
\[
e^{-t}\left[t|\widehat h_1|^2+
\sum_{k\ge2}\left(\frac{a_k(t)}{\sum_{j=1}^k a_j(t)}
+\frac{t a_{k+1}(t)}{\sum_{j=2}^{k+1}a_j(t)}\right)|\widehat h_k|^2\right].
\]
The \(k=1\) term comes solely from \(e_1\) mixing with \(e_2\). It cancels the direct contribution at the first harmonic. Combining all terms proves the boxed expansion. The interchange of infinite sums follows from the trace-norm Taylor estimate and, directly here, the upper bound on all displayed nonnegative cross terms together with Parseval.

**4. Strict ordering and sharpness.** For fixed integer \(n\ge0\) and \(m>n\), define
\[
R_{n,m}(t)=\frac{a_m(t)}{\sum_{j=n+1}^{m}a_j(t)}
=\left(\sum_{\ell=0}^{m-n-1}\frac{m!}{(m-\ell)!\,t^\ell}\right)^{-1}.
\]
As \(m\) increases the denominator increases strictly: all old terms are nondecreasing and at least one is strictly larger, and a new positive summand is added. Thus \(R_{n,m}(t)\) strictly decreases with \(m\). Both \(R_{0,k}\) and \(R_{1,k+1}\) decrease strictly in \(k\). Consequently \(D_k=t-R_{0,k}-tR_{1,k+1}\) strictly increases for \(k\ge2\). The exact \(k=2\) substitution gives
\[
D_2=t-\frac{t}{t+2}-\frac{t^2}{t+3}
=\frac{t(3+2t)}{(t+2)(t+3)}>0.
\]
Both ratios tend to zero, by their reciprocal sums, so \(D_k\uparrow t\). Positivity and sharpness of the quadratic bound follow coefficientwise; equality is characterized by the strict inequalities for \(k\ge3\). The free \(k=1\) modes agree with the translation invariance of localization spectra.

## Verification

The included `check_two_mode.py` constructs independently the finite-section matrix from numerical lower incomplete-gamma radial integrals and angular quadrature. It computes the top two eigenvalues at \(\varepsilon=0,\pm0.0125\), and compares central second differences against the closed Fourier coefficients at \(t=0.5,1,3\) for angular frequencies \(k=1,2,3,5\), plus a mixed two-frequency deformation. It also checks the exact \(D_2\) identity and a finite monotonicity sample. **Twenty-four deterministic assertions passed**. This is corroborating finite-section evidence, not proof of the infinite-dimensional or all-frequency claims; those follow from the analytical derivation above.

For exact replication: install Python, NumPy and SciPy; execute `python check_two_mode.py`. The checker uses 13 basis vectors and 512 equally spaced angular quadrature nodes, with numerical error tolerances specified in the script. No external network data are needed.

## Relationship to prior work

Abreu–Pereira–Romero (2017, arXiv:1704.02266) analyze accumulated spectrograms, leading localization eigenfunctions, and partial sums of localization eigenvalues. Their Sections 1–2 identify the Gaussian-disk Hermite eigenfunctions and eigenvalue formulas; they do not derive the nonradial rank-two shape Hessian here. This is the motivating steady-development source with first public date **2017-04-07**.

Gómez–Guerra–Ramos–Tilli (2023, arXiv:2307.09304) establish quantitative Faber–Krahn stability for the **largest single** Gaussian localization eigenvalue and its eigenfunction, not the two-eigenvalue Ky-Fan sum. Nicola–Riccardi–Tilli (2025, arXiv:2503.07069) prove the disk optimal for sums of the top \(K\) Fock Toeplitz eigenvalues among **circularly symmetric** sets, and explicitly leave the nonradial statement open in the introductory discussion of their Theorems 1.5–1.6. Their eigenvalue formulas do not imply the present nonradial Hessian. Nicola–Riccardi–Tilli (2026, arXiv:2607.20965) establish existence of globally optimal sets without identifying them for \(K>1\). The current result solves the second-order **local** \(K=2\) disk test, not either global conjecture. A prior spherical coherent-state **rank-one** shape variation has a Bargmann–Fock limiting Hessian, but it does not concern the rank-two sum or its cross-cluster coefficient. Historical priority remains subject to external independent confirmation.

## Limitations

Only fixed smooth mean-zero radial-squared deformations are covered. The result proves strict *second-order* local maximality modulo translations, not global maximality over arbitrary measurable nonradial shapes; it does not assert a uniform neighborhood over all \(C^3\) perturbations. The first harmonic is flat through second order and is not claimed to give exact translations along the literal radial-squared path. No higher eigenvalue-sum index, quantitative global Fraenkel-asymmetry bound, or stability uniform in the disk area is established. Numerical checks truncate the operator and do not constitute independent validation. Historical novelty remains provisional pending specialist literature review.

## References

1. L. D. Abreu, J. Pereira, J. L. Romero, *Sharp rates of convergence for accumulated spectrograms*, arXiv:1704.02266v1 (first public 2017-04-07), https://arxiv.org/html/1704.02266v1 .
2. J. Gómez, A. Guerra, J. P. G. Ramos, P. Tilli, *Stability of the Faber–Krahn inequality for the Short-time Fourier Transform*, arXiv:2307.09304v1 (2023-07-18), https://arxiv.org/html/2307.09304v1 .
3. F. Nicola, F. Riccardi, P. Tilli, *The isoperimetric inequality for partial sums of Toeplitz eigenvalues in the Fock space*, arXiv:2503.07069v2 (v1 first public 2025-03-10), https://arxiv.org/html/2503.07069v2 .
4. F. Nicola, F. Riccardi, P. Tilli, *On the existence of extremizers for the sum of eigenvalues of Toeplitz operators*, arXiv:2607.20965v1 (2026-07-23), https://arxiv.org/html/2607.20965v1 .
