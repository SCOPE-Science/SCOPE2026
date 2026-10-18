# Sharp minimax feedback shifts for bounded self-adjoint control spectra

## Finding

A scalar feedback shift admits an exact and unique **worst-case condition-number optimizer** for a finite self-adjoint control spectrum. Let \(0\leq\mu<L<\infty\), \(\alpha>0\), and consider every real symmetric matrix \(A\) of arbitrary finite dimension \(n\geq3\) with \(\mu I\preceq A\preceq LI\). For \(\delta>0\), define
\[
H_\delta(A)=(A+\delta I)^{-1}(I+\alpha A^2)(A+\delta I)^{-1}.
\]
Put \(\theta_0=\arctan(\sqrt\alpha\,\mu)\), \(\theta_1=\arctan(\sqrt\alpha\,L)\), and \(\Delta=\theta_1-\theta_0\). Then
\[
\boxed{\delta_* =\frac{1}{\sqrt\alpha}\cot\!\left(\frac{\theta_0+\theta_1}{2}\right)}
\]
is the **unique** minimizer of the uniform spectral condition number, and
\[
\boxed{\inf_{\delta>0}\;\sup_{n\geq3}\;\sup_{\mu I\preceq A\preceq LI}\kappa_2(H_\delta(A))
 =\sec^2\!\left(\frac{\Delta}{2}\right)<2.}
\]
For each fixed \(\delta>0\), the inner supremum is attained by a diagonal matrix with no more than three distinct eigenvalues. At \(\delta_*\), sharpness is attained by the three-mode matrix with eigenvalues \(\mu\), \(a_*=(\alpha\delta_*)^{-1}\), and \(L\). The two endpoint modes have equal transformed curvature; the middle mode has the smallest transformed curvature. A matrix whose spectrum uses **only the two endpoints** has \(H_{\delta_*}(A)\) proportional to the identity.

In the semidefinite endpoint case \(\mu=0\), writing \(s=\sqrt{1+\alpha L^2}\), these simplify to
\[
\delta_* = \frac{s+1}{\alpha L},\qquad
\inf_{\delta>0}\sup_A\kappa_2(H_\delta(A))=\frac{2s}{s+1}.
\]
The bound tends to \(2\) as \(\alpha L^2\to\infty\), but is strictly below \(2\) at every finite \(L\). For \(\alpha=L=1\) and \(\mu=0\), the optimal shift is \(1+\sqrt2\) and the sharp bound is \(4-2\sqrt2\); the conventional matched shift \(\delta=1\) has worst-case factor \(2\) over the same interval.

## Assumptions and scope

The optimization problem is the finite-dimensional quadratic control model
\[
\min_{x,u\in\mathbb R^n}\;\frac12\|x-y\|_2^2+\frac\alpha2\|u\|_2^2
\quad\text{subject to }Ax=u,
\]
where \(y\in\mathbb R^n\) is arbitrary. Feedback substitution \(u=-\delta x+v\) makes \((A+\delta I)x=v\), hence \(x=(A+\delta I)^{-1}v\) and \(u=A(A+\delta I)^{-1}v\). The Hessian in the transformed variable \(v\) is exactly \(H_\delta(A)\) above. The minimax criterion is the Euclidean spectral condition number of that **exact transformed Hessian**; it is not a bound in a PDE energy norm. The optimum does not depend on \(y\) or the control right-hand side. No claim is made for nonsymmetric dynamics, unequal observation/control weights, noncommuting operators, approximate inverses, or solver wall-clock complexity.

## Proof

**1. Exact Hessian and scalar spectral law.** Substituting the feedback expressions into the quadratic objective gives quadratic part
\[
\tfrac12 v^\mathsf{T}(A+\delta I)^{-2}v+	frac\alpha2v^\mathsf{T}A^2(A+\delta I)^{-2}v.
\]
Since \(A\) is symmetric and commutes with functions of itself, the Hessian is \(H_\delta(A)\), which is positive definite for every \(\delta>0\). Its eigenvalue corresponding to \(a\in[\mu,L]\) is
\[
f_\delta(a)=\frac{1+\alpha a^2}{(a+\delta)^2},\qquad
f'_\delta(a)=\frac{2(\alpha\delta a-1)}{(a+\delta)^3}.
\]
Consequently, for each \(\delta\), the maximum on \([\mu,L]\) occurs at an endpoint; the minimum occurs at the clipped value \(c_\delta=\min\{L,\max\{\mu,(\alpha\delta)^{-1}\}\}\). The entire worst-case curve is therefore exactly
\[
R(\delta)=\frac{\max\{f_\delta(\mu),f_\delta(L)\}}{f_\delta(c_\delta)}.
\]
Every admissible \(A\) satisfies \(\kappa_2(H_\delta(A))\leq R(\delta)\). Choosing a three-by-three diagonal \(A\) with eigenvalues \(\mu,c_\delta,L\) realizes equality. Thus the stated matrix supremum is \(R(\delta)\), without any assumption about the existence of a continuum of matrix eigenvalues.

