# Exact repeated-reset backtracking cost in fixed-baseline SCP
## Finding
For Algorithm 1 of Lu--Wang on the admissible scalar problem \(g(z)=a z^2/2\), \(q=\delta_{[-R,R]}\), and \(c(z)=z^2-R_c^2\) with \(a>0\), \(R_c>R\), nonzero \(z^0\), and a radius large enough that every reached line-search trial remains in the box, the surrogate constraint is inactive and every inner trial has \(z^{k+1,i}=(1-a/L_i)z^k\), where \(L_i=\underline L\rho^i\). A nonzero trial is accepted exactly when \(2L_i\ge a+\beta\), so every nonterminal outer iteration accepts at the same index \(i_*=\lceil\log_\rho((a+\beta)/(2\underline L))\rceil_+\) and at \(L_*=\underline L\rho^{i_*}\). With the exact smoothness constant \(L=a\), this \(i_*\) is exactly the upper bound in the source's Theorem 4, so that per-outer bound is attained at every outer iteration. The accepted recurrence is \(z^{k+1}=q_*z^k\), where \(q_*=1-a/L_*\) and \(|q_*|<1\). If \(L_*=a\), the method reaches zero and satisfies its stopping test on the first accepted outer step. If \(L_*\ne a\), the stopping test is exactly \(C_*|z^k|\le\tau\), where \(C_*=a|a-L_*|/L_*\), and the first stopping outer index is \(K_*=\lceil\log(C_*|z^0|/\tau)/\log(1/|q_*|)\rceil_+\). Consequently the method solves exactly \((K_*+1)(i_*+1)\) proximal subproblems, including \((K_*+1)i_*\) rejected trials. When \(i_*>0\), resetting the line search to \(\underline L\) therefore replays the same rejected curvature trials at every outer iteration; on this scalar family, starting each later outer iteration at the previously accepted \(L_*\) would save exactly \(K_*i_*\) rejected solves without changing the accepted step.

This gives an exact sharpness instance for the source's inner-loop bound and isolates a repeated calibration cost caused by resetting the line search to the same fixed baseline at every outer iteration.

## Assumptions and scope
Consider the scalar problem
\[
 g(z)=\frac{a}2 z^2,\qquad q(z)=\delta_{[-R,R]}(z),\qquad c(z)=z^2-R_c^2,
\]
with \(a>0\), \(R_c>R>0\). Use the source parameters \(\underline L>0\), \(\rho>1\), \(\beta>0\), and \(\tau>0\), and take a nonzero initial point \(z^0\in(-R,R)\). Define
\[
 i_*:=\left\lceil\log_\rho\!\left(\frac{a+\beta}{2\underline L}\right)\right\rceil_+,
 \qquad L_*:=\underline L\rho^{i_*},
\]
where \(\lceil t\rceil_+:=\max\{0,\lceil t\rceil\}\). Assume
\[
 R>|z^0|\max_{0\le i\le i_*}\left|1-\frac{a}{\underline L\rho^i}\right|.
\]
This ensures that every trial point reached before acceptance lies strictly inside the box. Since the constraint has Lipschitz-gradient constant \(L_c=2\), its quadratic upper model is exact:
\[
 c(w)+c'(w)(z-w)+\frac{L_c}2(z-w)^2=z^2-R_c^2.
\]
Hence it is strictly inactive for all trial points, and its multiplier is zero.

The corresponding two-point model function in the source's KL assumption reduces on its finite domain to the scalar quadratic. Its exact gap and limiting-subgradient norm are
\[
 \bar h(z,w)-\bar h^*=\frac{a}2z^2,
 \qquad \operatorname{dist}(0,\partial\bar h(z,w))=a|z|.
\]
Thus the source's KL condition holds globally with exponent \(1/2\) and constant \(\sqrt{2a}\). Taking the source level parameter at least \(aR^2/2\) covers the whole box. This verifies that the test family satisfies the assumptions used by the convergence and complexity analysis rather than merely reproducing the iteration algebra outside the stated regime.

