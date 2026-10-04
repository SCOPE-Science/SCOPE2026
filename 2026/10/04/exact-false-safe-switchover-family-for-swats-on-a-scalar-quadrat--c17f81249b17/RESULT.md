# Exact false-safe switchover family for SWATS on a scalar quadratic
## Finding

SWATS estimates an SGD learning rate from the projection of the current Adam step onto the gradient direction. It switches when the current projection estimate agrees with its bias-corrected exponential average.

That stationarity test does not enforce stability of the proposed SGD rate.

Consider
\[
f(x)=\frac12x^2.
\]
Use the source SWATS equations with no first-moment momentum,
\[
\beta_1=0,
\]
a second-moment coefficient
\[
b=\beta_2\in(0,1),
\]
a constant Adam base step
\[
\alpha>0,
\]
and the same positive
\[
\varepsilon
\]
in the Adam denominator and in the source switchover tolerance.

Fix any desired post-switch normalized SGD rate
\[
q>2.
\]
Define
\[
s=\sqrt{1-b},
\qquad
R=\sqrt{1+b},
\qquad
D=\sqrt{b+(q-1)^2}.
\]
Choose
\[
\varepsilon
=
\frac{\alpha s(D-R)}
{q(D-1)}
\]
and
\[
x_0
=
\frac{\alpha(R-1)}
{q(D-1)}.
\]
Because \(q>2\),
\[
D>R>1,
\]
so both quantities are strictly positive.

For this initialization, the first two Adam-phase projection estimates are exactly
\[
\gamma_1=\gamma_2=q.
\]
The exponential monitor is therefore
\[
\lambda_1=(1-b)q,
\]
\[
\lambda_2=(1-b^2)q,
\]
and its bias-corrected value at the second iteration is
\[
\frac{\lambda_2}{1-b^2}=q=\gamma_2.
\]
Hence the source switching test is satisfied with zero discrepancy:
\[
\left|
\frac{\lambda_2}{1-b^2}
-
\gamma_2
\right|
=
0
<
\varepsilon.
\]

SWATS therefore switches at iteration \(2\) and sets its SGD learning rate to
\[
\Lambda=q.
\]
Since the objective curvature is one, post-switch SGD obeys
\[
x_{k+1}=(1-q)x_k.
\]
For every
\[
q>2,
\]
\[
|1-q|>1,
\]
so the switched phase diverges geometrically.

The instability can be made arbitrarily strong because \(q\) is arbitrary. The trigger can therefore accept an arbitrarily unstable SGD rate while its monitored scalar is perfectly stationary.

The phenomenon also occurs with numerical values close to the source defaults for the Adam base step and second-moment decay. With
\[
\alpha=10^{-3},
\qquad
b=0.999,
\qquad
\varepsilon=10^{-9},
\]
the construction equation has a solution
\[
q\approx2.00003701018859.
\]
The corresponding initialization is
\[
x_0\approx4.99959124847467\times10^{-4}.
\]
Thus the no-momentum SWATS mode switches at its second opportunity to a strictly unstable SGD rate even with a positive \(10^{-9}\) denominator/tolerance.

## Assumptions and scope

The theorem uses the SWATS algorithm as published by Keskar and Socher, including its projection estimate
\[
\gamma_k
=
\frac{p_k^\top p_k}
{-p_k^\top g_k},
\]
its exponential monitor
\[
\lambda_k
=
\beta_2\lambda_{k-1}
+
(1-\beta_2)\gamma_k,
\]
and its switch test
\[
\left|
\frac{\lambda_k}{1-\beta_2^k}
-
\gamma_k
\right|
<
\varepsilon.
\]

The source explicitly discusses the no-momentum case
\[
\beta_1=0.
\]
The theorem is about that valid mode. It does not claim that the paper's default
\[
\beta_1=0.9
\]
has the same counterexample.

The objective is deterministic and scalar. The result is a counterexample to interpreting stationarity of the projection estimate as a stability certificate for the proposed SGD learning rate. It is not a claim about generalization performance.

The construction uses a positive denominator/tolerance and an interior second-moment coefficient
\[
0<\beta_2<1.
\]
It is therefore not a zero-epsilon or zero-\(\beta_2\) boundary artifact.

## Proof

Let the Adam-phase gradient at iteration \(k\) be
\[
g_k=x_{k-1}.
\]
With
\[
\beta_1=0,
\]
the first moment is simply
\[
m_k=g_k.
\]
Let the second-moment state be \(a_k\), initialized at zero:
\[
a_k
=
b a_{k-1}
+
(1-b)g_k^2.
\]

The source Adam-phase step is
\[
p_k
=
-\alpha
\frac{\sqrt{1-b^k}\,g_k}
{\sqrt{a_k}+\varepsilon}.
\]

