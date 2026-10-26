# Sharp covariance envelopes for Brownian gases with random-size batch resetting

## Finding
Consider a gas of \(N\ge3\) independent Brownian particles in one dimension, with diffusion coefficient \(D>0\). At the events of an independent rate-\(r>0\) Poisson process, draw an integer batch size \(M\in\{1,\ldots,N\}\) with an independently repeated distribution, then reset a uniform random subset of \(M\) distinct particles to zero. All particles start at zero. Let \(\mu=\mathbb E M\), \(q_1=\mu/N\), and \(q_2=\mathbb E[M(M-1)]/[N(N-1)]\). For distinct \(i,j\), write \(C(t)=\operatorname{Cov}(X_i(t)^2,X_j(t)^2)\).

At every \(t\ge0\), the exact covariance is
\[
 C(t)=r q_2\int_0^t e^{-r(2q_1-q_2)(t-s)}\left[\frac{2D}{rq_1}(1-e^{-rq_1s})\right]^2\,ds.
\]
It follows that at every fixed \(t>0\), \(C(t)\) is strictly increasing in \(q_2\) at fixed \(q_1>0\); the same holds at stationarity, where
\[
 C(\infty)=\frac{4D^2}{r^2q_1^2}\frac{q_2}{2q_1-q_2},\qquad
 \frac{C(\infty)}{\operatorname{Var}(X_i(\infty)^2)}=\frac{q_2}{5(2q_1-q_2)}.
\]

Fix the mean reset budget \(\mu\in[1,N]\), and put \(k=\lfloor\mu\rfloor\), \(\theta=\mu-k\). Among **all** size distributions supported on \(\{1,\dots,N\}\) with mean \(\mu\), the complete sharp attainable range is obtained by substituting
\[
 q_{2,\min}=\frac{k(k-1+2\theta)}{N(N-1)},\qquad
 q_{2,\max}=\frac{\mu-1}{N-1}
\]
into either covariance formula. The minimum is uniquely attained by \(\Pr(M=k)=1-\theta\), \(\Pr(M=k+1)=\theta\) (with the obvious singleton case for \(\theta=0\)). The maximum is uniquely attained by \(\Pr(M=1)=(N-\mu)/(N-1)\), \(\Pr(M=N)=(\mu-1)/(N-1)\). Every intermediate covariance value is attained. When \(\mu=1\) or \(N\), the two extrema coincide. When \(1<\mu<N\), the stationary upper and lower bounds differ strictly.

For example, at \(N=6\), \(\mu=2\), the minimum uses deterministic batches of size two and has stationary normalized correlation \(1/45\). The maximum draws size six with probability \(1/5\) and size one otherwise and has stationary normalized correlation \(3/35\), despite identical expected resetting activity for every particle.

## Assumptions and scope
The process uses independent standard Brownian drivers with infinitesimal variance \(2D\,dt\), independent Poisson event times, independently sampled batch sizes, independent uniform choices of subsets conditional on the batch sizes, instantaneous resets to the origin, and initially zero positions. The comparison keeps \(N,D,r,\mu\), and observation time fixed while varying only the distribution of \(M\). The moment formulas extend to arbitrary deterministic initial positions after suitable initial terms, but the all-time bound is claimed here for the zero initialization. The stationary law exists and is unique.

## Proof
**Sampling probabilities.** Conditional on \(M=m\), a prescribed particle is included with probability \(m/N\), and a prescribed distinct pair is included with probability \(m(m-1)/(N(N-1))\). Thus the probability of resetting at least one of a fixed pair at an event is \(2q_1-q_2\). Since \(1\le M\le N\), \(0\le q_2\le q_1\).

