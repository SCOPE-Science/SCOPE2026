# Exact continuum of neutral two-cycles for scalar Signum
## Finding

Consider deterministic Signum on the scalar quadratic
\[
f(x)=\frac{a}{2}x^2,\qquad a>0,
\]
with constant learning rate \(\delta>0\), momentum parameter \(\beta\in(0,1)\), and update
\[
m_{k+1}=\beta m_k+(1-\beta)a x_k,
\]
\[
x_{k+1}=x_k-\delta\,\operatorname{sign}(m_{k+1}),
\]
where \(\operatorname{sign}(0)=0\).

Every nontrivial period-two orbit belongs to one explicit one-parameter family. Choose the phase for which the position is positive and write it as
\[
x=u.
\]
Then a period-two orbit exists exactly when
\[
\frac{\beta\delta}{1+\beta}
<
u
<
\frac{\delta}{1+\beta}.
\]
At that phase the current momentum is
\[
m_-(u)=
a\left(
u-\frac{\delta}{1+\beta}
\right)<0.
\]
After one update the state is
\[
x=u-\delta<0,
\]
with momentum
\[
m_+(u)=
a\left(
u-\frac{\beta\delta}{1+\beta}
\right)>0,
\]
and the following update returns exactly to the first state.

Thus every nontrivial period-two orbit crosses the minimizer. Its two positions differ by exactly \(\delta\), so its position half-amplitude is always
\[
\frac{\delta}{2},
\]
independent of both \(a\) and \(\beta\).

The cycle midpoint
\[
b=
\frac{u+(u-\delta)}{2}
=
u-\frac{\delta}{2}
\]
is not fixed uniquely. Instead,
\[
|b|
<
\frac{\delta(1-\beta)}{2(1+\beta)}.
\]
Increasing \(\beta\) therefore narrows the allowable cycle-center bias toward the minimizer, but it does not reduce the step-induced half-amplitude \(\delta/2\).

The family is locally normally attracting rather than a collection of asymptotically stable isolated cycles. In a neighborhood where the alternating momentum-sign itinerary is unchanged, the exact two-step map is
\[
x_{k+2}=x_k,
\]
\[
m_{k+2}
=
\beta^2m_k
+
(1-\beta)a
\left[
(1+\beta)x_k-\delta
\right].
\]
Its invariant graph is
\[
m_\star(x)
=
a\left(
x-\frac{\delta}{1+\beta}
\right),
\]
and the transverse error contracts exactly by
\[
m_{k+2}-m_\star(x_{k+2})
=
\beta^2
\left[
m_k-m_\star(x_k)
\right].
\]
Hence the two-step tangential multiplier is \(1\), while the transverse multiplier is \(\beta^2\). Each individual two-cycle is therefore neutrally stable along the family and is not asymptotically stable as an isolated orbit.

This produces a precise deterministic tradeoff: as \(\beta\uparrow1\), the midpoint-bias interval collapses to zero, but the normal attraction factor \(\beta^2\) approaches one.

## Assumptions and scope

The theorem uses the Signum ordering introduced in the original source: the current gradient first updates the exponential moving average, and the parameter step then uses the sign of that new momentum.

The objective is a deterministic one-dimensional positive quadratic and the learning rate is constant. No stochastic gradient noise, minibatching, weight decay, higher-dimensional coordinate coupling, or learning-rate schedule is included.

The classification concerns nontrivial period-two orbits. The origin is the unique fixed point under the convention \(\operatorname{sign}(0)=0\). The theorem does not claim that every initial condition converges to the two-cycle family or exclude higher-period behavior outside the local alternating-sign region.

## Proof

Suppose a nontrivial period-two state is
\[
(x_0,m_0)\mapsto(x_1,m_1)\mapsto(x_0,m_0).
\]
Because each position update is either \(0\), \(+\delta\), or \(-\delta\), returning after two nontrivial steps forces the two momentum signs to be opposite. A zero sign on one step cannot be canceled by a single nonzero step of length \(\delta\).

Choose the phase so that
\[
m_1>0,
\qquad
m_0<0.
\]
Then
\[
x_1=x_0-\delta.
\]
Write
\[
u=x_0.
\]
The periodic momentum equations are
\[
m_1=\beta m_0+(1-\beta)a u,
\]
\[
m_0=\beta m_1+(1-\beta)a(u-\delta).
\]
Solving gives
\[
m_0=
a\left(
u-\frac{\delta}{1+\beta}
\right),
\]
and
\[
m_1=
a\left(
u-\frac{\beta\delta}{1+\beta}
\right).
\]
The required strict signs are therefore equivalent to
\[
u<
\frac{\delta}{1+\beta}
\]
and
\[
u>
\frac{\beta\delta}{1+\beta}.
\]
This proves existence, necessity, and uniqueness of the momentum values for every allowed \(u\). Since the interval lies inside \((0,\delta)\), the second position \(u-\delta\) is negative, so every such orbit crosses zero.

