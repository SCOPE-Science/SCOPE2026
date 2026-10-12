# Memoryless Sadam has a sharp softplus flip boundary
## Finding

Sadam replaces Adam's denominator by a softplus calibration,
\[
\operatorname{softplus}(s)
=
\frac{1}{\beta}\log(1+e^{\beta s}),
\qquad
\beta>0.
\]
The source presents \(\beta\) as a controller that interpolates between a smoother momentum-like regime and the Adam-like regime.

The calibration itself has an exact discrete stability transition.

Consider the scalar quadratic
\[
f(x)=\frac{\lambda}{2}x^2,
\qquad
\lambda>0,
\]
with constant base step
\[
\eta>0.
\]
Choose the permitted memoryless Sadam parameters
\[
\beta_1=\beta_2=0.
\]
Then
\[
g_t=\lambda x_t,
\qquad
m_t=g_t,
\qquad
v_t=g_t^2.
\]

Define
\[
a=\eta\beta\lambda,
\qquad
u_t=\beta\lambda |x_t|,
\qquad
L(u)=\log(1+e^u).
\]
The Sadam iteration is exactly
\[
\boxed{
x_{t+1}
=
x_t
\left(
1-\frac{a}{L(u_t)}
\right).
}
\]

This gives a complete local bifurcation picture and a sharp global convergence boundary.

If
\[
0<a<2\log 2,
\]
then every initial point converges to zero. Moreover,
\[
\boxed{
\frac{x_{t+1}}{x_t}
\longrightarrow
1-\frac{a}{\log 2}.
}
\]

At
\[
a=\log 2,
\]
the linear term vanishes and convergence is locally quadratic:
\[
\boxed{
\frac{|x_{t+1}|}{|x_t|^2}
\longrightarrow
\frac{\beta\lambda}{2\log 2}.
}
\]

At the sharp flip boundary
\[
a=2\log 2,
\]
every nonzero orbit still converges to zero, but eventually alternates sign. Its magnitude has the exact first-order critical law
\[
\boxed{
t|x_t|
\longrightarrow
\frac{\log 2}{\beta\lambda}.
}
\]
Consequently,
\[
\boxed{
t^2 f(x_t)
\longrightarrow
\frac{(\log 2)^2}{2\beta^2\lambda}.
}
\]

If
\[
a>2\log 2,
\]
the minimizer is linearly unstable. There is a unique symmetric nonzero two-cycle
\[
\{x_*,-x_*\}
\]
with
\[
\boxed{
\beta\lambda |x_*|
=
\log(e^{a/2}-1).
}
\]
This two-cycle is locally attracting.

Thus the softplus floor does more than cap an adaptive learning rate. In the memoryless scalar core, it creates a sharp flip transition controlled by the single dimensionless product
\[
\eta\beta\lambda.
\]
Increasing \(\beta\) makes Sadam more Adam-like, as intended by the source, but simultaneously narrows the local small-gradient stability range at fixed \(\eta\lambda\).

## Assumptions and scope

The result uses exactly Algorithm 1 of the source, with no bias correction, as displayed there.

The slice
\[
\beta_1=\beta_2=0
\]
is explicitly permitted by the source parameter range
\[
0\le\beta_1,\beta_2<1.
\]
It isolates the nonlinear effect of the softplus denominator from momentum and second-moment memory.

The objective is a deterministic scalar positive quadratic. The theorem does not assert the same threshold for nonzero moment memory, stochastic gradients, multidimensional coupled objectives, or bias-corrected implementations.

The supercritical claim is local for the nonzero two-cycle: it proves existence, uniqueness within symmetric cycles, and local attraction. It does not claim global convergence to that cycle from every nonzero initialization.

## Proof

For the stated parameter slice,
\[
m_t=\lambda x_t
\]
and
\[
\sqrt{v_t}=|\lambda x_t|.
\]
Therefore
\[
\operatorname{softplus}(\sqrt{v_t})
=
\frac{1}{\beta}
\log(1+e^{\beta\lambda|x_t|}),
\]
which gives the exact map
\[
x_{t+1}
=
x_t
\left(
1-\frac{a}{L(u_t)}
\right).
\]

Since
\[
L(0)=\log 2
\]
and \(L\) is strictly increasing, if
\[
0<a\le2\log 2,
\]
then every \(u>0\) satisfies
\[
0<\frac{a}{L(u)}<2.
\]
Hence
\[
|x_{t+1}|<|x_t|
\]
for every nonzero iterate. The magnitude therefore has a limit. A positive limiting magnitude would make the strict multiplier stay uniformly below one, a contradiction. Thus
\[
x_t\to0.
\]

