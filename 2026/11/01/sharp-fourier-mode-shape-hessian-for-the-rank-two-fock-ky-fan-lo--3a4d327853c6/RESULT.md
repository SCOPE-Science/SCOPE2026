# Sharp Fourier-mode shape Hessian for the rank-two Fock Ky Fan localization norm

## Finding

For every \(x>0\), the disk is a strictly stable stationary shape for the *rank-two* Fock localization Ky Fan functional, modulo translations, with an explicit sharp Fourier-mode Hessian. Unlike the previously established global maximization theorem, the present formula determines the complete local spectral curvature and its extremizing deformation.

Let \(\mathcal K_2(\Omega)\) denote the sum of the two largest eigenvalues of the positive Toeplitz localization operator \(T_\Omega\). For real \(C^2\) functions \(h,q\) on the circle with vanishing angular means, define the exactly area-preserving family
\[
\Omega_\varepsilon=\bigl\{re^{i\theta}:0\le r^2<x+\varepsilon h(\theta)+\varepsilon^2q(\theta)\bigr\}.
\]
For any sufficiently small real \(\varepsilon\), its area is \(\pi x\). Write
\[
\widehat h_k=\frac1{2\pi}\int_0^{2\pi}h(\theta)e^{-ik\theta}\,d\theta,\qquad
 a_j=\frac{x^j}{j!},\quad A_k=\sum_{j=1}^{k}a_j,\quad B_k=\sum_{j=2}^{k+1}a_j,
\]
and, for integers \(k\ge2\),
\[
H_k(x)=-x+\frac{a_k}{A_k}+x\frac{a_{k+1}}{B_k}.
\]
Then the exact second-order law is
\[
\boxed{\mathcal K_2(\Omega_\varepsilon)=2-(x+2)e^{-x}+\varepsilon^2e^{-x}\sum_{k=2}^\infty H_k(x)|\widehat h_k|^2+o(\varepsilon^2).}
\]
The coefficients are strictly decreasing and negative:
\[
 0>H_2(x)>H_3(x)>\cdots>-x,
 \qquad H_2(x)=-\frac{x(2x+3)}{(x+2)(x+3)}.
\]
The first angular harmonic has coefficient zero, as required by translation invariance. In particular, the sharp **transverse** local deficit is
\[
\mathcal K_2(D_x)-\mathcal K_2(\Omega_\varepsilon)
\ge \varepsilon^2e^{-x}\frac{x(2x+3)}{(x+2)(x+3)}
 \sum_{k=2}^\infty |\widehat h_k|^2+o(\varepsilon^2),
\]
and equality of its quadratic coefficient for a nonzero transverse perturbation occurs exactly when \(h\) has no frequencies \(k\ge3\). The optimal constant is attained by an elliptic/quadrupolar first-order deformation.

## Assumptions and scope

Use the complex Gaussian Bargmann--Fock Hilbert space
\[
\mathcal F^2=\left\{f\text{ entire}:\|f\|^2=\frac1\pi\int_{\mathbb C}|f(z)|^2e^{-|z|^2}dA(z)<\infty\right\},
\]
with orthonormal monomials \(e_n(z)=z^n/\sqrt{n!}\), \(n\ge0\). The localization operator has quadratic form
\[\langle T_\Omega f,g\rangle=\frac1\pi\int_\Omega f(z)\overline{g(z)}e^{-|z|^2}dA(z).\]
For finite-area domains, \(T_\Omega\) is positive trace class and \(\operatorname{tr}T_\Omega=|\Omega|/\pi\). The area-preserving paths here have \(h,q\in C^2(\mathbb T;\mathbb R)\) satisfying \(\widehat h_0=\widehat q_0=0\). Their squared-radius boundary is positive for sufficiently small \(\varepsilon\), with exact area \(\pi x\). The value of \(q\) affects neither the stated second-order coefficient nor the area.

The Gaussian normalization of references [1]--[3] uses \(e^{-\pi|z|^2}\); a spatial dilation gives the present equivalent normalization. The result is restricted to one complex dimension, rank two, smooth small perturbations, and second-order variation. It asserts neither a new global extremal inequality nor uniform nonlinear stability over nonsmooth sets.

