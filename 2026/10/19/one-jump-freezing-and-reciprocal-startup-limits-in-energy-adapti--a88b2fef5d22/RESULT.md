# One-jump freezing and reciprocal-startup limits in energy-adaptive descent

## Finding

**Large-base-step freezing theorem.** Let \(d\ge 1\), let \(L:\mathbb R^d\to\mathbb R\) be twice continuously differentiable and bounded below, choose \(c> -\inf L\), and let \(T(x)\) be a continuously differentiable positive-definite matrix field. Set
\[
\ell(x)=\sqrt{L(x)+c},\qquad F(x)=T(x)\nabla\ell(x).
\]
Start the unconstrained energy-adaptive preconditioned-gradient iteration at any \(x_0\) satisfying \(v_0:=F(x_0)\ne0\), with \(r_0=\ell(x_0)>0\). For a base step \(\eta>0\) define, for all integers \(k\ge0\),
\[
v_k=F(x_k),\quad r_{k+1}=\frac{r_k}{1+2\eta\|v_k\|_2^2},\quad
x_{k+1}=x_k-2\eta r_{k+1}v_k.
\]
Introduce the large-step landing point
\[
x_\star=x_0-\frac{r_0}{\|v_0\|_2^2}v_0.
\]
**If \(v_\star:=F(x_\star)\ne0\),** then for every sufficiently large finite \(\eta\), the *entire infinite trajectory* converges to a point \(x_\infty(\eta)\) with \(F(x_\infty(\eta))\ne0\), whereas \(r_k\to0\) geometrically. As \(\eta\to\infty\),
\[
x_\infty(\eta)=x_\star+\frac{r_0}{2\eta\|v_0\|_2^2}
\left(\frac{v_0}{\|v_0\|_2^2}-\frac{v_\star}{\|v_\star\|_2^2}\right)+O(\eta^{-2}).
\]
In particular the infinite sum of the displacements *after the first update* is \(O(\eta^{-1})\): increasing the base step indefinitely cannot repair a nonstationary first landing point. Since \(T\) is positive definite, \(F(x_\infty)\ne0\) means \(\nabla L(x_\infty)\ne0\).

**Strongly convex scalar specialization.** For \(L(x)=x^2/2\), any \(c>0\), the constant preconditioner \(T=1\), and any \(x_0\ne0\), the landing point is exactly
\[
x_\star=-\frac{2c}{x_0}\ne0.
\]
Thus every nonzero starting point has a nonstationary limit for all sufficiently large base steps, with \(x_\infty(\eta)\to-2c/x_0\). The inversion of the initial coordinate is the sharp large-step limit, not a finite-iteration observation.

For the concrete normalization \(c=x_0=1\), the fully explicit sufficient range \(\eta\ge16\) guarantees
\[
-2+\frac{9}{\eta+3}\le x_\infty(\eta)
\le -2+\frac{18}{\eta+3}<-1,\qquad \lim_{k\to\infty}r_k=0.
\]
The sharp first correction is
\[
x_\infty(\eta)=-2+\frac{9+9\sqrt2/2}{\eta}+O(\eta^{-2}).
\]
The objective is globally strongly convex with the unique minimizer \(x=0\), yet the iterates freeze away from it while their auxiliary energy vanishes.

## Assumptions and scope

All vectors and matrices are real and finite dimensional; norms are Euclidean. The objective is \(C^2\), bounded below, and \(\ell\) is strictly positive. The matrix field \(T\) is \(C^1\) and positive definite at every point, so the autonomous direction field \(F\) is locally Lipschitz and \(F(x)=0\) iff \(\nabla L(x)=0\). A fixed autonomous preconditioner is essential to the stated expansion; no claim is made for arbitrary history-dependent \(T_k\), projections or noisy gradients. The assumption \(F(x_\star)\ne0\) is explicit: the theorem does not assert freezing when the large-step landing point is stationary. The base step stays fixed as iterations tend to infinity; only afterward is the limit \(\eta\to\infty\) considered. The starting energy is initialized exactly as in the cited method.

## Proof

**1. Exact bookkeeping.** From the recursion, whenever \(v_k\ne0\),
\[
r_k-r_{k+1}=2\eta r_{k+1}\|v_k\|_2^2,
\qquad x_{k+1}-x_k=-\frac{r_k-r_{k+1}}{\|v_k\|_2^2}v_k.
\]
Therefore \(\|x_{k+1}-x_k\|_2=(r_k-r_{k+1})/\|v_k\|_2\). In particular, if \(\|v_j\|_2\ge m>0\) on indices \(j=p,\ldots,q\), then the *whole path length* on these indices obeys
\[
\sum_{j=p}^{q}\|x_{j+1}-x_j\|_2\le(r_p-r_{q+1})/m\le r_p/m.
\]
This telescoping length bound, not just a square-summability estimate, controls the infinite tail.

**2. Uniform trapping for large steps.** Put \(a=2\|v_0\|_2^2>0\). The exact first update is
\[
r_1=\frac{r_0}{1+a\eta},\qquad
x_1=x_\star+\frac{r_0}{\|v_0\|_2^2(1+a\eta)}v_0.
\]
Since \(v_\star\ne0\) and \(F\) is continuous, select a closed ball \(B(x_\star,\delta)\) and \(m>0\) with \(\|F(x)\|_2\ge m\) throughout the ball. For all sufficiently large \(\eta\),
\[
\|x_1-x_\star\|_2+r_1/m<\delta.
\]
A first-exit argument using the path-length estimate shows that every \(x_k\), \(k\ge1\), remains in this ball: before any purported exit, the distance from \(x_1\) is at most \(r_1/m\), contradicting the displayed strict inequality. Consequently
\[
0<r_{k+1}\le\frac{r_k}{1+2\eta m^2}\quad(k\ge1).
\]
It follows that \(r_k\to0\) geometrically and \(\sum_{k\ge1}\|x_{k+1}-x_k\|_2\le r_1/m<\infty\). Thus \(x_k\) converges to a point within \(O(\eta^{-1})\) of \(x_\star\). Choosing the ball small enough to exclude zeros of \(F\) proves \(F(x_\infty)\ne0\). This also proves the claim for an open set of starting states, since \(F(x_0)\ne0\) and \(F(x_\star)\ne0\) are open conditions on the starting state.

