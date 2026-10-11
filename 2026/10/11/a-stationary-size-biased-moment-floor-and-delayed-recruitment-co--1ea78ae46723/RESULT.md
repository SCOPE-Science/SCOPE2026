# A stationary size-biased moment floor and delayed-recruitment covariance law for Nicholson's blowflies
## Finding
Consider Nicholson's blowflies equation
\[
x'(t)
=
-\delta x(t)
+
p\,x(t-\tau)e^{-a x(t-\tau)},
\]
with
\[
p>\delta>0,
\qquad
a>0,
\qquad
\tau>0.
\]
Its positive equilibrium is
\[
K
=
\frac1a\log\!\left(\frac p\delta\right).
\]

Let \(\mu\) be a time-translation-invariant Borel probability measure on a compact family of bounded complete strictly positive solutions. Write
\[
X=x(0)
\]
for the current adult population and
\[
B=x(-\tau)e^{-a x(-\tau)}
\]
for the delayed recruitment input before multiplication by \(p\).

Then the first two stationary balance laws are
\[
\boxed{
p\,\mathbb E_\mu[B]
=
\delta\,\mathbb E_\mu[X]
}
\]
and
\[
\boxed{
p\,\mathbb E_\mu[XB]
=
\delta\,\mathbb E_\mu[X^2]
}.
\]
Consequently,
\[
\boxed{
\operatorname{Cov}_\mu(X,B)
=
\frac{\delta}{p}\operatorname{Var}_\mu(X)
}.
\]

Thus current population and delayed recruitment have an exact positive covariance calibration in every non-equilibrium compact stationary regime.

There is also a sharp moment floor. Define the size-biased current-population law
\[
d\nu
=
\frac{X}{\mathbb E_\mu[X]}\,d\mu.
\]
Stationarity gives
\[
\boxed{
\mathbb E_\nu[e^{-aX}]
=
\frac{\delta}{p}
=
e^{-aK}
}.
\]
Strict convexity of the exponential implies
\[
\boxed{
\frac{\mathbb E_\mu[X^2]}
{\mathbb E_\mu[X]}
\ge
K
}.
\]
Equality holds exactly for the positive equilibrium trajectory
\[
x(t)\equiv K.
\]
Therefore every non-equilibrium compact stationary state satisfies
\[
\boxed{
\mathbb E_\mu[X^2]
>
K\,\mathbb E_\mu[X]
}.
\]

Finally, Cauchy--Schwarz applied to the exact covariance law yields
\[
\boxed{
\operatorname{Var}_\mu(B)
\ge
\left(\frac{\delta}{p}\right)^2
\operatorname{Var}_\mu(X)
}.
\]
For a non-equilibrium state,
\[
\operatorname{Var}_\mu(X)>0,
\]
so the current-population/delayed-recruitment correlation is strictly positive.

## Assumptions and scope
The probability measure is placed on a compact set of complete positive solution trajectories and is invariant under time translation. This two-sided stationary formulation makes the delayed and current one-time marginals identical:
\[
x(-\tau)
\stackrel{d}{=}
x(0).
\]

Compactness supplies the boundedness needed to differentiate the expectations of the current coordinate and its square.

The theorem concerns the classical constant-coefficient Nicholson equation introduced for laboratory blowfly populations. It does not assert existence of a non-equilibrium invariant measure for every parameter choice.

Classical theory already establishes positivity, permanence, stability and oscillation properties. In particular, a standard theorem says that a positive solution which is eventually one-sided relative to \(K\) converges to \(K\). The present finding does not claim that qualitative oscillation result as new.

The earliest verified public date of the model source is 4 September 1980. The major review of the equation lists \(34K20\) first in its subject classification, which is used here.

## Proof
Let
\[
H(u)=u e^{-au}.
\]
For a stationary complete trajectory,
\[
X=x(0),
\qquad
B=H(x(-\tau)).
\]

Time-translation invariance implies that
\[
x(-\tau)
\]
and
\[
x(0)
\]
have the same marginal distribution. Hence
\[
\mathbb E[B]
=
\mathbb E[H(X)].
\]