**Moment closure.** With \(u(t)=\mathbb E[X_i(t)^2]\), the infinitesimal generator gives \(u'=2D-rq_1u\), \(u(0)=0\), and therefore \(u(t)=2D(1-e^{-rq_1t})/(rq_1)\). For \(i\ne j\), putting \(w(t)=\mathbb E[X_i(t)^2X_j(t)^2]\), independence of the driving Brownian motions and the reset-to-zero rule give \(w'=4Du-r(2q_1-q_2)w\), \(w(0)=0\). Subtracting \((u^2)'\) yields
\[
 C'=-r(2q_1-q_2)C+rq_2u^2,\quad C(0)=0.
\]
Variation of constants establishes the displayed time-dependent formula. Because \(u(s)>0\) for \(s>0\), increasing \(q_2\) strictly increases the positive forcing factor and decreases the exponential decay rate, proving strict comparison for every \(t>0\). The stationary expression follows by \(u\to2D/(rq_1)\) and constant-coefficient stability. One-coordinate resets occur at rate \(rq_1\), independently of that coordinate's driving Brownian motion; consequently its stationary marginal is Laplace, with fourth moment \(24D^2/(r^2q_1^2)\) and squared-position variance \(20D^2/(r^2q_1^2)\). This gives the normalized formula.

**Sharp distributional extrema.** For \(m\in\{1,\dots,N\}\), the second forward difference of \(m(m-1)\) is exactly two, so the lower convex envelope at prescribed mean \(\mu=k+\theta\) is the chord joining the two adjacent integers \(k\) and \(k+1\). Strict convexity yields the unique minimizing distribution. The secant line joining endpoint values at \(m=1\) and \(m=N\) is an upper bound for \(m(m-1)\) on this finite interval, with equality only at the endpoints; hence the unique maximizing distribution. Taking convex mixtures of these two distributions maintains the mean and varies \(q_2\) continuously across the full interval. Strict covariance monotonicity transfers these conclusions to every \(t>0\) and the stationary state.

**Existence and normalization.** Couple two realizations with the same Brownian drivers and the same batch-resetting events. A difference at coordinate \(i\) disappears at its first reset; the chance a coordinate has not reset by time \(t\) is \(e^{-rq_1t}\). A union bound gives \(N e^{-rq_1t}\) for a noncoalesced coordinate, yielding convergence to a unique joint stationary distribution. Standard finite stationary polynomial moments follow from the dissipative resets. This justifies limits in the moment equations.

## Verification
Run `python verify.py` with Python 3 (standard library). It checks inclusion probabilities by independent enumeration of uniform subsets, verifies the sharp endpoint size laws over many rational mean budgets, confirms covariance time-ordering by deterministic midpoint integration, checks the stationary formula against the fixed-size expression, and evaluates the illustrative \(N=6\) example using exact fractions. Numerical quadrature is corroboration, not proof of the strict inequality for all times.

## Relationship to prior work
De Mauro, Majumdar and Schehr (arXiv:2601.20077v1, January 27, 2026) derive exact fixed-size-batch marginal and pair-correlation formulas, including their Eq. (8); they explicitly identify **random numbers of reset particles** as a further problem in their conclusion. Setting \(M\equiv m\) here exactly reproduces their known correlation coefficient and is not claimed as a new result. The result here concerns the previously unclassified **complete fixed-mean random-batch correlation envelope** and its strict all-time ordering, not merely another fixed choice of \(m\). The underlying generator and elementary finite-support convexity are established techniques, not claimed as novel.

## Limitations
The formula concerns independent Brownian particles and zero-coordinate resetting, not interacting particles, location-dependent resetting, or adapted batch sizes. Correlation means covariance of squared positions, not ordinary position covariance (which is zero). No claim is made about optimizing search first-passage times, entropy production, or the complete joint probability density. Prior exact fixed-batch formulas encode part of the generator algebra, so additional priority assessment may identify broader abstract coverage.

## References
- G. de Mauro, S. N. Majumdar, and G. Schehr, *Tuning the strength of emergent correlations in a Brownian gas via batch resetting*, arXiv:2601.20077v1 (January 27, 2026), especially Eq. (8), Supplemental Material, and concluding discussion.
- M. R. Evans and S. N. Majumdar, *Diffusion with stochastic resetting*, Phys. Rev. Lett. 106, 160601 (2011), for classical Poisson resetting.