**2. Minimax geometry and uniqueness.** Make the changes of variables
\[
\theta=\arctan(\sqrt\alpha\,a),\qquad \phi=\arctan(\sqrt\alpha\,\delta).
\]
Then \(\theta\in[\theta_0,\theta_1]\), \(\phi\in(0,\pi/2)\), and the exact trigonometric identity is
\[
f_\delta(a)=\frac{\alpha\cos^2\phi}{\sin^2(\theta+\phi)}.
\]
Writing \(x=\theta_0+\phi\), the worst-case ratio is
\[
R(\delta)=\frac{\max_{t\in[x,x+\Delta]}\sin^2t}{\min_{t\in[x,x+\Delta]}\sin^2t},
\]
with \(0<x<x+\Delta<\pi\). If the interval lies to the left of \(\pi/2\), then \(R=(\sin(x+\Delta)/\sin x)^2\), which decreases strictly when the interval is shifted right because \(\cot(x+\Delta)<\cot x\). If it lies to the right of \(\pi/2\), the reciprocal ratio increases strictly under rightward translation. If it contains \(\pi/2\), then \(R=1/\min\{\sin^2x,\sin^2(x+\Delta)\}\). This decreases until the two endpoint sine values coincide and then increases. Since \(0<\Delta<\pi/2\), their unique equality at a straddling interval is \(2x+\Delta=\pi\). Therefore the unique global minimizer satisfies
\[
\phi_*=\frac\pi2-\frac{\theta_0+\theta_1}{2},
\]
which lies in \((0,\pi/2)\). Inverting the tangent gives \(\delta_*\), and the centered interval has end-point sine \(\cos(\Delta/2)\) and middle sine \(1\). Hence \(R(\delta_*)=\sec^2(\Delta/2)\). The strict monotonicities prove uniqueness, including when \(\mu=0\).

**3. Sharp witness, two-mode collapse, and limits.** At the centered interval, the scalar minimizer is \(a_*=(\alpha\delta_*)^{-1}\), with \(\mu<a_*<L\). Thus \(\operatorname{diag}(\mu,a_*,L)\) attains the stated worst-case condition number. Equality of the endpoint sine values yields \(f_{\delta_*}(\mu)=f_{\delta_*}(L)\). Hence every matrix with spectrum contained in the endpoint set has an exactly scalar transformed Hessian, requiring at most one exact-arithmetic conjugate-gradient update for any right-hand side. When \(\mu=0\), the half-angle identities yield the displayed elementary expressions for \(\delta_*\) and the condition number. Their \(s\to\infty\) limit is \(2\); no finite \(L\) attains it. All stated results hold for every specified \(\alpha,\mu,L\) and every finite dimension \(n\geq3\).

## Verification

The companion standalone `verify.py`, run with `python verify.py` using NumPy and SymPy, passed 7,146 checks. These include exact symbolic identities at \(\alpha=L=1,\mu=0\), 420 seeded random spectral intervals, comparisons against 12 distinct feedback shifts per interval, direct orthogonally rotated three-by-three Hessians, endpoint equality, and large-spectral-range examples. Finite computations corroborate but do not prove the universal or asymptotic statements; the analytic steps above provide those proofs.

## Relationship to prior work

Preuster, Schiela, Schaller, and Stoll (2026) introduce feedback-based preconditioning for optimal control and prove general upper condition-number bounds. Their Section 4.2 optimizes an upper bound for an elliptic PDE in its stated energy norm; it does not supply the exact Euclidean self-adjoint spectral-interval minimax law here. In particular, their bound of \(9\) is in a different setting and must **not** be numerically compared with the present bound below \(2\).

Pearson, Stoll, and Wathen (2012) use the classical matched-square Schur preconditioner with fixed shift proportional to the inverse square root of the regularization parameter and prove a dimension-independent factor-\(2\) spectral bound. Wang, Chen, and Sun (2023) recall that construction and give related matching Schur complement preconditioners. The rational spectral ratio and its parameter-robust bound are therefore **not** claimed as new. The result here is the **complete finite-endpoint optimal-shift problem** for precisely this ratio and the feedback-coordinate Hessian: a unique sharp endpoint-dependent optimizer, a three-eigenvalue extremizer, and exact two-endpoint collapse. The general factor \(2\) is the limit of the present finite-band optimum, not an improved general unbounded-spectrum guarantee.

## Limitations

The theorem assumes exact Euclidean inner products, real symmetric positive-semidefinite \(A\), identical identity state observation and control coupling, positive scalar regularization, scalar feedback, and knowledge of valid spectral endpoints. The robust minimax shift need not be optimal for one particular matrix whose eigenvalues do not fill the extremal pattern. Applying \((A+\delta I)^{-1}\) incurs additional linear-solve costs; a smaller transformed Hessian condition number alone does not imply a faster implemented algorithm. A matched-square Schur factor with comparable spectrum was already known; this statement does not assert originality of that factorization or of the universal factor-\(2\) bound. Equivalences in unindexed spectral-optimization literature remain possible.

## References

1. T. Preuster, A. Schiela, M. Schaller and M. Stoll, *Stabilize-then-optimize: Feedback transformations as preconditioners in optimal control*, arXiv:2607.11835v1 (first submitted 2026-07-13), https://arxiv.org/abs/2607.11835. Sections 3 and 4.2.
2. J. W. Pearson, M. Stoll and A. J. Wathen, *Regularization-Robust Preconditioners for Time-Dependent PDE-Constrained Optimization Problems*, SIAM Journal on Matrix Analysis and Applications 33 (2012), 1126–1152, https://doi.org/10.1137/110847949. Section 2.2 and matching-Schur spectral bound.
3. C. Wang, J. Chen and S. Sun, *A Matching-Strategy-Inspired Preconditioning for Elliptic Optimal Control Problems*, Mathematics 11 (2023), article 2599, https://doi.org/10.3390/math11122599. Sections 2.2 and 3.2.