## Proof

**1. Radial spectrum and isolated cluster.** For the disk \(D_x=\{z:|z|^2<x\}\), the matrix in the monomial basis is diagonal with eigenvalues
\[
\lambda_n(D_x)=\frac1{n!}\int_0^x t^ne^{-t}dt
 =1-e^{-x}\sum_{j=0}^{n}\frac{x^j}{j!},\qquad n\ge0.
\]
These are strictly decreasing for every \(x>0\). Hence the two top eigenvalues form an isolated spectral cluster with projection \(P=\operatorname{span}\{e_0,e_1\}\), and their sum is \(2-(x+2)e^{-x}\).

**2. Differentiating the shape.** In polar squared radius \(t=r^2\), exact matrix elements are
\[
(T_{\Omega_\varepsilon})_{mn}
 =\frac{1}{2\pi\sqrt{m!n!}}
\int_0^{2\pi}e^{i(n-m)\theta}
 \int_0^{x+\varepsilon h(\theta)+\varepsilon^2q(\theta)}
  t^{(m+n)/2}e^{-t}\,dt\,d\theta.
\]
Writing \(T_{\Omega_\varepsilon}=T_{D_x}+\varepsilon V+\varepsilon^2W+o(\varepsilon^2)\) in trace norm yields
\[
V_{mn}=\frac{e^{-x}x^{(m+n)/2}}{\sqrt{m!n!}}\,\widehat h_{m-n},
\]
\[
W_{mn}=\frac{e^{-x}x^{(m+n)/2}}{\sqrt{m!n!}}
\left[\widehat q_{m-n}+\frac12\left(\frac{m+n}{2x}-1\right)\widehat{h^2}_{m-n}\right].
\]
The trace-norm differentiability follows directly from the representation of \(T_\Omega\) as the integral of normalized coherent-state rank-one projectors: the integrand is smooth with uniformly bounded trace-norm derivatives near the fixed positive radius \(\sqrt{x}\). These formulas also show \(\operatorname{tr}(PV)=e^{-x}(1+x)\widehat h_0=0\).

**3. Second-order isolated-cluster perturbation.** Analytic perturbation of the separated spectral cluster, or an elementary resolvent contour expansion, gives
\[
[\varepsilon^2]\,\mathcal K_2(\Omega_\varepsilon)
 =\operatorname{tr}(PWP)+
 \sum_{n=0}^1\sum_{m=2}^\infty
\frac{|V_{mn}|^2}{\lambda_n(D_x)-\lambda_m(D_x)}.
\]
This expression requires no choice of eigenvectors within the cluster. Since \(\widehat q_0=0\), direct substitution and Parseval yield
\[
\operatorname{tr}(PWP)=-\frac12 xe^{-x}\widehat{h^2}_0
=-xe^{-x}\sum_{k\ge1}|\widehat h_k|^2.
\]
The denominators for \(m=k\ge2,n=0\) and \(m=k+1\ge2,n=1\) are respectively
\[
\lambda_0-\lambda_k=e^{-x}A_k,\qquad
\lambda_1-\lambda_{k+1}=e^{-x}B_k.
\]
The corresponding summands are
\[
e^{-x}\frac{a_k}{A_k}|\widehat h_k|^2\quad(k\ge2),\qquad
 e^{-x}x\frac{a_{k+1}}{B_k}|\widehat h_k|^2\quad(k\ge1).
\]
At \(k=1\), the second term equals \(xe^{-x}|\widehat h_1|^2\) and cancels the local-boundary term. Summation gives the claimed exact Fourier expansion, with no dependence on the mean-zero second-order adjustment \(q\).

