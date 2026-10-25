# Exact nullspace-variance law for doubly randomized coordinate descent on rank-one inverse problems

## Finding

Uniform, independent sampling of a data row and a solution coordinate in doubly stochastic block gradient descent (DSBGD) can recover exact data while failing to select the initial-guess minimum-norm solution. The failure is quantified by an exact second-moment identity for every deterministic admissible stepsize schedule, not merely by an isolated trajectory.

**Theorem.** Fix integers \(r\ge 2\), \(m\ge 2\), and positive reals \(c_1,\ldots,c_r\). Let \(A\in\mathbb R^{r\times m}\) have entries \(A_{ij}=c_i\), let \(y_i=c_i\), and initialize \(x^{(0)}=0\). For each \(t\ge0\), choose \(I_t\) uniformly in \(\{1,\ldots,r\}\) and \(J_t\) uniformly in \(\{1,\ldots,m\}\), independently across times and between indices, and make the source DSBGD update
\[
x^{(t+1)}=x^{(t)}+\eta_t c_{I_t}^{2}\bigl(1-\mathbf 1^\top x^{(t)}\bigr)e_{J_t}.
\]
Assume the deterministic stepsizes obey \(0<\eta_t<1/\lambda_{\max}\), \(\sum_{t=0}^{\infty}\eta_t=\infty\), where \(\lambda_i=c_i^2\) and \(\lambda_{\max}=\max_i\lambda_i\). Define
\[
a=\frac1r\sum_{i=1}^r\lambda_i,\qquad b=\frac1r\sum_{i=1}^r\lambda_i^2,\qquad q_t=1-2a\eta_t+b\eta_t^2,\qquad Q_t=\prod_{s=0}^{t-1}q_s,\quad Q_0=1.
\]
Then the unique Euclidean minimum-norm solution is \(x^\dagger=m^{-1}\mathbf1\), and for every integer \(k\ge0\),
\[
\boxed{\mathbb E\|x^{(k)}-x^\dagger\|_2^2=\frac{Q_k}{m}+\left(1-\frac1m\right)b\sum_{t=0}^{k-1}\eta_t^2Q_t},\qquad
\boxed{\mathbb E\|Ax^{(k)}-y\|_2^2=\left(\sum_{i=1}^r\lambda_i\right)Q_k}.
\]
The iterates converge almost surely and in mean square to a random exact solution \(x^{(\infty)}\). They satisfy \(\mathbb E x^{(\infty)}=x^\dagger\), yet
\[
\boxed{\mathbb E\|x^{(\infty)}-x^\dagger\|_2^2=\left(1-\frac1m\right)b\sum_{t=0}^{\infty}\eta_t^2Q_t\ge\left(1-\frac1m\right)b\eta_0^2>0}.
\]
Thus no positive deterministic stepsize schedule of the stated class, including decaying schedules, yields mean-square convergence to the minimum-norm solution for this family.

For constant \(\eta_t=\eta\) with \(0<\eta<1/\lambda_{\max}\), put \(q=1-2a\eta+b\eta^2\). The exact finite-time error and asymptotic floor simplify to
\[
\mathbb E\|x^{(k)}-x^\dagger\|_2^2=\frac{q^k}{m}+\left(1-\frac1m\right)\frac{\eta b}{2a-\eta b}(1-q^k),\qquad
\lim_{k\to\infty}\mathbb E\|x^{(k)}-x^\dagger\|_2^2=\left(1-\frac1m\right)\frac{\eta b}{2a-\eta b}.
\]

For the genuinely two-row and two-coordinate system
\[
A=\begin{pmatrix}1&1\\2&2\end{pmatrix},\quad y=\begin{pmatrix}1\\2\end{pmatrix},\quad \eta=\frac18,
\]
one has \(L=\max_i\|A_{i,:}\|_2^2=8\) and \(\eta L=1<2\), satisfying the fixed-step condition of the motivating source. Nevertheless,
\[
\boxed{\mathbb E\|x^{(k)}-(\tfrac12,\tfrac12)\|_2^2=\frac{17}{126}+\frac{23}{63}\left(\frac{65}{128}\right)^k},\qquad
\boxed{\mathbb E\|Ax^{(k)}-y\|_2^2=5\left(\frac{65}{128}\right)^k}.
\]
This isolates a persistent **solution-nullspace error**, despite geometrically vanishing data residual and unbiased limiting reconstruction.

