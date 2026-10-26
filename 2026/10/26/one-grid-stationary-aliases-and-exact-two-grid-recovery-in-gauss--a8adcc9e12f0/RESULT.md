# One-grid stationary aliases and exact two-grid recovery in Gaussian Euler--Maruyama dynamics

## Finding

A symmetric dissipative Ornstein--Uhlenbeck drift and its unknown isotropic Brownian diffusion strength can be recovered **uniquely from the stationary marginal laws of two different Euler--Maruyama time steps**, without temporal trajectories. At one step size, the same inverse problem has a complete square-root fiber, ranging from finitely many sign choices to continuous Grassmann families. In contrast, stationary marginals of the *exact* continuous-time process at arbitrarily many sampling intervals do not separate drift scale and noise intensity.

Precisely, for an integer \(d\ge1\), let \(A=A^\top\succ0\), \(q>0\), and \(h>0\) with \(0<h\lambda_{\max}(A)<2\). The Euler--Maruyama recursion for \(dX_t=-AX_t\,dt+\sqrt{2q}\,dW_t\) is
\[
X_{k+1}=(I-hA)X_k+\sqrt{2qh}\,\xi_k,\qquad \xi_k\stackrel{\mathrm{iid}}\sim N(0,I).
\]
Its unique stationary law is \(N(0,C_h)\) with
\[
C_h=q\left(A-\frac h2 A^2\right)^{-1},\qquad P_h:=C_h^{-1}=\frac Aq-\frac{hA^2}{2q}. \tag{1}
\]

**One-grid classification, known \(q\).** A prescribed positive-definite covariance \(C\) is realizable at a specified \(h\) if and only if \(C\succeq2qhI\). Its complete inverse fiber is
\[
\left\{A=\frac{I-S}{h}:\quad S=S^\top,\quad S^2=I-2hqC^{-1}\right\}. \tag{2}
\]
If \(C\) has \(d\) distinct eigenvalues all strictly above \(2qh\), the fiber has exactly \(2^d\) elements. A repeated eigenvalue strictly above the threshold, of multiplicity at least two, creates uncountably many distinct solutions, parameterized by orthogonal decompositions of its eigenspace; eigenvalues at the threshold force the corresponding sign to zero. The involution \(A\mapsto2I/h-A\) preserves the one-grid stationary law whenever the reflected drift remains inside the stable class (which it always does under the stated hypotheses).

**Two-grid identification, unknown \(q\).** Let \(h_1,h_2>0\), \(h_1\ne h_2\), and suppose both Euler schemes are stable for the same unknown pair \((A,q)\). Set \(P_j=C_{h_j}^{-1}\), and calculate
\[
U=\frac{h_2P_1-h_1P_2}{h_2-h_1},\qquad
V=\frac{2(P_1-P_2)}{h_2-h_1}. \tag{3}
\]
Then \(U=A/q\), \(V=A^2/q\), and exact reconstruction is
\[
\boxed{A=VU^{-1},\qquad q=\frac1d\operatorname{tr}(VU^{-2}).} \tag{4}
\]
In particular, two grid resolutions are sufficient, while one is not generally sufficient even if \(q\) is known. A pair of arbitrary positive-definite matrices \((C_1,C_2)\) can arise in this model at the specified resolutions if and only if \(U\succ0\), there is a scalar \(q>0\) such that \(V=qU^2\), and \(h_j q\lambda_{\max}(U)<2\) for \(j=1,2\). In that case (4) recovers the unique admissible parameters.

With known \(q\), if the observed precision matrices have errors \(E_j\), the explicit reconstruction \(\widehat A=q(h_2\widehat P_1-h_1\widehat P_2)/(h_2-h_1)\) satisfies the sharp algebraic estimate
\[
\|\widehat A-A\|_2\le q\frac{h_2\|E_1\|_2+h_1\|E_2\|_2}{|h_2-h_1|}. \tag{5}
\]
Thus exact identification becomes ill-conditioned when the two step sizes coalesce. The algebraic coefficient is attained with opposite scalar precision perturbations.

**Class boundary.** Symmetry is essential. In two dimensions, write \(J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\), \(A_\pm=\kappa I\pm\omega J\), where \(\kappa>0\), \(\omega\ne0\). For every \(0<h<2\kappa/(\kappa^2+\omega^2)\), both nonsymmetric Euler recursions are stable and have identical stationary marginal
\[
N\left(0,\;\frac{q}{\kappa-h(\kappa^2+\omega^2)/2}I\right). \tag{6}
\]
Therefore an arbitrarily large collection of resolutions cannot identify the sign of rotational drift outside the symmetric class.

## Assumptions and scope

The results concern exact stationary *one-time Gaussian marginals* of Euler simulations at designated, known grid steps. All coordinates are observed; the diffusion matrix is an **unknown scalar multiple of the identity**, the same across grid resolutions. The drift is real symmetric positive definite except in the explicit nonreversible counterexample. All steps satisfy the strict discrete stability boundary \(h\lambda_{\max}(A)<2\). The noise sequences need not be coupled between simulations at different resolutions. Matrix inequalities use Loewner order. All identities are exact, not asymptotic, and cover arbitrary finite dimension. No assertion is made about finite sampled empirical covariances.

