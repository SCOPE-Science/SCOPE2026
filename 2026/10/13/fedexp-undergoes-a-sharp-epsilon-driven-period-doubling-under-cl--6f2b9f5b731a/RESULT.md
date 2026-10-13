# FedExP undergoes a sharp epsilon-driven period doubling under client-update cancellation
## Finding

Consider deterministic, full-participation FedExP with two equally weighted scalar clients
\[
F_1(x)=\frac a2(x-b)^2,
\qquad
F_2(x)=\frac a2(x+b)^2,
\qquad
a,b>0.
\]
The global objective has the unique minimizer
\[
x^\star=0.
\]

Let each client take one full-batch gradient step of size
\[
\eta_l>0,
\qquad
s=\eta_l a\in(0,1].
\]
The client differences sent to the server are
\[
\Delta_1=s(x-b),
\qquad
\Delta_2=s(x+b),
\]
so
\[
\bar\Delta=sx.
\]

With the source FedExP rule and its positive denominator regularizer
\[
\epsilon>0,
\]
define
\[
r=\frac{\epsilon}{s^2b^2}.
\]
The exact scalar server map is
\[
T(x)
=
x-sx\max\left\{
1,
\frac{x^2+b^2}{2\left(x^2+\epsilon/s^2\right)}
\right\}.
\]

The global minimizer undergoes a sharp local stability transition:
\[
\boxed{
x^\star=0\text{ is linearly attracting}
\iff
\epsilon>\frac{s^3b^2}{4}.
}
\]
At
\[
\epsilon=\frac{s^3b^2}{4}
\]
the derivative at the optimum is
\[
T'(0)=-1,
\]
and for
\[
0<\epsilon<\frac{s^3b^2}{4}
\]
the optimum is linearly repelling.

In that repelling regime there is an exact nonzero symmetric two-cycle
\[
\boxed{
\{-x_c,x_c\},
\qquad
x_c^2
=
b^2\frac{s-4r}{4-s}.
}
\]
At either cycle point the extrapolation factor is exactly
\[
\eta_g=\frac2s.
\]
The cycle is linearly attracting exactly on the interval
\[
\boxed{
\frac{s(2-s)}{2(8-3s)}
<
r
<
\frac s4,
}
\]
or, in the source regularizer,
\[
\boxed{
\frac{s^3(2-s)}{2(8-3s)}\,b^2
<
\epsilon
<
\frac{s^3b^2}{4}.
}
\]

A particularly sharp witness uses
\[
a=b=\eta_l=1,
\qquad
\epsilon=\frac18.
\]
Each client then reaches its own minimizer exactly after its single local step. Vanilla FedAvg therefore averages the two local models to the true global minimizer
\[
0
\]
in one communication round from every initialization.

FedExP instead has
\[
T'(0)=-3,
\]
so the optimum is repelling, and it has the exact attracting two-cycle
\[
\boxed{
x_c=\pm\frac1{\sqrt6}.
}
\]
At each cycle point,
\[
T'(x_c)=\frac57,
\]
so the two-step cycle multiplier is
\[
\boxed{
\left(\frac57\right)^2=\frac{25}{49}<1.
}
\]

Thus a strictly positive denominator regularizer does not by itself prevent persistent extrapolation-induced oscillation. On this natural cancellation family, its sharp local-stability scale is explicit.

## Assumptions and scope

The result uses Algorithm 1 of FedExP with two equally weighted clients, full participation, one deterministic full-batch local gradient step, and the published server rule
\[
\eta_g
=
\max\left\{
1,
\frac{\sum_i\|\Delta_i\|^2}
{2M\left(\|\bar\Delta\|^2+\epsilon\right)}
\right\}.
\]

The local step parameter satisfies
\[
0<s\le1.
\]
This is the usual nonexpansive range for a scalar quadratic of curvature
\[
a.
\]

The client objectives deliberately have distinct minimizers. Hence the example is underparameterized in the sense relevant to the source motivation: the two local minimizer sets do not intersect.

The stability statements are local statements for the fixed point and the displayed two-cycle. No claim is made that the two-cycle attracts every nonzero initialization.

The result concerns last-iterate dynamics. It does not contradict convergence bounds for averaged iterates or bounds with a nonzero heterogeneity error floor.

## Proof

For one local gradient step,
\[
x_{1}^{\mathrm{loc}}
=
x-\eta_l a(x-b),
\qquad
x_{2}^{\mathrm{loc}}
=
x-\eta_l a(x+b).
\]
Therefore
\[
\Delta_1=x-x_{1}^{\mathrm{loc}}=s(x-b),
\qquad
\Delta_2=x-x_{2}^{\mathrm{loc}}=s(x+b),
\]
and
\[
\bar\Delta
=
\frac{\Delta_1+\Delta_2}{2}
=
sx.
\]

The numerator in the FedExP extrapolation ratio is
\[
\Delta_1^2+\Delta_2^2
=
2s^2(x^2+b^2).
\]
For
\[
M=2,
\]
the adaptive ratio is therefore
\[
\frac{x^2+b^2}
{2\left(x^2+\epsilon/s^2\right)}.
\]
This proves the displayed map.

