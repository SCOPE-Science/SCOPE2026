# Unique rate-optimal shift for the VBP stationary iteration

## Finding

For every integer \(n\ge 2\), let \(T\in\mathbb R^{n\times n}\) be symmetric positive definite and \(W\in\mathbb R^{n\times n}\) symmetric indefinite. Put \(B=WT^{-1}W\), and, for each \(\alpha>0\), let \(\ell_-(\alpha)\le \ell_+(\alpha)\) be the extreme generalized eigenvalues of the symmetric pair \((\alpha I-B,\,T+\alpha I)\). For the VBP stationary iteration of Makhdomi and Khojasteh Salkuyeh (2026), with **any** \(\gamma>0\), the exact spectral-radius convergence factor is

\[
\rho(\alpha)=\max\{|\ell_-(\alpha)|,|\ell_+(\alpha)|\}.
\]

There is exactly one \(\alpha_*\in(0,\infty)\) minimizing this factor. It is characterized constructively by

\[
\ell_-(\alpha_*)+\ell_+(\alpha_*)=0,
\qquad
\rho(\alpha_*)=\ell_+(\alpha_*)=-\ell_-(\alpha_*)<1.
\]

The objective is strictly decreasing before \(\alpha_*\) and strictly increasing after it. Thus a monotone scalar root search using only the extreme generalized eigenvalues is globally valid even when \(W\) and \(T\) do not commute. Independently, the **exact** convergence condition for every initial error is

\[
\alpha>\max\!\left\{0,\frac12\lambda_{\max}(WT^{-1}W-T)\right\}.
\]

For \(n=2\), if \(T=\operatorname{diag}(t_1,t_2)\), \(t_1,t_2>0\), and \(B=(b_{ij})\), the optimal shift is exactly

\[
\alpha_* = \frac{-d+\sqrt{d^2+8(b_{11}t_2+b_{22}t_1)}}4,
\qquad d=t_1+t_2-b_{11}-b_{22}.
\]

In particular, **the optimal shift in two dimensions is independent of \(b_{12}\) when the diagonal data in the eigenbasis of \(T\) are fixed**, although the optimal convergence factor generally depends on that coupling.

## Assumptions and scope

The actual real block coefficient matrix and the two-factor VBP preconditioner are

\[
\mathcal A=\begin{pmatrix}T&-W\\W&T\end{pmatrix},\qquad
P_{\alpha,\gamma}=
\begin{pmatrix}T+\alpha I&-\gamma W\\0&I\end{pmatrix}
\begin{pmatrix}I&0\\W&T\end{pmatrix},
\qquad \alpha,\gamma>0.
\]

All inner solves are exact, as is the algebraic recurrence \(e_{k+1}=L_{\alpha,\gamma}e_k\) with \(L_{\alpha,\gamma}=I-P_{\alpha,\gamma}^{-1}\mathcal A\). The conclusions concern this **stationary splitting iteration** and its asymptotic spectral radius; they are not claims about finite-step Euclidean amplification, inexact inner solves, or the convergence rate of a flexible GMRES outer solver. Symmetric indefiniteness of \(W\) means at least one strictly positive and one strictly negative eigenvalue; it ensures \(B\ne0\).

## Proof

**Block reduction.** Since \(T\) and \(T+\alpha I\) are positive definite, \(P_{\alpha,\gamma}\) is invertible. Direct multiplication gives

\[
\mathcal A P_{\alpha,\gamma}^{-1}=
\begin{pmatrix}
(T+B)(T+\alpha I)^{-1}&\gamma(T+B)(T+\alpha I)^{-1}W-WT^{-1}\\
0&I
\end{pmatrix}.
\]

The matrices \(\mathcal A P_{\alpha,\gamma}^{-1}\) and \(P_{\alpha,\gamma}^{-1}\mathcal A\) are similar. Consequently the eigenvalues of \(L_{\alpha,\gamma}\) are \(n\) zeros together with the generalized eigenvalues of \((\alpha I-B,T+\alpha I)\). This also proves the asserted \(\gamma\)-independence of the spectrum, but not of finite-step operator norms.

**Strict eigenvalue monotonicity.** The generalized eigenvalues are real, and their extrema are the extrema over nonzero real \(u\) of the Rayleigh quotient

\[
q_\alpha(u)=
\frac{\alpha\|u\|_2^2-u^\top Bu}
{\alpha\|u\|_2^2+u^\top Tu}.
\]

For every fixed \(u\ne0\),

\[
\frac{\partial q_\alpha(u)}{\partial\alpha}=
\frac{\|u\|_2^2\,u^\top(T+B)u}
{(\alpha\|u\|_2^2+u^\top Tu)^2}>0.
\]

For each two shifts with the second larger, the quotient difference has a strictly positive minimum on the unit sphere, by continuity and compactness. Hence both \(\ell_-(\alpha)\) and \(\ell_+(\alpha)\) are continuous and **strictly increasing** on \((0,\infty)\); this argument does not require simple eigenvalues or commuting matrices. At \(\alpha\downarrow0\), their limits are the extremes of \(-T^{-1/2}BT^{-1/2}\): both are nonpositive and at least one is strictly negative because \(B\ne0\). At \(\alpha\to\infty\), both converge to \(1\). Therefore the strictly increasing continuous function \(\ell_-+\ell_+\) has exactly one zero \(\alpha_*\). Before that point the radius is \(-\ell_-\), strictly decreasing; after it, the radius is \(\ell_+\), strictly increasing. Since for every \(u\ne0\) the quotient is strictly less than \(1\), the optimal radius is strictly less than \(1\).

