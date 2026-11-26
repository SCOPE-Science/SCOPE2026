# Exact nullspace-risk frontier for doubly sampled rank-one inverse updates

## Finding

For the rank-one row-coordinate update specified below, let
\[
 U_j=r^{-1}\sum_{i=1}^r u_i^j,\qquad V_j=\sum_{i=1}^c v_i^j\qquad(j=2,4),\qquad x^\dagger=v/V_2.
\]
For a constant step \(0<\eta<\eta_c=2U_2V_2/(U_4V_4)\), put
\[
 q=1-2\eta U_2V_2/c+\eta^2 U_4V_4/c,\qquad
 F=\frac{\eta U_4(V_2-V_4/V_2)}{2U_2V_2-\eta U_4V_4}.
\]
Then for every integer \(k\ge0\), with \(q^0=1\) also when \(q=0\),
\[
 \mathbb E|1-v^\top x_k|^2=q^k,\qquad
 \mathbb E\|x_k-x^\dagger\|_2^2=F(1-q^k)+q^k/V_2.
\]
The iterates converge almost surely and in \(L^2\) to a feasible random limit \(X_\infty\) with mean \(x^\dagger\) and covariance
\[
 \operatorname{Cov}(X_\infty)=\frac{\eta U_4}{2U_2V_2-\eta U_4V_4}
 \sum_{j=1}^c v_j^2(e_j-v_jx^\dagger)(e_j-v_jx^\dagger)^\top.
\]
Its selection risk is \(F>0\), so the limit differs from the minimum-norm solution with positive probability, **not necessarily almost surely**.

Write \(\eta_{\rm risk}=2U_2/(U_4V_2)\), which is strictly between 0 and \(\eta_c\). For \(0<q<1\), the expected squared reconstruction error strictly decreases below \(\eta_{\rm risk}\), is constant at that step, and strictly increases above it. At \(q=0\) the same sign rule compares step 1 with step 0, after which the risk is constant. Thus the stable interval contains a nonempty open subinterval with geometric residual contraction and strictly increasing reconstruction risk. The residual-optimal step (minimizing \(q\)) is \(\eta_{\rm res}=U_2V_2/(U_4V_4)\). Its floor is \((V_2^2-V_4)/(V_2V_4)\), larger than the initial risk precisely when \(V_2^2>2V_4\). As \(\eta\uparrow\eta_c\), \(F\) diverges.

## Assumptions and scope

Take finite \(r,c\ge2\), \(u\in\mathbb R^r\setminus\{0\}\), and \(v\in\mathbb R^c\) with at least two nonzero entries. Use \(A=uv^\top\), \(y=u\), \(x_0=0\), and independent uniform row and coordinate indices \(I_k,J_k\), drawn independently at every step. The exact-arithmetic update is
\[
 x_{k+1}=x_k+\eta u_{I_k}^2v_{J_k}(1-v^\top x_k)e_{J_k}.
\]
Feasibility means \(v^\top x=1\); the squared forward residual has expectation \(\|u\|_2^2q^k\). The upper threshold \(\eta_c\) characterizes strict scalar second-moment residual contraction under these assumptions, not stability of a general DSBGD problem or convergence on the threshold.

## Proof

Put \(s_k=1-v^\top x_k\), let \(P=I-vv^\top/V_2\) be the nullspace projector, and write \(z_k=Px_k\). The residual is multiplied at each step by \(1-\eta u_{I_k}^2v_{J_k}^2\). The square of that multiplier has mean \(q\ge0\); \(q<1\) for positive steps exactly when \(\eta<\eta_c\). Independence yields \(\mathbb E s_k^2=q^k\).

The projected increment is \(\Delta z_k=\eta u_{I_k}^2v_{J_k}s_kPe_{J_k}\). Given the past, its mean is zero since \(\sum_jv_jPe_j=Pv=0\). Its conditional second-moment matrix is \(\eta^2 U_4s_k^2 H/c\), where \(H=\sum_j v_j^2(Pe_j)(Pe_j)^\top\). Orthogonality of martingale increments gives
\[
 \mathbb E z_kz_k^\top=\frac{\eta^2U_4}{c}\frac{1-q^k}{1-q}H.
\]
The trace of \(H\) is \(V_2-V_4/V_2>0\), since at least two entries of \(v\) are nonzero. The decomposition \(x_k-x^\dagger=z_k-s_k x^\dagger\) is orthogonal; taking expected squares gives the risk identity.

For convergence, \(\|x_{k+1}-x_k\|_{L^2}=\eta\sqrt{U_4V_2/c}\,q^{k/2}\). Summability gives an \(L^2\) limit by completeness and almost-sure absolute summability by Tonelli. The residual tends to zero in \(L^2\), so the limit is feasible almost surely. Its mean and covariance follow from the martingale mean and the covariance identity by \(L^2\) convergence. In particular, a positive trace shows only that the limit is not identically the minimum-norm solution.

For \(R_k=\mathbb E\|x_k-x^\dagger\|_2^2\),
\[
 R_{k+1}-R_k=(1-q)q^k(F-1/V_2),\qquad
 F-1/V_2=\frac{\eta U_4V_2^2-2U_2V_2}{V_2(2U_2V_2-\eta U_4V_4)}.
\]
The monotonicity rule follows, including \(q=0\). That degeneracy requires every sampled multiplier to be zero and so can occur at only one step size for fixed \(u,v\). Since \(V_4<V_2^2\), the interval \((\eta_{\rm risk},\eta_c)\) is nonempty even after excluding that point. Minimizing the strictly convex quadratic \(q\) and substituting its minimizer into \(F\) proves the residual-optimal comparison. The floor diverges at the upper threshold because the numerator is positive there and the denominator approaches zero from above.

