# A sharp sampling-concentration frontier for one-step stale randomized Gauss–Seidel

## Finding
For each integer \(n\ge 2\), any positive diagonal matrix \(A=\operatorname{diag}(a_1,\ldots,a_n)\), and any fixed independent coordinate-sampling probabilities \(p_i>0\) with \(\sum_{i=1}^{n}p_i=1\), consider one-step-stale randomized Gauss–Seidel with relaxation \(\beta>0\). At every update it selects coordinate \(I_t=i\) with probability \(p_i\) and uses the *preceding global iterate*, rather than the current iterate, to evaluate the selected residual. The iteration is mean-square convergent for **every** deterministic initial pair precisely when
\[
0<\beta<\beta_{\mathrm{crit}}(p_{\max}),\qquad
\beta_{\mathrm{crit}}(p)=\frac{4}{1+\sqrt{1+8p}},\qquad
p_{\max}=\max_i p_i.
\]
At equality, some nonzero initial pairs have a strictly positive invariant expected quadratic energy. Above this threshold, some deterministic initial pairs have exponentially growing mean-square error. These alternatives are sharp and require no spectral bound on the diagonal entries of \(A\).

More precisely, *each coordinate* has its own complete stability classification with threshold \(\beta_{\mathrm{crit}}(p_i)\): below it all its initial pairs contract exponentially in mean square; at equality its nonzero initial pairs conserve a positive expected quadratic energy; above it every nonzero initial pair has exponentially increasing expected quadratic energy. Uniform sampling yields the exact dimension-dependent frontier
\[
\beta_{\mathrm{crit}}(1/n)=\frac{4}{1+\sqrt{1+8/n}}=2-\frac4n+O(n^{-2}).
\]
In particular, with uniform sampling and one-step staleness, the unrelaxed choice \(\beta=1\) is mean-square stable for every \(n\ge2\), whereas \(\beta>\beta_{\mathrm{crit}}(1/n)\) forces exponential mean-square growth for every nonzero initial pair.

## Assumptions and scope
Let \(b\in\mathbb R^n\) be arbitrary, let \(x_* = A^{-1}b\), and start with deterministic vectors \(x^{(-1)},x^{(0)}\in\mathbb R^n\). Let \(I_0,I_1,\ldots\) be independent, with \(\Pr(I_t=i)=p_i\), independent of the initial pair. With \(P_i=e_i e_i^{\mathsf T}\), the update is
\[
x^{(t+1)}=x^{(t)}-\beta P_{I_t}A^{-1}(Ax^{(t-1)}-b)
=x^{(t)}-\beta P_{I_t}(x^{(t-1)}-x_*).
\]
The second equality uses that \(A\) is diagonal. Thus for \(e^{(t)}=x^{(t)}-x_*\),
\[
e^{(t+1)}=e^{(t)}-\beta P_{I_t}e^{(t-1)}.
\]
At \(t=0\), the conventional one-state initialization is obtained by choosing \(x^{(-1)}=x^{(0)}\). The theorem permits arbitrary deterministic initial pairs to give a complete stability statement. Mean-square convergence means \(\mathbb E\|e^{(t)}\|_A^2\to0\); exponential convergence means a geometric bound in \(t\). The matrix is real positive diagonal, the sampling is fixed i.i.d., and arithmetic is exact. The stale state is a globally consistent one-step-old state, not a componentwise fresh local read.

## Proof
Fix a coordinate \(i\), abbreviate \(p=p_i\), and write \(y_t=e_i^{(t)}\). The sequence of indicators \(\xi_t=\mathbf1_{\{I_t=i\}}\) is i.i.d. Bernoulli with success probability \(p\). Therefore
\[
y_{t+1}=y_t-\beta\xi_t y_{t-1}.
\]
Define
\[
h=\frac{\beta p}{1+\beta p},\qquad
c=\frac{\beta^2p+2h}{2},\qquad
Q=\begin{pmatrix}1&-h\\-h&c\end{pmatrix},\qquad
\eta=\frac{\beta^2p-2h}{2}.
\]
The matrix \(Q\) is positive definite: \(0<h<1\), \(c>h>h^2\), so \(\det Q=c-h^2>0\). For \(z_t=(y_t,y_{t-1})^{\mathsf T}\), conditional on the past up to time \(t\), expand \(z_{t+1}^{\mathsf T}Qz_{t+1}\). Using \(\mathbb E\xi_t=\mathbb E\xi_t^2=p\) and \(\beta p(1-h)=h\), the mixed term cancels exactly and gives
\[
\mathbb E[z_{t+1}^{\mathsf T}Qz_{t+1}\mid z_t]
=z_t^{\mathsf T}Qz_t+\eta(y_t^2+y_{t-1}^2).
\]
The drift coefficient has the exact factorization
\[
\eta=\frac{\beta p\bigl(\beta(1+\beta p)-2\bigr)}{2(1+\beta p)}.
\]
Because \(Q\) is positive definite, its quadratic form is bounded above by \(\lambda_{\max}(Q)\|z\|_2^2\) and below by \(\lambda_{\min}(Q)\|z\|_2^2\). When \(\eta<0\), this conditional identity yields
\[
\mathbb E[z_{t+1}^{\mathsf T}Qz_{t+1}]
\le\left(1+\frac{\eta}{\lambda_{\max}(Q)}\right)
\mathbb E[z_t^{\mathsf T}Qz_t],
\]
where the factor is nonnegative and strictly below one. When \(\eta>0\), the inequality reverses, with a factor strictly above one. At \(\eta=0\), the expected quadratic form is exactly constant. For every nonzero deterministic initial coordinate pair, the initial quadratic form is positive, proving all three alternatives. The equation \(\eta=0\) is \(\beta^2p+\beta-2=0\), whose unique positive root is \(4/(1+\sqrt{1+8p})\).

