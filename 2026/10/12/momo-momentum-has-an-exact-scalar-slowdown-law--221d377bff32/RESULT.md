# MoMo momentum has an exact scalar slowdown law
## Finding

Consider deterministic source-form MoMo on the scalar strongly convex quadratic
\[
f(x)=\frac a2x^2,
\qquad
a>0,
\]
with exact lower bound
\[
f^\star=0.
\]
Use momentum
\[
0\le\beta<1,
\]
a constant user cap
\[
\alpha\ge\frac1{2a},
\]
no weight decay or preconditioning, and any nonzero initial point
\[
x^1.
\]

The cap is never active. The first step is exactly
\[
x^2=\frac12x^1.
\]

For
\[
\beta>0,
\]
define, for every
\[
k\ge2,
\]
the dimensionless state
\[
z_k
=
\frac{\beta d_{k-1}}
{(1-\beta)a x^k}.
\]
Then
\[
z_k>0
\]
and the complete MoMo dynamics reduce exactly to
\[
\boxed{
\frac{x^{k+1}}{x^k}
=
\frac{z_k+\tfrac12}{z_k+1},
}
\]
\[
\boxed{
z_{k+1}
=
\beta\frac{(1+z_k)^2}{z_k+\tfrac12},
\qquad
z_2=\frac{2\beta}{1-\beta}.
}
\]

The one-dimensional map
\[
F_\beta(z)
=
\beta\frac{(1+z)^2}{z+\tfrac12}
\]
is a contraction on
\[
[0,\infty).
\]
Indeed,
\[
F_\beta'(z)
=
\beta
\frac{z(z+1)}
{(z+\tfrac12)^2},
\]
and
\[
0\le F_\beta'(z)<\beta<1.
\]
Therefore
\[
z_k\to z_\beta
\]
for the unique fixed point.

If
\[
q_\beta
=
\lim_{k\to\infty}\frac{x^{k+1}}{x^k},
\]
then the fixed-point relation gives
\[
\beta=q_\beta(2q_\beta-1).
\]
Hence
\[
\boxed{
q_\beta
=
\frac{1+\sqrt{1+8\beta}}{4}.
}
\]
This formula also extends continuously to
\[
\beta=0,
\]
where source-form MoMo reduces to the stochastic Polyak step with no momentum and, on this deterministic quadratic,
\[
x^{k+1}=\frac12x^k
\]
at every step.

The exact asymptotic objective factor is therefore
\[
\boxed{
\lim_{k\to\infty}
\frac{f(x^{k+1})}{f(x^k)}
=
q_\beta^2.
}
\]
Moreover,
\[
\frac{dq_\beta}{d\beta}
=
\frac1{\sqrt{1+8\beta}}>0.
\]
Thus momentum is strictly rate-worsening on this benchmark.

At the defining paper's default
\[
\beta=0.9,
\]
the iterate factor is
\[
q_{0.9}
=
0.9658910531638176\ldots
\]
and the objective factor is
\[
q_{0.9}^2
=
0.9329455265819088\ldots.
\]
By contrast,
\[
\beta=0
\]
has iterate factor
\[
\frac12
\]
and objective factor
\[
\frac14.
\]

The adaptive learning rate itself also has an exact limit. If
\[
\tau_k
=
\frac{h_k}{d_k^2}
\]
denotes the uncapped MoMo learning rate, then
\[
\boxed{
\lim_{k\to\infty}a\tau_k
=
\frac{2(1-q_\beta)}{2q_\beta+1}.
}
\]
In particular, as
\[
\beta\uparrow1,
\]
\[
q_\beta
=
1-\frac{1-\beta}{3}
+
O((1-\beta)^2),
\]
and
\[
a\tau_k
\longrightarrow
\frac{2(1-\beta)}9
+
O((1-\beta)^2)
\]
after taking the iteration limit. The slowdown is therefore accompanied by collapse of the adaptive learning rate.

## Assumptions and scope

The result uses Algorithm 1 of the defining MoMo paper with the exponentially weighted coefficients whose total weight equals one.

There is one deterministic scalar objective, so there is no sampling noise.

The exact lower bound
\[
f^\star=0
\]
is supplied to MoMo.

The user cap is constant and satisfies
\[
\alpha\ge\frac1{2a}.
\]
The defining paper's default
\[
\alpha=1
\]
therefore satisfies the theorem for the normalized example
\[
a=1.
\]

