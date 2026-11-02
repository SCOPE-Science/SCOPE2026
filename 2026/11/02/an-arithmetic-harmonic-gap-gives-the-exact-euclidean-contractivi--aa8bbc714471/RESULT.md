# An arithmetic–harmonic gap gives the exact Euclidean contractivity horizon of rank-one IMEX Euler

## Finding

Let \(B\) be any real symmetric positive-definite matrix of order \(n\ge2\), let \(u\) be a unit vector, and let \(\rho>0\). Split the dissipative linear equation \(x'=-(A+B)x\) by assigning \(A=B+\rho uu^{\mathsf T}\) to implicit Euler and \(B\) to explicit Euler. Its step matrix is

\[
M_h=(I+hA)^{-1}(I-hB).
\]

Every finite positive step is strictly stable in the spectral-radius sense: all eigenvalues of \(M_h\) are real and belong to \((-1,1)\). However, its one-step Euclidean norm need not be at most one, even though \(A\succeq B\).

Put

\[
\alpha=u^{\mathsf T}Bu,\qquad
\lambda=\alpha-\frac1{u^{\mathsf T}B^{-1}u},\qquad
\kappa=\frac{2\lambda}{2\alpha+\rho},\qquad
\delta=\sqrt{1-\kappa}.
\]

Here \(0\le\kappa<1\). When \(\lambda=0\), \(\|M_h\|_2<1\) for every finite \(h>0\). When \(\lambda>0\), set

\[
\boxed{h_*=\frac{4\delta}{\rho(1-\delta)}.}
\]

Then the *exact* Euclidean nonexpansiveness set is \(0\le h\le h_*\). Strict contraction holds at every positive interior step, equality holds at the positive endpoint, and the norm is greater than one at every larger step.

For a two-eigenvalue matrix \(B=\operatorname{diag}(b_1,b_2)\), where \(b_1,b_2>0\) and \(b_1\ne b_2\), and \(u=(\cos\theta,\sin\theta)\), the noncommuting cutoff satisfies

\[
h_*\sim \frac{4b_2(2b_1+\rho)}{\rho(b_2-b_1)^2\theta^2}
\quad\text{as }\theta\to0,\quad\theta\ne0.
\]

Thus the all-step Euclidean contractivity property at an eigendirection is destroyed by an arbitrarily small angular perturbation; its replacement cutoff diverges at the sharp inverse-square angular rate.

## Assumptions and scope

The results hold for every integer \(n\ge2\), every real symmetric \(B\succ0\), every unit \(u\), every \(\rho>0\), and each real step \(h\ge0\). The operator norm is induced by the ordinary Euclidean vector norm, not the changing \((I+hA)\)-weighted norm. This is deterministic exact-arithmetic first-order IMEX Euler. No simultaneous diagonalizability or distinct-eigenvalue assumption is needed for the main theorem. The two-dimensional angular asymptotic additionally assumes distinct positive eigenvalues.

## Proof

**1. Spectral stability.** Set \(S=I+hA\) and \(T=I-hB\). For \(h>0\), \(S\succ0\) and \(M_h=S^{-1}T\) is similar to the real symmetric matrix \(K=S^{-1/2}TS^{-1/2}\). Moreover,

\[
S-T=h(A+B)\succ0,\qquad S+T=2I+h(A-B)=2I+h\rho uu^{\mathsf T}\succ0.
\]

Hence \(-I\prec K\prec I\), proving that the eigenvalues of \(M_h\) are real and strictly between \(-1\) and \(1\). The fixed-step powers converge to zero because this matrix is diagonalizable over \(\mathbb R\).

**2. Convert the norm condition into a symmetric pencil.** Since \(S,T\) are symmetric, \(M_hM_h^{\mathsf T}=S^{-1}T^2S^{-1}\). Congruence by \(S\) gives

\[
\|M_h\|_2\le1
\iff T^2\preceq S^2
\iff 2(A+B)+h(A^2-B^2)\succeq0
\quad(h>0).
\]

At \(h=0\), \(M_0=I\). In general \(A\succeq B\) alone does not imply \(A^2\succeq B^2\) when the factors do not commute.

**3. Exact rank-one Schur reduction.** Complete \(u\) to an orthonormal basis. In this basis write

\[
B=\begin{pmatrix}\alpha&g^{\mathsf T}\\g&C\end{pmatrix},
\qquad C\succ0.
\]

With \(A=B+\rho uu^{\mathsf T}\), direct multiplication gives

\[
2(A+B)+h(A^2-B^2)
=\begin{pmatrix}
4\alpha+2\rho+h\rho(2\alpha+\rho)&(4+h\rho)g^{\mathsf T}\\
(4+h\rho)g&4C
\end{pmatrix}.
\]

The Schur complement of \(4C\) is

\[
2(2\alpha+\rho)(1+2t)-4\lambda(1+t)^2,
\qquad t=\frac{h\rho}{4},
\qquad\lambda=g^{\mathsf T}C^{-1}g.
\]

The block-inverse identity yields \(\alpha-g^{\mathsf T}C^{-1}g=(u^{\mathsf T}B^{-1}u)^{-1}\); thus \(\lambda\) equals the stated arithmetic–harmonic Rayleigh gap. Since \(B\succ0\), \(0\le\lambda<\alpha\) and \(0\le\kappa<1\). The gap vanishes precisely when \(g=0\), equivalently \(Bu\) is parallel to \(u\).

Dividing the Schur complement by \(2(2\alpha+\rho)\) shows that the norm condition is exactly

\[
F(t):=1+2t-\kappa(1+t)^2\ge0.
\]

If \(\kappa=0\), \(F(t)>0\) for every \(t\ge0\). Otherwise \(F\) is a concave quadratic, is positive at zero, and has the unique positive root

\[
t_*=\frac{\sqrt{1-\kappa}}{1-\sqrt{1-\kappa}}=\frac{\delta}{1-\delta}.
\]

Consequently the pencil is positive definite on \(0<h<h_*\), positive semidefinite but singular at \(h=h_*\), and indefinite beyond. Congruence in Step 2 gives the exact norm trichotomy.

**4. Sharp angular singularity and rational witness.** In the two-dimensional eigenbasis, \(g=(b_2-b_1)\sin\theta\cos\theta\) up to sign and \(C=b_1\sin^2\theta+b_2\cos^2\theta\). Thus

\[
\lambda=\frac{(b_2-b_1)^2\sin^2\theta\cos^2\theta}{b_1\sin^2\theta+b_2\cos^2\theta}
\sim\frac{(b_2-b_1)^2}{b_2}\theta^2.
\]

Since \(\delta/(1-\delta)\sim(2\alpha+\rho)/\lambda\), the displayed asymptotic follows. The order cannot be improved: the ratio of the exact cutoff to the stated asymptotic expression converges to one.

For a concrete rational example choose

\[
B=\begin{pmatrix}1&0\\0&9\end{pmatrix},\quad
A=\begin{pmatrix}2&1\\1&10\end{pmatrix},\quad
\rho=2,\quad u=2^{-1/2}(1,1)^{\mathsf T}.
\]

Here \(A-B\succeq0\), \(\kappa=8/15\), and \(h_*=2\sqrt{7/15}/(1-\sqrt{7/15})\approx4.31173769149\). At \(h=5\), the norm-defining pencil is

\[
2(A+B)+5(A^2-B^2)=\begin{pmatrix}26&62\\62&138\end{pmatrix},
\qquad\det=-256<0.
\]

The step therefore expands some Euclidean vector at \(h=5\), although all its eigenvalues still have absolute value strictly smaller than one.

## Verification

Run `python verification.py` from the directory containing this file and `verification.py`. The pure-standard-library checker verifies the exact negative-determinant witness, a closed-form cutoff, 1,364 randomized tests of the norm threshold in dimensions two through four, and the inverse-square angular asymptotic at three decreasing angles. This is finite numerical and rational checking of examples, not a substitute for the all-dimensional Schur-complement proof. All exact identities used for the theorem are displayed above.

## Relationship to prior work

The IMEX schemes of Barrenechea, Castillo and Pacheco (2023, Sections 3, 5 and 6) distinguish unconditional and conditional energy estimates for variable-viscosity flow, with stability depending on the chosen split and norm. Their concrete PDE discretizations and Gronwall estimates do not state the present all-dimensional sharp Euclidean-norm cutoff for the constant symmetric rank-one matrix family. Ma, Huang and Yong (2023, Sections 2–3) study Fourier-discretized hyperbolic relaxation and multiplier stability of IMEX-BDF methods, not the present rank-one dissipative Euler pencil. Classical split-Runge–Kutta contractivity studies, including Bellen and Torelli (1997), address related stability concepts; no new method family or a general absence of prior research is claimed here.

The ingredients of matrix congruence, block inversion and Schur complements are standard. The contribution assessed here is their exact synthesis into an unconditional-spectral-versus-conditional-Euclidean separation, an all-dimensional arithmetic–harmonic-gap cutoff, and its sharp angular singularity for the rank-one-dominance model. Searches did not identify an equivalent published classification. A specialized result not uncovered by these searches remains a publication-priority risk.

## Limitations

A per-step Euclidean norm above one is transient amplification, **not** divergence: every fixed-step recurrence here converges to zero. The result concerns the finite-dimensional symmetric positive-definite family \(A-B=\rho uu^{\mathsf T}\), with exact solves and a fixed timestep. It does not assert behavior for general indefinite/nonsymmetric splits, arbitrary-rank increments, nonlinear or fully discretized fluid equations, errors caused by finite precision, or uniform bounds as \(h\) and the matrix dimension vary jointly. The result has not undergone independent scientific audit.

## References

1. G. R. Barrenechea, E. Castillo and D. R. Q. Pacheco, *Implicit-explicit schemes for incompressible flow problems with variable viscosity*, arXiv:2310.04182v1 (first posted 2023-10-06), https://arxiv.org/html/2310.04182v1 .
2. Z. Ma, J. Huang and W.-A. Yong, *Uniform accuracy of implicit-explicit backward differentiation formulas (IMEX-BDF) for linear hyperbolic relaxation systems*, arXiv:2310.05342v1 (first posted 2023-10-09), https://arxiv.org/html/2310.05342v1 .
3. A. Bellen and L. Torelli, *Unconditional Contractivity in the Maximum Norm of Diagonally Split Runge–Kutta Methods*, SIAM J. Numer. Anal. 34 (1997), 528–543, https://doi.org/10.1137/S0036142994267576 .
