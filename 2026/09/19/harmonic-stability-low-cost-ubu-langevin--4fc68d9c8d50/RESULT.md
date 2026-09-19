# Sharp harmonic stability phase diagram for low-cost UBU integrators

## Statement

Lyu, Wang, and Yang introduce the low-cost UBU integrator (LC-UBU) and two exponential-free variants, the Taylor method LCT-UBU and the Padé method LCP-UBU, for underdamped Langevin dynamics.  On a quadratic potential, their absolute stability regions admit closed forms that sharply separate the three schemes.

Consider
\[
U(x)=\frac12 x^T Hx,\qquad H\succ0,
\]
and one eigenmode of \(H\) with curvature \(\kappa>0\).  With the notation of arXiv:2609.20713, set
\[
z=\gamma h>0,\qquad s=\alpha\kappa h^2>0,
\]
and scale velocity by \(y=hv\).  The one-step chain is affine Gaussian,
\[
Y_{n+1}=M(z,s)Y_n+\xi_n,\qquad Y_n=(x_n,y_n)^T.
\]
The following conditions are exact Schur-stability criteria for the deterministic mean matrix \(M\).

### Exponential LC-UBU

Let \(q=e^{-z/2}\),
\[
A=\frac{1-q}{z},\qquad B=\frac{1-q^2}{z}.
\]
Then
\[
M_E=
\begin{pmatrix}
1-sA & B-sA^2\\
-sq & q^2-sqA
\end{pmatrix},
\]
and
\[
\boxed{\rho(M_E)<1\iff 0<s<S_E(z)},
\qquad
\boxed{S_E(z)=2z\coth(z/2)}.
\]
The boundary corresponds to an eigenvalue \(-1\).  Moreover, \(S_E\) is strictly increasing,
\[
S_E(z)=4+\frac{z^2}{3}+O(z^4),\qquad
S_E(z)\sim2z\quad(z\to\infty).
\]

### Taylor LCT-UBU

Using the Taylor coefficients of Eq. (2.23) of the source paper gives
\[
A_T=\frac{4-z}{8},\quad B_T=1-\frac z2,\quad
P_T=1-z+\frac{z^2}{2},\quad C_T=1-\frac z2,
\]
\[
M_T=
\begin{pmatrix}
1-s/2 & B_T-(s/2)A_T\\
-sC_T & P_T-sC_TA_T
\end{pmatrix}.
\]
Its exact stability region is
\[
\boxed{
\rho(M_T)<1
\iff
0<z<2\ \text{ and }\ 0<s<S_T(z)
},
\]
where
\[
\boxed{
S_T(z)=8\frac{z^2-2z+4}{z^2-2z+8}
}.
\]
Thus LCT-UBU has a hard friction-step barrier \(\gamma h<2\), independent of how small the quadratic curvature is.  The curvature threshold satisfies
\[
\min_{0<z<2}S_T(z)=S_T(1)=\frac{24}{7},
\]
and
\[
S_T(z)=4-z+\frac{z^2}{4}+O(z^3)\quad(z\downarrow0).
\]
At \(z=2\), \(M_T\) has eigenvalue \(+1\) for every \(s>0\).

### Padé LCP-UBU

Using the Padé coefficients of Eq. (2.26) gives
\[
A_P=\frac{2}{4+z},\quad B_P=\frac{2}{2+z},\quad
P_P=\frac{2-z}{2+z},\quad C_P=\frac{2}{2+z},
\]
\[
M_P=
\begin{pmatrix}
1-s/2 & B_P-(s/2)A_P\\
-sC_P & P_P-sC_PA_P
\end{pmatrix}.
\]
Here the exact region is
\[
\boxed{
\rho(M_P)<1
\iff
0<s<S_P(z)
},
\]
with
\[
\boxed{
S_P(z)=4\frac{(z+2)(z+4)}{z^2+8z+8}
}.
\]
There is no finite friction-only barrier.  The threshold has the global minimum
\[
\boxed{
\min_{z>0}S_P(z)=2+\sqrt2
}
\]
at \(z=2\sqrt2\), and
\[
S_P(z)=4-z+z^2+O(z^3),\qquad S_P(z)\to4\quad(z\to\infty).
\]
The stability boundary again corresponds to an eigenvalue \(-1\).