No weight decay, preconditioner, online lower-bound estimator, or bias-corrected averaging variant is used.

The theorem is not a statement that momentum is always harmful. It isolates the exact behavior of the source MoMo mechanism on the simplest interpolating strongly convex quadratic.

## Proof

The source initialization is
\[
\bar f_0=f(x^1),
\qquad
d_0=\nabla f(x^1)=a x^1,
\qquad
\gamma_0=d_0x^1.
\]
Because
\[
\gamma_0
=
a(x^1)^2
=
2f(x^1)
=
2\bar f_0,
\]
and because
\[
\nabla f(x^k)x^k
=
a(x^k)^2
=
2f(x^k),
\]
the exponentially weighted recurrences imply
\[
\gamma_k=2\bar f_k
\]
for every \(k\).

At the first iteration,
\[
\bar f_1=f(x^1),
\qquad
d_1=a x^1,
\qquad
h_1=f(x^1).
\]
Thus the adaptive proposal is
\[
\frac{h_1}{d_1^2}
=
\frac1{2a}.
\]
The cap assumption makes it inactive, so
\[
x^2=x^1-\frac1{2a}a x^1=\frac12x^1.
\]

We now show inductively that all later iterates have the same sign as \(x^1\), strictly decrease in magnitude, and remain uncapped.

Whenever step \(k-1\) is uncapped,
\[
x^k
=
x^{k-1}
-
\frac{h_{k-1}}{d_{k-1}^2}d_{k-1}.
\]
Using
\[
h_{k-1}
=
d_{k-1}x^{k-1}-\bar f_{k-1},
\]
which follows from
\[
\gamma_{k-1}=2\bar f_{k-1},
\]
we obtain
\[
\bar f_{k-1}
=
x^k d_{k-1}.
\]

The next source recurrence gives
\[
\bar f_k
=
(1-\beta)\frac a2(x^k)^2
+
\beta x^k d_{k-1}
\]
and
\[
d_k
=
(1-\beta)a x^k+\beta d_{k-1}.
\]
Therefore
\[
h_k
=
d_kx^k-\bar f_k
=
(1-\beta)\frac a2(x^k)^2.
\]

Assume, without loss of generality, that
\[
x^1>0.
\]
The first step gives
\[
0<x^2<x^1
\]
and
\[
d_1=a x^1\ge a x^2.
\]
If
\[
d_{k-1}\ge a x^{k-1}\ge a x^k>0,
\]
then
\[
d_k
=
(1-\beta)a x^k+\beta d_{k-1}
\ge
a x^k.
\]
Consequently,
\[
\frac{h_k}{d_k^2}
\le
\frac{1-\beta}{2a}
\le
\frac1{2a}
\le
\alpha.
\]
Thus the cap remains inactive.

For
\[
\beta>0,
\]
introduce
\[
z_k
=
\frac{\beta d_{k-1}}
{(1-\beta)a x^k}.
\]
Then
\[
d_k
=
(1-\beta)a x^k(1+z_k)
\]
and
\[
\frac{h_k}{d_k}
=
\frac{x^k}{2(1+z_k)}.
\]
Hence
\[
x^{k+1}
=
x^k
\left(
1-\frac1{2(1+z_k)}
\right)
=
x^k
\frac{z_k+\tfrac12}{z_k+1}.
\]
This ratio lies strictly between
\[
\frac12
\quad\text{and}\quad
1,
\]
which closes the sign and monotonicity induction.

Also,
\[
z_{k+1}
=
\frac{\beta d_k}
{(1-\beta)a x^{k+1}}
=
\beta
\frac{(1+z_k)^2}
{z_k+\tfrac12}.
\]
The first value is
\[
z_2
=
\frac{\beta a x^1}
{(1-\beta)a(x^1/2)}
=
\frac{2\beta}{1-\beta}.
\]

The derivative calculation in the finding proves that this map is a contraction. At its unique fixed point,
\[
z
=
\beta\frac{(1+z)^2}{z+\tfrac12},
\]
so
\[
\beta
=
\frac{z(z+\tfrac12)}{(1+z)^2}.
\]
Writing
\[
q
=
\frac{z+\tfrac12}{z+1}
\]
gives
\[
2q-1
=
\frac z{z+1},
\]
and therefore
\[
\beta=q(2q-1).
\]
Solving this quadratic for the root in
\[
\left[\frac12,1\right)
\]
gives the stated formula.

