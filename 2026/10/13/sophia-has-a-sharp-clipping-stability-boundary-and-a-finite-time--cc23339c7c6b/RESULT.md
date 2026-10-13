# Sophia has a sharp clipping-stability boundary and a finite-time resonance
## Finding

Sophia combines diagonal Hessian preconditioning with elementwise clipping. On a diagonal positive quadratic with exact current curvature and no moment memory, those two ingredients collapse to a one-dimensional clipped map in every coordinate.

Let
\[
F(x)=\frac12\sum_{i=1}^d h_i x_i^2,
\qquad
h_i>0.
\]
Use the practical Sophia update with zero weight decay,
\[
\beta_1=\beta_2=0,
\]
an exact diagonal Hessian refresh at every step, constant learning rate
\[
\eta>0,
\]
clipping/Hessian scale
\[
\gamma>0,
\]
and denominator floor
\[
0<\varepsilon\le\gamma\min_i h_i.
\]

Then
\[
g_i=h_i x_i,
\qquad
m_i=g_i,
\qquad
\widehat h_i=h_i,
\]
so the source preconditioned quantity is exactly
\[
\frac{m_i}{\max\{\gamma h_i,\varepsilon\}}
=
\frac{x_i}{\gamma}.
\]
Therefore each coordinate obeys
\[
\boxed{
x_{i,t+1}
=
x_{i,t}
-
\eta\,
\operatorname{clip}
\left(
\frac{x_{i,t}}{\gamma},1
\right).
}
\]

The curvature parameters \(h_i\) disappear completely from this recurrence.

For every initialization, Sophia converges to the minimizer if and only if
\[
\boxed{
0<\eta<2\gamma.
}
\]

In that range, define
\[
N_i
=
\max\left\{
0,
\left\lceil
\frac{|x_{i,0}|-\gamma}{\eta}
\right\rceil
\right\}
\]
and
\[
N=\max_i N_i.
\]
Then
\[
|x_{i,N}|\le\gamma
\]
for every coordinate. From that time onward clipping uses the linear branch, and
\[
\boxed{
x_{N+k}
=
\left(1-\frac{\eta}{\gamma}\right)^k x_N
}
\]
for every integer
\[
k\ge0.
\]
Consequently
\[
\boxed{
F(x_{N+k})
=
\left(1-\frac{\eta}{\gamma}\right)^{2k}
F(x_N).
}
\]

Moreover, when
\[
0<\eta<2\gamma,
\]
every nonzero step strictly decreases every nonzero coordinate magnitude and therefore strictly decreases \(F\).

The boundary is sharp. For
\[
\eta\ge2\gamma,
\]
choose one coordinate \(j\) and initialize
\[
x_0=\frac{\eta}{2}e_j.
\]
Then
\[
x_1=-\frac{\eta}{2}e_j,
\qquad
x_2=\frac{\eta}{2}e_j.
\]
Thus the practical clipped map has a nonzero exact two-cycle for every learning rate at or above the boundary.

A distinguished resonance occurs at
\[
\boxed{
\eta=\gamma.
}
\]
The map becomes
\[
x_i^+
=
\operatorname{sgn}(x_i)
\left(
|x_i|-\gamma
\right)_+.
\]
Hence
\[
\boxed{
x_{i,t}
=
\operatorname{sgn}(x_{i,0})
\left(
|x_{i,0}|-t\gamma
\right)_+.
}
\]
The exact minimizer is reached after
\[
\boxed{
T_\star
=
\max_i
\left\lceil
\frac{|x_{i,0}|}{\gamma}
\right\rceil
}
\]
steps.

This finite-time convergence is independent of the curvature spectrum. It is stronger than merely having a condition-number-independent asymptotic rate: at the resonance, exact diagonal quadratic curvature is cancelled and the clipping map removes a fixed amount of coordinate magnitude until every coordinate is annihilated.

## Assumptions and scope

The theorem concerns the practical Sophia recurrence, not only the simplified full-Hessian theoretical variant.

The Hessian estimate is exact and refreshed every step. The first-moment and Hessian EMAs are disabled by setting
\[
\beta_1=\beta_2=0.
\]

The quadratic is diagonal in the parameter coordinates used by Sophia. This is the natural setting in which a diagonal Hessian preconditioner is exact.

The denominator floor is small enough that
\[
\gamma h_i
\]
is selected in every coordinate. If the floor becomes active, the curvature cancellation is no longer exact.

Weight decay is zero.

The result is deterministic. It does not claim that stochastic Hessian estimates or gradient momentum inherit the finite-time property.

## Proof

Fix one coordinate and write its current value as
\[
x.
\]
The source update reduces to
\[
T(x)
=
x-\eta\operatorname{clip}(x/\gamma,1).
\]

If
\[
|x|\le\gamma,
\]
then
\[
T(x)
=
\left(1-\frac{\eta}{\gamma}\right)x.
\]