The midpoint formula follows by subtracting \(\delta/2\) from the two endpoint inequalities:
\[
-\frac{\delta(1-\beta)}{2(1+\beta)}
<
u-\frac{\delta}{2}
<
\frac{\delta(1-\beta)}{2(1+\beta)}.
\]

For local attraction of the family, fix an interior \(u\). The two momentum values have nonzero sign margins, so sufficiently small perturbations preserve the sign sequence \(+,-,+,-,\ldots\). On that neighborhood, two position steps cancel exactly:
\[
x_{k+2}=x_k.
\]
Substituting the two momentum updates gives
\[
m_{k+2}
=
\beta^2m_k
+
(1-\beta)a
\left[
(1+\beta)x_k-\delta
\right].
\]
The unique two-step momentum fixed point at a given \(x\) is
\[
m_\star(x)
=
a\left(
x-\frac{\delta}{1+\beta}
\right).
\]
Subtracting this graph from the two-step recurrence yields
\[
m_{k+2}-m_\star(x_{k+2})
=
\beta^2
\left[
m_k-m_\star(x_k)
\right].
\]
Thus the family contracts transversely at the exact two-step factor \(\beta^2\), while perturbations in \(x\) persist exactly. The tangential multiplier is therefore \(1\), proving that no individual member is asymptotically stable.

## Verification

The accompanying `verify.py` checks the closed-form two-cycle formulas in exact rational arithmetic, verifies the full interval classification on a dense parameter grid, and replays the exact two-step contraction law for perturbed momenta in the fixed-sign neighborhood.

The finite checks are algebra and transcription guards only. Exhaustiveness of the period-two classification follows from the sign-cancellation argument and exact solution of the two momentum equations.

## Relationship to prior work

Bernstein et al. introduced Signum as the momentum counterpart of signSGD. Their algorithm uses exactly the update ordering analyzed here. Their theory focuses on stochastic nonconvex convergence with decaying learning rates and growing batches, and interprets momentum as a bias-variance tradeoff in the gradient estimate. The inspected full text does not give the constant-step deterministic quadratic period-two family or its normal-stability structure.

Ma, Wu, and E studied the fixed-step dynamics of adaptive gradient algorithms and used sign-gradient flow to explain early behavior of RMSprop and Adam. They also analyzed oscillatory late-stage behavior of adaptive methods. Their inspected treatment is not an analysis of the discrete Signum recurrence above and does not state this two-cycle classification.

Later sign-momentum theory continues to emphasize stochastic convergence rates. Jiang et al. review Signum and analyze a sign-based momentum method with vanishing horizon-dependent parameters. Their inspected full text does not give a constant-step scalar period-two manifold, midpoint-bias interval, or normal multiplier.

The closest classical interpretation is a relay or quantized feedback system with an exponentially filtered signal. Targeted searches using Signum, signSGD with momentum, scalar quadratics, constant steps, limit cycles, relay dynamics, and period-two terminology did not identify the complete statement above.

## Limitations

The theorem is one-dimensional and deterministic. It does not prove global attraction to the two-cycle family, and it does not classify possible higher-period itineraries.

The normal-attraction statement is local: it requires perturbations small enough that the alternating momentum-sign sequence remains unchanged.

At the interval endpoints one of the momentum values is exactly zero, so the displayed nontrivial two-cycle disappears under the convention \(\operatorname{sign}(0)=0\).

The family is a constant-step phenomenon. Decaying learning rates, stochastic noise, weight decay, or other sign conventions can qualitatively change the asymptotic behavior.

Targeted searches cannot rule out an equivalent relay-system calculation under terminology unrelated to optimization; that remains the principal originality risk.

## References

1. Jeremy Bernstein, Yu-Xiang Wang, Kamyar Azizzadenesheli, and Anima Anandkumar, “signSGD: Compressed Optimisation for Non-Convex Problems,” arXiv:1802.04434v1, 2018.
2. Chao Ma, Lei Wu, and Weinan E, “A Qualitative Study of the Dynamic Behavior of Adaptive Gradient Algorithms,” arXiv:2009.06125v1, 2020.
3. Wei Jiang, Dingzhi Yu, Sifan Yang, Wenhao Yang, and Lijun Zhang, “Improved Analysis for Sign-based Methods with Momentum Updates,” arXiv:2507.12091v1, 2025.