**3. First-order limit coefficient.** Using \(F\in C^1\), expand
\[
x_1=x_\star+\frac{r_0v_0}{2\eta\|v_0\|_2^4}+O(\eta^{-2}),\qquad
r_1=\frac{r_0}{2\eta\|v_0\|_2^2}+O(\eta^{-2}).
\]
Because \(v_1=v_\star+O(\eta^{-1})\), the next step satisfies
\[
x_2-x_1=-\frac{r_1-r_2}{\|v_1\|_2^2}v_1
=-\frac{r_0}{2\eta\|v_0\|_2^2}\frac{v_\star}{\|v_\star\|_2^2}+O(\eta^{-2}).
\]
Here \(r_2=O(\eta^{-2})\). The total remaining movement from \(x_2\) is bounded by \(r_2/m=O(\eta^{-2})\). Adding these expansions yields the asserted first-order coefficient, including a controlled remainder over infinitely many later iterations.

**4. Scalar inversion and uniform explicit trap.** For \(L(x)=x^2/2\), \(\ell(x)=\sqrt{c+x^2/2}\) and \(F(x)=x/(2\ell(x))\). For any \(x_0\ne0\),
\[
x_\star=x_0-\frac{\ell(x_0)}{F(x_0)}
=x_0-\frac{x_0^2+2c}{x_0}=-\frac{2c}{x_0}\ne0.
\]
All hypotheses above therefore hold. For \(c=x_0=1\), direct substitution yields
\[
x_1=\frac{3-2\eta}{3+\eta}=-2+\frac9{\eta+3},\qquad
r_1=\frac{3\sqrt{3/2}}{\eta+3}.
\]
For \(-2\le x\le-1\), \(F(x)<0\) and \(|F(x)|\ge1/\sqrt6\). If \(\eta\ge16\), then \(x_1\in(-2,-1)\), and the maximum total future displacement while in this interval is
\[
r_1\sqrt6=\frac9{\eta+3}.
\]
All future updates increase \(x_k\); a first-exit argument bounds them above by \(x_1+9/(\eta+3)=-2+18/(\eta+3)<-1\), establishing the stated interval for the infinite limit. The general first-order formula with \(r_0=\sqrt{3/2}\), \(F(1)=1/\sqrt6\), \(F(-2)=-1/\sqrt3\) yields the coefficient \(9+9\sqrt2/2\).

## Verification

The accompanying standard-library-only `verify.py` checks the exact first-step formulas and discrete energy identity, all-time interval bounds on a deterministic grid of large base steps, first-order asymptotics in one and two dimensions, and rational telescoping identities for a constant direction field. Its saved output reports 2,372 passing checks. These computations are diagnostic only: they are not a substitute for the uniform first-exit and infinite-tail proof above. Run `python verify.py` from the extracted package directory.

## Relationship to prior work

Liu, Nurbekyan, Tian and Yang (arXiv:2310.06733, first posted 2023-10-10) introduce AEPG, including the recurrence used above. Their Theorem 2.1 proves unconditional **auxiliary-energy** stability, while Lemma 2.2 and Theorem 2.5 impose suitable small-base-step conditions for convergence to stationarity; Appendix A proves a positive effective-step lower bound in that regime. Their discussion notes the possibility of energy depletion. These statements do not imply the present opposite-regime theorem, which controls the infinite post-first-step path length, identifies the limiting *nonstationary* coordinate, and gives its sharp first correction.

Liu and Tian's earlier AEGD work (arXiv:2010.05109, first posted 2020-10-10) already includes the unpreconditioned energy update and emphasizes that energy stability alone does not establish convergence of primal iterates. That qualitative caution and the energy identity are prior art, not claimed new here. The present claim is the large-step dynamical limit and rigorous all-iteration trapping, extended to autonomous positive-definite preconditioning, with an explicit convex witness. Similar generic phenomena may have been formulated in the broader invariant-energy-quadratization or adaptive-gradient literature; the research comparison does not establish absolute novelty.

## Limitations

The result applies to deterministic exact arithmetic, a fixed base step, and an autonomous smooth positive-definite preconditioner. The general theorem requires a noncritical large-step landing point; it does not give a sharp finite critical base step for arbitrary objectives, or imply that all large-step trajectories are nonstationary. The scalar explicit threshold \(\eta\ge16\) is sufficient, not asserted optimal. An asymptotic formula is not an identity at finite step. No claim is made about stochastic AEPG, variable preconditioners, constrained projections, stabilized variants, or machine-learning benchmarks. This finding has not undergone independent scientific validation.

## References

1. H. Liu, L. Nurbekyan, X. Tian and Y. Yang, *Adaptive Preconditioned Gradient Descent with Energy*, arXiv:2310.06733 (first publicly posted 2023-10-10), Sections 1–2 and 7, Appendix A. https://arxiv.org/abs/2310.06733
2. H. Liu and X. Tian, *AEGD: Adaptive Gradient Descent with Energy*, arXiv:2010.05109 (first publicly posted 2020-10-10), energy-stability theorem, Remark 2 and convergence-rate discussion. https://arxiv.org/abs/2010.05109
