# The bounded p-exponential sample-maximum estimator is not the MLE
## Finding
Consider the bounded \(p\)-exponential density
\[
f_p(x)
=
\frac{p}{p+1}
\left(
1-\frac{x}{p+1}
\right)^{p-1},
\qquad
0<x<p+1,
\qquad
p>0.
\]
For a sample \(x_1,\ldots,x_n\), let
\[
m=\max_i x_i
\]
and
\[
p_*=\max\{0,m-1\}.
\]
The admissible parameter set is
\[
p>p_*.
\]

The source writes the correct constrained likelihood
\[
L(p)
=
\left(\frac{p}{p+1}\right)^n
\prod_{i=1}^n
\left(
1-\frac{x_i}{p+1}
\right)^{p-1},
\]
but then states that maximizing over the closure gives the closed-form boundary MLE
\[
\widehat p=p_*.
\]

That conclusion is not compatible with the likelihood. For every sample with
\[
m\notin\{1,2\},
\]
the exact lower-boundary behavior is
\[
\boxed{
\begin{array}{ll}
0<m<1:
&
L(p)\longrightarrow0
\quad(p\downarrow0),\\[4pt]
1<m<2:
&
L(p)\longrightarrow+\infty
\quad(p\downarrow m-1),\\[4pt]
m>2:
&
L(p)\longrightarrow0
\quad(p\downarrow m-1).
\end{array}
}
\]
At the opposite end,
\[
\boxed{
L(p)\longrightarrow
\exp\!\left(-\sum_{i=1}^n x_i\right)>0
\qquad(p\to\infty).
}
\]

Therefore:

\[
\boxed{
m<1\text{ or }m>2
\quad\Longrightarrow\quad
p_*\text{ cannot maximize the likelihood, even by a boundary-limit convention.}
}
\]

When
\[
1<m<2,
\]
the likelihood is unbounded as the excluded boundary is approached. In that regime there is no finite ordinary MLE attained at \(p_*\); the boundary is instead an infinite-likelihood singularity.

Thus
\[
\boxed{
\max\{0,m-1\}
}
\]
is a natural endpoint estimator, but it is not a universal maximum-likelihood estimator for this family.

The discrepancy affects the article's numerical inference. For its first real dataset,
\[
m=3.658,
\]
so the reported “MLE” is
\[
2.6580=m-1.
\]
The paper reports fitted log-likelihood
\[
-49.20.
\]
Using the same 41 published observations in the likelihood above gives
\[
\boxed{
\ell(20)=-44.4074950235\ldots>-49.20.
}
\]
Hence the reported parameter cannot be a likelihood maximizer.

For the second real dataset,
\[
m=7.89
\]
and the paper reports
\[
\widehat p=6.8900,
\qquad
\ell=-126.50.
\]
Using its 101 published observations gives
\[
\boxed{
\ell(20)=-104.3629229895\ldots>-126.50.
}
\]
Again the displayed estimate is not a maximum-likelihood fit.

The simulation study is affected on a large fraction of replicates in the larger-\(p\) regimes. For example, at the source's setting
\[
p=5.3245,
\qquad
n=20,
\]
the exact probability that the sample maximum exceeds two is
\[
\boxed{
\Pr(M_{20}>2)
=
1-
\left[
1-
\left(
\frac{p-1}{p+1}
\right)^p
\right]^{20}
=
0.9412282299\ldots.
}
\]
On this event the claimed boundary estimator satisfies \(M_{20}-1>1\), but the likelihood tends to zero at that boundary.

## Assumptions and scope
The sample values are positive and are evaluated under the model's own parameter-dependent support.

The exceptional equations
\[
m=1
\quad\text{or}\quad
m=2
\]
are excluded from the displayed trichotomy because the boundary powers change exactly there. Under a continuous sampling model these events have probability zero.

The result distinguishes two statements. The sample-maximum endpoint estimator can be consistent for the endpoint parameter, as the source proves. Consistency does not make an estimator an MLE. The correction concerns the claim that the same statistic maximizes the written likelihood.

The Bayesian procedure and other estimators are not reassessed here.

## Proof
The log-likelihood on the admissible set is
\[
\ell(p)
=
n\log p-n\log(p+1)
+
(p-1)
\sum_{i=1}^n
\log\!\left(
1-\frac{x_i}{p+1}
\right).
\]

First consider the large-\(p\) limit. For every fixed observation,
\[
\frac{p}{p+1}\longrightarrow1
\]
and
\[
(p-1)
\log\!\left(
1-\frac{x_i}{p+1}
\right)
\longrightarrow -x_i.
\]
Hence
\[
f_p(x_i)\longrightarrow e^{-x_i}
\]
and therefore
\[
L(p)\longrightarrow
\exp\!\left(-\sum_i x_i\right).
\]