## Assumptions and scope

All spaces are real and finite-dimensional with the ordinary Euclidean norm. The forward operator has rank one, with at least two nonzero data rows and two unknown coordinates. The exact data are consistent; there is no observation noise. Row and coordinate samples are mutually independent and uniform with replacement, as in DSBGD update (1.2) and Algorithm 1 of Xia and Zhou. The stepsizes are deterministic and strictly positive, with each \(\eta_t\lambda_i<1\) and divergent total sum. These hypotheses include source Assumption 2.1(i): take \(L=m\lambda_{\max}\), \(\eta_t=\mu_t/L\), \(0<\mu_t\le c_0<2\), and \(\sum_t\mu_t=\infty\), since \(m\ge2\). The coordinate-invariance Assumption 2.3 used separately for certain source rate statements does not hold for this rank-one operator.

## Proof

Since \(Ax=y\) is equivalent to \(\mathbf1^\top x=1\), its unique minimum-Euclidean-norm solution is \(x^\dagger=m^{-1}\mathbf1\). Let
\[
p_t=1-\mathbf1^\top x^{(t)},\qquad z_t=x^{(t)}-(1-p_t)m^{-1}\mathbf1,\qquad v_j=e_j-m^{-1}\mathbf1.
\]
Then \(\mathbf1^\top z_t=0\), \(p_0=1\), \(z_0=0\), and the update splits exactly into
\[
p_{t+1}=(1-\eta_t\lambda_{I_t})p_t,\qquad z_{t+1}=z_t+\eta_t\lambda_{I_t}p_t v_{J_t}.
\]
Because \(J_t\) is independent of the past and of \(I_t\), one has \(\mathbb E[v_{J_t}]=0\), \(\mathbb E\|v_{J_t}\|_2^2=1-m^{-1}\). Conditional cross terms in the squared norm of \(z_{t+1}\) therefore vanish. Independence of \(I_t\) from the past yields
\[
\mathbb E p_{t+1}^2=q_t\mathbb E p_t^2,\qquad
\mathbb E\|z_{t+1}\|_2^2=\mathbb E\|z_t\|_2^2+\left(1-\frac1m\right)b\eta_t^2\mathbb E p_t^2.
\]
Iterating from the initial conditions proves \(\mathbb E p_k^2=Q_k\) and the exact sum for \(\mathbb E\|z_k\|_2^2\). As
\[
x^{(k)}-x^\dagger=z_k-p_k m^{-1}\mathbf1,
\]
with the two summands orthogonal on every sample path, their squared norms add. The residual equals \(-p_k(c_1,\ldots,c_r)^\top\), proving the other finite-time identity.

For each row, \(0<1-\eta_t\lambda_i<1\), so \(0<p_t\le\exp(-\lambda_{\min}\sum_{s<t}\eta_s)\to0\) on every sample path. Moreover, every increment \(x^{(t+1)}-x^{(t)}\) has nonnegative entries, and the sum of its entries is \(p_t-p_{t+1}\). Thus the nonnegative vector sequence has total coordinate mass at most one and converges componentwise, hence in norm, to some \(x^{(\infty)}\) with \(\mathbf1^\top x^{(\infty)}=1\). Uniform boundedness of the iterates implies convergence in mean square by dominated convergence. Conditional mean-zero coordinate increments show \(\mathbb E z_k=0\); hence \(\mathbb E x^{(\infty)}=x^\dagger\). The displayed finite-time identity and \(Q_k\to0\) yield the limiting second moment. Its first summand in the nonnegative series, at \(t=0\), is strictly positive. Finally, for constant \(\eta\), \(q_t=q\in(0,1)\), and geometric summation yields the stated closed form.

In the two-by-two example, \(a=5/2\), \(b=17/2\), \(q=65/128\), and substitution gives the rational identities above. The positivity gap is not numerical roundoff: it holds in exact arithmetic for every iteration and for the almost-sure limit.

## Verification

