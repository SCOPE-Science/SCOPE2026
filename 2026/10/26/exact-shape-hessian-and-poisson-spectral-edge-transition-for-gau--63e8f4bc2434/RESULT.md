# Exact shape Hessian and Poisson spectral-edge transition for Gaussian time–frequency localization

## Finding

Consider the Bargmann–Fock localization operator on a Euclidean-area-preserving perturbation of a disk. Its **optimized largest eigenvalue** has a completely explicit angular Fourier Hessian, with a sharp transverse spectral gap, and the Hessian coefficients exhibit a Poisson-to-Gaussian transition as the disk area grows.

Fix \(s>0\) and a real-valued \(2\pi\)-periodic \(h\in C^2(\mathbb T)\) satisfying \(\widehat h_0=0\), with Fourier coefficients
\[
\widehat h_n=\frac{1}{2\pi}\int_0^{2\pi}h(\theta)e^{-in\theta}\,d\theta.
\]
For small real \(\varepsilon\), let
\[
\Omega_\varepsilon=\{r e^{i\theta}:0\le r^2<s+\varepsilon h(\theta)\}.
\]
Its Euclidean area is exactly \(\pi s\) at every admissible \(\varepsilon\). In the Gaussian Bargmann–Fock Hilbert space
\[
\mathcal F^2=\Big\{F\text{ entire}:\|F\|^2=\frac1\pi\int_{\mathbb C}|F(z)|^2e^{-|z|^2}\,dA(z)<\infty\Big\},
\]
set \(T_\varepsilon=P_{\mathcal F^2}\mathbf1_{\Omega_\varepsilon}\) (the associated nonnegative localization operator), and \(\Lambda(\varepsilon)=\|T_\varepsilon\|\). Define, for each integer \(n\ge1\),
\[
a_n(s)=\frac{s^n}{n!},\qquad A_n(s)=\sum_{j=1}^n\frac{s^j}{j!},\qquad d_n(s)=1-\frac{a_n(s)}{A_n(s)}.
\]
Then
\[
\boxed{\Lambda(\varepsilon)=1-e^{-s}-\varepsilon^2e^{-s}\sum_{n=2}^{\infty}d_n(s)|\widehat h_n|^2+o(\varepsilon^2).}
\]
The coefficients satisfy
\[
0=d_1(s)<d_2(s)=\frac{2}{s+2}<d_3(s)<\cdots<1,\qquad \lim_{n\to\infty}d_n(s)=1.
\]
Consequently the quadratic defect vanishes precisely on real first harmonics (infinitesimal translations), and
\[
\boxed{\lim_{\varepsilon\to0}\frac{1-e^{-s}-\Lambda(\varepsilon)}{\varepsilon^2}\ge \frac{e^{-s}}{s+2}\,\|h_{\ge2}\|_{L^2(d\theta/2\pi)}^2.}
\]
Here \(h_{\ge2}=h-\widehat h_1e^{i\theta}-\widehat h_{-1}e^{-i\theta}\). The coefficient is sharp, with equality in the limiting inequality for nonzero pure second harmonics, together with any first-harmonic component.

The same exact coefficients have a nontrivial large-area spectral law. Let \(n=n(s)\) be positive integers with \(n(s)/s\to\alpha\in[0,\infty)\). Then
\[
\boxed{d_{n(s)}(s)\longrightarrow \min\{\alpha,1\}.}
\]
At the critical edge, if \(n(s)=s+u\sqrt s+o(\sqrt s)\), with fixed real \(u\), and \(\varphi(u)=e^{-u^2/2}/\sqrt{2\pi}\), \(\Phi(u)=\int_{-\infty}^{u}\varphi(v)\,dv\), then
\[
\boxed{\sqrt s\,(1-d_{n(s)}(s))\longrightarrow\frac{\varphi(u)}{\Phi(u)}.}
\]
The large-area formulas concern the exact Hessian coefficients and do not claim a uniform nonlinear remainder in \(s\), \(n\), or \(h\).

## Assumptions and scope

The inner product in \(\mathcal F^2\) is \(\langle F,G\rangle=\pi^{-1}\int F\overline G e^{-|z|^2}dA\). Let \(P_{\mathcal F^2}\) denote orthogonal projection from the ambient weighted \(L^2\) space. The operator \(T_\varepsilon\) is the compression of multiplication by the indicator of \(\Omega_\varepsilon\). Its quadratic form is \(\langle T_\varepsilon F,F\rangle=\pi^{-1}\int_{\Omega_\varepsilon}|F|^2e^{-|z|^2}dA\). All perturbations satisfy \(\min_\theta(s+\varepsilon h(\theta))>0\).