Each coordinate contributes \(a_i y_t^2\) to the squared \(A\)-norm. Finite summation of the coordinatewise conclusions proves uniform mean-square convergence for every initial pair exactly when the strict inequality holds for all \(p_i\), i.e. when \(\beta<\beta_{\mathrm{crit}}(p_{\max})\), since \(\beta_{\mathrm{crit}}\) decreases strictly with \(p\). At and above this global threshold, initialize a coordinate realizing \(p_{\max}\) with a nonzero pair and all other coordinates at zero: the corresponding conservation or growth rules out convergence. Under uniform sampling every coordinate has the same drift sign, so all nonzero initial pairs grow exponentially above the frontier. Expanding \(\sqrt{1+8/n}\) proves the stated asymptotic formula. This completes the proof.

## Verification
The independent standalone script `verify_stale_rgs.py` reproduces the conditional quadratic identity with exact rational arithmetic, for both uniform and nonuniform coordinate probabilities, positive diagonal weights, and different relaxation parameters. It also exhaustively enumerates short independent coordinate-selection sequences and checks the three-moment recursion
\[
\begin{pmatrix}U_{t+1}\\V_{t+1}\\W_{t+1}\end{pmatrix}
=\begin{pmatrix}1&-2\beta p&\beta^2p\\1&-\beta p&0\\1&0&0\end{pmatrix}
\begin{pmatrix}U_t\\V_t\\W_t\end{pmatrix},
\]
where \(U_t=\mathbb Ey_t^2\), \(V_t=\mathbb Ey_ty_{t-1}\), and \(W_t=\mathbb Ey_{t-1}^2\). The script reports 1,366 successful exact checks. These finite checks corroborate, but do not replace, the algebraic proof for arbitrary dimension, distributions, and time horizons.

## Relationship to prior work
Carson and Ma, *Asynchronous Jacobi and randomized Gauss–Seidel methods in shared and distributed memory: A unified convergence-rate analysis* (arXiv:2609.15605v1, first public September 14, 2026), provide a general unified asynchronous framework with sufficient convergence conditions. The present result uses a globally consistent one-step-old read, a special shared-memory schedule within that framework, and gives a *necessary and sufficient* boundary on diagonal positive-definite systems, including a nonuniform-sampling classification. In the uniform identity case the general sufficient condition in their Theorem 1 reduces to \(\beta<2/[1+2(n^{-1/2}+n^{-1})]\), whereas the exact frontier above is \(\beta<4/[1+\sqrt{1+8/n}]\). These bounds are different, so the general sufficient theorem does not imply the exact classification.

Avron, Druinsky, and Gupta, *Revisiting Asynchronous Linear Solvers: Provable Convergence Rate Through Randomization* (arXiv:1304.6475; J. ACM 2015), introduce randomized shared-memory asynchronous Gauss–Seidel and sufficient rates. Their inconsistent-read theorem is restricted to underrelaxation and does not classify the sharp diagonal stability frontier. Related analysis of stale *off-coordinate* coupling in two-dimensional systems does not cover the same-coordinate stale-read recurrence used here. The update and its general convergence background are known; only the exact sampling-concentration stability classification and its positive quadratic identity are assessed here.

## Limitations
The conclusion does not extend automatically to nondiagonal matrices, data-dependent or history-dependent coordinate sampling, variable delays, inconsistent coordinatewise reads, or implementations guaranteeing fresh ownership of the updated coordinate. It concerns second moments rather than wall-clock performance or floating-point behavior. The exact criterion is relative to a fixed one-global-update delay and a fixed relaxation parameter. Bibliographic equivalence under differently named stochastic-delay systems remains a residual novelty risk.

## References
1. Erin Carson and Yuxin Ma, *Asynchronous Jacobi and randomized Gauss–Seidel methods in shared and distributed memory: A unified convergence-rate analysis*, arXiv:2609.15605v1 (2026-09-14), https://arxiv.org/abs/2609.15605.
2. Haim Avron, Alex Druinsky, and Anshul Gupta, *Revisiting Asynchronous Linear Solvers: Provable Convergence Rate Through Randomization*, arXiv:1304.6475 (2013); Journal of the ACM **62**(6) (2015), https://arxiv.org/abs/1304.6475, https://doi.org/10.1145/2814566.
