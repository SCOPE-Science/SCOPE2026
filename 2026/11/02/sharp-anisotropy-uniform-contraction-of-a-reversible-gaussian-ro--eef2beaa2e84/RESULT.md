# Sharp anisotropy-uniform contraction of a reversible Gaussian rotation--OU Strang sampler

## Finding

For every \(h>0\) and \(0<\lambda\leq1\), a symmetric exact-subflow splitting of the two-dimensional reversible Stratonovich-perturbed Gaussian Langevin model has **exactly** the target Gaussian as its unique invariant law, satisfies detailed balance, and has an explicit sharp synchronous mean-square convergence factor. Write
\[
 p=e^{-2h},\quad r=e^{-2\lambda h},\quad k=e^{-4h},\qquad
 \rho(h,\lambda)=\frac{(1+k)(p+r)+\sqrt{(1+k)^2(p+r)^2-16kpr}}4.
\]
This is the exact asymptotic spectral factor for squared synchronous-coupling error, achieved in the asymptotic sense by every nonzero initial deterministic difference. Moreover, for every \(h>0\),
\[
 \sup_{0<\lambda\leq1}\rho(h,\lambda)=\rho(h,0)<1,
 \qquad \rho(h,0)=1-(3-\sqrt5)h+O(h^2)\quad(h\downarrow0),
 \qquad\lim_{h\to\infty}\rho(h,0)=\tfrac12.
\]
Here \(\rho(h,0)\) means the explicit formula's continuous extension to \(\lambda=0\), not a stationary Gaussian model with zero precision. For the normalized quadratic Wasserstein distance, the same exact scheme obeys
\[
 W_2^2(\mu P_{h,\lambda}^n,\gamma_2)
 \leq\sqrt2\,\rho(h,0)^n W_2^2(\mu,\gamma_2)
\]
for every initial probability measure \(\mu\) with finite second moment; \(\gamma_2=N(0,I_2)\). Thus the discrete coupling-rate bound does not deteriorate as the target becomes arbitrarily anisotropic.

## Assumptions and scope

Let \(S=\operatorname{diag}(1,\lambda)\), \(0<\lambda\leq1\), and \(J=\begin{psmallmatrix}0&-1\\1&0\end{psmallmatrix}\). The continuous Langevin model is \(dX_t=-SX_tdt+\sqrt2\lambda^{-1/2}JSX_t\circ d\beta_t+\sqrt2dW_t\). Replacing \(J\) by \(-J\) gives the same law. Set \(Y=S^{1/2}X\); its target distribution is \(\gamma_2\), and its Stratonovich rotational noise coefficient is \(\sqrt2 JY\).

For step \(h>0\), take fresh independent standard Gaussian variables \(\xi_1,\xi_2\in\mathbb R^2\) and \(\zeta\in\mathbb R\). Define \(D=\operatorname{diag}(e^{-h/2},e^{-\lambda h/2})\), \(R_\theta=\exp(\theta J)\) and \(\theta=\sqrt{2h}\zeta\). The **symmetric exact-subflow** update is
\[
 Y^{(1)}=DY_n+(I-D^2)^{1/2}\xi_1,\quad
 Y^{(2)}=R_\theta Y^{(1)},\quad
 Y_{n+1}=DY^{(2)}+(I-D^2)^{1/2}\xi_2.
\]
Both OU half-steps, including their independent noises, and the random rotation are performed exactly. The same \(\xi_1,\xi_2,\zeta\) are shared for synchronous coupling. Sampling the Gaussian angles and exact matrix exponentials is assumed; this statement makes no floating-point exactness claim.

## Proof

