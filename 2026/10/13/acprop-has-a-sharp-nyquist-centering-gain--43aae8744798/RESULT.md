# ACProp has a sharp Nyquist centering gain
## Finding

ACProp combines two architectural choices: it centers its adaptive second moment around a gradient EMA, and it delays that denominator by one step so the current gradient does not enter the current denominator. On a persistent sign-alternating gradient, the centering mechanism has an exact high-frequency gain law.

Consider the unrectified paper-form ACProp recurrence on one coordinate:
\[
m_t
=
\beta_1m_{t-1}
+
(1-\beta_1)g_t,
\]
\[
s_t
=
\beta_2s_{t-1}
+
(1-\beta_2)(g_t-m_t)^2,
\]
and
\[
\Delta x_t
=
-\alpha
\frac{g_t}
{\sqrt{s_{t-1}}+\varepsilon},
\]
with
\[
m_0=s_0=0,
\qquad
\alpha>0,
\qquad
0<\beta_1<1,
\qquad
0\le\beta_2<1,
\qquad
\varepsilon\ge0.
\]

Feed the Nyquist-frequency real signal
\[
g_t=(-1)^{t-1}G,
\qquad
G\ne0.
\]

Define
\[
a
=
\frac{1-\beta_1}{1+\beta_1},
\qquad
c
=
\frac{2\beta_1}{1+\beta_1}.
\]
Then the first moment is exactly
\[
m_t
=
(-1)^{t-1}
aG
\left[
1-(-\beta_1)^t
\right].
\]
Therefore the centered residual is exactly
\[
g_t-m_t
=
(-1)^{t-1}
G
\left[
c+a(-\beta_1)^t
\right].
\]

The second-moment state has the exact representation
\[
s_t
=
(1-\beta_2)G^2
\sum_{j=1}^{t}
\beta_2^{t-j}
\left[
c+a(-\beta_1)^j
\right]^2.
\]
Since the squared residual converges geometrically to
\[
c^2G^2,
\]
the stable EMA satisfies
\[
s_t
\longrightarrow
c^2G^2.
\]
Hence the asymptotic ACProp update magnitude is
\[
\boxed{
U_{\rm AC}
=
\alpha
\frac{|G|}
{c|G|+\varepsilon}
}.
\]
The asymptotic magnitude is independent of
\[
\beta_2.
\]

To isolate the effect of momentum centering, compare with the matched asynchronous uncentered control
\[
v_t
=
\beta_2v_{t-1}
+
(1-\beta_2)g_t^2,
\]
\[
\Delta x_t^{\rm unc}
=
-\alpha
\frac{g_t}
{\sqrt{v_{t-1}}+\varepsilon},
\qquad
v_0=0.
\]
Because
\[
g_t^2=G^2
\]
at every step,
\[
v_t
=
G^2(1-\beta_2^t),
\]
and therefore
\[
U_{\rm unc}
=
\alpha
\frac{|G|}
{|G|+\varepsilon}.
\]

The exact asymptotic gain caused by centering is
\[
\boxed{
\frac{U_{\rm AC}}{U_{\rm unc}}
=
\frac{|G|+\varepsilon}
{
\dfrac{2\beta_1}{1+\beta_1}|G|
+
\varepsilon
}
}.
\]

In the zero-damping limit, or equivalently when
\[
|G|\gg\varepsilon,
\]
this becomes
\[
\boxed{
\frac{U_{\rm AC}}{U_{\rm unc}}
=
\frac{1+\beta_1}{2\beta_1}
}.
\]

Thus the high-frequency gain is controlled entirely by the first-moment decay. It decreases strictly with
\[
\beta_1
\]
and approaches one as
\[
\beta_1\uparrow1.
\]
At representative values,
\[
\beta_1=0.9
\quad\Longrightarrow\quad
\frac{U_{\rm AC}}{U_{\rm unc}}
=
\frac{19}{18}
=
1.055555\ldots,
\]
\[
\beta_1=0.5
\quad\Longrightarrow\quad
\frac{U_{\rm AC}}{U_{\rm unc}}
=
\frac32,
\]
and
\[
\beta_1=0.1
\quad\Longrightarrow\quad
\frac{U_{\rm AC}}{U_{\rm unc}}
=
\frac{11}{2}.
\]

With negligible damping, the factor diverges like
\[
\frac1{2\beta_1}
\]
as
\[
\beta_1\downarrow0.
\]
The reason is structural: when the gradient EMA tracks the current alternating gradient very rapidly, the centered residual becomes small even though the raw gradient keeps reversing sign at every iteration.

This gives a sharp complement to the usual centering intuition. Momentum centering can enlarge steps when gradients are predictable relative to their EMA, but sufficiently fast first-moment tracking can also make the highest-frequency deterministic signal appear low-variance to the centered denominator.

## Assumptions and scope

The theorem uses the paper-form ACProp update in which the current raw gradient is the numerator and the centered second moment from the previous iteration is the denominator.

The practical repository contains optional rectification, AMSGrad-style behavior, weight decay, and an alternative momentum numerator. Those options are excluded.

The paper omits bias correction in its theoretical algorithm for simplicity. The theorem follows that form. A standard multiplicative second-moment bias correction tends to one and does not change the stated asymptotic constant.