**Exact convergence boundary.** The upper extreme always satisfies \(\ell_+(\alpha)<1\). The condition \(\ell_-(\alpha)>-1\) is equivalent, uniformly in nonzero \(u\), to \(2\alpha\|u\|_2^2>u^\top(B-T)u\), or \(2\alpha>\lambda_{\max}(B-T)\). Together with \(\alpha>0\), this yields exactly the stated open stability interval. Equality at a positive critical boundary produces an eigenvalue \(-1\) and therefore does not give convergence from every initial error.

**Two-dimensional formula.** In the eigenbasis of \(T\), the balancing condition is equivalent to vanishing trace of \((\alpha I-B)(T+\alpha I)^{-1}\), since this matrix has two real eigenvalues. Thus

\[
\frac{\alpha-b_{11}}{\alpha+t_1}+
\frac{\alpha-b_{22}}{\alpha+t_2}=0,
\]

which is the quadratic \(2\alpha^2+d\alpha-(b_{11}t_2+b_{22}t_1)=0\). The constant term is strictly negative because \(B\succeq0\), \(B\ne0\), and \(t_1,t_2>0\). Therefore the displayed positive root is unique. The off-diagonal entry of \(B\) affects the determinant and hence the radius, but not this trace equation.

## Verification

For a genuinely noncommuting example, take

\[
T=\operatorname{diag}(1,4),\qquad W=\begin{pmatrix}-2&1\\1&3\end{pmatrix},
\quad B=\begin{pmatrix}17/4&-5/4\\-5/4&13/4\end{pmatrix}.
\]

Direct calculation yields \(\alpha_*=(5+\sqrt{673})/8\approx3.867780442768\) and \(\rho(\alpha_*)=\sqrt{(47602-1825\sqrt{673})/5481}\approx0.216710043902\), whereas the sharp convergence threshold is approximately \(1.804247641507\). In particular, this is not a disguised simultaneous-diagonalization calculation: \(TB\ne BT\).

The paper's fixed-\(\gamma\) Frobenius quasi-optimal prescription can behave very differently for **stationary iteration**. If \(T=I_2\), \(W=\operatorname{diag}(-4,4)\), and \(\gamma=10^{-6}\), then the prescription \(\alpha=\gamma\|W\|_F^2/2\) chooses \(\alpha=1.6\cdot10^{-5}\), with \(\rho\approx15.999728>1\). The exact rate-optimal choice is \(\alpha_*=16\), giving \(\rho=0\) and a nilpotent error matrix of index at most two. This contrast concerns the stationary method, **not** the source's FGMRES experiments.

The standalone Python checker in `verification/check_vbp_shift.py` reproduces both cases, checks the full \(2n\)-dimensional matrix against the symmetric generalized-eigenvalue reduction for several \(\gamma\), and performs 80 deterministic randomized consistency tests. See `verification/output.txt` for the recorded output and `verification/requirements.txt` for dependencies. Such finite checks support implementation but do not replace the proof above.

## Relationship to prior work

Makhdomi and Khojasteh Salkuyeh (arXiv:2608.29985, first posted August 30, 2026) give the VBP factorization, real eigenvalue quotient, sufficient convergence conditions, and a Frobenius-distance shift selection; their Sections 2–4 do not give the unique **exact spectral-radius optimizer for general noncommuting** \(T,W\), the strict generalized-eigenvalue balancing rule, or the above noncommuting two-dimensional formula. Our spectral reduction uses their block structure, and no novelty is claimed for the underlying quotient itself.

Huang and Chen (2018) analyze a different relaxed block splitting preconditioner with a different parameter-dependent lower block. Zhang and Dai (2017), and Xie, Huang, Cui and Li (2024), likewise study alternative preconditioning families. Their eigenvalue or optimal-parameter conclusions cannot be transferred to this particular VBP family merely by matching the words “complex symmetric.” The general principle of equioscillating extremal errors is classical; the subject-specific contribution here is its global validity, exact root characterization and consequences for this noncommuting VBP iteration.

## Limitations

The optimality is for asymptotic spectral radius, not transient norms or a prescribed fixed iteration count. Computing extreme generalized eigenvalues may itself be costly; inexact computation and floating-point safeguards are not analyzed. The global rule does not assert that VBP stationary iteration is preferable to Krylov solvers. A 2024 PMBP paper with optimal-parameter results was not available in full text through the attempted access routes; it represents a residual literature-comparison risk, although its preconditioner has a different block formula. No independent validation has been performed.

## References

1. M. Makhdomi and D. Khojasteh Salkuyeh, “A variant of the block preconditioner for indefinite complex symmetric linear systems,” arXiv:2608.29985 (first posted 2026-08-30), https://arxiv.org/abs/2608.29985 .
2. Y. Huang and G. Chen, “A relaxed block splitting preconditioner for complex symmetric indefinite linear systems,” *Open Mathematics* **16** (2018), 561–573, DOI: 10.1515/math-2018-0051.
3. J. Zhang and H. Dai, “A new block preconditioner for complex symmetric indefinite linear systems,” *Numerical Algorithms* **74** (2017), 889–903, DOI: 10.1007/s11075-016-0175-y.
4. X. Xie, Z. Huang, J. Cui and B. Li, “A preconditioned version of the MBP iteration method for a class of complex symmetric linear systems,” *Computational and Applied Mathematics* **43** (2024), article 123, DOI: 10.1007/s40314-024-02643-4.
