# Exact boundary criterion for the one-parameter UPHCT likelihood
## Finding
Consider the unit-scale lifetime model
\[
f_\gamma(x)=\frac{\gamma(\gamma+1)}{(\gamma+x)^2},
\qquad
0<x<1,
\qquad
\gamma>0,
\]
with survival function
\[
S_\gamma(x)=\frac{\gamma(1-x)}{\gamma+x}.
\]
For the unified progressive hybrid censoring likelihood used in the source, write the observed failure times as
\[
0<x_1<\cdots<x_\nu<1,
\]
let \(R_i\ge0\) be the removals at \(x_i\), let \(s^*\in(0,1)\) be the terminal time, and let \(R^*\ge0\) be the terminal removals. The source's likelihood, after suppressing factors independent of \(\gamma\), is
\[
L(\gamma)
\propto
(\gamma+1)^\nu
\gamma^{\nu+\sum_iR_i+R^*}
(\gamma+s^*)^{-R^*}
\prod_{i=1}^\nu(\gamma+x_i)^{-(2+R_i)}.
\]

Define the observed weighted-time statistic
\[
\boxed{
T
=
R^*s^*
+
\sum_{i=1}^{\nu}(2+R_i)x_i.
}
\]
Then the existence of a finite MLE has the exact classification
\[
\boxed{
\widehat\gamma<\infty
\quad\Longleftrightarrow\quad
T<\nu.
}
\]

If
\[
T\ge\nu,
\]
the likelihood has no finite maximizer: it increases toward its supremum as
\[
\gamma\to\infty.
\]
The limiting model is the uniform distribution on \((0,1)\), since
\[
f_\gamma(x)\longrightarrow1.
\]

For complete iid data, \(R_i=R^*=0\) and \(\nu=n\), so the condition becomes particularly simple:
\[
\boxed{
\widehat\gamma<\infty
\quad\Longleftrightarrow\quad
\bar X<\frac12.
}
\]
Thus any complete sample with
\[
\bar X\ge\frac12
\]
has no finite MLE. This is not a probability-zero pathology. A sufficient boundary event is
\[
X_i\ge\frac12
\quad\text{for every }i,
\]
whose probability under the model is
\[
\boxed{
\left(\frac{\gamma}{2\gamma+1}\right)^n>0.
}
\]

The criterion supplies a deterministic pre-optimization diagnostic for the likelihood procedure. When it fails, Newton-Raphson should not be interpreted as producing an ordinary finite MLE, and finite observed-information or Wald inference for \(\gamma\) is not available without explicitly treating the uniform boundary.

## Assumptions and scope
The parameter space in the source is
\[
\gamma>0.
\]
The observed failure and censoring times are taken in the interior \((0,1)\), which holds almost surely under the continuous model for nondegenerate life-test observations. Removals are nonnegative integers.

The theorem addresses existence of a finite global likelihood maximizer. When \(T<\nu\), it proves that at least one finite global maximizer exists; it does not claim that every such sample has a unique stationary point.

When \(T\ge\nu\), the natural extended-parameter maximizer is the boundary point \(\gamma=\infty\), corresponding to the uniform limit. This is not a finite value in the source's parameter space.

The result is about maximum likelihood. Proper Bayesian inference with a proper gamma prior can remain well-defined even when the likelihood itself is maximized at the boundary.

## Proof
Set
\[
\delta=\frac1\gamma,
\qquad
\delta>0.
\]
Substitution into the source likelihood cancels all powers of \(\delta\). Up to a positive factor depending only on the observed data,
\[
L(\delta)
=
(1+\delta)^\nu
(1+\delta s^*)^{-R^*}
\prod_{i=1}^{\nu}
(1+\delta x_i)^{-(2+R_i)}.
\]
Hence
\[
D(\delta)
:=
\frac{d}{d\delta}\log L(\delta)
=
\frac{\nu}{1+\delta}
-
\frac{R^*s^*}{1+\delta s^*}
-
\sum_{i=1}^{\nu}
\frac{(2+R_i)x_i}{1+\delta x_i}.
\]

For every \(y\in(0,1]\) and \(\delta\ge0\),
\[
\frac{y}{1+\delta y}
\ge
\frac{y}{1+\delta}.
\]
Applying this to every observed time gives
\[
D(\delta)
\le
\frac{\nu-T}{1+\delta}.
\]
Therefore if \(T\ge\nu\), then \(D(\delta)\le0\) for all \(\delta\ge0\). For interior observations the inequality is strict for every \(\delta>0\) in the equality case as well. Thus \(L\) decreases with \(\delta\), or equivalently increases with \(\gamma\), and no finite \(\gamma\) attains the supremum.