For
\[
0<a<2\log 2,
\]
continuity at zero gives
\[
\frac{x_{t+1}}{x_t}
\to
1-\frac{a}{\log 2}.
\]

The Taylor expansion
\[
L(u)
=
\log 2+\frac{u}{2}+\frac{u^2}{8}+O(u^3)
\]
shows that when
\[
a=\log 2,
\]
\[
1-\frac{a}{L(u)}
=
\frac{u}{2\log 2}+O(u^2).
\]
Because
\[
u=\beta\lambda|x|,
\]
this yields the quadratic convergence constant.

Now let
\[
a=2\log 2.
\]
For sufficiently small positive \(u\), the multiplier is negative, so signs eventually alternate. The magnitude recurrence is
\[
u_{t+1}
=
u_t
\left(
\frac{2\log 2}{L(u_t)}-1
\right)
=
u_t-\frac{u_t^2}{\log 2}+O(u_t^3).
\]
The reciprocal expansion gives
\[
\frac{1}{u_{t+1}}-\frac{1}{u_t}
=
\frac{1}{\log 2}+O(u_t).
\]
Since \(u_t\to0\), averaging these increments yields
\[
t u_t\to\log 2,
\]
which proves both critical limits.

Finally suppose
\[
a>2\log 2.
\]
The derivative at zero is
\[
1-\frac{a}{\log 2}<-1,
\]
so zero is unstable.

A symmetric nonzero two-cycle requires
\[
x_{t+1}=-x_t,
\]
equivalently
\[
1-\frac{a}{L(u_*)}=-1.
\]
Thus
\[
L(u_*)=\frac{a}{2}.
\]
Strict monotonicity of \(L\) gives the unique solution
\[
u_*=\log(e^{a/2}-1)>0.
\]

Let
\[
q=\frac{a}{2},
\qquad
p=1-e^{-q}.
\]
The derivative of the signed map at either cycle point is
\[
d
=
-1+\frac{4u_*p}{a}.
\]
Because
\[
u_*=\log(e^q-1)=q+\log(1-e^{-q})<q
\]
and
\[
0<p<1,
\]
we have
\[
0<\frac{4u_*p}{a}<2.
\]
Therefore
\[
-1<d<1.
\]
The two-step multiplier is \(d^2<1\), proving local attraction.

## Verification

The accompanying `verify.py` reconstructs the source memoryless Sadam map directly.

It checks global magnitude decrease in the subcritical and critical regimes, the ordinary linear factor below threshold, the quadratic resonance at
\[
a=\log 2,
\]
the critical law
\[
t u_t\to\log 2,
\]
the exact supercritical two-cycle amplitude, and the strict local two-cycle multiplier bound.

The computations are transcription and asymptotic guards. The global subcritical statement, critical asymptotic, and supercritical local stability are proved analytically above.

## Relationship to prior work

Tong, Liang, and Bi introduce Sadam by applying a softplus function to the square root of Adam's second-moment state. They prove that this bounds the adaptive learning rate, explain that small \(\beta\) behaves more like momentum while large \(\beta\) approaches the original adaptive method, and recommend tuning \(\beta\).

The inspected source develops nonconvex, convex, and Polyak--Łojasiewicz convergence bounds. It does not analyze the scalar quadratic map above, state a stability threshold at
\[
\eta\beta\lambda=2\log 2,
\]
identify the quadratic resonance at
\[
\eta\beta\lambda=\log 2,
\]
derive the critical inverse-linear amplitude law, or exhibit the supercritical attracting symmetric two-cycle.

Focused searches for Sadam quadratic stability, softplus-preconditioned two-cycles, normalized-gradient cycles, and equivalent \(\log 2\) thresholds did not identify an implication-equivalent published result. Closest indexed optimization results concern other adaptive or normalized steps and do not contain Sadam's softplus map.

## Limitations

The theorem isolates the source-permitted memoryless slice and therefore does not describe the full recommended momentum parameters.

The exact threshold is scalar and deterministic.

The attracting two-cycle statement is local rather than global.

The result identifies a mechanism and a parameter boundary; it does not by itself show that the source's recommended practical settings fail on neural-network training.

## References

1. Qianqian Tong, Guannan Liang, and Jinbo Bi, “Calibrating the Adaptive Learning Rate to Improve Convergence of ADAM,” arXiv:1908.00700v1, first submitted 2019-08-02.
2. Qianqian Tong, Guannan Liang, and Jinbo Bi, “Calibrating the adaptive learning rate to improve convergence of ADAM,” Neurocomputing 481 (2022), 333--356, DOI `10.1016/j.neucom.2022.01.014`.
