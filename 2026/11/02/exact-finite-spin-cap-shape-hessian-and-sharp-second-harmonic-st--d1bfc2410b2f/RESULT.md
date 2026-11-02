# Exact finite-spin cap-shape Hessian and sharp second-harmonic stability

## Finding

In the degree-\(N\) spin-coherent polynomial space, the entire angular shape Hessian of the largest cap-localization eigenvalue is explicit. For every integer \(N\ge2\), cap area fraction \(0<p<1\), and real \(h\in C^3(\mathbb T)\) with mean zero, let the exactly area-preserving deformation have normalized radial coordinate \(u(z)=|z|^2/(1+|z|^2)\) and boundary \(u=p+\varepsilon h(\theta)\). With the operator and Fourier normalization defined below, the largest eigenvalue has the expansion

\[
\Lambda_N(\varepsilon)=1-(1-p)^{N+1}-\varepsilon^2Q_N(p)\sum_{j=2}^{\infty}d_{N,j}(p)|\widehat h_j|^2+O_{N,p,h}(\varepsilon^3),
\qquad Q_N(p)=N(N+1)(1-p)^{N-1}.
\]

Set \(b_{N,j}(p)=\binom{N+1}{j}p^j(1-p)^{N+1-j}\). For \(1\le j\le N\), the complete spectral multipliers are

\[
d_{N,j}(p)=1-\frac{N+1-j}{N}\frac{b_{N,j}(p)}{\sum_{k=1}^j b_{N,k}(p)},
\qquad d_{N,j}(p)=1\quad(j>N).
\]

They satisfy the strict finite-spin ordering

\[
0=d_{N,1}(p)<d_{N,2}(p)<\cdots<d_{N,N}(p)<1=d_{N,N+1}(p)=d_{N,N+2}(p)=\cdots,
\qquad
 d_{N,2}(p)=\frac{2-p}{2+(N-2)p}.
\]

Consequently angular first harmonics are exactly the quadratic null directions, and **the sharp least-stable nontranslation directions are the second harmonics**. More precisely, on deformations with \(\widehat h_1=0\), the coefficient of the quadratic concentration deficit is bounded sharply below by

\[
Q_N(p)\frac{2-p}{2+(N-2)p}\sum_{j=2}^{\infty}|\widehat h_j|^2,
\]

with equality for—and, apart from zero, only for—real second-harmonic deformations. Adding arbitrary first harmonics does not change this quadratic bound.

For a fixed \(s>0\) and \(p=s/N\), the rescaled deformation \(\varepsilon h/N\) has a quadratic Hessian that converges as \(N\to\infty\) to the Bargmann–Fock disk-shape Hessian: for every fixed \(j\ge1\),

\[
 d_{N,j}(s/N)\longrightarrow 1-\frac{s^j/j!}{\sum_{k=1}^j s^k/k!},
 \qquad Q_N(s/N)/N^2\longrightarrow e^{-s}.
\]

The convergence also holds for the full quadratic form of any fixed square-summable Fourier sequence because the multipliers are bounded between zero and one. This statement concerns the quadratic Hessians, not a uniform-in-\(N\) nonlinear remainder.

## Assumptions and scope

Let \(\mathcal P_N=\{P\in\mathbb C[z]:\deg P\le N\}\) with inner product

\[
\langle P,R\rangle_N=(N+1)\int_{\mathbb C}P(z)\overline{R(z)}(1+|z|^2)^{-N}\,dm(z),
\qquad dm(z)=\frac{dA(z)}{\pi(1+|z|^2)^2}.
\]

Under \(z=\sqrt{u/(1-u)}e^{i\theta}\), the sphere probability measure is \(dm=du\,d\theta/(2\pi)\), and the normalized reproducing basis is \(e_j(z)=\sqrt{\binom Nj}z^j\), \(0\le j\le N\). For any measurable domain \(\Omega\), the positive localization operator is defined by its form

