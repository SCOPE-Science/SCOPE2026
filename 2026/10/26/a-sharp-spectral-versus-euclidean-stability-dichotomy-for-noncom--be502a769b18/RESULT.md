# A sharp spectral-versus-Euclidean stability dichotomy for noncommuting exponential Euler

## Finding

Let \(H,K\) be real symmetric positive-definite \(d\times d\) matrices, \(d\ge1\), not necessarily commuting. Apply exponential Euler to \(\dot u=-Ku\) after splitting its vector field into \(-Hu+(H-K)u\). At every positive step \(h\) the exact iteration is
\[
S_h=I-W_hK,\qquad W_h=H^{-1}(I-e^{-hH}).
\]
The following statements hold.

**Exact unconditional stability and physical-energy criterion.** Every positive step is strictly Schur stable, equivalently strictly contractive in the *same*, step-independent quadratic energy \(\|u\|_K^2=u^\mathsf TKu\), exactly when
\[
\boxed{K\preceq2H.}
\]
When this Loewner inequality fails, every sufficiently large step is Schur unstable. Under the inequality, the energy decreases at each nonzero step, including for arbitrarily varied positive steps (without a uniform convergence-rate claim for arbitrary step sequences).

**Sharp Euclidean amplification law.** Under \(0\prec K\preceq2H\), for every \(h>0\),
\[
\|S_h\|_2\le\sqrt{\kappa_2(W_h)}\le\sqrt{\kappa_2(H)}.
\]
For every fixed positive-definite \(H\), this dimension-free last bound is optimal:
\[
\boxed{\sup_{h>0,\;0\prec K\preceq2H}\|S_h\|_2=\sqrt{\kappa_2(H)}.}
\]
Moreover, \(\|S_h\|_2\le1\) for every admissible \(K\) and every \(h>0\) **if and only if \(H\) is a scalar multiple of the identity**. If \(H\) has two distinct eigenvalues, then for each fixed \(h>0\) there exists an admissible positive-definite \(K\) for which \(\|S_h\|_2>1\). Thus no positive universal Euclidean-nonexpansivity step size exists for a nonscalar reference operator, despite strict spectral and physical-energy stability.

An exact nondegenerate witness uses
\[
H=\begin{pmatrix}4&0\\0&1\end{pmatrix},\quad
K=\begin{pmatrix}4&-9/5\\-9/5&1\end{pmatrix},\quad h=\log2.
\]
Both \(K\) and \(2H-K\) are positive definite, and
\[
S_h=\begin{pmatrix}1/16&27/64\\9/10&1/2\end{pmatrix},\qquad
\frac{\|S_h(1,1)^\mathsf T\|_2^2}{\|(1,1)^\mathsf T\|_2^2}
=\frac{224729}{204800}>1.
\]

## Assumptions and scope

All matrices are finite-dimensional real symmetric positive definite; \(A\preceq B\) means \(B-A\) is positive semidefinite. The eigenvalue condition number is \(\kappa_2(H)=\lambda_{\max}(H)/\lambda_{\min}(H)\). Matrix exponentials and \(\varphi_1\) are evaluated exactly. The split treats \(-H\) in the exponential and the remaining linear term \(H-K\) explicitly. The physical quadratic energy is \(E(u)=u^\mathsf TKu/2\); the Euclidean squared norm is a different quantity. Each supremum permits \(K\) to depend on \(h\) and is not asserted to be attained by any admissible finite step.

The first public motivating preprint is the 28 March 2023 version of Caliari--Cassini--Einkemmer--Ostermann, arXiv:2303.15861, primary MSC2020 65L05. Its Theorem 2.1 treats the scalar Fourier-mode splitting. No assertion of an unrestricted PDE operator result, of componentwise positivity, or of floating-point stability is made here.

## Proof

