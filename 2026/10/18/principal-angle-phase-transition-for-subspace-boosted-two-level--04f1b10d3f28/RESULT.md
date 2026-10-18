# Principal-angle phase transition for subspace-boosted two-level systems

## Finding

Consider a symmetric positive-definite linear system with two spectral levels: a low eigenspace of dimension \(k\) at eigenvalue \(\mu\) and its orthogonal complement at eigenvalue \(L=\kappa\mu\), where \(\kappa>1\). Suppose an approximate \(k\)-dimensional low-eigenspace is available. Boosting that approximate subspace by a scalar \(\gamma\geq1\) is a natural low-rank positive-definite preconditioner.

The exact condition number of the symmetrically preconditioned matrix depends **only on the largest principal angle** \(\theta\in[0,\pi/2]\) between the true and approximate low-eigenspaces, regardless of either dimension or the other principal angles. Set
\[
 c=\cos\theta,\quad s=\sin\theta,\quad a=\kappa c^2+s^2,\quad b=c^2+\kappa s^2,\quad T_\gamma=a+\gamma b.
\]
For every \(\gamma\geq1\), its extreme eigenvalues are precisely
\[
 \lambda_\pm(\gamma)=\frac{\mu}{2}\left(T_\gamma\pm\sqrt{T_\gamma^2-4\kappa\gamma}\right).
\]
The **unique** condition-number-minimizing boost is
\[
 \gamma_* =\max\left\{1,\frac{\kappa c^2+s^2}{c^2+\kappa s^2}\right\}.
\]
With \(z=(\kappa-1)sc/\sqrt\kappa\), the attained spectral condition number is
\[
 \min_{\gamma\geq1}\kappa_2(C_\gamma)=
 \begin{cases}
  (\sqrt{1+z^2}+z)^2,&0\leq\theta\leq\pi/4,\\
  \kappa,&\pi/4\leq\theta\leq\pi/2.
 \end{cases}
\]
Thus, **exactly at** \(\theta=\pi/4\), subspace boosting ceases to improve conditioning: every \(\gamma>1\) worsens it when \(\theta\geq\pi/4\).

There is a sharp high-contrast accuracy scale. For any sequence \(\kappa\to\infty\), potentially with varying matrix and subspace dimensions, the optimally boosted condition numbers stay bounded precisely when \(\theta_\kappa=O(\kappa^{-1/2})\). More precisely, if \(\sqrt\kappa\,\theta_\kappa\to t\in[0,\infty)\), then
\[
 \gamma_*/\kappa\longrightarrow\frac{1}{1+t^2},\qquad
 \min_{\gamma\geq1}\kappa_2(C_\gamma)\longrightarrow
 (\sqrt{1+t^2}+t)^2.
\]
All bounds are exact, rather than estimates; their extremizers are already present in a two-dimensional principal-angle block.

## Assumptions and scope

Let \(d\geq2\), \(1\leq k<d\), \(\mu>0\), \(\kappa>1\), and let \(E,F\subset\mathbb R^d\) be \(k\)-dimensional subspaces. Denote their orthogonal projectors by \(\Pi_E,\Pi_F\), and define
\[
 H=\mu\Pi_E+\mu\kappa(I-\Pi_E),\quad
 W_\gamma=I+(\gamma-1)\Pi_F,\quad
 C_\gamma=W_\gamma^{1/2}HW_\gamma^{1/2},\quad\gamma\geq1.
\]
The condition number is the Euclidean spectral \(\lambda_{\max}(C_\gamma)/\lambda_{\min}(C_\gamma)\). The largest principal angle is \(\theta=\arcsin\|\Pi_E-\Pi_F\|_2\). The multiplier \(W_\gamma\) is an **inverse preconditioner**: applying it to a residual accelerates the low-frequency modes when \(F\) accurately approximates \(E\). The theorem does not claim that this multiplier equals any particular multilevel solver's Galerkin coarse correction.

## Proof