\[
\langle T_\Omega P,R\rangle_N=(N+1)\int_\Omega P(z)\overline{R(z)}(1+|z|^2)^{-N}\,dm(z),
\qquad \Lambda_N(\Omega)=\|T_\Omega\|.
\]

The undeformed spherical cap is \(\Omega_0=\{z:u(z)<p\}\). Fix a real, \(2\pi\)-periodic \(C^3\) function \(h\) satisfying \(\widehat h_0=0\), where

\[
\widehat h_j=\frac1{2\pi}\int_0^{2\pi}h(\theta)e^{-ij\theta}\,d\theta.
\]

For all sufficiently small real \(\varepsilon\), define \(\Omega_\varepsilon=\{\sqrt{u/(1-u)}e^{i\theta}:0\le u<p+\varepsilon h(\theta)\}\). Its measure is exactly \(p\) for every such \(\varepsilon\), not just to first order. The expansion is at fixed \(N,p,h\). The case \(N=1\) is excluded because all projective rays are coherent states and the claimed strict mode ordering is not applicable.

## Proof

**1. Exact unperturbed spectrum and gap.** The cap is rotationally invariant, hence diagonal in \(\{e_j\}\), with eigenvalues

\[
\lambda_j=(N+1)\binom Nj\int_0^p u^j(1-u)^{N-j}\,du
=\Pr\{X\ge j+1\},\qquad X\sim\operatorname{Binomial}(N+1,p).
\]

Thus \(\lambda_0=1-(1-p)^{N+1}\), and \(\lambda_0-\lambda_j=\sum_{k=1}^j b_{N,k}>0\) for \(1\le j\le N\). In particular the principal eigenvalue is simple, so ordinary analytic Hermitian-matrix perturbation theory applies.

**2. Shape derivatives.** The exact matrix is

\[
M_{jk}(\varepsilon)=(N+1)\sqrt{\binom Nj\binom Nk}\,\frac1{2\pi}\int_0^{2\pi}e^{i(j-k)\theta}
\int_0^{p+\varepsilon h(\theta)}u^{(j+k)/2}(1-u)^{N-(j+k)/2}\,du\,d\theta.
\]

