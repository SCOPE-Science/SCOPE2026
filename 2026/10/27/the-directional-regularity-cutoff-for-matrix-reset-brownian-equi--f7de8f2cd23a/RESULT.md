# The directional regularity cutoff for matrix-reset Brownian equilibria

## Finding

**Theorem (spectral regularity classification).** Fix an integer \(d\ge1\), a symmetric positive-definite \(d\times d\) matrix \(\Sigma\), a reset rate \(\lambda>0\), and a real \(d\times d\) matrix \(A\) with spectral radius \(\rho(A)<1\). Let \(X\) be the càdlàg process which follows Brownian motion with covariance rate \(\Sigma\) between independent rate-\(\lambda\) Poisson times, and is mapped to \(A X_{t-}\) at each such time. Then \(X\) has a unique stationary distribution \(\mu\). Write \(\Sigma_j=A^j\Sigma(A^\mathsf{T})^j\). Its characteristic function and an independent-series representation are

\[
\widehat\mu(u)=\prod_{j=0}^{\infty}\left(1+\frac{u^\mathsf{T}\Sigma_j u}{2\lambda}\right)^{-1},\qquad
X_{\infty}\ \stackrel{\mathrm d}=\ \sum_{j=0}^{\infty} A^j G_j,
\]

where the \(G_j\) are independent, identically distributed \(B(E)\), with \(E\sim\mathrm{Exp}(\lambda)\) independent of Brownian motion \(B\) of covariance rate \(\Sigma\). The series converges in \(L^2\); \(\mu\) is infinitely divisible.

For each nonzero \(v\in\mathbb R^d\), define \(m(v)=\min\{j\ge1:(A^\mathsf T)^jv=0\}\), with \(m(v)=\infty\) if this set is empty. The one-dimensional projection \(v^\mathsf T X_\infty\) has a bounded \(C^\infty\) density **if and only if** \(m(v)=\infty\). If \(m=m(v)<\infty\), the projected density belongs to \(C^{2m-2}(\mathbb R)\) but not to \(C^{2m-1}(\mathbb R)\). Indeed, putting \(a_j=v^\mathsf T\Sigma_jv/(2\lambda)>0\) for \(0\le j<m\), its \((2m-1)\)-st derivative has one-sided limits at the origin with exact jump

\[
 f_v^{(2m-1)}(0+)-f_v^{(2m-1)}(0-)
 =\frac{(-1)^m}{\prod_{j=0}^{m-1}a_j}.
\]

In particular, the *full* equilibrium law has a bounded \(C^\infty\) density whenever \(A\) is invertible; if \(A\) is singular, its density cannot belong to \(C^2(\mathbb R^d)\). For every nonzero \(v\in\ker A^\mathsf T\), the projection is exactly Laplace, with scale \(\sqrt{v^\mathsf T\Sigma v/(2\lambda)}\) and a cusp at zero. The classification applies equally to nonnormal, defective, and nilpotent reset matrices.

## Assumptions and scope

All matrices and Brownian coordinates are real. Brownian motion has \(\mathbb E[B_t]=0\) and \(\operatorname{Cov}(B_t)=t\Sigma\); a Brownian interval and its independent Poisson waiting time are independent. The resetting map has no translation or random component. Spectral radius strictly below one (not necessarily an operator-norm bound) is the contraction assumption. The statements concern the stationary law and its ordinary Lebesgue densities, with no reliance on limiting plots or finite truncations. \(C^k\) means continuous classical derivatives through order \(k\) on the whole indicated Euclidean space. The displayed derivative jump concerns analytic continuations from each open half-line. A *singular* matrix has nontrivial kernel, not merely a small eigenvalue.

## Proof