## Proof
At inner trial \(i\), Algorithm 1 uses
\[
 L_i=\underline L\rho^i.
\]
Because the box and surrogate constraint are inactive at every reached trial, the constrained proximal-gradient subproblem has the unique solution
\[
 z^{k+1,i}=z^k-\frac{g'(z^k)}{L_i}
 =\left(1-\frac{a}{L_i}\right)z^k.
\]
For \(z^k\ne0\), write \(s_i=z^{k+1,i}-z^k=-a z^k/L_i\). The source sufficient-decrease condition is
\[
 g(z^{k+1,i})\le g(z^k)-\frac{\beta}2|s_i|^2.
\]
Substitution gives
\[
 \frac{a}2\left(1-\frac{a}{L_i}\right)^2|z^k|^2
 \le \frac{a}2|z^k|^2-\frac{\beta a^2}{2L_i^2}|z^k|^2,
\]
which is equivalent to
\[
 2L_i\ge a+\beta.
\]
Therefore every nonzero outer state rejects precisely the trials \(0,\ldots,i_*-1\) and accepts trial \(i_*\). The accepted value is always \(L_*\). The source's Theorem 4 states the per-outer upper index
\[
 \bar i=\left\lceil\log_\rho\!\left(\frac{\beta+L}{2\underline L}\right)\right\rceil_+.
\]
For this problem the exact gradient-Lipschitz constant is \(L=a\), so \(\bar i=i_*\). The theorem's inner-loop bound is therefore attained exactly on every outer iteration before termination.

The accepted recurrence is
\[
 z^{k+1}=q_*z^k,
 \qquad q_*:=1-\frac{a}{L_*}.
\]
Since \(L_*\ge(a+\beta)/2>a/2\), one has \(|q_*|<1\). If \(L_*=a\), then \(q_*=0\), the first accepted step reaches the solution, and the stopping residual vanishes.

Now suppose \(L_*\ne a\). The constraint multiplier is zero, so the source stopping test reduces to
\[
 |g'(z^{k+1})-g'(z^k)-L_*(z^{k+1}-z^k)|\le\tau.
\]
Using \(g'(z)=az\) and \(z^{k+1}-z^k=-a z^k/L_*\), this is exactly
\[
 C_*|z^k|\le\tau,
 \qquad C_*:=\frac{a|a-L_*|}{L_*}.
\]
Because \(|z^k|=|q_*|^k|z^0|\), the first outer index satisfying the test is
\[
 K_*=
 \left\lceil
 \frac{\log(C_*|z^0|/\tau)}{\log(1/|q_*|)}
 \right\rceil_+.
\]
The executed outer indices are \(0,1,\ldots,K_*\). Each performs exactly \(i_*+1\) proximal subproblem solves, of which exactly \(i_*\) are rejected. Hence the total counts are
\[
 N_{\rm sub}=(K_*+1)(i_*+1),
 \qquad
 N_{\rm rej}=(K_*+1)i_*.
\]
When \(i_*>0\), the rejected sequence is identical at every outer iteration because the algorithm restarts from the same \(\underline L\). On this family only, if each later outer iteration were instead initialized at the previously accepted \(L_*\), its first trial would satisfy the same exact acceptance inequality, and the number of rejected solves would fall from \((K_*+1)i_*\) to \(i_*\). The exact saving is therefore \(K_*i_*\). This comparison is diagnostic and does not assert a convergence theorem for a modified algorithm outside this family.

## Verification
The companion `verify.py` reproduces the symbolic threshold and checks a concrete instance
\[
 a=3,\quad \beta=1,\quad \underline L=0.2,\quad \rho=2,
 \quad \tau=10^{-3},\quad z^0=0.1,
\]
with \(R=2\) and \(R_c=3\). It obtains \(i_*=4\), \(L_*=3.2\), \(q_*=1/16\), \(K_*=2\), fifteen proximal subproblem solves, and twelve rejected trials. It also checks the source stopping residual at each accepted outer step and verifies that every reached trial stays strictly inside the box and strictly satisfies the inactive constraint.

The executable check is a finite consistency test for the representative parameter choice. The general statement above is proved algebraically and does not rely on finite enumeration.

## Relationship to prior work
Lu and Wang's Algorithm 1 fixes \(L_{k,i}=\underline L\rho^i\) at every outer iteration and Theorem 4 gives an upper bound on the accepted inner index. The paper does not state that this upper bound is attained at every outer iteration, nor does it derive the exact repeated-rejection count or the scalar warm-start comparison above.

The earlier line-search SCP framework of Yu, Pong, and Lu chooses outer-iteration initial local constants from bounded intervals and line-searches objective and constraints separately. Lu's earlier structured nonlinear-programming SCP variant likewise allows dynamically selected local Lipschitz estimates. Those mechanisms do not imply the fixed-baseline reset identity analyzed here. The present finding is therefore source-specific: it identifies the exact behavior of the 2025/2026 fixed-baseline scheme on an admissible quadratic instance rather than asserting a property of SCP methods in general.

## Limitations
The exact count is proved for a one-dimensional quadratic whose constraint is strictly inactive. The box-radius condition is needed so that no reached trial is clipped. The logarithmic formula for \(K_*\) assumes \(L_*\ne a\); the case \(L_*=a\) is handled separately by immediate solution after the first accepted step. The warm-start statement is only a counterfactual calculation on this family and is not a global safety or convergence claim for a modified method. No claim is made that the repeated-reset cost dominates the total complexity on general constrained minimax problems.

## References
1. Z. Lu and X. Wang, *A first-order method for constrained nonconvex-nonconcave minimax optimization*, arXiv:2510.01168; later published with DOI 10.1007/s10107-026-02415-4. Algorithm 1 and Theorem 4 are the primary objects analyzed here.
2. P. Yu, T. K. Pong, and Z. Lu, *Convergence rate analysis of a sequential convex programming method with line search for a class of constrained difference-of-convex optimization problems*, arXiv:2001.06998, DOI 10.1137/20M1314057.
3. Z. Lu, *Sequential Convex Programming Methods for A Class of Structured Nonlinear Programming*, arXiv:1210.3039.
