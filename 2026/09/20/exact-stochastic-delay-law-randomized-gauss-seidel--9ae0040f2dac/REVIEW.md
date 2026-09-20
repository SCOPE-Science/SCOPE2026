# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** For the scaled error coordinates, an update of coordinate 1 replaces
its squared contribution by \(r^2(y_2^{k-D})^2\) while leaving the second
coordinate unchanged; the coordinate-2 case is symmetric. Uniform coordinate
sampling therefore makes the two terms combine exactly into the scalar
second-moment recurrence
\[
S_{k+1}=\frac12S_k+\frac{r^2}{2}\mathbb E[S_{k-D}].
\]
No independence between the two coordinates is used. Independence of the
current delay from the past is the essential probabilistic hypothesis.

For finite delay support, the recurrence has a nonnegative companion matrix.
After trimming unused trailing delays, its positive current-state coefficient
and positive maximal-delay coefficient make it primitive. The Perron factor is
the unique positive root of
\[
2q-1=r^2\mathbb E[q^{-D}],
\]
because the difference between the two sides is strictly increasing in \(q\)
and changes sign between \(1/2\) and \(1\).

The delay-ordering result was checked directly from the fact that
\(d\mapsto q^{-d}\) is increasing and convex for \(q<1\). The extremal
fixed-mean distributions are the standard convex-order extremizers on bounded
integer support. The deterministic-delay large-\(\tau\) limit follows by
taking logarithms of \(q^\tau(2q-1)=r^2\). The near-singular expansion follows
by a second-order Taylor expansion; coefficient matching gives exactly the
formula in `RESULT.md`.

The verification artifact solves the root equation by bisection and compares
it with direct iteration of the scalar recurrence for several delay laws,
including two distributions of equal mean but different variability.

## Originality

**PASS, to the best of our knowledge, with explicit residual risk.** The
closest older literature found has substantial but distinguishable coverage:

- Chazan--Miranker (1969) gives foundational chaotic-relaxation convergence
  conditions.
- Beidas--Papavassilopoulos (1993) treats a general linear asynchronous model
  with stochastic Markov delays and reports second-moment and mean convergence
  conditions. Its full text was not inspected here, so a specialized hidden
  corollary is the principal older-literature risk.
- Moga--Dubois (1995), whose analytical section was inspected, uses state
  augmentation to obtain convergence rates for two-variable asynchronous
  linear iterations with stochastic delays. Its displayed two-variable model
  evolves the expected trajectory and specializes to zero/one delays; it does
  not state the coordinate-randomized exact second-moment closure, arbitrary
  bounded-delay root law, convex-order extremizers, or near-singular expansion
  reported here.
- Verkama (1996) studies random coordinate relaxation of fixed-point
  iterations.
- Avron--Druinsky--Gupta (2015) gives linear convergence guarantees for
  randomized asynchronous SPD solvers, but the accessible statement is a
  general bound rather than this exact two-coordinate delay-distribution law.
- Peng--Xu--Yan--Yin (2019) gives convergence and rate guarantees depending on
  delay statistics, including unbounded delays, but does not supply the exact
  scalar law here.
- Carson--Ma, arXiv:2609.15605 (2026), is directly relevant and establishes
  general asynchronous Jacobi/RGS convergence-rate bounds depending on
  communication structure and maximum delay. Only its abstract was inspected;
  the full text was not, so contemporaneous overlap beyond the abstract cannot
  be excluded.

Repository searches by method, stochastic-delay terminology, mean-square
terminology, and equivalent rate language did not identify a prior SCOPE
record covering this contribution.

## Value

**PASS.** Exact low-dimensional models are useful for testing how much general
asynchronous bounds lose. Here the rate depends on the probability generating
function of the delay evaluated at \(1/q\), yielding qualitative information
not visible from a maximum-delay parameter alone. In particular, the theorem
proves that burstier delays are worse at fixed mean, identifies the extremal
bounded laws, and shows that near ill-conditioning the mean delay enters at
first order while variance appears at second order.

## Limitations

The finding is a two-coordinate benchmark rather than a general-dimensional
theorem. It assumes uniform coordinate sampling, exact coordinate overwrites,
bounded i.i.d. delays independent of the history, and a consistent stale read
of the other coordinate. The exact observable is a diagonal-scaled mean-square
error, not the \(A\)-energy. Correlated delays, unequal sampling, relaxation,
unbounded-delay tails, inconsistent multi-coordinate reads, and higher
dimensions require separate analysis. The two full-text access gaps described
above remain material originality uncertainties.
