# Rank-controlled sharpness of a quantum interior-point preconditioner
## Finding
Wu, Yang, and Terlaky's quantum interior-point method preconditions a reduced augmented Newton system using a scalar proxy for its positive-definite block. The source proves a worst-case \(O(1/\mu)\) condition-number bound as the duality-gap parameter \(\mu\) decreases, improving the prior quadratic dependence. The following rank-sensitive statement identifies when that rate is genuinely attained.

Let \(A\in\mathbb R^{m\times n}\), \(b\in\mathbb R^m\), and \(c\in\mathbb R^n\) be integer data with \(\operatorname{rank}(A)=m\), \(b\ne0\), and the source's strictly feasible primal-dual and admissible-basis assumptions. Assume the exact central path
\[
Ax(\mu)=b,\quad A^\top y(\mu)+s(\mu)=c,\quad x_i(\mu)s_i(\mu)=\mu
\]
converges as \(\mu\downarrow0\) to a strictly complementary optimum \((x^*,y^*,s^*)\): for every index exactly one of \(x_i^*,s_i^*\) is positive.

Fix \(0<\gamma_1<1\). Put
\[
J=\{i:x_i^*>0\},\quad N=J^c,\quad r=\operatorname{rank}(A_J),
\]
and write
\[
\omega_0=\max\{\|x^*\|_\infty,\|s^*\|_\infty\},\qquad
h_0=\frac{\gamma_1\sigma_{\min}(A)^2}{\omega_0^2}.
\]
Here the smallest singular value is positive because \(A\) has full row rank. The source's threshold partition equals \((J,N)\) for all sufficiently small positive \(\mu\).

When \(r=m\), the reduced preconditioned matrix \(Y(\mu)\) obeys
\[
\boxed{\lim_{\mu\downarrow0}\kappa_2(Y(\mu))=1.}
\]
When \(1\le r<m\), let \(P_\perp\) be the orthogonal projector onto \(\ker A_J^\top\), and let \(Q_\perp\) denote the following operator restricted to that \((m-r)\)-dimensional subspace:
\[
Q_\perp=
\left.
P_\perp A_N\operatorname{diag}\!\bigl((s_N^*)^{-2}\bigr)A_N^\top P_\perp
\right|_{\ker A_J^\top}.
\]
Then \(Q_\perp\) is positive definite and
\[
\boxed{\lim_{\mu\downarrow0}\mu\kappa_2(Y(\mu))
=\frac{h_0}{\lambda_{\min}(Q_\perp)}>0.}
\]
More precisely, \(r\) singular values of \(Y(\mu)\) tend to \(1\), and the remaining \(m-r\) singular values, divided by \(\mu\), tend to the eigenvalues of \(Q_\perp/h_0\), counting multiplicity.

An integer-data instance in just two constraints and three variables realizes the sharp regime. Take
\[
A=\begin{pmatrix}1&0&0\\0&1&-1\end{pmatrix},\quad
b=\begin{pmatrix}1\\0\end{pmatrix},\quad
c=\begin{pmatrix}0\\1\\1\end{pmatrix}.
\]
Its exact central path is
\[
x(\mu)=\begin{pmatrix}1\\\mu\\\mu\end{pmatrix},\quad
y(\mu)=\begin{pmatrix}-\mu\\0\end{pmatrix},\quad
s(\mu)=\begin{pmatrix}\mu\\1\\1\end{pmatrix}.
\]
For all sufficiently small positive \(\mu\), the source's prescribed scalar proxy is \(\hat h=\gamma_1\), and its reduced preconditioned matrix is exactly
\[
\boxed{Y(\mu)=\operatorname{diag}\left(
\frac{1+\mu}{1+\gamma_1\mu(1+\mu)},
\frac{2\mu}{\gamma_1}\right).}
\]
Consequently
\[
\boxed{\lim_{\mu\downarrow0}\mu\kappa_2(Y(\mu))=\frac{\gamma_1}{2}.}
\]
For comparison, the unpreconditioned normal matrix is \(\operatorname{diag}(1/\mu,2\mu)\), with condition number \(1/(2\mu^2)\) for small \(\mu\). Thus the source's linear reciprocal-gap bound is sharp for its specified choice of preconditioner even when the optimal partition is already identified exactly.

## Assumptions and scope
The LP and preconditioning notation is exactly that of the primary source. In addition to the source's integer data, full-row-rank constraints, admissible basis, and strict primal-dual feasibility, the theorem explicitly assumes convergence of the central path to a strictly complementary optimum and \(b\ne0\). Strict complementarity means all coordinates have exactly one positive limiting primal or dual slack component. These hypotheses guarantee \(r\ge1\) and a fixed optimal partition near \(\mu=0\).

