# The modified Muth law is exactly a log-Gamma scale family
## Finding
For the modified Muth distribution with scale
\[
\theta>0,
\]
the cumulative distribution function is
\[
F_\theta(x)
=
1-\frac{1+e^{2x/\theta}}{2}
\exp\!\left[-\left(e^{x/\theta}-1\right)\right],
\qquad x>0.
\]
Its density is
\[
f_\theta(x)
=
\frac{1}{2\theta}
\left(e^{x/\theta}-1\right)^2
\exp\!\left[
\frac{x}{\theta}-\left(e^{x/\theta}-1\right)
\right].
\]

Define
\[
G=e^{X/\theta}-1.
\]
Then
\[
\boxed{G\sim\operatorname{Gamma}(3,1)}
\]
with shape \(3\) and rate \(1\). Equivalently,
\[
\boxed{X\overset{d}=\theta\log(1+G)}.
\]

This supplies a rejection-free exact generator: draw
\[
G\sim\operatorname{Gamma}(3,1)
\]
and return
\[
X=\theta\log(1+G).
\]
It also gives
\[
\boxed{
Q_\theta(u)
=
\theta\log\!\left(1+Q_{\Gamma(3,1)}(u)\right),
\qquad0<u<1.
}
\]

There is also an exact finite-sample scale theorem for all six estimators studied in the source. For
\[
x^{(c)}=(cx_1,\ldots,cx_n),\qquad c>0,
\]
the log-likelihood obeys
\[
\ell(c\theta;x^{(c)})=\ell(\theta;x)-n\log c,
\]
while the MPS, LS, WLS, CvM, and AD criteria obey
\[
Q(c\theta;x^{(c)})=Q(\theta;x).
\]
Therefore
\[
\boxed{
\operatorname{ArgOpt}_{\vartheta>0}Q(\vartheta;x^{(c)})
=
c\,\operatorname{ArgOpt}_{\vartheta>0}Q(\vartheta;x).
}
\]
If a unique optimizer is selected,
\[
\widehat\theta(cx)=c\,\widehat\theta(x).
\]

Thus for a sample
\[
X_i=\theta Z_i,
\qquad
Z_i\sim\mathrm{MMuth}(1),
\]
the law of
\[
\widehat\theta/\theta
\]
is independent of \(\theta\) for every finite \(n\). Mean relative error is exactly scale-invariant and RMSE scales exactly linearly with \(\theta\).

For the observed-information Wald interval,
\[
I_{cx}(c\vartheta)=c^{-2}I_x(\vartheta),
\]
so its estimated standard error and endpoints scale by \(c\), interval length scales by \(c\), and coverage probability is exactly invariant.

The source notes that these scaling patterns hold asymptotically and allows finite-sample departures from ideal scaling. For the mathematical criteria it prints, however, the statistical scaling identities are exact. Independent Monte Carlo tables can still differ because of simulation noise, numerical stopping rules, search bounds, or other implementation effects.

## Assumptions and scope
The parameter satisfies
\[
\theta>0.
\]
The Gamma law is parameterized by shape \(3\) and rate \(1\), with density
\[
g(y)=\frac12 y^2e^{-y},
\qquad y>0.
\]

The scale-equivariance statements concern global optimizer sets of the mathematical criteria printed in the source. They do not assert that every software implementation finds the exact global optimum.

The Wald statement concerns the article's observed-information interval with a fixed normal critical value.

## Proof
Set
\[
y=e^{x/\theta}-1.
\]
Then
\[
x=\theta\log(1+y),
\qquad
dx=\frac{\theta}{1+y}\,dy.
\]
Substitution gives
\[
f_\theta(x)\,dx
=
\frac{1}{2\theta}y^2
e^{\log(1+y)-y}
\frac{\theta}{1+y}\,dy
=
\frac12y^2e^{-y}\,dy,
\]
which is the \(\operatorname{Gamma}(3,1)\) density.

The source's scale form gives
\[
F_{c\theta}(cx)=F_\theta(x),
\qquad
f_{c\theta}(cx)=c^{-1}f_\theta(x).
\]
Summing log densities proves the likelihood identity.

MPS depends on CDF spacings, while LS, WLS, CvM, and AD depend only on fitted ordered CDF values and fixed rank weights. Those values are unchanged by simultaneous sample-and-parameter scaling, which proves all five remaining criterion identities and hence the optimizer-set relation.

Finally, from
\[
\ell_c(cu)=\ell(u;x)-n\log c
\]
two differentiations yield
\[
\ell_c''(cu)=c^{-2}\ell''(u;x).
\]
The observed-information and interval scaling statements follow.

## Verification
The bundled checker verifies the Gamma-transformed CDF and quantile identity.

For a fixed positive sample and several scale factors, it evaluates ML, MPS, LS, WLS, CvM, and AD criteria and checks their exact scaling identities to numerical precision.

It also numerically optimizes representative ML and LS criteria before and after scaling, and checks the \(c^{-2}\) observed-information law.

These computations are reproducibility checks; the general statements are proved algebraically.

## Relationship to prior work
The primary article explicitly identifies the model as a scale family. In its moment proof it uses
\[
y=e^x-1
\]
and obtains an integral whose weight is exactly the \(\operatorname{Gamma}(3,1)\) density, but it does not state the resulting stochastic representation, exact generator, or Gamma-quantile formula.

The article also states that MRE and coverage are theoretically scale-invariant while RMSE and interval length scale with \(\theta\), then describes these relations as asymptotic and allows finite-sample departures from ideal statistical scaling. The exact objective identities above strengthen that statement for all six estimators used in the study.

A previous result for the same distribution proves global uniqueness of the ML estimator after reciprocal-scale reparameterization. That theorem is complementary: uniqueness of one likelihood optimizer does not identify the Gamma transform and does not establish exact equivariance of MPS, LS, WLS, CvM, or AD.

General transformation literature catalogs many relations among standard univariate distributions. Focused searches using the modified Muth name, its DOI, Gamma-transform terminology, exact simulation, and scale-equivariance terminology did not locate this model-specific representation or the six-estimator finite-sample theorem.

## Limitations
The theorem does not guarantee that numerical software reaches the global mathematical optimizer.

Independent simulations at different scales need not have identical empirical summaries because of Monte Carlo variability.

The Gamma representation does not make every transformed moment elementary.

A recent or unindexed source could contain the same representation.

## References
1. H. M. Barakat, H. S. Bakouch, M. A. Abd Elgawad, H. Semary, M. A. Alawady, I. A. Husseiny, M. G. Enany, and T. S. Taher, “The modified Muth distribution: Statistical properties, entropy measures, and parameter estimation,” AIMS Mathematics 11 (2026), 6269–6296. DOI: 10.3934/math.2026259.
2. L. M. Leemis and J. T. McQueston, “Univariate Distribution Relationships,” The American Statistician 62 (2008), 45–53. DOI: 10.1198/000313008X270448.