**1. Invariance and reversibility.** Each OU half-step is a coordinatewise stationary Gaussian OU transition, so it preserves \(\gamma_2\) and is self-adjoint on \(L^2(\gamma_2)\). Each rotation preserves \(\gamma_2\) because it is orthogonal. Its random-angle kernel is self-adjoint, since \(\theta\) and \(-\theta\) have identical laws and \(R_\theta^{-1}=R_{-\theta}\). The composition \(P_{h,\lambda}=P_{OU,h/2}P_{R,h}P_{OU,h/2}\) is therefore both \(\gamma_2\)-invariant and self-adjoint, proving detailed balance. Uniqueness follows from contraction below.

**2. Exact second-moment map.** Under synchronous coupling the Gaussian OU noises cancel. The difference satisfies \(e_{n+1}=DR_{\theta_n}De_n\). If \(Q_n=\mathbb E(e_ne_n^{\mathsf T})\), then \(Q_{n+1}=\mathbb E_\theta[DR_\theta DQ_nDR_\theta^{\mathsf T}D]\). The normal characteristic function gives \(\mathbb E\cos(2\theta)=k=e^{-4h}\) and \(\mathbb E\sin(2\theta)=0\). Hence for \(u_n=(Q_n)_{11}\), \(v_n=(Q_n)_{22}\),
\[
 \begin{pmatrix}u_{n+1}\\v_{n+1}\end{pmatrix}=
 M_{h,\lambda}\begin{pmatrix}u_n\\v_n\end{pmatrix},\qquad
 M_{h,\lambda}=\frac12\begin{pmatrix}(1+k)p&(1-k)\sqrt{pr}\\ (1-k)\sqrt{pr}&(1+k)r\end{pmatrix}.
\]
The off-diagonal moment is independently multiplied by \(k\sqrt{pr}\). The symmetric matrix \(M_{h,\lambda}\) has trace \((1+k)(p+r)/2\), determinant \(kpr\), and strictly positive entries. Its top eigenvalue is exactly \(\rho(h,\lambda)\); its other eigenvalue is positive. The off-diagonal eigenvalue satisfies \(k\sqrt{pr}<\sqrt{kpr}\leq\rho(h,\lambda)\). Perron--Frobenius positivity of the top eigenvector implies \(\lim_{n\to\infty}[\mathbb E\|e_n\|^2]^{1/n}=\rho(h,\lambda)\) whenever the initial difference \(e_0\) is a nonzero deterministic vector: the initial nonnegative diagonal moment vector has a strictly positive projection on the top eigenvector.

**3. Uniform sharp factor.** At fixed \(h>0\), \(p,k\) are constant and all nonconstant entries of \(M_{h,\lambda}\) strictly increase with \(r=e^{-2\lambda h}\). Therefore its Perron eigenvalue strictly decreases as \(\lambda\) increases. The supremum over positive \(\lambda\) is exactly the continuous endpoint \(\rho(h,0)\).

At this endpoint \(D=\operatorname{diag}(e^{-h/2},1)\). For every nonzero coordinate basis vector \(e_i\), \(\|DR_\theta De_i\|\leq1\) for every angle; the inequality is strict with positive probability because \(h>0\) and the Gaussian angle is not supported on integer multiples of \(\pi\). The two column sums of the nonnegative \(M_{h,0}\) are respectively \(\mathbb E\|DR_\theta De_1\|^2\) and \(\mathbb E\|DR_\theta De_2\|^2\), both strictly less than one. Consequently \(\rho(h,0)\leq\|M_{h,0}\|_1<1\), and \(0<\rho(h,\lambda)\leq\rho(h,0)<1\).

For \(h\downarrow0\), expand \(M_{h,0}=I+h\begin{psmallmatrix}-4&2\\2&-2\end{psmallmatrix}+O(h^2)\); the top eigenvalue of the coefficient matrix is \(-(3-\sqrt5)\). This proves the stated small-step law. For \(h\to\infty\), \(p,k\to0\) and \(M_{h,0}\to\operatorname{diag}(0,1/2)\), proving the large-step limit.