**4. Sharp sign and monotonicity.** For all \(k\ge2\), use the falling factorial \((m)_\ell=m(m-1)\cdots(m-\ell+1)\) to write
\[
\frac{A_k}{a_k}=\sum_{\ell=0}^{k-1}\frac{(k)_\ell}{x^\ell},\qquad
\frac{B_k}{a_{k+1}}=\sum_{\ell=0}^{k-1}\frac{(k+1)_\ell}{x^\ell}.
\]
Both positive denominators increase strictly when \(k\) increases, as each old nonconstant falling factorial increases and a new positive term appears. Thus each ratio \(a_k/A_k\) and \(a_{k+1}/B_k\) decreases strictly. Consequently \(H_k\) strictly decreases. Direct calculation gives
\[
 H_2=-x+\frac{x}{x+2}+\frac{x^2}{x+3}
 =-\frac{x(2x+3)}{(x+2)(x+3)}<0.
\]
Hence \(H_k<0\) for all \(k\ge2\), and the sharp least-negative transverse coefficient is \(H_2\). The bound is saturated at quadratic order by a nonzero real second harmonic, such as \(h(\theta)=\cos(2\theta)\). The \(k=1\) nullspace corresponds to infinitesimal translation of the disk, consistent with Gaussian Weyl displacement invariance. This completes the proof.

## Verification

The accompanying standalone Python program `experiments/check_hessian.py` evaluates truncated Toeplitz matrices directly from the incomplete-Gamma integral and compares their symmetric second differences against the exact Fourier Hessian, for three disk areas and five Fourier frequencies. It also tests coefficient monotonicity and the closed form of the sharp \(k=2\) coefficient at six further radii. In the executed checks all **21 cases passed**. These finite-dimensional and floating-point checks are supplementary: the infinite-dimensional theorem is proved above by the trace-norm expansion, spectral perturbation, and positive-series comparison. Reproduce with Python 3, NumPy and SciPy by running `python experiments/check_hessian.py`.

## Relationship to prior work

Nicola, Riccardi and Tilli [1] prove global disk maximization of partial Fock Toeplitz eigenvalue sums within the radial class, and describe unrestricted shape optimization as difficult. Their theorem does not give nonradial second variations. Their later work [2] proves existence of unrestricted optimizers but does not identify a sharp Fourier-mode curvature. Abreu [3] subsequently proves **global disk maximization for arbitrary measurable sets and all Ky Fan ranks**. Therefore the qualitative inequality and global optimality are explicitly prior results; the present contribution is solely the exact rank-two nonradial second-order Fourier spectrum, its translational kernel, and the *sharp quantitative* least-curvature constant. The global upper bound in [3] alone implies a nonpositive second variation (where it exists), but does not supply the explicit numbers \(H_k(x)\), their strict ordering, or the sharp quadrupolar stability coefficient.

Relevant source-priority limitations: the full 2025 preprint [1] was examined for its main statements and proofs. The abstracts and available summaries of [2] and [3] were reviewed, but their primary full texts could not be obtained. In particular, [3] could contain an unindexed quantitative lemma of similar strength; this remains an unresolved literature-priority risk rather than a mathematical assumption or an implication of the published global statement.

## Limitations

This is a **local**, quadratic-order result for smooth radial-graph deformations at fixed area. The null Hessian of first harmonics does not imply they describe exact translations at every order for an arbitrary second-order shape path. No global spectral inequality is claimed as original; Abreu's prior result already supplies it. No higher rank, higher-dimensional, fourth-order, or nonsmooth quantitative stability theorem is asserted. Publication priority of an exact quantitative formula remains subject to full-text comparison with [2] and [3].

## References

[1] F. Nicola, F. Riccardi, P. Tilli, *The isoperimetric inequality for partial sums of Toeplitz eigenvalues in the Fock space*, arXiv:2503.07069 (first publicly posted 2025-03-10), https://arxiv.org/html/2503.07069v2 .

[2] F. Nicola, F. Riccardi, P. Tilli, *On the existence of extremizers for the sum of eigenvalues of Toeplitz operators*, arXiv:2607.20965 (first publicly posted 2026-07-23), https://arxiv.org/abs/2607.20965 .

[3] L. D. Abreu, *The isoperimetric inequality for the Ky Fan norm*, arXiv:2607.28376 (first publicly posted 2026-07-30), https://arxiv.org/abs/2607.28376 .
