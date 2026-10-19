# A balanced two-query phase transition for one-step reduced-basis preconditioning

## Finding
For every real \(t>1\), consider the symmetric positive-definite matrix \(A_t=\operatorname{diag}(1,t,t,t^2)\), the reduced basis matrix \(P=[e_2\ e_3]\) with invariant range \(U=\operatorname{range}(P)\), and the Type-I additive reduced-basis inverse preconditioner
\[
F_\alpha=P(P^{\mathsf T}A_tP)^{-1}P^{\mathsf T}+\alpha I
=\operatorname{diag}(\alpha,\alpha+t^{-1},\alpha+t^{-1},\alpha),\qquad\alpha>0.
\]
At the zero initial guess, apply exactly one *standard preconditioned conjugate-gradient step* to each system \(A_tx=b\). The right-hand side is \(b_L=e_1+e_2\) with probability \(1/(t+1)\), or \(b_H=e_2+e_4\) with probability \(t/(t+1)\); the same value of \(\alpha\) is used for both systems. The weights balance their initial squared energy errors: each right-hand side contributes exactly \(1/t\) to the expected initial squared energy error.

Write \(\mathcal E_t(\alpha)=\mathbb E_b\|A_t^{-1}b-x_1(b;\alpha)\|_{A_t}^2\) and \(\theta=t+1/\alpha>t\). Then the exact risk is
\[
\mathcal E_t(\alpha)=R_t(\theta):=\frac1{t+1}\left[\frac{(\theta-1)^2}{\theta^2+t}+\frac{(\theta-t^2)^2}{t(\theta^2+t^3)}\right].
\]
There is a sharp transition at \(t=3\).

* If \(1<t\le3\), \(R_t\) is strictly increasing for \(\theta>t\), so no finite positive \(\alpha\) minimizes it. Its sharp infimum is the ordinary unpreconditioned one-step conjugate-gradient risk, attained only in the limit \(\alpha\to\infty\):
\[
\inf_{\alpha>0}\mathcal E_t(\alpha)=\frac{2(t-1)^2}{t(t+1)^2}.
\]
Every finite regularization increases the expected squared energy error.

* If \(t>3\), there is a **unique finite** minimizer
\[
\theta_+(t)=\frac t2\left(t-1+\sqrt{(t-3)(t+1)}\right),\qquad
\alpha_*(t)=\frac{2}{t\left(t-3+\sqrt{(t-3)(t+1)}\right)},
\]
with exact optimal expected squared energy error
\[
\min_{\alpha>0}\mathcal E_t(\alpha)=\frac{t-2}{t(t-1)}.
\]
The absolute gain over one step of ordinary conjugate gradients is precisely
\[
\frac{(t-3)^2}{(t-1)(t+1)^2}>0.
\]

For every positive \(\alpha\), the condition number of the symmetrically preconditioned matrix is at least \(t^2\), the condition number of \(A_t\) itself. At the risk-optimal \(\alpha_*\) when \(t>3\), it is exactly \(t^2\). Hence **strict finite-budget benefit can coexist with no possible improvement in spectral condition number**.

## Assumptions and scope
All matrices, parameters, and vectors are real. The theorem holds for every \(t>1\), exact arithmetic, the fixed two-dimensional invariant reduced subspace shown above, the fixed probability distribution over exactly two right-hand sides, and exactly one standard PCG step from \(x_0=0\). The risk is the **expected unnormalized squared** \(A_t\)-energy error; it is not Euclidean residual loss, a ratio of expectations, or an asymptotic rate. No claim is made for other workloads, nonlinear methods, inexact preconditioners, or more than one PCG step.

## Proof
**1. Positivity, scaling, and workload balance.** Both \(A_t\) and \(F_\alpha\) are positive definite. Since multiplying an SPD PCG inverse preconditioner by a positive scalar leaves the first PCG iterate unchanged, scale \(F_\alpha\) by \(1/\alpha\). The effective diagonal inverse-preconditioner multipliers are then \(1,\theta/t,\theta/t,1\). The two exact solutions have initial squared energy errors
\[
\|A_t^{-1}b_L\|_{A_t}^2=1+t^{-1},\qquad
\|A_t^{-1}b_H\|_{A_t}^2=t^{-1}+t^{-2}.
\]
Their probability-weighted initial contributions both equal \(1/t\).

**2. Direct one-step energy identity.** For arbitrary SPD \(A\), inverse preconditioner \(F\succ0\), and nonzero right-hand side \(b\), the first PCG direction is \(Fb\) and its line minimizer is
\[
x_1=\frac{b^{\mathsf T}Fb}{b^{\mathsf T}FAFb}\,Fb,\qquad
\|A^{-1}b-x_1\|_A^2=b^{\mathsf T}A^{-1}b-\frac{(b^{\mathsf T}Fb)^2}{b^{\mathsf T}FAFb}.
\]
For a right-hand side activating the reduced coordinate of eigenvalue \(t\) and one unselected coordinate of eigenvalue \(\lambda\in\{1,t^2\}\), substitution gives
\[
E_\lambda(\theta)=\frac{(\theta-\lambda)^2}{\lambda(\theta^2+t\lambda)}.
\]
Thus \(E_1=(\theta-1)^2/(\theta^2+t)\), \(E_{t^2}=(\theta-t^2)^2/[t^2(\theta^2+t^3)]\). Weighting these by \(1/(t+1)\) and \(t/(t+1)\) proves the risk formula.