Mean zero gives \(M'_{00}(0)=0\), while

\[
\frac12M''_{00}(0)=-\frac12N(N+1)(1-p)^{N-1}\frac1{2\pi}\int_0^{2\pi}h(\theta)^2\,d\theta
=-Q_N(p)\sum_{j=1}^{\infty}|\widehat h_j|^2.
\]

For \(1\le j\le N\),

\[
|M'_{j0}(0)|^2=(N+1)^2\binom Nj p^j(1-p)^{2N-j}|\widehat h_j|^2.
\]

**3. Complete Hessian and first-harmonic cancellation.** The second coefficient of a simple Hermitian eigenvalue equals its diagonal second coefficient plus \(\sum_{j=1}^N|M'_{j0}(0)|^2/(\lambda_0-\lambda_j)\). Dividing the latter summands by \(Q_N(p)\) yields precisely

\[
\frac{1}{Q_N(p)}\frac{|M'_{j0}(0)|^2}{\lambda_0-\lambda_j}
=\frac{N+1-j}{N}\frac{b_{N,j}}{\sum_{k=1}^j b_{N,k}}|\widehat h_j|^2.
\]

For \(j=1\), the coefficient equals \(|\widehat h_1|^2\) and cancels the corresponding diagonal loss. For \(j>N\), the polynomial space has no such coupling; the negative diagonal contribution remains with multiplier one. The displayed Hessian follows. The eigenvalue and all matrix entries are analytic near zero because the moving boundaries stay in the compact interval \((0,1)\), which justifies the claimed fixed-parameter cubic remainder.

**4. Strict mode ordering and sharpness.** The consecutive binomial ratios

\[
\frac{b_{N,k-1}}{b_{N,k}}=\frac{k(1-p)}{(N+2-k)p}
\]

increase strictly with \(k\) over their admissible range. Therefore \(\sum_{k=1}^j b_{N,k}/b_{N,j}\) increases strictly in \(j\): each common backward product of consecutive ratios grows and one additional positive product appears. Thus \(b_{N,j}/\sum_{k=1}^j b_{N,k}\) strictly decreases. Its product with the strictly decreasing positive prefactor \((N+1-j)/N\) decreases for \(1\le j\le N\), proving \(0=d_{N,1}<d_{N,2}<\cdots<d_{N,N}<1\). The extra modes equal one. Simplification of \(d_{N,2}\) gives the displayed rational formula. This strictly ordered Fourier diagonalization makes precisely the second harmonic sharp on the complement of the null directions.

**5. Finite-spin to Gaussian limit.** As \(N\to\infty\) with \(p=s/N\), each fixed binomial mass \(b_{N,j}(p)\) tends to \(e^{-s}s^j/j!\), giving the claimed multiplier limit. Also \(N(N+1)(1-s/N)^{N-1}/N^2\to e^{-s}\). The multipliers lie in \([0,1]\), so dominated convergence against \(\sum_{j\ge1}|\widehat h_j|^2<\infty\) gives convergence of the complete Hessian after scaling the boundary variation by \(1/N\).

## Verification

A standalone reproducibility program, `checker.py`, evaluates the complete localization matrices using incomplete-beta integrals and direct Hermitian diagonalization. At several independently chosen integer degrees, cap measures and angular Fourier perturbations, central finite differences of the largest matrix eigenvalue agree with the analytical Hessian coefficients. Additional tests check exact formula simplifications, ordering and the finite-spin-to-Poisson transition. Executing `python checker.py` using Python 3, NumPy and SciPy produced `PASS: 163 deterministic assertions; numerical eigenvalue Hessians and finite-spin limits` (reported test count as implemented). These finite computations corroborate rather than establish the all-degree theorem; the proof above is analytic.

## Relationship to prior work

Frank's 2022 sharp coherent-state concentration theorem identifies spherical caps and coherent states as optimizers for the \(SU(2)\) coherent-state problem, but does not give the second variation with respect to angular cap deformation. García-Ferrero and Ortega-Cerdà (first public version, August 14, 2024) prove quantitative polynomial concentration stability, including distance-to-disk estimates, without the full binomial-tail Fourier Hessian or the sharp second-harmonic coefficient. Gómez, Guerra, Ramos and Tilli study quantitative stability of the Gaussian Bargmann–Fock localization problem, which involves a different (infinite-dimensional) coherent-state space. The present result supplies exact finite-spin direction-dependent coefficients and exhibits their Gaussian limit; qualitative stability and the limiting Gaussian calculation alone do not imply the finite-degree formulas.

## Limitations

The result is local in shape and assumes a fixed integer degree, fixed nondegenerate cap area fraction, and a smooth mean-zero angular boundary perturbation. It does not assert a global optimal stability constant, a nonlocal neighborhood radius, an error uniform in degree, or a classification of nonsmooth cap perturbations. Novelty is assessed against the cited accessible primary literature and searchable research records; implicit deductions in other prior works cannot be completely excluded without independent historical review. No independent mathematical audit has been performed.

## References

1. Rupert L. Frank, *Sharp inequalities for coherent states and their optimizers*, first publicly available October 26, 2022; arXiv:2210.14798v1, https://arxiv.org/abs/2210.14798.
2. María Ángeles García-Ferrero and Joaquim Ortega-Cerdà, *Stability of the concentration inequality on polynomials*, first publicly available August 14, 2024; arXiv:2408.07424v1, https://arxiv.org/abs/2408.07424.
3. Jaime Gómez, André Guerra, João P. G. Ramos and Paolo Tilli, *The stability of the Faber–Krahn inequality for the short-time Fourier transform*, first publicly available July 18, 2023; arXiv:2307.09304v1, https://arxiv.org/abs/2307.09304.