Finally,
\[
\tau_k
=
\frac{(1-\beta)a(x^k)^2/2}
{(1-\beta)^2a^2(x^k)^2(1+z_k)^2}
=
\frac1{2(1-\beta)a(1+z_k)^2}.
\]
Since
\[
q
=
1-\frac1{2(1+z)},
\]
we have
\[
1+z=\frac1{2(1-q)}.
\]
Using
\[
1-\beta=(1-q)(2q+1)
\]
yields
\[
a\tau_\infty
=
\frac{2(1-q)}{2q+1}.
\]

## Verification

The accompanying `verify.py` reconstructs Algorithm 1 directly from the loss, gradient, exponentially weighted loss model, gradient momentum, and source lower-bound update.

For multiple curvatures and momentum values it checks that the source cap is inactive under the theorem's assumption, that the direct iteration agrees with the reduced \(z_k\) recurrence, and that the observed consecutive-iterate ratio converges to
\[
\frac{1+\sqrt{1+8\beta}}4.
\]

It separately verifies the exact no-momentum halving law and the default
\[
\beta=0.9
\]
numerical constants.

Finite iteration checks are transcription guards only. The all-iteration recurrence and asymptotic limit are proved analytically above.

## Relationship to prior work

Schaipp, Ohana, Eickenberg, Defazio, and Gower introduced MoMo as a model-based adaptive learning rate for stochastic gradient descent with momentum. Their Algorithm 1 uses momentum averages of function values and gradients, a known lower bound, and a user cap. They prove a convex interpolation guarantee and explicitly remark that the constant in that guarantee is best when
\[
\beta=0,
\]
while empirical momentum often helps. The inspected paper does not give an exact deterministic scalar-quadratic rate law or the fixed-point recurrence above.

The same paper states that the no-momentum case reduces to the capped stochastic Polyak step. The exact
\[
\beta=0
\]
halving law on a scalar quadratic is therefore used only as the baseline against which the momentum branch is compared.

Wang, Johansson, and Zhang independently develop generalized Polyak step sizes for heavy-ball and moving-average-gradient momentum. Their method is different from MoMo. In particular, their smooth heavy-ball variant is constructed from a different distance-minimization principle and is shown to solve a one-dimensional least-squares problem in one step. That result does not imply the MoMo recurrence or slowdown law.

Oikonomou and Loizou later develop stochastic Polyak step sizes specifically for stochastic heavy-ball momentum. Their update is again a different momentum algorithm, with convergence guarantees designed around heavy-ball dynamics rather than MoMo's moving loss model.

Focused searches for MoMo together with scalar quadratics, exact rates, fixed-point recurrences, and momentum-dependent Polyak steps did not identify an implication-equivalent published statement.

## Limitations

The theorem is one-dimensional and deterministic.

It assumes the exact optimal lower bound and a cap large enough not to bind. A smaller cap can alter the dynamics.

The result concerns the original exponentially weighted MoMo variant with total averaging weight one, not the bias-corrected averaging variant or MoMo-Adam.

The theorem does not claim momentum is detrimental on noisy, ill-conditioned, or high-dimensional problems. Its value is as an exact benchmark showing that the source adaptive rule can turn momentum into a severe learning-rate slowdown even when conditioning and stochasticity are absent.

## References

1. Fabian Schaipp, Ruben Ohana, Michael Eickenberg, Aaron Defazio, and Robert M. Gower, “MoMo: Momentum Models for Adaptive Learning Rates,” arXiv:2305.07583v1, first submitted 2023-05-12; ICML 2024, PMLR 235.
2. Xiaoyu Wang, Mikael Johansson, and Tong Zhang, “Generalized Polyak Step Size for First Order Optimization with Momentum,” ICML 2023, PMLR 202.
3. Nicolas Loizou, Sharan Vaswani, Issam Laradji, and Simon Lacoste-Julien, “Stochastic Polyak Step-size for SGD: An Adaptive Learning Rate for Fast Convergence,” arXiv:2002.10542v1, first submitted 2020-02-24.
4. Dimitris Oikonomou and Nicolas Loizou, “Stochastic Polyak Step-sizes and Momentum: Convergence Guarantees and Practical Performance,” arXiv:2406.04142v1, first submitted 2024-06-06.