Scaling by \(\mu\) reduces the proof to \(\mu=1\). The nonzero spectra of \(W_\gamma^{1/2}HW_\gamma^{1/2}\) and \(H^{1/2}W_\gamma H^{1/2}\) coincide, and both are positive definite, so analyze the latter. The cosine-sine decomposition for equal-dimensional subspaces gives mutually orthogonal principal-angle planes on which \(H\) equals \(\operatorname{diag}(1,\kappa)\) and \(\Pi_F\) is the rank-one projector onto \((\cos\theta_i,\sin\theta_i)\); zero-angle directions and unused high directions contribute only diagonal eigenvalues \(\gamma\) and \(\kappa\).

On one such plane, let \(c_i=\cos\theta_i\), \(s_i=\sin\theta_i\). The symmetric matrix \(H^{1/2}W_\gamma H^{1/2}\) has trace
\[
 T_i=1+\kappa+(\gamma-1)(c_i^2+\kappa s_i^2)
     =(\kappa c_i^2+s_i^2)+\gamma(c_i^2+\kappa s_i^2)
\]
and determinant \(\kappa\gamma\). Therefore its eigenvalues are the two roots of \(x^2-T_i x+\kappa\gamma=0\). For \(\gamma\geq1\), the trace is nondecreasing with \(\sin^2\theta_i\). At a fixed positive determinant, the larger quadratic root increases with the trace and the smaller decreases. Consequently the plane with the **largest** principal angle supplies the global maximum and minimum among all coupled planes. The eigenvalues \(\gamma\) and \(\kappa\) of any uncoupled directions lie between that plane's extreme roots, because the corresponding zero-angle roots are \(\min(\gamma,\kappa)\) and \(\max(\gamma,\kappa)\). If every angle is zero, those are directly the global endpoints. Hence the exact extreme-eigenvalue formula holds for all \(d,k\), including coincident and perpendicular subspaces.

For positive numbers with fixed product \(\kappa\gamma\), their ratio is a strictly increasing function of the sum divided by the square root of that product. It therefore suffices to minimize
\[
 \frac{T_\gamma}{\sqrt\gamma}=\frac a{\sqrt\gamma}+b\sqrt\gamma,
 \qquad a=\kappa c^2+s^2,\quad b=c^2+\kappa s^2.
\]
Its derivative changes sign exactly once, at \(\gamma=a/b\). The constraint \(\gamma\geq1\) gives the displayed unique minimizer. Since \(a-b=(\kappa-1)(c^2-s^2)\), this minimizer exceeds one precisely when \(\theta<\pi/4\).

For \(\theta\leq\pi/4\), at \(\gamma_*=a/b\) one has \(T_{\gamma_*}=2a\) and \(\sqrt{\kappa\gamma_*}=\sqrt{\kappa a/b}\). The identity
\[
 ab=\kappa+(\kappa-1)^2c^2s^2
\]
gives \(T_{\gamma_*}/(2\sqrt{\kappa\gamma_*})=\sqrt{1+z^2}\). The two eigenvalues normalized by the geometric mean are \(\sqrt{1+z^2}\pm z\), whose quotient equals \((\sqrt{1+z^2}+z)^2\). For \(\theta\geq\pi/4\), the constrained minimizer is \(\gamma=1\) and \(C_1=H\) has condition number \(\kappa\). At the boundary the two formulas coincide.

Finally, bounded optimal condition number as \(\kappa\to\infty\) excludes \(\theta\geq\pi/4\) eventually. In the remaining interval, boundedness is equivalent to bounded \(z=(\kappa-1)\sin\theta\cos\theta/\sqrt\kappa\), which is equivalent to \(\theta=O(\kappa^{-1/2})\). If \(\sqrt\kappa\theta\to t\), then \(z\to t\) and
\[
 \frac{\gamma_*}{\kappa}
 =\frac{\kappa\cos^2\theta+\sin^2\theta}
 {\kappa(\cos^2\theta+\kappa\sin^2\theta)}\to\frac1{1+t^2}.
\]
Continuity proves the limiting condition number. No sampling, asymptotic interpolation, or unverified finite census enters the proof.