Now suppose
\[
m>1.
\]
Write
\[
p=m-1+\varepsilon,
\qquad
\varepsilon>0.
\]
For every observation equal to the sample maximum,
\[
1-\frac{m}{p+1}
=
\frac{\varepsilon}{m+\varepsilon}
\]
and
\[
p-1=m-2+\varepsilon.
\]
If the maximum occurs \(k\ge1\) times, its combined contribution has the leading power
\[
\varepsilon^{k(m-2)}
\]
up to a positive finite factor, because
\[
\varepsilon^{k\varepsilon}\longrightarrow1.
\]
Every observation strictly below \(m\) contributes a positive finite factor at the boundary. Thus
\[
L(p)\to+\infty
\]
for \(1<m<2\), while
\[
L(p)\to0
\]
for \(m>2\).

Finally suppose
\[
0<m<1.
\]
Then the lower feasible boundary is \(p=0\). For each observation,
\[
\frac{p}{p+1}\sim p
\]
and
\[
\left(
1-\frac{x_i}{p+1}
\right)^{p-1}
\longrightarrow
\frac{1}{1-x_i}.
\]
Consequently
\[
L(p)
\sim
p^n
\prod_{i=1}^n
\frac{1}{1-x_i}
\longrightarrow0.
\]

These limits prove the trichotomy and the failure of the proposed boundary-MLE formula.

For the simulation probability, when the true parameter is \(p>1\),
\[
F_p(2)
=
1-
\left(
\frac{p-1}{p+1}
\right)^p.
\]
Independence gives
\[
\Pr(M_n>2)=1-F_p(2)^n,
\]
which yields the stated numerical value.

## Verification
The included checker implements the published density and log-likelihood without using any alternative parameterization.

It verifies all three lower-boundary regimes numerically while the proof above supplies the exact limits.

The checker also verifies the large-\(p\) likelihood limit and the exact simulation probability.

For reproducibility of the applied consequence, the two observation lists printed in the article are embedded directly in the checker. Their lengths, maxima, and sums are checked before evaluating the likelihood. The calculations reproduce
\[
m_1=3.658,
\qquad
\sum_i x_i=44.608,
\]
and
\[
m_2=7.89,
\qquad
\sum_i x_i=103.51.
\]
At \(p=20\), both resulting log-likelihoods strictly exceed the values reported for the paper's purported MLE fits.

As an additional stress test, the one-observation sample \(x=3\) has claimed boundary value \(p=2\), where the boundary likelihood tends to zero, while an interior value near \(p=5.9744\) has strictly positive likelihood.

## Relationship to prior work
Bakouch et al. correctly identify the sample-dependent admissible set and write the likelihood and log-likelihood. They then state that maximizing over its closure produces
\[
\widehat p=\max\{0,M_n-1\}
\]
and use this statistic as the “MLE” in their simulation study and real-data analyses.

Their consistency argument for that endpoint statistic is compatible with the correction here: an endpoint estimator can converge to the true endpoint parameter without maximizing the likelihood at finite samples.

General work on parameter-dependent support emphasizes that such models are nonregular and that ordinary likelihood theory need not apply. It does not imply that a sample maximum is automatically the likelihood maximizer; the shape of the density at the moving endpoint matters. In the present model, that endpoint density behavior changes at \(p=1\), which is precisely why the likelihood boundary has different regimes.

Focused searches using the exact DOI, bounded \(p\)-exponential name, boundary-MLE formula, sample-maximum estimator, support constraint, and likelihood-limit formulations did not locate a published correction of this inference claim.

## Limitations
The result does not supply a complete closed-form formula for the true MLE in every sample configuration.

For some samples the likelihood may have a finite interior maximizer; for others its supremum can occur only as \(p\to\infty\). Determining that full phase diagram is separate from the present correction.

The endpoint statistic may remain useful as a consistent estimator even though it is not generally an MLE.

A very recent unindexed correction could exist outside the sources examined.

## References
1. H. S. Bakouch, H. S. Salinas, F. A. Moala, T. Hussain, S. Aldossari, and A. Al-Buainain, “The One-Parameter Bounded p-Exponential Distribution: Properties, Inference, and Applications,” Mathematics 14 (2026), 1076. DOI: 10.3390/math14061076.
2. K. Hirano and J. R. Porter, “Asymptotic Efficiency in Parametric Structural Models with Parameter-Dependent Support,” Econometrica 71 (2003), 1307–1338. DOI: 10.1111/1468-0262.00451.