If
\[
x>\gamma,
\]
then
\[
T(x)=x-\eta.
\]
If
\[
x<-\gamma,
\]
then
\[
T(x)=x+\eta.
\]

Assume first
\[
0<\eta<2\gamma.
\]
Whenever
\[
|x|>\gamma,
\]
we have
\[
0<\eta<2|x|,
\]
so
\[
|T(x)|<|x|.
\]
When
\[
|x|\le\gamma,
\]
the multiplier satisfies
\[
\left|
1-\frac{\eta}{\gamma}
\right|<1,
\]
so again every nonzero coordinate magnitude strictly decreases.

For a coordinate starting outside the clipping core, repeated clipped steps change its magnitude by \(\eta\) until the first entry. The smallest possible entry index is exactly
\[
N_i
=
\left\lceil
\frac{|x_{i,0}|-\gamma}{\eta}
\right\rceil.
\]
Because
\[
\eta<2\gamma,
\]
the first overshoot across zero cannot pass beyond the opposite boundary of the interval
\[
[-\gamma,\gamma].
\]
Thus the stated \(N_i\) is valid, and once a coordinate enters the interval it never leaves because the linear multiplier has modulus below one.

Taking the maximum entry time over coordinates gives \(N\). The exact linear recurrence and objective ratio then follow immediately.

Now suppose
\[
\eta\ge2\gamma.
\]
At
\[
x=\eta/2,
\]
we have
\[
|x|\ge\gamma,
\]
so clipping returns the sign and
\[
T(\eta/2)=-\eta/2.
\]
Applying the same calculation again returns \(\eta/2\). This proves failure of global convergence at and above the boundary.

Finally, if
\[
\eta=\gamma,
\]
the two branches combine into
\[
T(x)
=
\operatorname{sgn}(x)
\left(
|x|-\gamma
\right)_+.
\]
Iteration gives the closed finite-time formula coordinate by coordinate.

## Verification

The accompanying `verify.py` reconstructs the practical diagonal Sophia recurrence from the stated assumptions.

It checks the exact curvature cancellation, the entry-time formula, the post-entry linear law, strict objective decrease throughout the stable range, the exact two-cycle at and above the boundary, and the finite-time closed form at
\[
\eta=\gamma.
\]

The numerical checks are transcription guards. The stability boundary and finite-time resonance are proved analytically above.

## Relationship to prior work

Liu, Li, Hall, Liang, and Ma introduce Sophia as a diagonal-Hessian preconditioned optimizer followed by elementwise clipping. Their practical algorithm updates parameters using
\[
\operatorname{clip}
\left(
m/\max\{\gamma h,\varepsilon\},
1
\right).
\]
The paper explains that clipping controls worst-case update size and that Hessian preconditioning adapts to heterogeneous curvatures.

The source also proves a condition-number-independent runtime bound for a simplified deterministic full-Hessian version. That theorem fixes its own step and clipping parameters and establishes a burn-in phase followed by exponential decay.

Those results are prior work. The inspected source does not state the exact practical diagonal quadratic map above, the sharp learning-rate boundary
\[
\eta=2\gamma,
\]
the exact two-cycle beyond the boundary, or the finite-time resonance
\[
\eta=\gamma.
\]
Searches for soft-threshold, finite-step, and two-cycle formulations in the source returned no matching statement.

The result here therefore sharpens the source's qualitative curvature-adaptation story in the exact setting where its diagonal Hessian is correct. It shows not only that the condition number disappears, but precisely what replaces it: a single scalar ratio
\[
\eta/\gamma.
\]
At one special value of that ratio, the practical update becomes a finite-time annihilation map.

Focused published-record searches for Sophia quadratic stability, clipped-Newton two-cycles, exact learning-rate/clipping-scale boundaries, and finite-step convergence did not identify an implication-equivalent result.

## Limitations

The theorem deliberately removes first-moment memory and Hessian averaging.

The exact Hessian is refreshed every step; stale or noisy Hessian estimates can change the map.

The result applies to diagonal positive quadratics in Sophia's coordinate basis.

Finite-time convergence at
\[
\eta=\gamma
\]
should not be extrapolated to nonquadratic or stochastic training.

Generic clipped-Newton and trust-region methods provide broader conceptual context, so originality is restricted to the exact practical Sophia recurrence and its sharp hyperparameter law.

## References

1. Hong Liu, Zhiyuan Li, David Hall, Percy Liang, and Tengyu Ma, “Sophia: A Scalable Stochastic Second-order Optimizer for Language Model Pre-training,” arXiv:2305.14342v1, first submitted 2023-05-23.
2. Hong Liu, Zhiyuan Li, David Hall, Percy Liang, and Tengyu Ma, “Sophia: A Scalable Stochastic Second-order Optimizer for Language Model Pre-training,” ICLR 2024.