The accompanying `verify.py` enumerates independent row/column choices in exact rational arithmetic for 0 through 6 iterations of the two-by-two example, plus additional variable-step systems with up to three data rows and four coordinates. For each finite case it independently compares exhaustive branching against the algebraic expected squared solution error, expected squared residual, and mean scalar residual. It also checks the rational constant-step formula. Run `python verify.py` using only the Python standard library. All exact finite checks pass. Enumeration is not a proof of the all-step formula or almost-sure convergence; the derivation above supplies those universal facts.

## Relationship to prior work

Xia and Zhou (arXiv:2610.15399v1, Sections 2–3, Algorithm 1, Assumption 2.1, Theorems 2.1 and 3.1) formulate doubly sampled DSBGD and state convergence to the initial-guess minimum-norm solution under the stated stepsize condition. Their proof of Theorem 3.1 passes from convergence to an exact solution to a uniqueness assertion. In a noninjective inverse problem, uniqueness of the minimum-norm solution does not imply uniqueness of all exact solutions. The present exact moment identity identifies the specific residual-versus-nullspace distinction in a rank-one subfamily and quantifies the extent of that distinction.

Jin and Liu (arXiv:2405.13340, Section 2) analyze randomized block coordinate descent with only coordinate sampling and prove convergence to a random solution in a general setting; this provides the relevant precedent for the qualitative possibility of a random exact solution. Their results do not state the present doubly sampled exact finite-time variance formula. Razaviyayn, Hong, Reyhanian and Luo (arXiv:1810.05251, Theorems 1–2) treat a differently sampled doubly stochastic Gauss–Seidel method, with full-column-rank solution-error bounds and broader residual estimates. Du and Sun (arXiv:1912.13291, Theorems 2, 8, 11) explicitly distinguish norm-of-expected-error, full-column-rank mean-square error and residual convergence. Han and Xie (arXiv:2208.05437, Theorems 3.1–3.2) likewise distinguish residual mean-square convergence from norm of the expected iterate. Xie and Yang (arXiv:2610.04685v1, Section 1) assume full column rank, excluding the present nullspace regime. None of these materially inspected statements gives the specific time-dependent nullspace variance identity or its all-admissible-stepsize positive lower bound.

## Limitations

The calculation is exact for the specified rank-one operator, uniform independent row/coordinate sampling, real scalar coordinate blocks, consistent data and deterministic stepsizes. It does not characterize arbitrary rank-deficient operators or data noise, nor the sampling-without-replacement case. The positive floor depends on the stepsize schedule; for small constant \(\eta\), it is of order \(\eta\), not uniform in \(\eta\to0\). A vanishing data residual is compatible with a nonzero distance to the selected minimum-norm solution. Older general randomized-coordinate results motivate the qualitative issue, so novelty is claimed only for the explicit doubly sampled moment law and its all-schedule consequence.

## References

- Y. Xia and Z. Zhou, *On the convergence of doubly stochastic block gradient descent method for linear inverse problems*, arXiv:2610.15399v1 (11 October 2026), https://arxiv.org/html/2610.15399v1.
- Q. Jin and D. Liu, *Randomized block coordinate descent method for linear ill-posed problems*, arXiv:2405.13340 (2024), https://arxiv.org/abs/2405.13340.
- M. Razaviyayn, M. Hong, N. Reyhanian and Z.-Q. Luo, *A linearly convergent doubly stochastic Gauss–Seidel algorithm for solving linear equations and a certain class of over-parameterized optimization problems*, arXiv:1810.05251, https://arxiv.org/pdf/1810.05251.
- K. Du and X.-H. Sun, *A doubly stochastic block Gauss–Seidel algorithm for solving linear equations*, arXiv:1912.13291, https://arxiv.org/pdf/1912.13291.
- D. Han and J. Xie, *On pseudoinverse-free randomized methods for linear systems: Unified framework and acceleration*, arXiv:2208.05437, https://arxiv.org/pdf/2208.05437.
- D.-Y. Xie and X. Yang, *On randomized batch-sampling coordinate descent methods for solving linear least-squares problems*, arXiv:2610.04685v1 (3 October 2026), https://arxiv.org/html/2610.04685v1.
