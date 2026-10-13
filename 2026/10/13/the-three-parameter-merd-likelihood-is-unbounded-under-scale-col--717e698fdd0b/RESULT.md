# The three-parameter MERD likelihood is unbounded under scale collapse
## Finding
The 2026 modified exponential root distribution (MERD) paper introduces a location-scale extension
\[
X
=
\tau+\sigma\left\{(T+1)^2-1\right\},
\qquad
T\sim\operatorname{Exp}(\lambda),
\]
with
\[
\tau\in\mathbb R,
\qquad
\sigma>0,
\qquad
\lambda>0.
\]
Its density is
\[
f(x;\tau,\sigma,\lambda)
=
\frac{\lambda}
{2\sigma\sqrt{1+(x-\tau)/\sigma}}
\exp\!\left[
-\lambda\left(
\sqrt{1+\frac{x-\tau}{\sigma}}-1
\right)
\right],
\qquad
x\ge\tau.
\]

For a nondegenerate sample
\[
x_1,\ldots,x_n,
\]
let
\[
m=\min_i x_i,
\]
and let \(k\ge1\) be the multiplicity of \(m\). The source proves that, for fixed \(\sigma\) and \(\lambda\), the likelihood is increasing in \(\tau\), so its threshold profile is attained at
\[
\widehat\tau=m.
\]

Put
\[
y_i=x_i-m
\]
and
\[
S(\sigma)
=
\sum_{i=1}^n
\left(
\sqrt{1+\frac{y_i}{\sigma}}-1
\right).
\]
For fixed \(\tau=m\) and \(\sigma\), maximization over \(\lambda\) gives
\[
\widehat\lambda(\sigma)
=
\frac{n}{S(\sigma)}.
\]
The profile log-likelihood printed in the source is
\[
\ell_p(\sigma)
=
n\log\!\frac{n}{S(\sigma)}
-n
-n\log(2\sigma)
-\frac12
\sum_{i=1}^n
\log\!\left(
1+\frac{y_i}{\sigma}
\right).
\]

The profile has no finite global maximum. More precisely,
\[
\boxed{
\ell_p(\sigma)
=
-\frac{k}{2}\log\sigma+O(1),
\qquad
\sigma\downarrow0.
}
\]
Therefore
\[
\boxed{
\ell_p(\sigma)\longrightarrow+\infty
}
\]
for every nondegenerate sample.

Consequently, the three-parameter MERD likelihood is unbounded above and has no finite ordinary MLE. In the almost-sure case of a unique sample minimum,
\[
k=1,
\]
the profiled likelihood diverges proportionally to
\[
\sigma^{-1/2}
\]
up to a finite positive factor.

At the same time,
\[
\widehat\lambda(\sigma)
\asymp
\sqrt{\sigma}
\longrightarrow0.
\]
Thus the divergence occurs along the admissible path
\[
\tau=m,
\qquad
\sigma\downarrow0,
\qquad
\lambda=\widehat\lambda(\sigma)\downarrow0.
\]

The paper's proposed one-dimensional numerical maximization over \(\sigma>0\) therefore cannot have a finite global maximizer unless an additional constraint, penalty, or prior regularization is imposed.

## Assumptions and scope
The sample is assumed nondegenerate: at least one observation is strictly larger than the sample minimum. Under the continuous MERD model this occurs with probability one for samples of size at least two.

The result concerns the joint three-parameter likelihood of the location-scale extension. It does not contradict the source's one-parameter exact inference for the original MERD model.

It also does not contradict the source's proposition that, when \(\sigma\) and \(\lambda\) are held fixed, the likelihood is increasing in \(\tau\) and is maximized at the sample minimum.

Identifiability and MLE existence are distinct properties. The source's identifiability argument may remain correct even though the likelihood has an unbounded boundary ridge.

The completely degenerate sample in which all observations are equal is excluded. It has probability zero under the continuous model and makes the source's quantity \(S(\sigma)\) identically zero.

## Proof
Set
\[
m=\min_i x_i,
\qquad
y_i=x_i-m,
\]
and let exactly \(k\) of the \(y_i\) be zero. Write
\[
r=n-k.
\]
For the \(r\) positive values,
\[
\sqrt{1+\frac{y_i}{\sigma}}
=
\frac{\sqrt{y_i}}{\sqrt{\sigma}}
\left(1+O(\sigma)\right)
\]
as \(\sigma\downarrow0\). Hence
\[
S(\sigma)
=
\frac{C}{\sqrt{\sigma}}+O(1),
\qquad
C=
\sum_{y_i>0}\sqrt{y_i}>0.
\]
Therefore
\[
\log S(\sigma)
=
-\frac12\log\sigma+\log C+o(1)
\]
and
\[
\widehat\lambda(\sigma)
=
\frac{n}{S(\sigma)}
=
\frac{n}{C}\sqrt{\sigma}\{1+o(1)\}.
\]

