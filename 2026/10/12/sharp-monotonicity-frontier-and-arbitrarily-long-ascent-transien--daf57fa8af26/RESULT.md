# Sharp monotonicity frontier and arbitrarily long ascent transients for AdaNorm on a scalar quadratic
## Finding
Consider deterministic exact-gradient AdaNorm
\[
\gamma_-1=\varsigma>0,\qquad
\gamma_k=\gamma_k - 1+\|\nabla f(x_k)\|^2,
\qquad
x_k + 1=x_k-\frac{\eta}{\sqrt{\gamma_k}}\nabla f(x_k),
\]
with \(\eta>0\), on the scalar strongly convex quadratic
\[
f(x)=\frac{\lambda}{2}x^2,\qquad \lambda>0.
\]
Write
\[
c=\frac{\eta\lambda}{\sqrt{\varsigma}}.
\]
Then objective monotonicity for every initialization and every iteration has the sharp frontier
\[
f(x_{k+1})\le f(x_k)\text{ for all starts and all }k
\quad\Longleftrightarrow\quad
c\le2.
\]

When \(c>2\), the first step increases the objective exactly on
\[
0<|x_0|<
\frac{1}{\lambda}
\sqrt{\frac{\eta^2\lambda^2}{4}-\varsigma},
\]
and the exact worst first-step amplification is
\[
\sup_{x_0\ne0}\frac{f(x_1)}{f(x_0)}=(c-1)^2,
\]
with the supremum approached as \(x_0\to0\).

The instability is not merely a one-step event. For every fixed integer \(N\ge1\),
\[
\frac{x_j}{x_0}\longrightarrow(1-c)^j,
\qquad
\frac{f(x_j)}{f(x_0)}\longrightarrow(c-1)^{2j}
\quad (0\le j\le N)
\]
as \(x_0\to0\). Therefore, if \(c>2\), for every prescribed \(N\) there is a neighborhood of the minimizer in which every nonzero start sufficiently close to zero produces \(N\) consecutive strict objective increases.

## Assumptions and scope
The result uses the one-block, exact-gradient specialization of AdaNorm stated by Gratton and Toint. Their notation initializes the scalar preconditioner with \(\gamma_{-1}=\varsigma\) and updates it using the current squared gradient before taking the step. On the quadratic above,
\[
\nabla f(x)=\lambda x,
\]
so the recurrence is exactly
\[
\gamma_k=\gamma_{k-1}+\lambda^2x_k^2,
\qquad
x_{k+1}=x_k\left(1-\frac{\eta\lambda}{\sqrt{\gamma_k}}\right).
\]
No stochastic noise, momentum, block coupling, or matrix preconditioning is used.

The statement concerns objective monotonicity and transient stability, not eventual convergence. It does not contradict global convergence results for AdaNorm with arbitrary positive hyperparameters.

## Proof
For any iteration with \(x_k\ne0\),
\[
\frac{f(x_{k+1})}{f(x_k)}=
\left(1-\frac{\eta\lambda}{\sqrt{\gamma_k}}\right)^2.
\]
Because \(\gamma_k\ge\varsigma\), if
\[
c=\frac{\eta\lambda}{\sqrt{\varsigma}}\le2,
\]
then
\[
0<
\frac{\eta\lambda}{\sqrt{\gamma_k}}
\le2,
\]
and hence \(f(x_{k+1})\le f(x_k)\) at every iteration. This proves sufficiency.

For necessity, suppose \(c>2\). At the first iteration
\[
\gamma_0=\varsigma+\lambda^2x_0^2.
\]
Strict ascent is equivalent to
\[
\left|1-\frac{\eta\lambda}{\sqrt{\varsigma+\lambda^2x_0^2}}\right|>1.
\]
The fraction is positive, so this is equivalent to
\[
\frac{\eta\lambda}{\sqrt{\varsigma+\lambda^2x_0^2}}>2,
\]
which rearranges to the stated open interval
\[
0<|x_0|<
\lambda^{-1}
\sqrt{\eta^2\lambda^2/4-\varsigma}.
\]
Thus universal monotonicity fails whenever \(c>2\).