Set
\[
s=\sqrt{1-b}.
\]
At the first step,
\[
a_1=s^2x_0^2.
\]
The chosen \(x_0\) and \(\varepsilon\) satisfy
\[
s x_0+\varepsilon
=
\frac{\alpha s}{q}.
\]
Therefore
\[
p_1=-q x_0
\]
and
\[
x_1=(1-q)x_0.
\]

In one dimension the SWATS projection estimate reduces exactly to the effective scalar learning rate:
\[
\gamma_k
=
-\frac{p_k}{g_k}.
\]
Hence
\[
\gamma_1=q.
\]

At the second step,
\[
a_2
=
b s^2x_0^2
+
s^2x_1^2
=
s^2x_0^2
\left[
b+(q-1)^2
\right]
=
s^2x_0^2D^2.
\]
Thus
\[
\sqrt{a_2}=s x_0D.
\]

By the definitions of \(x_0\) and \(\varepsilon\),
\[
s x_0D+\varepsilon
=
\frac{\alpha sR}{q},
\]
where
\[
R=\sqrt{1+b}.
\]
Since
\[
\sqrt{1-b^2}=sR,
\]
the second Adam step is
\[
p_2
=
-\alpha
\frac{sR\,x_1}
{s x_0D+\varepsilon}
=
-qx_1.
\]
Therefore
\[
\gamma_2=q.
\]

The monitored exponential average starts from zero. Hence
\[
\lambda_1=(1-b)q,
\]
and
\[
\lambda_2
=
b(1-b)q+(1-b)q
=
(1-b^2)q.
\]
The second-iteration bias correction gives exactly
\[
\frac{\lambda_2}{1-b^2}=q.
\]
Since the source checks the criterion for
\[
k>1,
\]
the switch occurs immediately at \(k=2\).

The selected SGD learning rate is
\[
\Lambda=q.
\]
With no momentum, the switched phase is ordinary gradient descent:
\[
x_{k+1}
=
x_k-qx_k
=
(1-q)x_k.
\]
Because \(q>2\), its magnitude grows by the factor
\[
q-1>1
\]
on every subsequent step.

For the numerical instance with
\[
\alpha=10^{-3},
\qquad
b=0.999,
\qquad
\varepsilon=10^{-9},
\]
substituting the construction's expression for \(\varepsilon\) produces a continuous scalar equation in \(q\). Direct bracketing places a root in
\[
2.00003701018<q<2.00003701020.
\]
The accompanying verifier recomputes that bracket and replays the SWATS recurrence.

## Verification

The accompanying `verify.py` evaluates the closed-form construction across multiple interior values of \(\beta_2\) and multiple target rates \(q>2\).

It replays the first two Adam-phase steps, recomputes the SWATS projection estimates, verifies exact bias-corrected agreement to numerical precision, and then checks geometric growth after the automatic SGD switch.

The script also bisects the source-scale numerical case
\[
\alpha=10^{-3},
\quad
\beta_2=0.999,
\quad
\varepsilon=10^{-9}
\]
and confirms the stated unstable root.

The proof itself is algebraic; numerical replay is used only as an implementation and transcription guard.

## Relationship to prior work

Keskar and Socher introduced SWATS to automate both the switchover point from Adam to SGD and the SGD learning rate used after the switch. Their projection estimate is intended to capture a feasible scalar rate, and the switch is triggered when its bias-corrected exponential average is sufficiently close to the current estimate.

The source explicitly notes that when
\[
\beta_1=0,
\]
the projection estimate is positive and has a Rayleigh-quotient interpretation. It reports empirical success of the automatic criterion but does not provide a deterministic stability theorem for the selected SGD rate.

A recent optimization survey continues to describe SWATS as switching when the monitored Adam-derived rate becomes sufficiently stable. The inspected discussion does not add a curvature-based safety test or a scalar quadratic counterexample.

The present result separates two notions that the trigger does not distinguish: temporal stationarity of the estimated rate and dynamical stability of the rate after switching. On a strongly convex quadratic, the first can hold exactly while the second fails by an arbitrarily large margin.

## Limitations

The counterexample uses
\[
\beta_1=0,
\]
so it does not establish failure for the default momentum setting used in the paper's experiments.

The constructed initialization depends on the optimizer parameters. This is appropriate for an exact stability counterexample but does not claim typicality in neural-network training.

The theorem concerns deterministic optimization of a scalar quadratic and says nothing about SWATS's reported generalization benefits.

A modified switch rule that also checks a curvature-sensitive stability condition could reject this family; such a repair is not analyzed here.

## References

1. Nitish Shirish Keskar and Richard Socher, “Improving Generalization Performance by Switching from Adam to SGD,” arXiv:1712.07628v1, 2017.
2. “First-order optimization algorithms: state of the art, classification, and performance: a practitioner's guide,” Neural Computing and Applications, 2026, DOI `10.1007/s00521-026-12014-1`.