The source defines
\[
D=X^{-1}S,\quad D=\operatorname{diag}(D_1,D_2),\quad
F_1=I+D_1,\quad B=A_JF_1^{-1/2},
\]
\[
H=BB^\top+A_ND_2^{-1}A_N^\top,\quad
\hat h=\gamma_1\sigma_{\min}(A)^2/\omega(\mu)^2,
\]
\[
\hat Z=B^\top B/\hat h+D_1,\quad
G=B\hat Z^{-1}B^\top/\hat h,\quad
Y=G+(I-G)H/\hat h.
\]
The running scalar \(\omega(\mu)\) is the maximum coordinate magnitude among \(x(\mu)\) and \(s(\mu)\). Since this is the exact central path, \(x_i(\mu)s_i(\mu)=\mu\), and its points satisfy every fixed central-neighborhood parameter \(0<\gamma_1<1\).

The conclusion concerns the condition number of the actual reduced matrix used in the source's quantum linear-system stage. It is not a lower bound for every conceivable preconditioner or for the total query complexity of all quantum interior-point algorithms. The theorem does not assert that every central path has a strictly complementary limit; that is a stated assumption.

## Proof
**Partition stabilization.** For \(i\in J\), \(x_i(\mu)\to x_i^*>0\). For \(i\in N\), strict complementarity implies \(s_i(\mu)\to s_i^*>0\), hence \(x_i(\mu)=\mu/s_i(\mu)=O(\mu)\). The source puts coordinate \(i\) in partition 1 precisely when
\[
x_i(\mu)\ge\sqrt{[(1-\gamma_1)n+\gamma_1]\mu}.
\]
Thus partition 1 equals \(J\) for every sufficiently small \(\mu>0\), regardless of the fixed \(\gamma_1\).

**Fixed subspaces and limiting blocks.** Write \(\mathcal R=\operatorname{ran}(A_J)\) and \(\mathcal N=\ker A_J^\top\). Their orthogonal direct sum is \(\mathbb R^m\), with dimensions \(r\) and \(m-r\). On the central path,
\[
D_1=\mu\operatorname{diag}(x_J(\mu)^{-2}),\qquad
D_2^{-1}=\mu\operatorname{diag}(s_N(\mu)^{-2}).
\]
Introduce
\[
Q(\mu)=A_N\operatorname{diag}(s_N(\mu)^{-2})A_N^\top,
\qquad Q(\mu)\longrightarrow Q_0.
\]
Also \(\hat h(\mu)\to h_0>0\). The matrix \(B=A_JF_1^{-1/2}\) has fixed range \(\mathcal R\) and tends to \(A_J\). Consequently
\[
H=BB^\top+\mu Q(\mu).
\]

**The source's preconditioner.** The resolvent identity applied to \(G\) gives
\[
G=\left(BD_1^{-1}B^\top\right)
\left(\hat h I+BD_1^{-1}B^\top\right)^{-1}.
\]
Set
\[
C(\mu)=B\operatorname{diag}(x_J(\mu)^2)B^\top.
\]
Then \(G=C(\mu)[C(\mu)+\mu\hat h I]^{-1}\). On \(\mathcal R\), the restriction of \(C(\mu)\) is uniformly positive definite because \(C(\mu)\to A_J\operatorname{diag}((x_J^*)^2)A_J^\top\) and all \(x_i^*>0\) on \(J\). On \(\mathcal N\), \(C\) and \(G\) vanish. Thus, in an orthonormal basis adapted to \(\mathcal R\oplus\mathcal N\),
\[
G=\begin{pmatrix}I_r+O(\mu)&0\\0&0\end{pmatrix},
\qquad
I-G=\begin{pmatrix}O(\mu)&0\\0&I_{m-r}\end{pmatrix}.
\]
The displayed \(O(\mu)\) terms are in operator norm.

**Rank-dependent singular values.** In the same orthonormal coordinates,
\[
H=\begin{pmatrix}O(1)&\mu Q_{12}(\mu)\\
\mu Q_{21}(\mu)&\mu Q_{22}(\mu)
\end{pmatrix},
\]
where \(Q_{22}(\mu)\to Q_\perp\). Combining this with the exact source formula \(Y=G+(I-G)H/\hat h\) yields
\[
Y(\mu)=\begin{pmatrix}
I_r+O(\mu)&O(\mu^2)\\
O(\mu)&\mu Q_\perp/h_0+o(\mu)
\end{pmatrix}.
\]
If \(r=m\), this says \(Y\to I_m\), whence \(\kappa_2(Y)\to1\).

Suppose \(1\le r<m\). Because \(A\) has full row rank, \(Q_\perp\) is positive definite: if \(v\in\mathcal N\setminus\{0\}\), then \(A_J^\top v=0\) and \(A_N^\top v\ne0\), so
\[
v^\top Q_\perp v=\sum_{j\in N}\frac{(A_j^\top v)^2}{(s_j^*)^2}>0.
\]
The upper-left block of \(Y\) is invertible for small \(\mu\). Block Gaussian elimination on the left and right with factors \(I+O(\mu)\) reduces it to a block diagonal matrix with upper block \(I_r+O(\mu)\) and lower Schur complement
\[
\frac{\mu}{h_0}Q_\perp+o(\mu),
\]
because the correction from the off-diagonal blocks is \(O(\mu^3)\). Left and right factors tending to the identity preserve the leading singular-value asymptotics. Therefore \(r\) singular values tend to one, and the others divided by \(\mu\) converge to the eigenvalues of \(Q_\perp/h_0\). In particular,
\[
\lim_{\mu\downarrow0}\mu\kappa_2(Y)=h_0/\lambda_{\min}(Q_\perp).
\]