For the continuous-time comparison, the same SDE has stationary covariance \(C_*=qA^{-1}\); samples of stationary one-time marginals at different temporal intervals always have this same \(C_*\). The unobserved transitions and temporal correlations are explicitly *not* part of the data. This is why jointly rescaling \(A\) and \(q\) by any positive factor leaves all those continuous-time marginals unchanged.

## Proof

**1. Discrete Lyapunov equation.** Define \(B_h=I-hA\). Under \(0<h\lambda_{\max}(A)<2\), \(B_h\) is symmetric with spectral radius strictly below one. The linear Gaussian Markov recursion has a unique zero-mean stationary law and its covariance solves
\[
C_h=B_hC_hB_h^\top+2qhI,
\quad C_h=2qh\sum_{n=0}^\infty B_h^{2n}.
\]
Because \(B_h\) is symmetric, the convergent series is \(2qh(I-B_h^2)^{-1}\). Since \(I-B_h^2=2hA-h^2A^2\), canceling \(2h\) gives (1). Gaussianity is inherited from Gaussian innovations and the convergent stationary linear series.

**2. Complete one-step inverse fiber.** From (1), \(2hqC^{-1}=2hA-h^2A^2=I-(I-hA)^2\). Put \(S=I-hA\): it is a real symmetric square root of \(I-2hqC^{-1}\), yielding (2). Conversely, if \(C\succeq2hqI\), then \(D=I-2hqC^{-1}\) is symmetric positive semidefinite; since \(C\succ0\), all eigenvalues of \(D\) lie in \([0,1)\). Every real symmetric square root \(S\) of \(D\) therefore has all eigenvalues in \((-1,1)\); \(A=(I-S)/h\) is SPD, stable, and (1) recovers \(C\). Conversely (1) implies \(C\succeq2hqI\), because each scalar \(a-ha^2/2\) is positive and at most \(1/(2h)\) for \(0<a<2/h\).

To count the fiber, \(S\) commutes with its square \(D\), so each eigenspace of \(D\) is invariant. When an eigenvalue \(\delta>0\) of \(D\) has multiplicity \(m\), the corresponding block of \(S\) is \(\sqrt\delta(2\Pi-I)\) for an arbitrary orthogonal projector \(\Pi\) on that eigenspace: indeed, division by \(\sqrt\delta\) gives a symmetric involution, whose \(+1\) eigenspace is the projector range. Rank \(r\) projectors are a Grassmann manifold \(\mathrm{Gr}(r,m)\); if \(m=1\), just two signs, whereas if \(m\ge2\) and \(1\le r<m\), there are continuum many. At \(\delta=0\), symmetry forces \(S=0\) on that block. Since \(D\) is a matrix function of \(C\), this gives the counts and the exact fiber.

**3. Recovering both unknowns at two resolutions.** Equation (1) makes \(P_h\) an *affine matrix function of the step size*: \(P_h=A/q-hA^2/(2q)\). Eliminating the slope gives precisely \(U=A/q\) and \(V=A^2/q\) in (3). Because \(A\succ0\) and \(q>0\), \(U\) is invertible. Hence \(VU^{-1}=A\), and \(VU^{-2}=qI\), proving (4) and uniqueness. For sufficiency of the data consistency criterion, assume \(U\succ0\), \(V=qU^2\) and the two stability inequalities. Define \(A=qU\), then \(V=A^2/q\). Inverting the two defining linear equations (3) gives \(P_j=U-h_jV/2\); these are positive definite under stability, and equation (1) yields the exact observed \(C_j\). Necessity has already been proved.

**4. Precision sensitivity.** With fixed known \(q\), subtract the reconstruction (3) from the same algebraic estimator computed using \(P_j+E_j\). The error is \(q(h_2E_1-h_1E_2)/(h_2-h_1)\); the operator-norm triangle inequality is (5). Taking \(E_1=tI\), \(E_2=-tI\) for \(t>0\) gives equality. Perturbations are algebraic precision errors; no stochastic sampling assertion is implied.

**5. Continuous-time and nonsymmetric limits.** The continuous Lyapunov equation is \(AC_*+C_*A=2qI\), and symmetry gives \(C_*=qA^{-1}\); the scaling ambiguity follows immediately. For the nonsymmetric witness, since \(J^\top=-J\) and \(J^2=-I\), the Euler transition matrices \(B_\pm=(1-h\kappa)I\mp h\omega J\) satisfy \(B_\pm B_\pm^\top=((1-h\kappa)^2+h^2\omega^2)I\). The stated range of \(h\) is exactly the strict condition that this scalar be less than one. Substituting \(C_h=cI\) in the Lyapunov equation gives \(c=2qh/[1-(1-h\kappa)^2-h^2\omega^2]\), which simplifies to (6), independent of rotational sign. This completes all assertions.