For an SPD quadratic in any dimension, orthogonal diagonalization of \(H\) decouples the update mode by mode.  Hence the full chain is Schur stable exactly when the corresponding inequality holds for every eigenvalue of \(H\); equivalently it is enough to test \(s=\alpha\lambda_{\max}(H)h^2\).

## Proof

For a real \(2\times2\) matrix with characteristic polynomial
\[
r^2-Tr+D,
\]
the Jury conditions are
\[
1-D>0,\qquad 1-T+D>0,\qquad 1+T+D>0.
\]

For LC-UBU, direct substitution gives
\[
D=q^2,
\]
\[
1-T+D=\frac{s(1-q^2)}{z}>0,
\]
\[
1+T+D
=\frac{2z(1+q^2)-s(1-q^2)}{z}.
\]
The first two inequalities hold automatically for \(z,s>0\), while the third is exactly
\[
s<2z\frac{1+e^{-z}}{1-e^{-z}}
=2z\coth(z/2).
\]
Its derivative is
\[
S_E'(z)=2\frac{\sinh z-z}{\cosh z-1}>0.
\]

For LCT-UBU, the same calculation yields
\[
1-D=\frac{z\{s(z+2)+8(2-z)\}}{16},
\]
\[
1-T+D=\frac{s(2-z)}2,
\]
\[
1+T+D
=\frac{8(z^2-2z+4)-s(z^2-2z+8)}8.
\]
The middle condition forces \(z<2\).  In this range the first condition is automatic, and the last condition is precisely \(s<S_T(z)\).  Differentiation gives
\[
S_T'(z)=\frac{64(z-1)}{(z^2-2z+8)^2},
\]
which proves the minimum at \(z=1\).

For LCP-UBU,
\[
1-T+D=s\frac{z^2+2z+4}{(z+2)^2}>0,
\]
\[
1+T+D
=\frac{2\{4z^2+24z+32-s(z^2+8z+8)\}}
{(z+2)^2(z+4)},
\]
and
\[
1-D
=-\frac{z\{s(z^2+4z-4)-4(z^2+6z+8)\}}
{2(z+2)^2(z+4)}.
\]
The second displayed condition gives \(s<S_P(z)\).  If \(z^2+4z-4\le0\), then \(1-D>0\) automatically.  If \(z^2+4z-4>0\), its upper bound on \(s\) is weaker because its denominator is strictly smaller than \(z^2+8z+8\).  Thus \(s<S_P(z)\) is necessary and sufficient.  Finally,
\[
S_P'(z)=\frac{8(z^2-8)}{(z^2+8z+8)^2},
\]
which gives the unique minimum at \(z=2\sqrt2\).

The additive Gaussian increments do not alter mean Schur stability.  In the quadratic case the two Brownian functionals used in each update have linearly independent scalar kernels, so their one-mode covariance is positive definite.  Therefore Schur stability is also the exact criterion for existence of the usual causal finite-second-moment stationary Gaussian law and for geometric convergence of means and covariances in that harmonic mode.

## Stiff-friction consequence

Let \(\lambda=\alpha\kappa\) be fixed and let \(h_{\max}(\gamma)\) denote the supremum of stable steps for one quadratic mode.  The three methods separate sharply as \(\gamma\to\infty\):
\[
\boxed{
 h_{\max}^{E}(\gamma)\sim\frac{2\gamma}{\lambda},\qquad
 h_{\max}^{T}(\gamma)\sim\frac{2}{\gamma},\qquad
 h_{\max}^{P}(\gamma)\to\frac{2}{\sqrt\lambda}.
}
\]
For LC-UBU, the boundary equation is
\[
\lambda h=2\gamma\coth(\gamma h/2),
\]
whose positive root is unique and has the first asymptotic above.  For LCT-UBU, the hard constraint \(\gamma h<2\) becomes asymptotically active because \(s=O(\gamma^{-2})\) there.  For LCP-UBU, \(S_P(z)\to4\) and \(S_P(z)\le4\), yielding the third limit.