**1. Exact map and sharp Loewner condition.** Since \(\varphi_1(z)=(e^z-1)/z\), direct substitution into exponential Euler gives \(S_h=I-W_hK\), where \(W_h\) is symmetric positive definite. The matrix
\[
A_h=K^{1/2}W_hK^{1/2}
\]
is symmetric positive definite and \(K^{1/2}S_hK^{-1/2}=I-A_h\). The scalar inequality \(0<1-e^{-h\lambda}<1\), for \(\lambda>0\), gives
\[
0\prec W_h\prec H^{-1},\qquad A_h\prec K^{1/2}H^{-1}K^{1/2}.
\]
The largest eigenvalue of the latter matrix is the largest eigenvalue of \(H^{-1/2}KH^{-1/2}\). If \(K\preceq2H\), it is at most \(2\), so every eigenvalue of \(A_h\) is strictly between \(0\) and \(2\). It follows that
\[
\rho(S_h)=\|I-A_h\|_2=\|S_h\|_K<1,
\]
where the displayed equality involving \(\rho\) uses similarity, and \(\|S_h\|_K\) denotes the operator norm induced by \(u^\mathsf TKu\). Thus every nonzero step decreases that same energy independently of any other steps chosen. Conversely, if \(K\npreceq2H\), then \(K^{1/2}H^{-1}K^{1/2}\) has an eigenvalue \(>2\); since \(W_h\to H^{-1}\) as \(h\to\infty\), continuity forces an eigenvalue of \(S_h\) below \(-1\) for all sufficiently large \(h\).

**2. Universal Euclidean upper bound.** Another similarity writes
\[
W_h^{-1/2}S_hW_h^{1/2}=I-W_h^{1/2}KW_h^{1/2}.
\]
The right-hand side is symmetric and has all eigenvalues in \((-1,1)\) under the Loewner condition. Hence \(\|S_h\|_2\le\sqrt{\kappa_2(W_h)}\). Its eigenvalues are \(w_h(\lambda)=(1-e^{-h\lambda})/\lambda\), strictly decreasing in \(\lambda>0\), as follows by differentiating and using \(e^x>1+x\). If \(a\) and \(b\) are the smallest and largest eigenvalues of \(H\),
\[
\kappa_2(W_h)=\frac ba\frac{1-e^{-ha}}{1-e^{-hb}}\le\frac ba=\kappa_2(H),
\]
with strict inequality if \(a<b\) and \(h\) is finite.

**3. Sharpness.** If \(a<b\), take orthonormal eigenvectors corresponding to these extreme eigenvalues. Let \(Q\) interchange the two vectors and vanish on their orthogonal complement. For \(0<\eta<1\), define
\[
K_\eta=H^{1/2}(I-\eta Q)H^{1/2}.
\]
The eigenvalues of \(I-\eta Q\) lie strictly between \(0\) and \(2\), so \(0\prec K_\eta\prec2H\). As \(h\to\infty\),
\[
S_h\longrightarrow I-H^{-1}K_\eta=\eta H^{-1/2}QH^{1/2}.
\]
On the extreme-eigenvector plane its two off-diagonal entries have absolute values \(\eta\sqrt{b/a}\) and \(\eta\sqrt{a/b}\), and all other entries vanish. Its Euclidean norm is \(\eta\sqrt{b/a}\). Let \(\eta\uparrow1\), giving the claimed supremum. For scalar \(H\), \(S_h\) is symmetric, so the norm bound is at most one; the supremum one is approached as \(h\downarrow0\).

**4. Nonexpansivity fails at every fixed step for nonscalar \(H\).** Choose a unit vector \(u\) with nonzero components along two eigenvectors belonging to distinct eigenvalues of \(H\). Let \(K_0=2H^{1/2}uu^\mathsf TH^{1/2}\), temporarily semidefinite. Write \(S_0=I-ab^\mathsf T\), where \(a=2W_hH^{1/2}u\) and \(b=H^{1/2}u\). The strict decrease of \(w_h(\lambda)\) implies that \(a\) and \(b\) are not parallel. In an orthonormal basis whose first vector is parallel to \(b\), the restriction of \(S_0\) to the plane of \(a,b\) has form
\[
\begin{pmatrix}\xi&0\\\zeta&1\end{pmatrix},\qquad\zeta\ne0.
\]
The determinant of this block's \(S_0^\mathsf TS_0-I\) is \(-\zeta^2<0\). Thus \(\|S_0\|_2>1\). Now take \(K_\varepsilon=H^{1/2}[2(1-\varepsilon)uu^\mathsf T+\varepsilon(I-uu^\mathsf T)]H^{1/2}\). For sufficiently small \(\varepsilon>0\), both \(K_\varepsilon\) and \(2H-K_\varepsilon\) are positive definite, and continuity preserves \(\|S_h\|_2>1\). This works for each prescribed positive \(h\), without claiming a single \(K\) works for all \(h\).

