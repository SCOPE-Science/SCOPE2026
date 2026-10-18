# Exact nullspace-risk frontier for doubly sampled rank-one inverse updates

## Finding

Consider the doubly stochastic block gradient descent (DSBGD) rule that independently samples one data row and one signal coordinate. On rank-one, exactly consistent inverse problems, its mean-square residual can tend to zero while the solution-reconstruction error converges to a strictly positive, explicitly computable floor. This report gives an exact finite-horizon risk identity, a limiting covariance matrix, and a sharp step-size frontier separating decreasing from increasing reconstruction error.

For the precise assumptions below, put
\[
U_2=\frac{1}{r}\sum_{i=1}^r u_i^2,\qquad U_4=\frac{1}{r}\sum_{i=1}^r u_i^4,\qquad
V_2=\sum_{j=1}^c v_j^2,\qquad V_4=\sum_{j=1}^c v_j^4.
\]
For \(0<\eta<\eta_c:=2U_2V_2/(U_4V_4)\), define
\[
q=1-\frac{2\eta U_2V_2}{c}+\frac{\eta^2U_4V_4}{c},\qquad
F=\frac{\eta U_4(V_2-V_4/V_2)}{2U_2V_2-\eta U_4V_4}.
\]
With \(x^\dagger=v/V_2\), the following identities hold for every integer \(k\ge0\):
\[
\mathbb E|1-v^\top x_k|^2=q^k,\qquad
\mathbb E\|x_k-x^\dagger\|_2^2=F(1-q^k)+\frac{q^k}{V_2}.
\]
The iterates converge almost surely and in mean square to an exactly feasible but non-minimum-norm random limit \(X_\infty\), with \(\mathbb E X_\infty=x^\dagger\) and
\[
\operatorname{Cov}(X_\infty)=
\frac{\eta U_4}{2U_2V_2-\eta U_4V_4}
\sum_{j=1}^c v_j^2(e_j-v_jx^\dagger)(e_j-v_jx^\dagger)^\top.
\]
The reconstruction error decreases, stays constant, or increases with iteration according as
\[
\eta\lessgtr\eta_{\mathrm{risk}}:=\frac{2U_2}{U_4V_2},
\]
with equality giving constant risk. Because at least two entries of \(v\) are nonzero, \(0<\eta_{\mathrm{risk}}<\eta_c\). Thus a nonempty interval has contracting residual and strictly *increasing* expected squared solution error. The unique residual-optimal step is \(\eta_{\mathrm{res}}=U_2V_2/(U_4V_4)\). At this step the limiting error is \((V_2^2-V_4)/(V_2V_4)\), larger than the starting risk exactly when \(V_2^2>2V_4\). As \(\eta\uparrow\eta_c\), the reconstruction-error floor diverges even though each smaller step gives \(q<1\).

A counterexample respecting a conservative original-source step bound is
\[
u=(1,2)^\top,\qquad v=(1,1)^\top,\qquad \eta=\tfrac18,
\quad A=\begin{pmatrix}1&1\\2&2\end{pmatrix},\quad y=(1,2)^\top.
\]
Here \(\|A_2\|_2^2=8\), so the constant normalized step is \(\mu_k=\eta\max_i\|A_i\|^2=1<2\). Nevertheless \(q=65/128\) and \(F=17/126>0\). Hence a hypothesis consisting solely of the paper's Assumption 2.1(i) does not force mean-square convergence to the minimum-norm solution. Moreover, for aligned data noise \(y^\delta=(1+\delta/\sqrt5)y\) and stopping index \(k(\delta)=\lceil\delta^{-1}\rceil\), the advertised conditions \(k(\delta)\to\infty\) and \(\delta^2\sum_{t=1}^{k(\delta)}\mu_t\to0\) hold, yet the limiting mean-square reconstruction error is again \(17/126\).

## Assumptions and scope

Let \(r,c\ge2\) be finite integers, let \(u\in\mathbb R^r\setminus\{0\}\), and let \(v\in\mathbb R^c\) have at least two nonzero entries. Take the rank-one forward operator \(A=uv^\top\), exact observations \(y=u\), initial iterate \(x_0=0\), and constant step \(\eta>0\). At each integer step sample \(I_k\) uniformly from \(\{1,\ldots,r\}\) and \(J_k\) uniformly from \(\{1,\ldots,c\}\), independently of one another and all past samples, and update
\[
x_{k+1}=x_k+\eta u_{I_k}^2v_{J_k}(1-v^\top x_k)e_{J_k}.
\]
All operations are exact real arithmetic. The inequality \(0<\eta<\eta_c\) is necessary and sufficient for strict second-moment contraction of the scalar residual in this family; it is not assumed to be the admissible interval of a different algorithm or of arbitrary matrices. The minimum Euclidean-norm solution of \(Ax=y\) relative to \(x_0=0\) is \(x^\dagger=v/V_2\). The forward residual is \(Ax_k-y=-u(1-v^\top x_k)\), so its expected squared norm is \(\|u\|_2^2q^k\).