The gradient sequence is externally prescribed. It is an optimizer input-response diagnostic, not a claim about a fixed objective.

The comparison keeps the asynchronous delay, learning rate, second-moment decay, and denominator regularizer fixed and changes only centered versus uncentered second-moment construction.

For
\[
\varepsilon=0,
\]
the theorem assumes
\[
\beta_1>0.
\]
At the boundary
\[
\beta_1=0,
\]
the centered residual vanishes identically and the undamped denominator is singular.

## Proof

Unroll the first-moment recurrence:
\[
m_t
=
(1-\beta_1)
\sum_{j=1}^{t}
\beta_1^{t-j}g_j.
\]
With
\[
g_j=(-1)^{j-1}G,
\]
factor out the current sign:
\[
m_t
=
(-1)^{t-1}
(1-\beta_1)G
\sum_{r=0}^{t-1}
(-\beta_1)^r.
\]
The geometric sum gives
\[
m_t
=
(-1)^{t-1}
\frac{1-\beta_1}{1+\beta_1}
G
\left[
1-(-\beta_1)^t
\right].
\]

Subtracting from
\[
g_t
=
(-1)^{t-1}G
\]
gives
\[
g_t-m_t
=
(-1)^{t-1}
G
\left[
1-a+a(-\beta_1)^t
\right].
\]
Since
\[
1-a
=
\frac{2\beta_1}{1+\beta_1}
=
c,
\]
this is the displayed residual formula.

Unrolling the centered second moment gives
\[
s_t
=
(1-\beta_2)
\sum_{j=1}^{t}
\beta_2^{t-j}(g_j-m_j)^2,
\]
which immediately yields the exact sum in the finding.

The forcing sequence
\[
(g_t-m_t)^2
\]
converges geometrically to
\[
c^2G^2.
\]
A stable scalar EMA of a convergent sequence has the same limit, so
\[
s_t\to c^2G^2.
\]
The one-step asynchronous delay does not alter that limit:
\[
s_{t-1}\to c^2G^2.
\]
Substitution into the update gives
\[
U_{\rm AC}
=
\alpha|G|/(c|G|+\varepsilon).
\]

For the uncentered control, the squared input is constant:
\[
g_t^2=G^2.
\]
Hence
\[
v_t
=
\beta_2v_{t-1}
+
(1-\beta_2)G^2
=
G^2(1-\beta_2^t).
\]
This proves the uncentered update limit.

The ratio follows by division. In the zero-damping limit,
\[
\frac{U_{\rm AC}}{U_{\rm unc}}
=
\frac1c
=
\frac{1+\beta_1}{2\beta_1}.
\]
Differentiation gives
\[
\frac{d}{d\beta_1}
\frac{1+\beta_1}{2\beta_1}
=
-\frac1{2\beta_1^2}
<
0,
\]
which proves the stated monotonicity.

## Verification

The accompanying `verify.py` directly replays the paper-form ACProp recurrence on alternating gradients.

It checks the exact first-moment and residual formulas, the exact unrolled centered second moment, convergence of the denominator for several
\[
(\beta_1,\beta_2)
\]
pairs, the matched uncentered control, and the stated high-signal gain factors.

The numerical checks are transcription guards. The exact formulas and asymptotic limits are proved algebraically above.

## Relationship to prior work

Zhuang, Ding, Tang, Dvornek, Tatikonda, and Duncan introduced ACProp by combining asynchronous adaptive scaling with momentum centering. The defining paper classifies ACProp as asynchronous and centered: the current gradient enters the current numerator, while the denominator uses the previous centered second moment. It motivates centering through the prediction error
\[
g_t-m_t
\]
and proves that asynchronous centering can weaken convergence conditions on specific online convex examples.

The source also gives a periodic sparse-gradient example to explain why centered and uncentered asynchronous denominators can behave differently. That example contains long zero-gradient stretches and compares convergence inequalities over a period; it does not state the pure alternating-gradient response derived here.

The original implementation confirms the same centered state construction and exposes
\[
\beta_1=0.9,
\qquad
\beta_2=0.999
\]
as default decay parameters, while also offering optional practical extensions not used in the theorem.

Focused published-record and web searches for ACProp alternating gradients, high-frequency response, periodic centered denominators, and exact centered-versus-uncentered gain did not identify an implication-equivalent result.

Nearby AdaBelief and AdaMomentum analyses use different numerator or denominator couplings. In particular, AdaMomentum squares a momentumized gradient in a synchronous denominator, whereas ACProp uses a raw current-gradient numerator and a delayed centered prediction-error denominator.

## Limitations

The theorem concerns the Nyquist-frequency deterministic input and does not characterize arbitrary-frequency full adaptive dynamics.

It analyzes the paper-form unrectified recurrence rather than every option in the reference implementation.

The large small-\(\beta_1\) gain is a boundary diagnostic, not a claim that such parameter choices are used in the source experiments.

The result does not determine whether high-frequency amplification is beneficial or harmful on a particular optimization problem.

## References

1. Juntang Zhuang, Yifan Ding, Tommy Tang, Nicha Dvornek, Sekhar Tatikonda, and James S. Duncan, “Momentum Centering and Asynchronous Update for Adaptive Gradient Methods,” arXiv:2110.05454v1, 2021; NeurIPS 2021.