Conversely, if
\[
T<\nu,
\]
then
\[
D(0)=\nu-T>0.
\]
As \(\delta\to\infty\),
\[
D(\delta)
=
-\frac{\nu+\sum_iR_i+R^*}{\delta}
+o(\delta^{-1}),
\]
so \(D(\delta)<0\) for all sufficiently large \(\delta\). Moreover,
\[
L(\delta)
=O\!\left(
\delta^{-\nu-\sum_iR_i-R^*}
\right)
\longrightarrow0.
\]
Since \(L\) is continuous, is initially increasing away from the boundary \(\delta=0\), and tends to zero at infinity, it attains a global maximum at some finite \(\delta>0\), equivalently at finite \(\gamma>0\).

For complete data, the statistic is
\[
T=2\sum_{i=1}^nX_i,
\]
which yields the stated sample-mean criterion.

Finally,
\[
\Pr_\gamma(X\ge1/2)
=S_\gamma(1/2)
=\frac{\gamma}{2\gamma+1}.
\]
Independence gives the positive-probability boundary event for a complete sample.

## Verification
The included checker evaluates the likelihood in both \(\gamma\) and \(\delta=1/\gamma\) parameterizations and verifies their equality up to the data-only factor.

For the complete sample
\[
(0.6,0.7,0.8),
\]
one has \(\bar X=0.7\), so the theorem predicts no finite MLE. The checker confirms that the score in \(\delta\) is negative over a wide range and that the likelihood approaches its uniform-boundary value monotonically.

For the complete sample
\[
(0.1,0.2,0.3),
\]
one has \(\bar X=0.2\), so a finite MLE must exist. The checker numerically locates an interior maximizer and verifies that its likelihood exceeds the boundary value.

A censored example with
\[
\nu=2,
\quad
(x_1,x_2)=(0.3,0.4),
\quad
(R_1,R_2)=(1,2),
\quad
s^*=0.6,
\quad
R^*=3
\]
has
\[
T=4.3>2,
\]
and the checker confirms boundary monotonicity. These computations are reproducibility checks; the existence classification is proved analytically above.

## Relationship to prior work
The 2026 source writes the UPHCT likelihood and score explicitly and states that maximum-likelihood estimates are obtained by Newton-Raphson. It reports single-peaked profile likelihoods for its three real datasets and describes those examples as confirming well-defined parameter estimates. It does not state an existence criterion covering arbitrary admissible censored samples.

The underlying bounded-support distribution was introduced by Muhammad in 2016, where numerical maximum-likelihood estimation was also studied. The inspected text gives a numerical likelihood equation and simulation results but does not provide the weighted-time boundary classification above.

Boundary failures of maximum likelihood are known for some other bounded-support lifetime models, so boundary behavior is not a new phenomenon in general. For example, Jiang discusses a different finite-support model whose location MLE may approach the sample maximum. That result concerns a different parameter and likelihood and does not imply the exact criterion
\[
T<\nu
\]
for the present unit model.

Focused searches by DOI, model formula, Newton-Raphson terminology, boundary-MLE language, and the earlier bounded-support model did not locate a published correction or an equivalent existence theorem for this likelihood.

## Limitations
The theorem classifies finite-MLE existence but does not prove uniqueness of the finite maximizer when \(T<\nu\).

The positive-probability calculation uses complete iid sampling as a transparent special case. The probability of the boundary region under a particular progressive hybrid censoring design depends on that design and is not quantified here.

The result does not invalidate the source's three reported datasets, whose displayed profile likelihoods have finite interior maxima. It shows that those examples do not establish universal existence of a finite MLE under the model.

## References
1. E. M. Almetwally, “Statistical inference for a one-parameter lifetime model under unified progressive hybrid censoring with binomial random removals,” AIMS Mathematics 11 (2026), 211–242. DOI: 10.3934/math.2026009.
2. M. Muhammad, “A new two parameter distribution with a finite support,” Applied Mathematical Sciences 10 (2016), 1–12.
3. R. Jiang, “A new bathtub curve model with a finite support,” Reliability Engineering & System Safety 119 (2013), 44–51. DOI: 10.1016/j.ress.2013.05.019.