**Integral sharpness witness.** For the displayed \(2\times3\) LP, directly checking \(Ax=b\), \(A^\top y+s=c\), and \(x_is_i=\mu\) proves the stated central path. The unique primal optimal solution is \(x^*=(1,0,0)\), and the limiting dual slack is \(s^*=(0,1,1)\), so strict complementarity holds. The basis consisting of columns 1 and 2 of \(A\) is \(I_2\), which satisfies the source's admissible-basis condition, and \(AA^\top=\operatorname{diag}(1,2)\). For small \(\mu\), the partition is \(J=\{1\}\), \(N=\{2,3\}\); \(\omega=1\) and \(\hat h=\gamma_1\). Hence
\[
D_1=(\mu),\quad D_2=\operatorname{diag}(\mu^{-1},\mu^{-1}),\quad
B=\begin{pmatrix}(1+\mu)^{-1/2}\\0\end{pmatrix},
\]
\[
H=\operatorname{diag}((1+\mu)^{-1},2\mu),\quad
G=\operatorname{diag}((1+\gamma_1\mu(1+\mu))^{-1},0).
\]
Substitution into \(Y=G+(I-G)H/\gamma_1\) gives the exact claimed diagonal spectrum. Its entries tend respectively to \(1\) and \(0\), with the smaller asymptotic to \(2\mu/\gamma_1\). Therefore \(\mu\kappa_2(Y)\to\gamma_1/2\). Finally
\[
AD^{-1}A^\top=\operatorname{diag}(\mu^{-1},2\mu),
\]
so the original normal-equation condition number is \(1/(2\mu^2)\) for all sufficiently small \(\mu\).

## Verification
All universal statements are proved by finite-dimensional matrix identities and singular-value perturbation, not numerical extrapolation. The strict-complementarity limit is an explicit hypothesis. The integer-data example has exact rational central-path coordinates and a fully explicit diagonal preconditioned matrix.

The bundled standard-library checker constructs the example's source blocks at rational central-path values, checks the identities in exact fractional arithmetic, confirms the admissible integer LP and optimal support, and tests the asserted limiting constant at decreasing positive rational gaps. Finite tests corroborate the exact proof; they do not certify the asymptotic theorem by themselves.

## Relationship to prior work
Wu, Yang, and Terlaky, *A preconditioned inexact infeasible quantum interior point method for linear optimization* (arXiv:2412.11307; DOI 10.1007/s10589-025-00750-4), derive the precise scalar preconditioner \(\hat H=\hat hI\) and the reduced matrix \(Y\) used above. Their Lemma 3.6 bounds \(\kappa_2(Y)=O(1/\mu)\), without identifying an asymptotic support-rank dichotomy or an example attaining the rate on the exact central path. This result supplies both and computes the leading coefficient.

Chai and Toh, *Preconditioning and iterative solution of symmetric indefinite linear systems arising from interior point methods for linear programming* (DOI 10.1007/s10589-006-9006-8), provide the foundational reduced-augmented preconditioner and general spectral decomposition. Their Section 6 studies other diagonal approximations, notably \(\hat H=\mu I\) and \(\hat H=\operatorname{diag}(H)\), and identifies eigenvalue clustering associated with rank-deficient partitions. This is important prior context for the rank mechanism. It does not give the source's fixed-scalar \(\hat h=\gamma_1\sigma_{\min}(A)^2/\omega^2\) singular-value limit, the exact \(Q_\perp\) coefficient, or the present minimal integer central-path witness. The finding is not a claim of discovering the generic phenomenon of degenerate interior-point conditioning.

## Limitations
The theorem concerns the particular reduced matrix and fixed scalar preconditioner prescribed by Wu, Yang, and Terlaky. Other scalar or matrix-valued preconditioners can behave differently; indeed Chai and Toh study such choices. The conclusion is about matrix conditioning, not a lower bound for quantum query complexity or an impossibility theorem for all quantum interior-point methods. The general asymptotics assume a strictly complementary central-path limit and nonzero right-hand side, and exclude the special case of an empty positive optimal support. No rates are asserted away from the asymptotic central-path regime.

## References
1. Z. Wu, X. Yang, and T. Terlaky, *A preconditioned inexact infeasible quantum interior point method for linear optimization*, arXiv:2412.11307v1 (first publicly posted 2024-12-15); *Computational Optimization and Applications* 93 (2026), 1225--1257, DOI 10.1007/s10589-025-00750-4.
2. J.-S. Chai and K.-C. Toh, *Preconditioning and iterative solution of symmetric indefinite linear systems arising from interior point methods for linear programming*, *Computational Optimization and Applications* 36 (2007), 221--247, DOI 10.1007/s10589-006-9006-8.