Thus the exponential, Taylor, and Padé variants have the same formal second-order convergence class in the source paper but radically different absolute-stability behavior in the stiff-friction regime.  The Padé replacement removes the Taylor scheme's hard friction barrier, yet unlike the exponential method it does not inherit friction-expanded curvature stability.

A small-step comparison makes the mechanism visible:
\[
S_E(z)=4+\frac{z^2}{3}+O(z^4),
\]
whereas
\[
S_T(z)=4-z+O(z^2),\qquad
S_P(z)=4-z+O(z^2).
\]
All three approach the familiar Verlet threshold \(s<4\) as \(z\downarrow0\), but the exponential damping initially enlarges the stable curvature window while both exponential-free replacements initially shrink it.

For example, at \(z=3,s=1\), the spectral radii are approximately
\[
\rho(M_E)=0.657305,
\qquad
\rho(M_T)=2.415686,
\qquad
\rho(M_P)=0.343672.
\]
The exponential and Padé methods are stable there, while the Taylor method is unstable solely because \(z>2\).

## Relation to prior work and originality boundary

Harmonic stability analysis of Langevin and stochastic-Verlet integrators is established methodology.  In particular, N. Grønbech-Jensen, *Linear Analysis of Stochastic Verlet-Type Integrators for Langevin Equations*, Journal of Statistical Physics 193, 12 (2026), develops general linear criteria for a broad class of stochastic Verlet-type schemes and analyzes many existing methods.  The Jury/Schur test itself is classical.  These general facts are not novelty claims.

The source arXiv:2609.20713 introduces LC-UBU, LCT-UBU, and LCP-UBU and proves their non-asymptotic Wasserstein error rates under stated regularity assumptions.  Its displayed method definitions and convergence theory do not give the closed harmonic stability regions above.  Searches by the scheme names, source identifier, harmonic/linear stability terminology, and the threshold formulas found no source stating this source-specific phase diagram.

The claim here is therefore restricted to the exact stability regions for these newly introduced LC-UBU variants, the hard \(z=2\) Taylor barrier, the Padé minimum \(2+\sqrt2\), and the resulting three-way stiff-friction scaling law.  To the best of our knowledge this theorem package has not appeared previously.  A residual originality risk remains because older general Langevin/Verlet or rational-integrator literature may imply portions of the calculation after recasting these new schemes into another parameterization.

## Limitations

The result is exact for quadratic potentials and linear mean-square stability.  It is not a nonlinear stability theorem, a replacement for the source paper's Wasserstein convergence analysis, or a claim that one variant is uniformly preferable in sampling accuracy.  The stability thresholds concern the deterministic amplification matrix; invariant-covariance bias inside the stable region is not characterized here.  For nonquadratic targets, local Hessian eigenvalues can still make the phase diagram diagnostically useful, but no global conclusion follows without additional assumptions.

## Reproducibility

`artifacts/verify_ubu_stability.py` constructs all three amplification matrices, compares the closed-form criteria against direct eigenvalue tests on deterministic pseudo-random points, checks the threshold constants, evaluates a representative stability separation, and verifies the stiff-friction scaling numerically.  Its captured output is in `artifacts/verification_output.txt`.

## References

1. W. Lyu, X. Wang, B. Yang, *A Unified Framework for Wasserstein Convergence of ULMC Methods beyond Log-Concavity: Old and New*, arXiv:2609.20713v1 (2026). https://arxiv.org/abs/2609.20713
2. N. Grønbech-Jensen, *Linear Analysis of Stochastic Verlet-Type Integrators for Langevin Equations*, Journal of Statistical Physics 193, 12 (2026). https://doi.org/10.1007/s10955-025-03553-3