**4. Global \(W_2\) bound.** For any coupling of starting points, sharing step noises gives \(\mathbb E\|e_n\|^2=\mathbf1^{\mathsf T}M_{h,\lambda}^n(e_{0,1}^2,e_{0,2}^2)^{\mathsf T}\). Because \(M\) is symmetric with operator norm \(\rho\), Cauchy--Schwarz gives \(\mathbb E\|e_n\|^2\leq\sqrt2\rho(h,\lambda)^n\|e_0\|^2\). Integrate against an optimal initial coupling, taking its second marginal \(\gamma_2\), and use exact invariance and the definition of \(W_2\). This gives uniqueness among invariant laws with finite second moment. For uniqueness among arbitrary invariant probabilities, the final OU half-step has a positive, nondegenerate Gaussian transition density everywhere and smooths bounded measurable functions. Thus the full kernel is strong Feller and topologically irreducible, so it admits at most one invariant probability measure.

## Verification

A dependency-free Python file `verify_split.py` independently integrates Gaussian rotation angles by Simpson quadrature, compares the full diagonal and off-diagonal moment maps to the exact formulas on a parameter grid, checks determinant and spectral identities, validates the \(\sqrt2\) coupling bound on repeated iterations, and checks isotropy plus both endpoint limits. Run `python verify_split.py`. Its numerical finite grid is a consistency check, not a replacement for the preceding proof.

## Relationship to prior work

Louis, Pavliotis and Vilmart [1] introduce the rotational Stratonovich perturbation and prove the continuous-time spectral-gap guarantee for the same Gaussian family. Their Section 6.3 writes a symmetric splitting with exact OU substeps and numerical RK4 perturbation maps, and identifies rigorous analysis of the discretized process as open. Here the *exact Gaussian rotation* supplies a different, explicitly reversible discrete Markov transition, and the new quantitative object is its exact sharp squared-coupling spectral factor, uniform in \(\lambda\), with no invariant-distribution bias. Neither the continuous-time spectral-gap guarantee nor the general idea of splitting invariant substeps is presented as new.

The earlier reversible Stratonovich framework of Abdulle, Pavliotis and Vilmart [2] and the nonreversible Langevin splitting analysis of Duncan, Pavliotis and Zygalakis [3] provide background. The latter analyzes deterministic nonreversible drift splitting, not the random-rotation covariance matrix above. General splitting folklore establishes preservation and symmetry when exact subkernels are combined appropriately; it does not alone supply the explicit uniform Perron rate.

## Limitations

This is an exact-arithmetic, two-dimensional quadratic-target statement for the specifically defined exact-subflow Strang scheme. The Wasserstein upper bound's exponent is the *sharp synchronous squared-error exponent*, not a proved exact optimal \(W_2\) mixing exponent or an \(L^2(\gamma_2)\) spectral gap. It does not quantify sample-average asymptotic variance, computational wall-clock cost, bias of RK4 approximations, higher-dimensional or non-Gaussian dynamics, or finite-precision evaluation of sine/cosine and matrix exponentials. Literature equivalence with unlocated older specialized splitting calculations cannot be excluded.

## References

[1] G. Louis, G. A. Pavliotis, G. Vilmart, *Reversible Stratonovich perturbations for accelerating convergence to equilibrium of Langevin dynamics*, arXiv:2610.03191v1 (first public 2026-10-02), especially Theorem 2 and Section 6.3, https://arxiv.org/abs/2610.03191.

[2] A. Abdulle, G. A. Pavliotis, G. Vilmart, *Accelerated convergence to equilibrium and reduced asymptotic variance for Langevin dynamics using Stratonovich perturbations*, Comptes Rendus Mathématique 357 (2019), 349--354, arXiv:1903.03024, https://arxiv.org/abs/1903.03024.

[3] A. B. Duncan, G. A. Pavliotis, K. C. Zygalakis, *Nonreversible Langevin samplers: Splitting schemes, analysis and implementation*, arXiv:1701.04247 (2017), https://arxiv.org/abs/1701.04247.