The exact-area constraint is essential; \(h\) has zero mean, not an arbitrary mean. The power-series assertion holds for each fixed \(s\) and each fixed \(h\) with \(\varepsilon\to0\). The eigenvalue is the optimized operator norm, rather than a Rayleigh quotient at the fixed vacuum vector. The classification of the Hessian is modulo translations and is not a global inequality for arbitrary domains.

## Proof

**1. Exact matrix and baseline gap.** The functions \(e_n(z)=z^n/\sqrt{n!}\), \(n\ge0\), are an orthonormal Fock basis. Substitution of \(t=r^2\) in the polar integral gives the exact matrix
\[
\langle T_\varepsilon e_n,e_m\rangle=\frac1{2\pi\sqrt{m!n!}}\int_0^{2\pi}e^{i(n-m)\theta}\int_0^{s+\varepsilon h(\theta)} t^{(m+n)/2}e^{-t}\,dt\,d\theta.
\]
At \(\varepsilon=0\), it is diagonal, and repeated integration by parts gives
\[
\lambda_n(s)=\frac1{n!}\int_0^s t^ne^{-t}\,dt=1-e^{-s}\sum_{j=0}^n\frac{s^j}{j!}.
\]
Thus \(\lambda_0(s)=1-e^{-s}\) is simple and strictly exceeds every other eigenvalue; its gap to the \(n\)-th diagonal entry is \(\lambda_0-\lambda_n=e^{-s}A_n(s)>0\). For \(n\ge1\), these gaps have a common positive lower bound \(se^{-s}\). Compact support and smooth dependence of the boundary imply \(T_\varepsilon\) is twice continuously differentiable in trace norm for \(\varepsilon\) near zero: express it as an angular integral of rank-one coherent-state projectors over \(0\le t\le s+\varepsilon h(\theta)\), and differentiate the finite upper limit twice. Consequently the top isolated eigenvalue has the ordinary second-order self-adjoint perturbation expansion.

**2. Shape derivatives and optimized eigenvalue.** Differentiation of the matrix at zero yields
\[
\langle T'_0 e_0,e_n\rangle=\frac{e^{-s}s^{n/2}}{\sqrt{n!}}\,\widehat h_n,
\qquad \langle T'_0e_0,e_0\rangle=e^{-s}\widehat h_0=0,
\]
with complex-conjugation convention immaterial for the modulus. The second derivative of the vacuum diagonal is
\[
\langle T''_0e_0,e_0\rangle=-e^{-s}\frac1{2\pi}\int_0^{2\pi}h(\theta)^2\,d\theta.
\]
The second-order eigenvalue formula therefore gives
\[
\begin{aligned}
[\varepsilon^2]\Lambda(\varepsilon)
&=-\frac{e^{-s}}2\|h\|_{L^2(d\theta/2\pi)}^2
+\sum_{n\ge1}\frac{e^{-2s}s^n/n!}{e^{-s}A_n(s)}|\widehat h_n|^2\\
&=-e^{-s}\sum_{n\ge1}\left(1-\frac{s^n/n!}{A_n(s)}\right)|\widehat h_n|^2.
\end{aligned}
\]
The last equality uses reality, the zero mean, and Parseval's identity, \(\|h\|^2=2\sum_{n\ge1}|\widehat h_n|^2\). The first coefficient vanishes. Absolute convergence follows from \(0\le d_n<1\) and \(h\in L^2\).

**3. Strict mode ordering and sharpness.** Write
\[
\frac{A_n(s)}{a_n(s)}=\sum_{j=0}^{n-1}\frac{n(n-1)\cdots(n-j+1)}{s^j}.
\]
For every fixed \(s>0\), increasing \(n\) strictly increases each nonconstant term already present and adds a new positive term. Thus \(A_n/a_n\) strictly increases from one; equivalently \(d_n\) strictly increases from zero. Its limit is one because \(A_n\ge s>0\), whereas \(a_n=s^n/n!\to0\). Direct substitution gives \(d_2=2/(s+2)\). Since \(\|h_{\ge2}\|^2=2\sum_{n\ge2}|\widehat h_n|^2\), the smallest positive quadratic-deficit coefficient is \(e^{-s}d_2/2=e^{-s}/(s+2)\); strict ordering proves its exact equality family.