Apply stationarity to the observable
\[
x(0).
\]
Compactness and the differential equation justify differentiation under the integral, so
\[
0
=
\mathbb E[x'(0)]
=
-\delta\mathbb E[X]
+
p\mathbb E[B].
\]
This gives
\[
p\mathbb E[B]
=
\delta\mathbb E[X].
\]

Now apply stationarity to
\[
\frac12 x(0)^2.
\]
Again differentiating under the integral,
\[
0
=
\mathbb E[Xx'(0)]
=
-\delta\mathbb E[X^2]
+
p\mathbb E[XB].
\]
Therefore
\[
p\mathbb E[XB]
=
\delta\mathbb E[X^2].
\]

Subtracting the product of means gives
\[
p\,\operatorname{Cov}(X,B)
=
\delta
\left(
\mathbb E[X^2]
-
\mathbb E[X]^2
\right),
\]
hence
\[
\operatorname{Cov}(X,B)
=
\frac{\delta}{p}\operatorname{Var}(X).
\]

For the moment floor, let
\[
m=\mathbb E[X]>0
\]
and define
\[
d\nu=\frac Xm\,d\mu.
\]
Using the equality of delayed and current marginals in the first balance,
\[
\frac{\delta}{p}
=
\frac{\mathbb E[Xe^{-aX}]}{\mathbb E[X]}
=
\mathbb E_\nu[e^{-aX}].
\]
Since
\[
\frac{\delta}{p}
=
e^{-aK},
\]
we have
\[
\mathbb E_\nu[e^{-aX}]
=
e^{-aK}.
\]

The function
\[
u\longmapsto e^{-au}
\]
is strictly convex. Jensen's inequality gives
\[
e^{-a\mathbb E_\nu[X]}
\le
\mathbb E_\nu[e^{-aX}]
=
e^{-aK}.
\]
Because the exponential is strictly decreasing,
\[
\mathbb E_\nu[X]
\ge
K.
\]
But
\[
\mathbb E_\nu[X]
=
\frac{\mathbb E[X^2]}{\mathbb E[X]},
\]
so
\[
\mathbb E[X^2]
\ge
K\mathbb E[X].
\]

Equality in Jensen occurs only when
\[
X
\]
is constant under \(\nu\). Strict positivity makes \(\nu\) and \(\mu\) equivalent with respect to zero sets, so
\[
X=c
\]
almost surely under \(\mu\). Translation invariance gives the same statement at every rational time; continuity of the trajectories then makes almost every complete trajectory constant. Substitution into the differential equation gives
\[
e^{-ac}=\frac{\delta}{p},
\]
so
\[
c=K.
\]
Thus equality is exactly the positive equilibrium measure.

Every non-equilibrium state therefore has
\[
\operatorname{Var}(X)>0
\]
and strict size-biased moment inequality. Finally,
\[
\operatorname{Cov}(X,B)^2
\le
\operatorname{Var}(X)\operatorname{Var}(B)
\]
and the exact covariance identity give
\[
\operatorname{Var}(B)
\ge
\left(\frac{\delta}{p}\right)^2\operatorname{Var}(X).
\]

## Verification
The packaged checker uses exact rational arithmetic for the algebraic implications of the two stationary balances.

It verifies that
\[
p\mathbb E[B]=\delta\mathbb E[X]
\]
and
\[
p\mathbb E[XB]=\delta\mathbb E[X^2]
\]
imply
\[
\operatorname{Cov}(X,B)
=
\frac{\delta}{p}\operatorname{Var}(X).
\]

It also checks the variance lower bound after squaring the covariance identity and applying the Cauchy--Schwarz inequality.

A separate symbolic check verifies the equilibrium relation
\[
e^{-aK}=\frac{\delta}{p}
\]
at an exact logarithmic test parameterization.

The stored checker output is `VERIFY_OK`.

The stationary-trajectory argument, strict Jensen equality case and time-translation marginal identity are analytic parts of the proof and are not inferred from numerical delay simulations.

## Relationship to prior work
Gurney, Blythe and Nisbet introduced the delayed recruitment model to explain Nicholson's laboratory blowfly cycles.

Berezansky, Braverman and Idels give a broad review of the classical equation. Their review treats positivity, persistence, permanence, oscillation, local and global stability, periodic coefficients and distributed delays. It states the positive equilibrium and the theorem that a positive solution which is nonoscillatory about that equilibrium converges to it.

That review was inspected at the model definition, equilibrium and oscillation sections, together with document-wide searches for `average`, `moment` and `mean`. None of those three statistical terms occurs in the searchable manuscript, and no stationary first/second-moment identity or size-biased law was located.

A complete open 2016 treatment reproduces the classical equation and surveys positive periodic, almost-periodic, persistence, permanence, oscillation and stability theory before developing time-scale generalizations. Document-wide searches likewise found no `average`, `moment` or `mean` formulation matching the present result.

The qualitative fact that non-equilibrium recurrent solutions oscillate about the positive equilibrium is therefore treated as prior context. The new statement is different: it fixes the size-biased stationary mean through
\[
\mathbb E[X^2]/\mathbb E[X]
\]
and gives an exact covariance between current population and the delayed nonlinear recruitment input.

## Limitations
The theorem is formulated for compact time-translation-invariant laws on complete strictly positive solutions.

It does not cover extinction-supported stationary measures, noncompact statistical states, stochastic forcing or time-dependent coefficients.

The moment floor does not determine the ordinary mean
\[
\mathbb E[X]
\]
by itself, and the variance lower bound for delayed recruitment is not claimed to be an equality in general.

The original 1980 article was inspected through its public bibliographic record and abstract rather than complete full text. The comprehensive 2009/2010 review and the complete 2016 open article were used for the detailed implication comparison.

Because the stationary balance calculation is short, an equivalent identity could remain in older unindexed applied literature.

## References
1. W. S. C. Gurney, S. P. Blythe, and R. M. Nisbet, “Nicholson's blowflies revisited,” Nature 287, 17--21 (1980), DOI 10.1038/287017a0.
2. L. Berezansky, E. Braverman, and L. Idels, “Nicholson's blowflies differential equations revisited: Main results and open problems,” Applied Mathematical Modelling 34, 1405--1417 (2010), DOI 10.1016/j.apm.2009.08.027.
3. Y. Li and B. Li, “Existence and exponential stability of positive almost periodic solution for Nicholson's blowflies models on time scales,” SpringerPlus 5, 1096 (2016), DOI 10.1186/s40064-016-2700-9.