**5. Exact rational witness.** At \(h=\log2\), \(W_h=\operatorname{diag}(15/64,1/2)\). Both \(K\) and \(2H-K\) have leading diagonal entry \(4\) and determinant \(19/25\), so are positive definite. Direct multiplication yields the displayed rational matrix \(S_h\). Its image of \((1,1)^\mathsf T\) is \((31/64,7/5)^\mathsf T\), and exact squaring yields \(224729/204800>1\).

## Verification

The accompanying standalone Python standard-library verifier reproduces every entry of the rational witness, verifies the two positive-definiteness tests with exact fractions, and checks the strict Euclidean norm inequality with an exact fraction. It also performs 336 deterministic parameter checks for the two-dimensional family used for sharpness. The latter are finite diagnostics, **not** proofs of the quantified statements above; the proof is the matrix similarity, Loewner comparison, and rank-one perturbation argument.

Run: `python3 verify.py`. No external dependencies are required.

## Relationship to prior work

Caliari, Cassini, Einkemmer, and Ostermann (2023), Theorem 2.1, establish the classical threshold for exponential Euler applied to a commuting scalar Fourier-mode split of the heat equation. That scalar condition is the motivating case of the Loewner criterion, but does not state the sharp norm-amplification dichotomy or the universal anisotropic counterexample. D'Autilia, Sgura, and Simoncini (2019) study matrix-oriented exponential integration and scalar-mode stability, not this full noncommuting split. General preconditioned Richardson and weighted-Jacobi theory explains why a symmetric similarity may coexist with Euclidean nonnormality; that general principle is background, not claimed as new. The assessed statement is the *combined sharp result for this exponential-Euler operator family*, especially the any-step nonexpansivity impossibility and exact \(\sqrt{\kappa_2(H)}\) supremum. A recent paper on splitting exponential-like matrix functions for noncommuting operators studies a different operation; its full text was not available for comparison.

## Limitations

The claim assumes finite-dimensional symmetric positive-definite operators and exact arithmetic; nonsymmetric advection, singular Laplacians, componentwise positivity, PDE discretization error, and nonconstant operator splittings are not covered. All-step strict contraction need not imply convergence under an arbitrary sequence of steps approaching zero too quickly. The Euclidean supremum is a supremum over admissible \(K\) and step sizes, not a maximum. Publication priority remains subject to comparison with uncatalogued specialized work on preconditioned stationary iterations and nonnormal transient amplification; no independent audit has been performed.

## References

1. M. Caliari, F. Cassini, L. Einkemmer, A. Ostermann, *Accelerating exponential integrators to efficiently solve semilinear advection-diffusion-reaction equations*, arXiv:2303.15861 (first public version 2023-03-28), especially Theorem 2.1, Section 2, and Appendix. https://arxiv.org/abs/2303.15861
2. M. C. D'Autilia, I. Sgura, V. Simoncini, *Matrix-oriented discretization methods for reaction-diffusion PDEs: comparisons and applications*, arXiv:1903.05030 (2019), especially Sections 2, 4.1 and 7. https://arxiv.org/abs/1903.05030
3. M. Hochbruck and A. Ostermann, *Exponential integrators*, Acta Numerica 19 (2010), 209-286, overview of exponential time stepping (background; not relied upon for any claimed novelty).
4. L. Battestini, M. Caliari, F. Cassini, *Analysis of split exponential integrators for semilinear problems with noncommuting operators*, arXiv:2610.07989 (2026), abstract-level comparison only; full text not inspected. https://arxiv.org/abs/2610.07989