**1. Series and stationarity.** Let \(E_j\) be independent exponential variables of rate \(\lambda\), and let \(G_j\) be independent Brownian increments over durations \(E_j\). Thus each \(G_j\) is centered with covariance \(\Sigma/\lambda\). As \(\rho(A)<1\), the matrix series \(\sum_{j\ge0}\|A^j\|^2\) converges. Independence and centering imply that \(\sum_{j\ge0}A^jG_j\) converges in \(L^2\). The renewal equation of a stationary Poisson point process, read backward from a typical observation time, decomposes the elapsed Brownian segments into independent exponential gaps. Each older increment has suffered precisely \(j\) resets, hence carries the coefficient \(A^j\). The resulting series has an invariant distribution. Equivalently, this follows directly from the generator and the transform equation in step 2. Two processes started at arbitrary finite random initial points and driven by the same Brownian motion and Poisson epochs differ at time \(t\) by \(A^{N_t}\) times their initial difference. Since \(N_t\to\infty\) almost surely and \(A^{N_t}\to0\), the stationary distribution is unique.

**2. Characteristic function and infinite divisibility.** Conditioning on \(E\) gives

\[
\mathbb E e^{i u^\mathsf TG_0}
=\mathbb E\exp(-E u^\mathsf T\Sigma u/2)
=\frac{\lambda}{\lambda+u^\mathsf T\Sigma u/2}.
\]

Independence and \(L^2\) convergence yield the claimed infinite product. For \(w\ge0\), Frullani's integral identity yields

\[
-\log(1+w/\lambda)
=\int_0^\infty (e^{-sw}-1)e^{-\lambda s}\,\frac{ds}{s}.
\]

Consequently \(\mu\) is symmetric infinitely divisible with Lévy measure

\[
\nu(H)=\sum_{j=0}^\infty\int_0^\infty
\frac{e^{-\lambda s}}s\,
\mathbb P\big\{N(0,s\Sigma_j)\in H\big\}\,ds,
\qquad H\subset\mathbb R^d\setminus\{0\}.
\]

The Gaussian in this formula may be degenerate for \(j\ge1\). Each term is a valid symmetric Lévy measure; the series satisfies \(\int(1\wedge\|x\|^2)\,\nu(dx)\le\sum_j \operatorname{tr}(\Sigma_j)/\lambda<\infty\). There is no independent Gaussian part or drift in this Lévy representation.

**3. Exact directional regularity.** Fix \(v\ne0\). The scalar characteristic function is

\[
\phi_v(t)=\prod_{j\ge0}(1+a_jt^2)^{-1},\qquad
 a_j=\frac{\|(\Sigma^{1/2})(A^\mathsf T)^jv\|^2}{2\lambda}.
\]

Positive definiteness of \(\Sigma\) shows \(a_j=0\) exactly when \((A^\mathsf T)^jv=0\). If no power kills \(v\), the first \(N\) positive factors bound \(|\phi_v(t)|\le C_N(1+|t|)^{-2N}\) for each \(N\). Every polynomially weighted Fourier transform is integrable; Fourier inversion proves a bounded \(C^\infty\) density.

If the first vanishing power is \(m\), exactly \(m\) positive factors remain. This is the characteristic function of a convolution of \(m\) symmetric Laplace densities \(\ell_j(x)=\exp(-|x|/\sqrt{a_j})/(2\sqrt{a_j})\). The estimate \(|\phi_v(t)|=O(|t|^{-2m})\) implies, by Fourier inversion, that the resulting density is \(C^{2m-2}\). It is real analytic separately on the positive and negative half-lines, as follows either by convolution of exponential kernels or by partial-fraction inversion (including repeated poles). In the sense of distributions, \((1-a_j\partial_x^2)\ell_j=\delta_0\). Hence

\[
\prod_{j=0}^{m-1}(1-a_j\partial_x^2)f_v=\delta_0.
\]

Integrate across a shrinking symmetric interval around zero. The terms of derivative order at most \(2m-2\) have vanishing integrals because the corresponding derivatives are continuous. The highest term is \((-1)^m\prod a_j\,\partial_x^{2m}f_v\), whose integral tends to \((-1)^m\prod a_j\,[f_v^{(2m-1)}(0+)-f_v^{(2m-1)}(0-)]\). Equality to the unit atom proves the stated nonzero jump and rules out \(C^{2m-1}\).