Now expand each term of the source's profile log-likelihood. First,
\[
n\log\!\frac{n}{S(\sigma)}
=
\frac{n}{2}\log\sigma+O(1).
\]
Second,
\[
-n\log(2\sigma)
=
-n\log\sigma+O(1).
\]
Finally, the \(k\) zero observations contribute nothing to the logarithmic sum, while each positive \(y_i\) satisfies
\[
\log\!\left(1+\frac{y_i}{\sigma}\right)
=
\log y_i-\log\sigma+o(1).
\]
Thus
\[
-\frac12
\sum_{i=1}^n
\log\!\left(1+\frac{y_i}{\sigma}\right)
=
\frac{r}{2}\log\sigma+O(1).
\]

Combining the three logarithmic coefficients gives
\[
\frac n2-n+\frac r2
=
-\frac{k}{2}.
\]
Hence
\[
\ell_p(\sigma)
=
-\frac{k}{2}\log\sigma+O(1),
\]
which tends to \(+\infty\) because \(k\ge1\).

Since the source has already profiled \(\tau\) at \(m\) and \(\lambda\) at \(n/S(\sigma)\), this is a path inside the admissible parameter space along which the full likelihood is arbitrarily large. Therefore no finite joint MLE exists.

## Verification
The included checker implements the density and the source's profiled likelihood directly.

For the nondegenerate sample
\[
(1,2,5),
\]
which has a unique minimum, it verifies that the direct joint log-likelihood at
\[
\tau=1,
\qquad
\lambda=\widehat\lambda(\sigma)
\]
agrees with the profiled formula. As \(\sigma\) decreases by one decade, successive profile-log-likelihood increments approach
\[
\frac12\log 10,
\]
as predicted by the coefficient \(k/2=1/2\).

For the sample
\[
(1,1,2,5),
\]
which has two tied minima, the increments approach
\[
\log 10,
\]
matching the coefficient \(k/2=1\).

The checker also confirms
\[
\frac{\widehat\lambda(\sigma)}{\sqrt{\sigma}}
\longrightarrow
\frac{n}{\sum_{y_i>0}\sqrt{y_i}}.
\]
These finite calculations replay the formulas; the divergence theorem itself is the analytic asymptotic proof above.

## Relationship to prior work
The MERD paper introduces the three-parameter extension specifically to relax the original model's fixed lower bound and scale. It proves identifiability, proves that the threshold profile is maximized at the sample minimum for fixed remaining parameters, then proposes profiling \(\lambda\) and numerically maximizing the resulting one-dimensional log-likelihood over \(\sigma>0\).

The unboundedness result comes from that same displayed profile likelihood. It is not a challenge to the algebra of the transformation or to the identifiability proposition. Rather, it identifies a nonregular boundary direction that identifiability alone does not exclude.

General statistical work on parameter-dependent support emphasizes that such models can have nonstandard likelihood behavior and fall outside ordinary regular asymptotic theory. That general observation does not itself imply the MERD scale-collapse rate or prove that this particular profile is unbounded.

Focused searches using the exact source identifier, MERD and modified-exponential-root names, profile-likelihood terminology, scale-collapse language, and location-scale MLE formulations did not locate a published source-specific correction.

## Limitations
The result establishes nonexistence of a finite unconstrained joint MLE. It does not prescribe a unique replacement estimator.

A constrained parameter space, penalized likelihood, or proper Bayesian analysis could regularize the scale-collapse direction, but those alternatives require their own inferential study.

The all-equal sample is excluded, although it has probability zero under the continuous model.

A very recent unindexed correction could exist outside the sources examined.

## References
1. K. A. Rashedi, L. S. Diab, A. H. Alenezy, and G. A. Marei, “A one-parameter decreasing-hazard lifetime model with exact inference on a bounded-below support,” AIMS Mathematics 11 (2026), 24445–24489. DOI: 10.3934/math.2026987.
2. K. Hirano and J. R. Porter, “Asymptotic Efficiency in Parametric Structural Models with Parameter-Dependent Support,” Econometrica 71 (2003), 1307–1338. DOI: 10.1111/1468-0262.00451.