**4. Spectral large-area law.** With \(N_s\) Poisson distributed with mean \(s\), exactly
\[
1-d_n(s)=\frac{\mathbb P(N_s=n)}{\mathbb P(1\le N_s\le n)}.
\]
Alternatively the reciprocal is the positive falling-factorial sum displayed in Step 3. If \(n(s)/s\to\alpha<1\), its summands for each fixed \(j\) tend to \(\alpha^j\), and for all large \(s\) they are dominated by \(\beta^j\) for some \(\alpha<\beta<1\). Dominated convergence yields \(A_n/a_n\to(1-\alpha)^{-1}\), hence \(d_n\to\alpha\). This also includes \(\alpha=0\) and bounded \(n\). If \(\alpha>1\), the Poisson point probability tends to zero while \(\mathbb P(1\le N_s\le n)\to1\), so \(d_n\to1\). If \(\alpha=1\), choose integers \(J_s\to\infty\) such that \(J_s(|n/s-1|+J_s/s)\to0\). The first \(J_s\) terms of \(A_n/a_n\) are each \(1-o(1)\), implying \(A_n/a_n\to\infty\) and again \(d_n\to1\). These cases prove the full crossover.

Finally, for \(n=s+u\sqrt s+o(\sqrt s)\), the Poisson local central limit theorem gives \(\sqrt s\,\mathbb P(N_s=n)\to\varphi(u)\), while the distributional central limit theorem gives \(\mathbb P(1\le N_s\le n)\to\Phi(u)>0\). Their ratio gives the asserted critical-edge limit.

## Verification

A standalone reproducibility script, `checker.py`, evaluates the exact truncated Fock concentration matrices by incomplete-gamma quadrature, computes their highest eigenvalues for fixed-area Fourier boundary perturbations, and compares the observed quadratic deficits against the theorem. It also checks strict coefficient ordering by high-precision arithmetic and the large-area/edge limits by finite calculations. Executing `python checker.py` with NumPy, SciPy and mpmath produced `PASS 249 independent finite and high-precision checks`.

These finite calculations are corroboration only. The proof of all-mode positivity, infinite-dimensional perturbation validity, and all asymptotic limits is analytic in Steps 1–4, not inferred from truncated matrices or numerical data.

## Relationship to prior work

Nicola and Tilli, *The Faber–Krahn inequality for the Short-time Fourier transform* (first posted 2021-06-07), prove that the Gaussian time-frequency localization norm at fixed area is maximized by a disk, with the value \(1-e^{-s}\). This supplies the extremal geometric setting, not the angular shape Hessian of the optimized principal eigenvalue.

Gómez, Guerra, Ramos and Tilli, *Stability of the Faber–Krahn inequality for the Short-time Fourier Transform* (first posted 2023-07-18), obtain quantitative global stability and, in their Section 5 and Lemma 5.6, an explicit second variation of a **different functional**: the best-superlevel-set concentration as an analytic Fock vector changes. Their optimization is over the set at fixed vector, whereas the present calculation optimizes the vector at each prescribed set; the two variations have different spectral coefficients. Their formulas motivate a possible Schur-complement connection but do not state the Poisson ratio shape spectrum or its semiclassical edge limit.

Nicola and Tilli, *The norm of time-frequency and wavelet localization operators* (first posted 2022-07-18), prove sharp symbol-norm envelopes. These general inequalities do not specify a full Fourier-mode Hessian of an area-preserving disk deformation. A previously unlocated equivalent formulation or an implicit elimination of the vector perturbation from earlier second-variation identities remains a historical-priority risk.

## Limitations

The expansion is local in a single fixed domain perturbation. The theorem does not establish a global sharp Fraenkel-asymmetry constant, a nonlinear stability inequality uniform over all shapes, a spectral formula for non-Gaussian windows, or any uniformity of the Taylor remainder as the area tends to infinity. The crossover governs coefficients of the already computed second variation, not the nonlinear eigenvalue itself when the area and perturbation vary simultaneously. Reproduced finite matrices are not an independent mathematical audit and do not establish historical priority.

## References

1. F. Nicola and P. Tilli, *The Faber–Krahn inequality for the Short-time Fourier transform*, arXiv:2106.03423, initial public version 2021-06-07, https://arxiv.org/abs/2106.03423.
2. F. Nicola and P. Tilli, *The norm of time-frequency and wavelet localization operators*, arXiv:2207.08624, initial public version 2022-07-18, https://arxiv.org/abs/2207.08624.
3. J. Gómez, A. Guerra, J. P. G. Ramos and P. Tilli, *Stability of the Faber-Krahn inequality for the Short-time Fourier Transform*, arXiv:2307.09304, initial public version 2023-07-18, https://arxiv.org/abs/2307.09304; *Inventiones mathematicae* 236 (2024), 779–836, DOI: 10.1007/s00222-024-01248-2.
4. Standard spectral perturbation formula for an isolated simple eigenvalue and standard local central limit theorem for the Poisson distribution (used explicitly in the proof).
