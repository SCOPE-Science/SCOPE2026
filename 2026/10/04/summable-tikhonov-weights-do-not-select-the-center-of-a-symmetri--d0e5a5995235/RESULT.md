# Summable Tikhonov weights do not select the center of a symmetric Pareto interval

## Finding
Consider the deterministic unconstrained specialization of the adaptive projected-gradient method of Li--Wang--Chen with two objectives
\[
F_1(x)=\frac12(x-c)^2,\qquad F_2(x)=\frac12(x+c)^2,\qquad c>0.
\]
The Pareto set is the whole interval \([-c,c]\). Let the method start from
\[
0<|x_0|<c,\qquad \sigma_0\ge 1,
\]
and let \(\rho_k>0\) be any sequence satisfying \(\sum_{k=0}^\infty\rho_k<\infty\), exactly as allowed by Algorithm 1 of the source paper.

Set
\[
\beta_k:=\frac{\rho_k}{2c^2+\rho_k}\in(0,1).
\]
Then the algorithm has the exact scalar recursion
\[
x_{k+1}=x_k\left(1-\frac{\beta_k}{\sigma_k}\right),
\qquad
\sigma_{k+1}=\sigma_k+\frac{\beta_k^2x_k^2}{\sigma_k}.
\]
Hence \(x_k\) never changes sign, \(|x_k|\) decreases, and
\[
x_\infty
=x_0\prod_{k=0}^\infty\left(1-\frac{\beta_k}{\sigma_k}\right)
\]
exists and is nonzero. In particular, the limit is an interior Pareto-stationary point rather than the symmetry center unless \(x_0=0\).

The total displacement obeys the explicit bound
\[
|x_0-x_\infty|
\le \frac{|x_0|}{2c^2\sigma_0}\sum_{k=0}^\infty\rho_k.
\]
Thus, for any fixed nonzero interior start, choosing a legal positive-summable Tikhonov schedule with sufficiently small total mass leaves the limiting Pareto point arbitrarily close to that start.

The unique regularized simplex multiplier also has an exact formula. Writing
\[
\lambda_k=\left(\frac{1+t_k}2,\frac{1-t_k}2\right),
\]
one has
\[
t_k=\frac{2cx_k}{2c^2+\rho_k},
\]
so that
\[
\lambda_k\longrightarrow
\left(\frac{1+x_\infty/c}2,\frac{1-x_\infty/c}2\right).
\]
This limit is nonuniform whenever \(x_\infty\ne0\). The per-iteration Tikhonov term therefore gives a unique, regularized multiplier without creating a cumulative preference for the central Pareto point.

## Assumptions and scope
The result concerns the exact deterministic SAA problem with \(\mathcal X=\mathbb R\) and the two smooth convex quadratics above. The initialization restriction \(0<|x_0|<c\) places the start strictly inside the Pareto interval, and \(\sigma_0\ge1\) ensures every multiplicative state factor is positive. The Tikhonov sequence is arbitrary subject only to the source algorithm's conditions \(\rho_k>0\) and \(\sum_k\rho_k<\infty\).

No claim is made about selection outside this symmetric family, about nonsummable Tikhonov schedules, or about noisy gradients. The result is a selection statement, not a faster stationarity-rate theorem.

## Proof
For \(m=2\), write a simplex vector as
\[
\lambda=\left(\frac{1+t}2,\frac{1-t}2\right),\qquad -1\le t\le1.
\]
At a point \(x\), the gradient matrix has columns \(x-c\) and \(x+c\), hence
\[
G(x)\lambda=x-ct,
\qquad
\|\lambda\|_2^2=\frac{1+t^2}2.
\]
For the unconstrained case, the source gives the closed-form step
\[
p_{\rho,\sigma}(x;G)=-\frac1\sigma G(x)\lambda_\rho(G),
\]
where \(\lambda_\rho(G)\) minimizes
\[
\frac12|G(x)\lambda|^2+\frac\rho2\|\lambda\|_2^2
\]
over the simplex. Up to an additive constant, this one-dimensional problem is
\[
\frac12(x-ct)^2+\frac\rho4 t^2.
\]
Its unconstrained stationary point is
\[
t_\rho(x)=\frac{2cx}{2c^2+\rho}.
\]
If \(|x|<c\), then \(|t_\rho(x)|<1\), so the stationary point is the simplex minimizer. Substitution yields
\[
G(x)\lambda_\rho(G)
=x-c t_\rho(x)
=\frac\rho{2c^2+\rho}x
=\beta x.
\]
Therefore the exact step is \(p=-\beta x/\sigma\). Algorithm 1 updates \(x^+=x+p\) and \(\sigma^+=\sigma+\sigma p^2\), giving
\[
x^+=x\left(1-\frac\beta\sigma\right),
\qquad
\sigma^+=\sigma+\frac{\beta^2x^2}\sigma.
\]