**3. Exact minimax certificate and strict derivative sign.** Put
\[
q_t(\theta)=\theta^2-t(t-1)\theta+t^2.
\]
Direct expansion yields, for every \(t>1\) and \(\theta>t\), the exact nonnegative-square decomposition
\[
R_t(\theta)=\frac{t-2}{t(t-1)}+
\frac{q_t(\theta)^2}{t(t-1)(\theta^2+t)(\theta^2+t^3)}.
\]
Direct differentiation also factors exactly as
\[
R'_t(\theta)=\frac{2(\theta-t)(\theta+t)
[\theta^2+(t-1)\theta+t^2]q_t(\theta)}
{(\theta^2+t)^2(\theta^2+t^3)^2}.
\]
The sign on \(\theta>t\) is consequently the sign of \(q_t\). Its discriminant is \(t^2(t-3)(t+1)\).

For \(1<t<3\), this discriminant is negative, hence \(q_t>0\) everywhere. For \(t=3\), it is zero and \(q_3(\theta)=(\theta-3)^2>0\) for \(\theta>3\). Thus \(R_t\) strictly increases on \((t,\infty)\), and its infimum is the boundary value \(R_t(t)\), corresponding to \(\alpha\to\infty\), rather than a finite regularization.

For \(t>3\), \(q_t(t)=t^2(3-t)<0\). Its two positive roots satisfy \(\theta_-<t<\theta_+\) and are \(t(t-1\mp\sqrt{(t-3)(t+1)})/2\). The derivative is strictly negative on \((t,\theta_+)\) and strictly positive on \((\theta_+,\infty)\), giving a unique minimizer. The square decomposition vanishes at \(\theta_+\), proving its exact attained risk. Evaluating the boundary value gives \(R_t(t)=2(t-1)^2/[t(t+1)^2]\), and subtraction yields the claimed positive gain.

**4. Condition-number obstruction.** The eigenvalues of \(F_\alpha A_t/\alpha\) are \(1,\theta,\theta,t^2\). Therefore
\[
\kappa(F_\alpha^{1/2}A_tF_\alpha^{1/2})=\max\{t^2,\theta\}\ge t^2=\kappa(A_t).
\]
For \(t>3\), \(q_t(t^2)=t^2(t+1)>0\), while \(q_t(t)<0\), so \(t<\theta_+<t^2\), and equality holds at the unique risk optimum.

## Verification
The independent direct-PCG computation in the accompanying \(\texttt{verify.py}\) checks the unnormalized energy identity for both right-hand sides across thousands of exact rational parameter choices; it also verifies four symbolic identities using polynomial/rational simplification and numerical instances of the unique minimizer. Execute \(\texttt{python verify.py}\) using Python 3 and SymPy. These computations check the algebra and implementation; the proof above, rather than finite sampling, establishes the theorem for all real \(t>1\).

For example, with \(t=10\), the initial squared risk is \(81/605\), the sharp optimized risk is \(4/45\), and the spectral condition number remains \(100\) at the risk optimum. The associated \(\theta_+\) equals \(45+5\sqrt{77}\).

## Relationship to prior work
Fan, Hu, and Zhang introduce Type-I additive reduced-basis preconditioning using the same \(\widetilde M+\alpha I\) inverse-preconditioner construction, chiefly analyzing nonsingularity, Richardson bounds, and FGMRES; their paper does not supply this two-query PCG risk classification. Diouane, Gürol, Mouhtal, and Orban already motivate choosing spectral cluster locations by finite-budget PCG energy error for a fixed system; that single-right-hand-side objective and its general analysis are prior work, not a claim of this result. Work on deflation across multiple right-hand sides likewise supplies context but not the stated balanced-workload threshold. The new assertion is the exact \(t=3\) division and unique risk optimum for the specified fixed Type-I regularization shared by two systems, including its sharp mismatch with spectral condition-number tuning.

## Limitations
The two-query probability weights balance initial energy by design, and the matrix is a four-dimensional, exactly invariant, diagonal benchmark. It is a structural example, not a theorem about general large-scale preconditioner performance. The classical one-step PCG minimization formula is not claimed as new. Equal-weight or continuously distributed workloads can have other optima; no such extension is proved. A matching theorem under a different name in older spectral-preconditioning or average-case Krylov literature remains a possible bibliographic overlap until independently checked.

## References
1. X. Fan, Q. Hu, S. Zhang, *Additive Reduced Basis Preconditioners for Large-Scale Parametrized PDEs*, arXiv:2609.11097v1, September 10, 2026, especially §3.1–3.5. https://arxiv.org/html/2609.11097v1
2. Y. Diouane, S. Gürol, O. Mouhtal, D. Orban, *A Spectral Preconditioner for the Conjugate Gradient Method with Iteration Budget*, arXiv:2603.28969v1, March 30, 2026, especially §§3–4. https://arxiv.org/html/2603.28969v1
3. A. Stathopoulos, K. Orginos, *Computing and Deflating Eigenvalues While Solving Multiple Right Hand Side Linear Systems in Quantum Chromodynamics*, arXiv:0707.0131, 2007. https://arxiv.org/abs/0707.0131