## Proof

Set \(s_k=1-v^\top x_k\) and \(z_k=x_k-(1-s_k)x^\dagger\). Then \(s_0=1\), \(z_0=0\), and \(v^\top z_k=0\) identically. Direct substitution gives
\[
s_{k+1}=(1-\eta u_{I_k}^2v_{J_k}^2)s_k,
\]
and, conditional on the history before step \(k\),
\[
\mathbb E[s_{k+1}^2\mid\mathcal F_k]
=s_k^2\left(1-\frac{2\eta U_2V_2}{c}+\frac{\eta^2U_4V_4}{c}\right)
=q s_k^2.
\]
Here \(q=\mathbb E(1-\eta u_I^2v_J^2)^2\ge0\). For positive \(\eta\), the strict inequality \(q<1\) is equivalent to \(\eta<\eta_c\), and induction yields \(\mathbb E s_k^2=q^k\).

The orthogonal component has increments
\[
z_{k+1}-z_k=\eta u_{I_k}^2v_{J_k}s_k(e_{J_k}-v_{J_k}x^\dagger).
\]
Because \(\sum_j v_j(e_j-v_jx^\dagger)=v-V_2x^\dagger=0\), the process \((z_k)\) is a square-integrable martingale. In particular its increments are pairwise orthogonal in \(L^2\), and their conditional matrix second moment is
\[
\mathbb E[(z_{k+1}-z_k)(z_{k+1}-z_k)^\top\mid\mathcal F_k]
=\frac{\eta^2U_4s_k^2}{c}\sum_j v_j^2(e_j-v_jx^\dagger)(e_j-v_jx^\dagger)^\top.
\]
Summing this martingale identity from \(0\) to \(k-1\) gives
\[
\operatorname{Cov}(z_k)=\frac{\eta^2U_4}{c}\frac{1-q^k}{1-q}
\sum_jv_j^2(e_j-v_jx^\dagger)(e_j-v_jx^\dagger)^\top.
\]
Since \(1-q=\eta(2U_2V_2-\eta U_4V_4)/c\), this is the claimed covariance coefficient times \(1-q^k\). The trace of the fixed matrix is \(\sum_jv_j^2(1-v_j^2/V_2)=V_2-V_4/V_2\), which is strictly positive when \(v\) has at least two nonzero coordinates. Finally \(x_k-x^\dagger=z_k-s_kx^\dagger\), and the two terms are orthogonal pointwise; \(\|x^\dagger\|^2=1/V_2\). This yields the finite-horizon risk identity.

For convergence, the exact conditional increment second moment is \(\eta^2U_4V_2s_k^2/c\). Thus
\[
\sum_{k=0}^\infty\mathbb E\|x_{k+1}-x_k\|_2
\le\eta\sqrt{U_4V_2/c}\sum_{k=0}^\infty q^{k/2}<\infty.
\]
Tonelli's theorem implies the increments are absolutely summable almost surely. Moreover the orthogonal martingale has bounded second moments and converges in \(L^2\), while \(s_k\to0\) in \(L^2\). Hence \(x_k\to X_\infty\) almost surely and in \(L^2\); \(v^\top X_\infty=1\) almost surely. Since \(\mathbb E z_k=0\) and \(\mathbb E s_k\to0\), the limiting mean is \(x^\dagger\); passage to the limit gives its displayed covariance and positive risk floor.

Subtracting the starting risk gives
\[
F-\frac1{V_2}=
\frac{\eta U_4V_2^2-2U_2V_2}{V_2(2U_2V_2-\eta U_4V_4)}.
\]
The denominator is strictly positive throughout the stable interval. Therefore the sign is that of \(\eta-\eta_{\mathrm{risk}}\), and because \(\mathbb E\|x_k-x^\dagger\|^2=F+(1/V_2-F)q^k\), the indicated monotonicity is exact. The strict inequality \(V_4<V_2^2\) proves \(\eta_{\mathrm{risk}}<\eta_c\). Completing the square in \(q(\eta)\) shows that its unique minimum is at \(\eta_{\mathrm{res}}=U_2V_2/(U_4V_4)\). Substitution supplies the stated floor; its divergence at \(\eta_c\) follows from the positive numerator and the vanishing denominator.