## Verification

Run `python verify.py` after installing the single dependency given in `requirements.txt`. The checker independently constructs symmetrically preconditioned matrices from principal-angle bases, compares their computed extreme eigenvalues against the two-root formula for 50 combinations of spectral contrasts and principal angles, and checks 300 boost strengths. It also checks the high-contrast critical window. These tests are transcription guards; the preceding cosine-sine decomposition and optimization establish the theorem for all dimensions and real parameters.

## Relationship to prior work

Sun, Qi, Han, and Xie (2026, arXiv:2605.29304v1, §1 and §3.2) motivate subspace-constrained preconditioning and prove randomized-iteration convergence using an **orthogonal constraint projection**. The present theorem instead optimizes a **positive-definite scalar subspace boost** on an exactly two-level SPD spectrum. Their projection operator, objective, and convergence bounds do not express or imply the piecewise condition number of this different multiplier.

Benanti, Han, and Qin (2026, arXiv:2601.20174v1, §4.1–4.2 and Appendix A) motivate approximating leading smooth-error subspaces for low-rank preconditioning and prove properties of a learned subspace loss. Their actual algorithm is a multilevel coarse-grid correction, not the scalar-boosted matrix analyzed here, and the inspected theorem and algorithm do not optimize a scalar boost or classify a worst principal-angle transition.

Kahl and Rittich (arXiv:1209.1963v4, §2 and §4) bound the **effective condition number of a singular deflated-CG operator** in terms of the largest principal angle to the ideal deflation subspace; their Proposition 4.3 is a nonsharp perturbation upper bound for that different operator. It motivates the importance of angular accuracy, but it does not give the positive-definite boost spectrum, unique best boost, or exact phase boundary established here.

Helmberg (2023 preprint/2024 journal, DOI:10.1007/s10107-023-01986-w, §4, Corollary 5 and Theorem 6) bound spectral conditioning of a low-rank Galerkin-type approximation in conic optimization. Their matrix and objective are different, and the inspected bounds do not establish the exact scalar-boost optimum on a two-level spectrum. Published analysis of stale-coordinate SOAP updates uses entrywise adaptive normalization rather than this projector multiplier, so its \(45^\circ\) example also does not cover the claim.

## Limitations

The spectrum is assumed to have exactly two levels and the candidate subspace has exactly the dimension of the low eigenspace. A multi-level or clustered—but nonidentical—spectrum can depend on additional principal-vector information. Only scalar boosts \(\gamma\geq1\) are optimized; allowing contraction, anisotropic weights, or nonprojector corrections changes the problem. Condition number is a standard worst-case convergence proxy for preconditioned CG but does not determine its actual finite-iteration history or computational cost. The related preconditioners in the cited papers are not asserted to be identical.

## References

1. Y. Sun, H.-D. Qi, D. Han and J. Xie, *On subspace-constrained preconditioning for randomized iterative methods*, arXiv:2605.29304v1, first public 2026-05-28, https://arxiv.org/html/2605.29304v1.
2. A. Benanti, X. Han and H. Qin, *NeuraLSP: An Efficient and Rigorous Neural Left Singular Subspace Preconditioner for Conjugate Gradient Methods*, arXiv:2601.20174v1, first public 2026-01-28, https://arxiv.org/html/2601.20174v1.
3. K. Kahl and H. Rittich, *The Deflated Conjugate Gradient Method: Convergence, Perturbation and Accuracy*, arXiv:1209.1963v4 (2017), https://arxiv.org/pdf/1209.1963.
4. C. Helmberg, *A preconditioned iterative interior point approach to the conic bundle subproblem*, Mathematical Programming (2024), DOI:10.1007/s10107-023-01986-w.
5. Published result *Exact stale-basis singular-value collapse in SOAP*, https://github.com/published-finding corpus/2026/blob/main/2026/10/4/SCOPE-exact-stale-basis-singular-value-collapse-in-soap--91a933b03a1c/RESULT.md.