Because \(0<\beta_k<1\) and \(\sigma_k\ge\sigma_0\ge1\),
\[
0<1-\frac{\beta_k}{\sigma_k}<1.
\]
Thus the sign of \(x_k\) is invariant and \(|x_k|\) is nonincreasing. In particular \(|x_k|<c\) for every \(k\), so the interior multiplier formula remains valid globally along the trajectory.

Moreover,
\[
\sum_{k=0}^\infty\frac{\beta_k}{\sigma_k}
\le \frac1{\sigma_0}\sum_{k=0}^\infty\beta_k
\le \frac1{2c^2\sigma_0}\sum_{k=0}^\infty\rho_k
<\infty.
\]
Every factor in the product for \(x_k/x_0\) lies strictly between zero and one, and the sum of the factor deficits is finite. The standard infinite-product criterion therefore gives
\[
\prod_{k=0}^\infty\left(1-\frac{\beta_k}{\sigma_k}\right)>0.
\]
Consequently \(x_k\to x_\infty\ne0\) with the same sign as \(x_0\).

Since the motion is one-sided toward zero,
\[
|x_0-x_\infty|
=\sum_{k=0}^\infty |x_{k+1}-x_k|
=\sum_{k=0}^\infty\frac{\beta_k|x_k|}{\sigma_k}
\le \frac{|x_0|}{2c^2\sigma_0}\sum_{k=0}^\infty\rho_k.
\]
Also
\[
0\le\sigma_\infty-\sigma_0
=\sum_{k=0}^\infty\frac{\beta_k^2x_k^2}{\sigma_k}
\le\frac{x_0^2}{\sigma_0}\sum_{k=0}^\infty\beta_k^2
\le\frac{x_0^2}{2c^2\sigma_0}\sum_{k=0}^\infty\rho_k,
\]
so \(\sigma_k\) has a finite limit as well.

Finally, summability implies \(\rho_k\to0\). Since \(x_k\to x_\infty\),
\[
t_k=\frac{2cx_k}{2c^2+\rho_k}\to\frac{x_\infty}c,
\]
which gives the stated nonuniform multiplier limit. Because \(|x_\infty|<c\), that limiting multiplier is precisely the convex combination of the two gradients that equals zero at \(x_\infty\), confirming Pareto stationarity directly.

## Verification
The derivation uses the source paper's exact unconstrained multiplier subproblem and exact update rule, not a continuous-time approximation. A standalone replay script checks the closed-form multiplier against direct one-dimensional minimization, verifies the two update identities, the monotone sign-preserving trajectory, the displacement bound, and convergence to a nonzero interior point for a geometric legal Tikhonov schedule.

The proof does not infer an infinite-time statement from finite numerics: positivity of the limiting product follows analytically from \(\sum_k\rho_k<\infty\).

## Relationship to prior work
Li--Wang--Chen introduce the regularized multi-gradient subproblem, state that the Tikhonov term gives a unique and stable simplex multiplier, allow an arbitrary positive-summable \(\rho_k\), and prove stationarity/complexity guarantees for SAA-RMGDA. Their paper does not state a Pareto-point selection theorem, and its convex-rate discussion explicitly leaves improved convergence-rate analysis for future work. The present result instead isolates what the summable multiplier regularization selects on a symmetric non-singleton Pareto set.

The source also explains that its step-length update is motivated by objective-function-free adaptive regularization. That single-objective lineage does not contain a simplex multiplier or a non-singleton Pareto set, so it does not imply the selection law here. A recent objective-function-free multi-objective AdaGrad-like method uses a different adaptive mechanism and likewise does not provide this Tikhonov multiplier selection statement.

Targeted searches for aliases such as vanishing Tikhonov multiplier selection, symmetric quadratic Pareto selection, and summable regularization bias found no statement equivalent to the exact product formula or the total-Tikhonov-mass displacement bound. This is evidence of noncoverage, not a proof of priority.

## Limitations
The family is deliberately one-dimensional and symmetric so that multiplier selection can be solved exactly. The theorem does not say that every SAA-RMGDA trajectory converges to a noncentral Pareto point, nor that nonsummable regularization would select the center. The condition \(\sigma_0\ge1\) is sufficient for sign preservation in this normalization and is not asserted to be necessary.

The literature comparison is strongest for the source paper and the closely related objective-function-free papers inspected; a missed equivalent result elsewhere remains possible.

## References
1. Y. Li, L. Wang, and X. Chen, *An Adaptive Projected-Gradient Algorithm for Sample-Average Approximations of Stochastic Multi-Objective Optimization*, arXiv:2609.02722v1, 2026. https://arxiv.org/abs/2609.02722
2. M. De Santis, G. Eichfelder, and M. Porcelli, *Objective-Function Free Multi-Objective Optimization: Rate of Convergence and Performance of an Adagrad-like algorithm*, arXiv:2602.05893, 2026. https://arxiv.org/abs/2602.05893
3. S. Gratton, S. Jerad, and P. L. Toint, *A Stochastic Objective-Function-Free Adaptive Regularization Method with Optimal Complexity*, Open Journal of Mathematical Optimization 6 (2025), Article 5. https://doi.org/10.5802/ojmo.41
