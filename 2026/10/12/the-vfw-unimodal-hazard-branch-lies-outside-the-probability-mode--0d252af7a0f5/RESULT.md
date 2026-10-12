# The VFW unimodal hazard branch lies outside the probability model
## Finding
The very flexible Weibull model in the source is defined by
\[
G(x)
=
1-
\exp\!\left\{
-\exp\!\left(
\theta x^{\vartheta}-x^{-1}
\right)
\right\},
\qquad
x>0,
\]
with
\[
\vartheta>0,
\qquad
\theta>0.
\]
Its density is
\[
g(x)
=
\left(
\vartheta\theta x^{\vartheta-1}+x^{-2}
\right)
\exp\!\left(
\theta x^\vartheta-x^{-1}
\right)
\exp\!\left\{
-\exp\!\left(
\theta x^\vartheta-x^{-1}
\right)
\right\}.
\]

The source subsequently classifies hazard shapes by allowing negative, zero, and positive values of \(\theta\), and attributes an increase-then-decrease hazard to \(\theta<0\) and another unimodal branch to \(\theta=0\).

Those two branches do not belong to the probability model.

For every fixed
\[
\vartheta>0,
\]
the displayed formulas define a proper finite-lifetime distribution exactly when
\[
\boxed{\theta>0.}
\]

If
\[
\theta=0,
\]
then
\[
\lim_{x\to\infty}G(x)
=
1-e^{-1}
<
1.
\]
Thus the formula is only a defective subdistribution, with missing mass
\[
e^{-1}.
\]

If
\[
\theta<0,
\]
then
\[
\lim_{x\to\infty}G(x)=0.
\]
Moreover,
\[
\vartheta\theta x^{\vartheta-1}+x^{-2}
=
x^{-2}
\left(
1+\vartheta\theta x^{\vartheta+1}
\right)
\]
changes sign at
\[
\boxed{
x_c
=
\left(
-\frac{1}{\vartheta\theta}
\right)^{1/(\vartheta+1)}.
}
\]
Hence the displayed density is negative for
\[
x>x_c,
\]
and the displayed \(G\) decreases there. It is not a cumulative distribution function.

For the admissible domain
\[
\theta>0,
\]
the hazard
\[
h(x)
=
\left(
\vartheta\theta x^{\vartheta-1}+x^{-2}
\right)
\exp\!\left(
\theta x^\vartheta-x^{-1}
\right)
\]
has the endpoint limits
\[
\boxed{
h(x)\to0
\qquad
(x\downarrow0)
}
\]
and
\[
\boxed{
h(x)\to\infty
\qquad
(x\to\infty).
}
\]

Therefore the proper VFW family cannot have a globally unimodal increase-then-decrease hazard. Any admissible hazard that decreases over an interior range must eventually turn upward again.

For the illustrative extension
\[
(\vartheta,\theta)=(1,-1),
\]
the displayed formula gives
\[
G(1)
=
0.1265769815\ldots
\]
but
\[
G(10)
=
0.0000410787\ldots,
\]
and
\[
g(10)
=
-0.0000406671\ldots.
\]
This directly exhibits the loss of the CDF and PDF properties outside the positive-\(\theta\) domain.

## Assumptions and scope
The claim concerns the exact VFW CDF, PDF, reliability function, and hazard formulas printed in the source.

The shape parameter satisfies
\[
\vartheta>0.
\]
The classification distinguishes the ordinary finite-lifetime probability model from formal extensions of the formulas to
\[
\theta\le0.
\]

A defective distribution at
\[
\theta=0
\]
could be interpreted as a finite lifetime with an atom at infinity. That is not the proper lifetime distribution defined and estimated in the article.

The conclusion does not challenge the source's numerical likelihood or Bayesian calculations, which use positive parameter values and positive-support priors.

The result also does not claim that every positive-\(\theta\) hazard is monotone increasing. The source's positive-\(\theta\) increase-decrease-increase regime remains compatible with the endpoint limits.

## Proof
Set
\[
A(x)
=
\exp\!\left(
\theta x^\vartheta-x^{-1}
\right).
\]
Then
\[
G(x)=1-e^{-A(x)}.
\]

As
\[
x\downarrow0,
\]
one has
\[
\theta x^\vartheta-x^{-1}\to-\infty
\]
for every fixed real \(\theta\), so
\[
A(x)\to0,
\qquad
G(x)\to0.
\]

Now consider the upper endpoint.

If
\[
\theta>0,
\]
then
\[
\theta x^\vartheta-x^{-1}\to+\infty.
\]
Consequently
\[
A(x)\to\infty,
\qquad
G(x)\to1.
\]
Also
\[
A'(x)
=
\left(
\vartheta\theta x^{\vartheta-1}+x^{-2}
\right)A(x)>0,
\]
so \(G\) is increasing and its derivative is the nonnegative density printed by the source. Thus this parameter regime gives a proper distribution.