## Exact examples and boundary cases

* For \(u=(1,2)^\top\), \(v=(1,1)^\top\), and \(\eta=1/8\), one has \(q=65/128\), \(F=17/126\), and the normalized step \(\mu_k=\eta\max_i\|A_i\|_2^2=1<2\) for singleton rows. With data \(y^\delta=(1+\delta/\sqrt5)y\) the noise has norm \(\delta\), and the coupled iterates obey \(x_k^\delta=(1+\delta/\sqrt5)x_k\) by linearity and zero initialization. For \(k(\delta)=\lceil\delta^{-1}\rceil\), \(\delta^2\sum_{t=1}^{k(\delta)}\mu_t\to0\) and \(k(\delta)\to\infty\); hence \(x_{k(\delta)}^\delta\to X_\infty\) in \(L^2\) and \(\mathbb E\|x_{k(\delta)}^\delta-x^\dagger\|_2^2\to17/126\).
* For \(u=(1,1)^\top\), \(v=(1,1,1)^\top\), and \(\eta=1\), every first update lands at a coordinate vector and eliminates the residual: \(q=0\) and the risk is \(1/3\) at step 0 and \(2/3\) at every later step.
* For \(u=(4,5)^\top\), \(v=(3,4)^\top\), and \(\eta=1/400\), each weighted squared entry \(\eta u_i^2v_j^2\) lies in \((0,1]\), so \(0<q<1\). First choosing row 1 and coordinate 1 gives \(x_1=(3/25,0)^\top\) and residual \(16/25\). Next choosing row 2 and coordinate 2 gives \(x_2=(3/25,4/25)^\top=x^\dagger\), and the state is then absorbed. The specified two-step event has probability \(1/16\), even though the overall limiting risk is positive.

## Verification

`python3 verify.py` in the source package reproduces its finite exact-rational checks: direct affine iteration of first and second moments, path enumeration through six updates in the two-row example, and cases of risk increase and residual-optimal steps. The script includes the one-step-absorption risk example. The displayed two-step event is checked directly by its exact updates above. Finite checks are not the proof of convergence or of the general risk law.

## Relationship to prior work and limitations

Xia and Zhou [1] use the same DSBGD update. The first example satisfies their conservative Assumption 2.1(i) and tests the minimum-norm conclusions of their Theorems 2.1 (noisy data) and 3.1 (exact data). The exact-data failure of minimum-norm selection is already known qualitatively for other randomized Gauss–Seidel and coordinate-descent rules [2,3]. General convergence bounds for pseudoinverse-free methods [4] are not the rank-one finite-horizon covariance and upper-versus-lower step threshold derived here. Under the conservative normalized bound \(\eta\max_i\|A_i\|^2<2\), one has \(\eta<\eta_{\rm risk}\) since \(U_4/U_2\le\max_i u_i^2\). The interval with strictly increasing risk is a result for the broader rank-one residual-stable family; the counterexample to minimum-norm selection uses a step within the conservative bound. No claims are made for arbitrary matrices, nonuniform sampling, general noise, or variable steps.

## References

The divergent sum of normalized steps in Xia and Zhou's Assumption 2.1(i) holds since \(\mu_k=1\). Their one-based indexing shifts the stopping index by one without changing either limit. Neither of the two cited theorems requires the later Assumption 2.3. The explicit examples therefore contradict the stated exact-data and noisy-data minimum-norm conclusions as written in v1.

The public reports [5,6] give risk formulas in all-ones signal-coordinate subfamilies. In particular [5] includes this same two-row example and floor and treats variable step schedules in that subfamily. Those special cases are not claimed as distinct contributions here. The result here concerns arbitrary \(v\), the full covariance, and the risk frontier in the larger residual-stable constant-step interval.

1. Y. Xia and Z. Zhou, *On the convergence of doubly stochastic block gradient descent method for linear inverse problems*, arXiv:2610.15399v1, https://arxiv.org/html/2610.15399v1.
2. A. Ma, D. Needell and A. Ramdas, *Convergence properties of randomized extended Gauss-Seidel and Kaczmarz methods*, arXiv:1503.08235, https://arxiv.org/abs/1503.08235.
3. Q. Jin and D. Liu, *Randomized block coordinate descent method for linear ill-posed problems*, arXiv:2405.13340, https://arxiv.org/abs/2405.13340.
4. D. Han and J. Xie, *Pseudoinverse-free randomized methods for linear systems: Unified framework and acceleration*, arXiv:2208.05437, https://arxiv.org/abs/2208.05437.
5. *Exact nullspace-variance law for doubly randomized coordinate descent on rank-one inverse problems*, https://github.com/Resultary/2026/blob/main/2026/10/25/SCOPE-exact-nullspace-variance-law-for-doubly-randomized-coordinate-de--28e88f145876/RESULT.md.
6. *Finite-budget reconstruction-optimal steps in rank-one randomized coordinate descent*, https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-finite-budget-reconstruction-optimal-steps-in-rank-one-randomize--13ced3d5640d/RESULT.md.