For the explicit two-row example, \(U_2=5/2\), \(U_4=17/2\), \(V_2=V_4=2\), and \(c=2\), yielding exactly \(q=65/128\) and \(F=17/126\). For the noisy example, by linearity of the update with respect to the observations and with zero initial iterate, every noisy path equals \(x_k^\delta=(1+\delta/\sqrt5)x_k\). Consequently the noisy terminal error tends to \(F\) in mean square along the given stopping rule; the additional deterministic bias tends to zero. This example uses two *distinct* sampled row values and two coordinates.

## Verification

Run `python3 verify.py` in a standard Python environment. It propagates exact-rational first and second moments by independent direct enumeration of the affine transition matrices, not by calling the claimed martingale formula to generate states. It additionally enumerates every sampled path through six steps for the displayed two-row example and checks both three-coordinate risk-increase and residual-optimal examples. The packaged program completes **5,579 exact comparison checks**. Finite tests support the algebra but cannot certify the universal theorem; the analytical arguments above establish its quantifiers.

## Relationship to prior work

Xia and Zhou (2026, arXiv:2610.15399v1) define the identical doubly sampled row-coordinate update and state minimum-norm convergence under Assumption 2.1(i) in Theorem 3.1 and a noisy-data regularizing property in Theorem 2.1. Their proof of Theorem 3.1 identifies an arbitrary feasible solution with the minimum-norm solution without the additional nullspace-invariance justification. The source's more restrictive Assumption 2.3 is introduced for different later rate claims; it is not part of those two theorems. The exact counterexample above is within Assumption 2.1(i), but the full covariance and sharp residual-versus-reconstruction frontier are the principal quantitative results here.

The *qualitative* phenomenon that randomized Gauss–Seidel may fail to reach the minimum-norm solution on underdetermined systems is already known: Ma, Needell and Ramdas (2015, arXiv:1503.08235) explicitly explain it and motivate randomized extended methods. Jin and Liu (2024, arXiv:2405.13340) prove weak convergence to a random feasible solution for randomized block coordinate descent and impose additional conditions to identify the minimum-norm solution. Han and Xie (2022, arXiv:2208.05437) give broad convergence bounds for pseudoinverse-free randomized schemes. These results are acknowledged; they do not directly state the displayed rank-one exact finite-time solution-risk law, full limiting covariance and sharp step thresholds for the independently *doubly sampled* update. No claim is made that failure of minimum-norm convergence itself is a new observation.

## Limitations

The exact formulas require a finite-dimensional rank-one forward matrix, independent uniform row and coordinate sampling, exact consistent data, zero initialization, and constant step. The true exact-data theorem does not establish any identical formula for general matrices, nonuniform or dependent sampling, noisy data beyond the explicit aligned-noise construction, finite precision, or time-varying steps. The bound \(\eta<\eta_c\) is a mean-square-residual threshold, not a general stability guarantee for the full iterate at the endpoint. The three-coordinate example of increasing reconstruction risk at \(\eta=1/4\) lies outside the source's conservative bound \(\eta\max_i\|A_i\|^2<2\); it is used only for the exact rank-one mean-square-stable family. The two-coordinate counterexample, separately, satisfies that conservative bound. Exact formulas do not imply bibliographic uniqueness; equivalent classical random-projection formulations remain a possible overlap risk.

## References

1. Y. Xia and Z. Zhou, *On the convergence of doubly stochastic block gradient descent method for linear inverse problems*, arXiv:2610.15399v1 (first public 2026-10-11). https://arxiv.org/html/2610.15399v1
2. A. Ma, D. Needell and A. Ramdas, *Convergence properties of randomized extended Gauss-Seidel and Kaczmarz methods*, arXiv:1503.08235 (2015). https://arxiv.org/abs/1503.08235
3. Q. Jin and D. Liu, *Randomized block coordinate descent method for linear ill-posed problems*, arXiv:2405.13340 (2024). https://arxiv.org/abs/2405.13340
4. D. Han and J. Xie, *On pseudoinverse-free randomized methods for linear systems: Unified framework and acceleration*, arXiv:2208.05437 (2022). https://arxiv.org/abs/2208.05437