For the first-step amplification, put
\[
t(x_0)=\frac{\eta\lambda}{\sqrt{\varsigma+\lambda^2x_0^2}}.
\]
As \(|x_0|\) ranges over positive values, \(t(x_0)\) ranges over \((0,c)\), with \(t(x_0)\to c\) as \(x_0\to0\). Therefore
\[
\sup_{x_0\ne0}\frac{f(x_1)}{f(x_0)}
=
\sup_{0<t<c}(1-t)^2
=
(c-1)^2
\]
when \(c>2\).

It remains to prove arbitrarily long ascent transients. Fix \(N\). For each fixed \(j\le N\), the recurrence is continuous in the initial value near \(x_0=0\). Inductively,
\[
x_j=O(x_0),
\]
and hence, for every fixed \(k<N\),
\[
\gamma_k
=
\varsigma+\lambda^2\sum_{i=0}^k x_i^2
=
\varsigma+O(x_0^2).
\]
Consequently
\[
1-\frac{\eta\lambda}{\sqrt{\gamma_k}}
=
1-c+O(x_0^2).
\]
Induction on \(j\) gives
\[
\frac{x_j}{x_0}\to(1-c)^j.
\]
Since \(f(x)=\lambda x^2/2\), it follows that
\[
\frac{f(x_j)}{f(x_0)}\to(c-1)^{2j}.
\]
Equivalently, for every fixed \(j<N\),
\[
\frac{f(x_{j+1})}{f(x_j)}\to(c-1)^2>1.
\]
There are only finitely many such inequalities for a fixed \(N\), so all remain strictly larger than one for sufficiently small nonzero \(|x_0|\). This proves the arbitrary finite ascent claim.

## Verification
The bundled script `artifacts/verify_adanorm_frontier.py` checks the exact first-step frontier, replays universal monotonicity for random scalar instances satisfying \(c\le2\), and demonstrates increasingly long ascent prefixes for \(c=3\) as the starting point approaches the minimizer.

These finite checks are consistency tests only. The quantified statements for every initialization and every fixed \(N\) follow from the algebra and continuity argument above.

## Relationship to prior work
Gratton and Toint formulate AdaNorm in exactly the cumulative-squared-gradient form used here and prove convergence and complexity results in a unified adaptive-preconditioning framework without requiring a sufficiently small master stepsize. Their paper does not state an objective-monotonicity threshold, a local repelling multiplier, or an arbitrarily long ascent-transient theorem for scalar quadratics.

Ward, Wu, and Bottou prove robust convergence of AdaGrad-Norm for arbitrary positive hyperparameters and emphasize adaptation to an unknown smoothness constant. Their full text gives the same scalar accumulator mechanism but does not state the frontier \(c=2\) or the finite-horizon local law above.

Liu, Nguyen, Ene, and Nguyen analyze vanilla AdaGradNorm using the current gradient in the accumulator and derive explicit deterministic and stochastic convergence rates. Their full text includes quadratic experiments but no matching monotonicity or local-repeller result.

Targeted searches for AdaNorm/AdaGrad-Norm objective monotonicity, scalar-quadratic transient ascent, local stability, and initial-accumulator thresholds did not identify a prior statement implying the result. Nearby exact stability records concern different algorithms such as scaled Polyak steps, Barzilai--Borwein steps, reflected gradient, and other adaptive feedback rules.

## Limitations
The exact frontier and transient theorem are proved only for a one-dimensional quadratic with exact gradients and no momentum. They establish a sharp transient-stability boundary, not divergence of AdaNorm. The result does not quantify how many ascent steps occur for a fixed nonzero starting point, nor does it assert analogous behavior under stochastic noise or general nonlinear objectives.

The originality assessment is based on the inspected primary texts and targeted searches; an equivalent elementary calculation could exist in older or differently named AdaGrad-Norm literature.

## References
1. S. Gratton and Ph. L. Toint, *A unified convergence theory for adaptive first-order methods in the nonconvex case, including AdaNorm, full and diagonal AdaGrad and Muon*, arXiv:2604.17423v3. First public version: 2026-04-19.
2. R. Ward, X. Wu, and L. Bottou, *AdaGrad Stepsizes: Sharp Convergence Over Nonconvex Landscapes*, Proceedings of Machine Learning Research 97, 2019; arXiv:1806.01811.
3. Z. Liu, T. D. Nguyen, A. Ene, and H. L. Nguyen, *On the Convergence of AdaGrad(Norm) on \(\mathbb{R}^d\): Beyond Convexity, Non-Asymptotic Rate and Acceleration*, arXiv:2209.14827v4, ICLR 2023.