Write
\[
\delta=\frac{\epsilon}{s^2}=rb^2.
\]
Near the origin the extrapolation branch is active whenever
\[
r<\frac12.
\]
On that branch,
\[
T(x)
=
x-
sx\frac{x^2+b^2}{2(x^2+\delta)},
\]
so
\[
T'(0)
=
1-\frac{s}{2r}.
\]
For
\[
0<s\le1,
\]
the condition
\[
|T'(0)|<1
\]
is exactly
\[
r>\frac s4.
\]
If
\[
r\ge\frac12,
\]
the maximum selects the FedAvg branch near the origin and
\[
T'(0)=1-s,
\]
which is also strictly inside the unit disk. Hence
\[
x^\star=0
\]
is linearly attracting exactly when
\[
r>\frac s4,
\]
neutral in linearization at equality, and repelling below it. Replacing
\[
r
\]
by
\[
\epsilon/(s^2b^2)
\]
gives the stated threshold.

For a symmetric two-cycle, solve
\[
T(x)=-x
\]
on the extrapolation branch. For
\[
x\ne0,
\]
this requires
\[
\frac{x^2+b^2}{2(x^2+\delta)}
=
\frac2s.
\]
Solving gives
\[
x_c^2
=
b^2\frac{s-4r}{4-s}.
\]
This is positive exactly when
\[
r<\frac s4.
\]
At such a point the adaptive factor is
\[
2/s>1,
\]
so the assumed branch is self-consistent.

Differentiating the extrapolation branch and substituting the cycle identity yields
\[
D
:=
T'(x_c)
=
-\frac{5rs-16r-s^2+3s}{s(r-1)}.
\]
Because
\[
T
\]
is odd,
\[
T'
\]
is even, so the two-step multiplier is
\[
D^2.
\]

The two boundary equations factor as
\[
D-1=0
\iff
r=
\frac{s(2-s)}{2(8-3s)},
\]
and
\[
D+1=0
\iff
r=\frac s4.
\]
For
\[
0<s\le1
\]
the first value lies strictly between
\[
0
\]
and
\[
s/4,
\]
and direct sign inspection gives
\[
|D|<1
\]
exactly between those two boundaries. This proves the attracting-cycle interval.

For
\[
a=b=\eta_l=1,
\qquad
\epsilon=\frac18,
\]
one has
\[
s=1,
\qquad
r=\frac18.
\]
The two local models are exactly
\[
b
\quad\text{and}\quad
-b,
\]
so FedAvg sends every point to
\[
0.
\]
For FedExP,
\[
T'(0)
=
1-\frac1{2(1/8)}
=
-3.
\]
The cycle formula gives
\[
x_c^2=\frac16,
\]
and substitution into the derivative gives
\[
D=\frac57.
\]
Therefore its two-step multiplier is
\[
25/49<1.
\]

## Verification

The accompanying `verify.py` reconstructs the client differences from the published FedExP update, derives the exact scalar map, checks the sharp fixed-point threshold over a dense parameter sample, verifies the two-cycle formula and its branch condition, and checks the exact attracting-cycle interval.

It also verifies the witness
\[
a=b=\eta_l=1,
\qquad
\epsilon=\frac18
\]
using rational arithmetic wherever possible, including the fixed-point derivative
\[
-3,
\]
the cycle square
\[
1/6,
\]
the cycle derivative
\[
5/7,
\]
and the two-step multiplier
\[
25/49.
\]

Finite checks are used only as transcription guards. The thresholds and cycle formulas are proved algebraically above.

## Relationship to prior work

Jhunjhunwala, Wang, and Joshi introduced FedExP and explicitly identified the denominator constant
\[
\epsilon
\]
as a safeguard against server-step blow-up when the averaged client update is small but individual updates are not. They also observed oscillating last-iterate loss, explained it through alternating emphasis on client updates, and recommended averaging the last two iterates. Their sensitivity study notes that choosing
\[
\epsilon
\]
too small is not always beneficial.

Those observations are the closest prior statements. The inspected source does not give a sharp
\[
\epsilon
\]
threshold at which the global optimum changes linear stability, does not exhibit an attracting nonzero two-cycle around an underparameterized optimum, and does not show an example where FedAvg solves the global problem in one round while FedExP creates a stable periodic orbit.

The source's oscillation example is qualitatively different: it uses intersecting client solution sets, exact projections, and a modified exact-projection extrapolation factor, while the distance to a common optimum decreases monotonically. The present example uses the published Algorithm 1 rule with positive
\[
\epsilon
\]
and disjoint client minimizers; the oscillation is a genuine nonconvergent last-iterate two-cycle.

Li, Acharya, and Richtárik later develop extrapolated FedProx methods and analyze server extrapolation in smooth convex and strongly convex interpolation problems. Their framework is broader in extrapolation design but assumes the interpolation regime for its main FedExProx theory, so it does not imply the cancellation-driven underparameterized phase boundary here.

Focused indexed searches for FedExP two-cycles, period doubling, denominator-regularizer stability, and cancellation-induced repelling optima did not identify an implication-equivalent exact result.

## Limitations

The exact phase diagram is for two symmetric scalar quadratics, one local step, equal client weights, and deterministic full participation.

The cycle-stability interval is local. Basin size and global dynamics outside the displayed interval are not classified.

The exact-local-solve witness uses
\[
s=1,
\]
which is larger than the conservative client-step size used in the source's general convergence theorem. The general formulas nevertheless apply throughout
\[
0<s\le1.
\]

The result does not imply that the practical
\[
\epsilon
\]
values recommended in the source are unstable on realistic datasets.

## References

1. Divyansh Jhunjhunwala, Shiqiang Wang, and Gauri Joshi, “FedExP: Speeding Up Federated Averaging via Extrapolation,” arXiv:2301.09604v1, first submitted 2023-01-23; ICLR 2023.
2. Hanmin Li, Kirill Acharya, and Peter Richtárik, “The Power of Extrapolation in Federated Learning,” arXiv:2405.13766v1, first submitted 2024-05-22; NeurIPS 2024.