## Verification

Run the included standard-library checker using `python check_stationary_ou.py` from the extracted file directory. It performs 63 exact-rational configurations: diagonal and rotated SPD drifts with unknown \(q\), stationary discrete Lyapunov identities and recovery at two steps, eight independent sign aliases at one step, repeated-eigenvalue rotated fibers, a sharp precision-error witness, and opposite-circulation examples. The checker reports success if and only if each exact assertion passes. Its finite tests are not proofs of the universal matrix theorem; the proof above supplies the infinite-family argument. In particular, the Grassmannian cardinality follows from the projector parametrization, not three tested rotations.

For an explicit one-step alias example with \(d=3\), \(h=q=1\), take \(A=\mathrm{diag}(1/3,1/2,3/4)\). Independently replacing any diagonal entry \(a\) with \(2-a\) produces the same covariance, and all eight drifts are SPD and Euler-stable. For a continuous family, \(C=(8/3)I\), \(h=q=1\), has drifts \(A=R\mathrm{diag}(1/2,3/2)R^\top\) for every orthogonal \(2\times2\) matrix \(R\).

## Relationship to prior work

Wang and Wu (arXiv:2604.14543; Sections 2–5) establish numerical invariant measures and Wasserstein convergence for Euler schemes applied to McKean–Vlasov SDEs; their problem is *forward approximation of invariant measures*, not inversion from one-time stationary laws at distinct numerical step sizes. The linear Ornstein--Uhlenbeck class here is a motivated exactly solvable test case, not a claim to generalize their convergence theorem.

Higham (SIAM Review 43, 2001; numerical Euler--Maruyama and mean-square stability sections) develops the classical linear Euler discretization and stability analysis. The scalar stationary AR(1) variance and the ambiguity of the sign of its autoregression coefficient are elementary prior ingredients. Neither the scalar AR(1) formula nor elementary eigenvalue calculations are claimed as new. The specific assessed contribution is the complete *matrix inverse fiber*, including Grassmann families and realizability boundary, combined with the exact recovery of **unknown drift and noise intensity from two stationary numerical resolutions**, the consistency criterion, and the sharp limitations outside reversibility.

Tran, Tran, and Nguyen (arXiv:2601.20268; Methods, Theorem 3) identify drift and diffusion coefficients from **temporally ordered transition observations**. Their premise supplies conditional transitions and is strictly more informative than the stationary one-time marginals used here. Thus their ordered-trajectory identification does not imply the present two-grid stationary-marginal inverse theorem by its stated assumptions. Related multilevel parameter-inference works use trajectories, couplings or posterior likelihoods rather than only exact marginal stationary covariances.

## Limitations

The results make no inference promise from finite noisy samples. Because the estimator inverts empirical covariances, small eigenvalues and closely spaced steps can amplify error. Formula (5) treats arbitrary precision perturbations only when \(q\) is already known; there is no asserted global Lipschitz bound for joint unknown-\(q\) inversion. The diffusion covariance must be isotropic and common across experiments, the drift symmetric positive definite, and the entire state observed. Nonreversible drifts demonstrably retain rotational ambiguity even with arbitrarily many resolutions. For any fixed finite set of numerical resolutions, the data must come from actual stationary Euler models satisfying stability. The classification is not about the exact continuous-time transition kernel, finite-horizon distributions, or trajectories.

The proof is self-contained. Historical priority is not claimed established beyond the inspected literature: matrix spectral square-root fibers and extrapolation of modified numerical invariant measures may have been recorded in other forms, and classical Gaussian AR(1) identification theory provides ingredients. A targeted independent bibliographic review remains worthwhile before public claims of priority.

## References

1. Z. Wang and M. Wu, *The Euler-Maruyama method for invariant measures of McKean-Vlasov stochastic differential equations*, arXiv:2604.14543 (first public 2026-04-16), https://arxiv.org/abs/2604.14543. Relevant material: introduction, Theorems 2.1–2.4 and numerical-invariant-measure sections.
2. D. J. Higham, *An Algorithmic Introduction to Numerical Simulation of Stochastic Differential Equations*, SIAM Review 43 (2001), 525–546, DOI:10.1137/S0036144500378302. Relevant material: Euler--Maruyama and numerical stability.
3. L. V. Tran, T. Tran, and P. Nguyen, *Robust SDE Parameter Estimation Under Missing Time Information Setting*, arXiv:2601.20268 (2026), https://arxiv.org/abs/2601.20268. Relevant material: Methods, Theorem 3 and transition-data estimator.
4. K. Hellmuth, Q. Li, and Y. Yang, *Two Adjoint Perspectives on Fokker-Planck Optimization*, arXiv:2609.02072 (2026), https://arxiv.org/abs/2609.02072. Related context on numerical-versus-continuum optimization, not an inverse stationary-Gaussian recovery theorem.