**4. The sharp joint dichotomy.** If \(A\) is invertible, then each \(\Sigma_j\) is positive definite. For any finite \(N\), the first \(N\) factors in \(\widehat\mu(u)\) are uniformly bounded by \(C_N(1+\|u\|)^{-2N}\); thus \(\widehat\mu\) and all polynomially weighted transforms are integrable on \(\mathbb R^d\). Fourier inversion gives a bounded \(C^\infty\) joint density.

For any \(A\), the first Brownian-exponential increment has a Lebesgue density (being a mixture of nondegenerate Gaussian densities), hence so does its convolution \(\mu\). Stationarity under the generator gives, as an identity of distributions,

\[
\left(\lambda-\frac12\sum_{i,j}\Sigma_{ij}\partial_i\partial_j\right)\mu
=\lambda A_\#\mu.
\]

If \(A\) is singular then \(A_\#\mu\) is a probability measure supported on the proper linear subspace \(\operatorname{ran}A\), hence is singular with respect to Lebesgue measure. Were the density of \(\mu\) globally \(C^2\), the entire left side would be given by a continuous function and thus be absolutely continuous. This is impossible. This completes the regularity classification.

## Verification

Run `python verify.py` with Python 3 and SymPy. The included checker uses exact rational arithmetic for four distinct \(2\times2\) stable reset matrices (diagonal, nonnormal triangular, nilpotent, and rank-one), tests the covariance Lyapunov identity, computes the stationary fourth-cumulant tensor by solving a \(16\times16\) rational linear system, compares its one-step renewal relation on specified projection directions, and checks exact nilpotent chain lengths and the associated scale parameters. The checker reported **104 exact-rational checks passed**. These computations are independent finite-dimensional consistency tests, not substitutes for the Fourier and distributional proofs of infinitely many scales or smoothness.

## Relationship to prior work

Tal-Friedman, Roichman, and Reuveni [2] already obtained the infinite independent-Laplace convolution and Fourier product for a **scalar** Brownian partial reset factor, including its full-reset Laplace endpoint. Grzywny, Palmowski, Szczypkowski, and Trojan [3] prove stationary density regularity for multivariate stable drivers with a **single scalar** partial-reset factor \(c\in(0,1)\); their smoothness results cover the invertible scalar-multiple-of-identity case. Assefa, Keller-Ressel, and Palmowski [1] study **general affine** resets of polynomial processes and derive moment and cross-moment formulas, but the inspected primary text does not assert the stated complete directional regularity cutoff or the singular-matrix obstruction. The result here is the sharp classification by the first annihilating power of \(A^\mathsf T\), including the derivative jump, and the non-\(C^2\) joint consequence. The product formula and scalar invertible special cases are explicitly acknowledged as previously known or immediate extensions.

## Limitations

This theorem assumes constant positive-definite Brownian covariance, deterministic linear resets, independent exponential reset times, and \(\rho(A)<1\). The proof does not treat general random reset matrices, nonlinear resets, non-Poisson renewal clocks, degenerate driving noise, or arbitrary Lévy drivers. The assertion that the matrix-directional cutoff and joint singular-rank dichotomy are original is based on the inspected sources and targeted searches, not an exhaustive literature certification; an equivalent theorem implicit in general reset-generator or smoothing literature is a residual risk. Independent scientific audit has not been performed.

## References

[1] J. Assefa, M. Keller-Ressel, and Z. Palmowski, *Moments of polynomial processes under affine resetting*, arXiv:2610.01363 (first public 2026-10-01). https://arxiv.org/html/2610.01363v1

[2] O. Tal-Friedman, Y. Roichman, and S. Reuveni, *Diffusion with Partial Resetting*, arXiv:2205.03363 (2022). https://arxiv.org/pdf/2205.03363

[3] T. Grzywny, Z. Palmowski, K. Szczypkowski, and B. Trojan, *Stationary states for stable processes with partial resetting*, arXiv:2412.15626 (first public 2024-12-20). https://arxiv.org/pdf/2412.15626