If
\[
\theta=0,
\]
then
\[
A(x)=e^{-1/x}\to1
\]
and therefore
\[
G(x)\to1-e^{-1}.
\]
The finite-line mass is strictly less than one.

If
\[
\theta<0,
\]
then
\[
\theta x^\vartheta-x^{-1}\to-\infty,
\]
so
\[
A(x)\to0,
\qquad
G(x)\to0.
\]
Furthermore,
\[
A'(x)
=
x^{-2}
\left(
1+\vartheta\theta x^{\vartheta+1}
\right)A(x).
\]
The bracket vanishes once, at
\[
x_c
=
\left(
-\frac{1}{\vartheta\theta}
\right)^{1/(\vartheta+1)},
\]
and is negative after that point. Since
\[
G'(x)=A'(x)e^{-A(x)},
\]
the displayed density is negative for all
\[
x>x_c.
\]
Thus the formal negative-\(\theta\) extension is not a probability distribution.

It remains to determine what the valid parameter domain implies for the hazard endpoints. When
\[
\theta>0,
\]
the hazard is
\[
h(x)
=
\left(
\vartheta\theta x^{\vartheta-1}+x^{-2}
\right)
e^{\theta x^\vartheta-x^{-1}}.
\]
Near zero, every algebraic power is dominated by
\[
e^{-1/x},
\]
so
\[
h(x)\to0.
\]
At infinity, the positive term
\[
\vartheta\theta x^{\vartheta-1}
e^{\theta x^\vartheta-x^{-1}}
\]
diverges, and therefore
\[
h(x)\to\infty.
\]
A hazard that rises and then decreases forever cannot satisfy the latter limit.

## Verification
The bundled checker evaluates the source formulas directly.

It verifies the full parameter-domain trichotomy:

- positive \(\theta\): the CDF approaches one and the density stays positive;
- zero \(\theta\): the CDF approaches \(1-e^{-1}\);
- negative \(\theta\): the density changes sign exactly at the analytic threshold \(x_c\), and the CDF returns toward zero.

For
\[
(\vartheta,\theta)=(1,-1),
\]
the checker reproduces the numerical CDF and density values stated above.

For the two positive parameter pairs used as simulation populations in the source,
\[
(\vartheta,\theta)=(0.5,0.8)
\]
and
\[
(\vartheta,\theta)=(1.5,2.0),
\]
it verifies a near-zero hazard close to zero and rapid eventual growth.

The proof of properness and of the endpoint limits is analytic; these numerical calculations are reproducibility aids.

## Relationship to prior work
The original VFW paper defines both parameters as positive and presents the model as a lifetime distribution with flexible failure rates. The 2025 source likewise explicitly states
\[
\vartheta>0,\qquad\theta>0
\]
when defining the PDF and CDF.

The 2025 source then gives a new hazard-shape classification that includes separate cases
\[
\theta<0,\qquad\theta=0,\qquad\theta>0,
\]
and uses the negative-\(\theta\) branch to advertise an increase-then-decrease hazard.

The complete properness calculation above shows that those extra sign cases are not alternative hazard shapes of the same probability model. The positive-\(\theta\) restriction is mathematically necessary, not merely a convention.

Focused searches using the article DOI, the VFW name, negative-scale terminology, hazard-shape terminology, defective-distribution language, and correction terms did not locate a published model-specific correction.

## Limitations
The result does not classify the number of positive critical points of the hazard inside the admissible parameter domain.

It does not reassess the source's censoring likelihood, point estimators, interval estimators, or positive-parameter Bayesian computations.

The formal case
\[
\theta=0
\]
can be interpreted as a defective lifetime law with mass at infinity, but it is not the proper finite-lifetime VFW distribution studied in the inference sections.

A recent or unindexed correction could exist outside the sources examined.

## References
1. A. Elshahhat and E. A. Seyam, “Very Flexible Weibull Reliability Modeling for Shock Environments Using Unified Censoring Plans,” Mathematics 13 (2025), 3896. DOI: 10.3390/math13243896.
2. Z. Ahmad and Z. Hussain, “Very Flexible Weibull Distribution,” Mayfeb Journal of Mathematics 2 (2017), 61–73.
3. E. S. Brito, P. H. Ferreira, V. L. D. Tomazella, D. S. B. Martins Neto, and R. S. Ehlers, “Inference methods for the Very Flexible Weibull distribution based on progressive type-II censoring,” Communications in Statistics—Simulation and Computation 53 (2024), 5342–5366. DOI: 10.1080/03610918.2023.2180646.
