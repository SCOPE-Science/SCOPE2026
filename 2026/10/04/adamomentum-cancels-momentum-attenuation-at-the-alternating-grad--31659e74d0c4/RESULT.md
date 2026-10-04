# AdaMomentum cancels momentum attenuation at the alternating-gradient frequency
## Finding

AdaMomentum replaces the raw gradient in Adam's second-moment estimate by the momentumized gradient itself. On the highest-frequency deterministic gradient signal, this twofold exponential moving average has an exact and initially counterintuitive effect: after normalization, it cancels the attenuation produced by the first-moment filter.

Consider one coordinate of source-form AdaMomentum Algorithm 1 with
\[
0\le\beta_1,\beta_2<1,
\qquad
\alpha>0,
\qquad
\varepsilon\ge0,
\]
zero initial moment states, and the alternating gradient input
\[
g_t=(-1)^{t-1}G,
\qquad
G\ne0.
\]
The source recurrence is
\[
m_t
=
\beta_1m_{t-1}
+
(1-\beta_1)g_t,
\]
\[
v_t
=
\beta_2v_{t-1}
+
(1-\beta_2)m_t^2
+
\varepsilon,
\]
with bias corrections
\[
\widehat m_t
=
\frac{m_t}{1-\beta_1^t},
\qquad
\widehat v_t
=
\frac{v_t}{1-\beta_2^t},
\]
and update
\[
\Delta\theta_t
=
-\alpha
\frac{\widehat m_t}{\sqrt{\widehat v_t}}.
\]

Define
\[
a
=
\frac{1-\beta_1}{1+\beta_1},
\qquad
d
=
\frac{\varepsilon}{1-\beta_2}.
\]
Then the first moment has the exact transient
\[
m_t
=
(-1)^{t-1}
aG
\left[
1-(-\beta_1)^t
\right].
\]
In particular,
\[
m_t
\longrightarrow
(-1)^{t-1}aG
\]
in the period-two sense.

The bias-corrected second moment converges to
\[
\widehat v_t
\longrightarrow
a^2G^2+d.
\]
Consequently the parameter update converges to an alternating signal of magnitude
\[
U_{\rm AM}
=
\alpha
\frac{a|G|}
{\sqrt{a^2G^2+d}}.
\]

Now isolate the effect of AdaMomentum's defining substitution. Keep the same first moment, bias corrections, and inner-\(\varepsilon\) placement, but let the second moment use the raw squared gradient:
\[
v_t^{\rm raw}
=
\beta_2v_{t-1}^{\rm raw}
+
(1-\beta_2)g_t^2
+
\varepsilon.
\]
Because
\[
g_t^2=G^2
\]
at every iteration,
\[
\widehat v_t^{\rm raw}
=
G^2+d
\]
for every \(t\). Hence its asymptotic normalized update magnitude is
\[
U_{\rm raw}
=
\alpha
\frac{a|G|}
{\sqrt{G^2+d}}.
\]

The exact restoration factor produced by replacing raw-gradient squares with momentum squares is therefore
\[
\boxed{
\frac{U_{\rm AM}}{U_{\rm raw}}
=
\sqrt{
\frac{G^2+d}
{a^2G^2+d}
}
}.
\]
For positive damping and
\[
0<\beta_1<1,
\]
this factor is strictly increasing in
\[
|G|.
\]
It starts at \(1\) in the damping-dominated limit and approaches
\[
\frac1a
=
\frac{1+\beta_1}{1-\beta_1}
\]
in the signal-dominated limit.

In particular, when
\[
\varepsilon=0,
\]
the limiting AdaMomentum update has the exact magnitude
\[
U_{\rm AM}=\alpha
\]
for every
\[
0\le\beta_1<1.
\]
The first-moment EMA has attenuated the alternating gradient by the factor
\[
a,
\]
but the second moment tracks the square of that attenuated signal and divides the same factor back out.

The corresponding raw-gradient control has
\[
U_{\rm raw}=\alpha a.
\]
At the commonly used source setting
\[
\beta_1=0.9,
\]
one has
\[
a=\frac1{19},
\]
so the signal-dominated restoration factor is exactly
\[
19.
\]

With the source table values
\[
\beta_1=0.9,
\qquad
\beta_2=0.999,
\qquad
\varepsilon=10^{-8},
\]
the crossover gradient scale at which the momentum-squared contribution equals the damping floor is
\[
G_c
=
\frac1a
\sqrt{\frac{\varepsilon}{1-\beta_2}}
=
0.060083275543\ldots.
\]
At
\[
|G|=G_c,
\]
the AdaMomentum limiting update magnitude is exactly
\[
\frac{\alpha}{\sqrt2}.
\]
For gradients large relative to this scale, the normalized alternating update is already close to a full sign step.

Thus the twofold EMA does smooth the internal momentum and its square, but the final adaptive normalization can undo the first-moment attenuation at the alternating-gradient frequency.

## Assumptions and scope

The result concerns the displayed source AdaMomentum recurrence and one coordinate.

The gradient sequence is deterministic and externally prescribed. It can be viewed as a frequency-response diagnostic for the optimizer or as the gradients of alternating linear sample losses. It is not asserted to arise from a single fixed smooth objective.

The raw-gradient control changes only the quantity squared inside the second-moment recurrence. It retains AdaMomentum's bias correction and its placement of \(\varepsilon\) inside the second-moment state. This isolates the defining momentum-squared substitution rather than conflating it with a different damping convention.

The zero-damping statement is a limit of the source recurrence and matches the source paper's simplified adaptive-method form used for motivation.

No claim is made about global stochastic convergence, generalization, or basin escape.

## Proof

Let
\[
g_t=(-1)^{t-1}G.
\]
Unrolling the first-moment recurrence gives
\[
m_t
=
(1-\beta_1)
\sum_{i=1}^{t}
\beta_1^{t-i}g_i.
\]
Writing \(j=t-i\) gives
\[
m_t
=
(-1)^{t-1}
(1-\beta_1)G
\sum_{j=0}^{t-1}
(-\beta_1)^j.
\]
The geometric sum yields
\[
m_t
=
(-1)^{t-1}
\frac{1-\beta_1}{1+\beta_1}
G
\left[
1-(-\beta_1)^t
\right],
\]
which is the claimed formula.

For the second moment,
\[
v_t
=
(1-\beta_2)
\sum_{i=1}^{t}
\beta_2^{t-i}m_i^2
+
\varepsilon
\sum_{i=1}^{t}
\beta_2^{t-i}.
\]
After bias correction,
\[
\widehat v_t
=
\frac{1-\beta_2}{1-\beta_2^t}
\sum_{i=1}^{t}
\beta_2^{t-i}m_i^2
+
\frac{\varepsilon}{1-\beta_2}.
\]
The first term is an exponentially weighted average of \(m_i^2\). Since
\[
m_i^2
\longrightarrow
a^2G^2
\]
geometrically, that weighted average converges to the same limit. Therefore
\[
\widehat v_t
\longrightarrow
a^2G^2+d.
\]

Likewise,
\[
\widehat m_t
=
\frac{m_t}{1-\beta_1^t}
\longrightarrow
(-1)^{t-1}aG.
\]
Substitution into the parameter update proves
\[
|\Delta\theta_t|
\longrightarrow
U_{\rm AM}.
\]

For the raw-gradient control,
\[
g_i^2=G^2
\]
for every \(i\), so
\[
v_t^{\rm raw}
=
(1-\beta_2^t)G^2
+
\varepsilon
\frac{1-\beta_2^t}{1-\beta_2}.
\]
Thus
\[
\widehat v_t^{\rm raw}
=
G^2+d
\]
exactly, and the formula for
\[
U_{\rm raw}
\]
follows.

Finally, write
\[
x=G^2.
\]
The square of the restoration factor is
\[
R(x)^2
=
\frac{x+d}{a^2x+d}.
\]
For
\[
d>0
\]
and
\[
0<a<1,
\]
\[
\frac{d}{dx}R(x)^2
=
\frac{d(1-a^2)}
{(a^2x+d)^2}
>
0.
\]
The endpoint limits are
\[
R(0)=1,
\qquad
\lim_{x\to\infty}R(x)=\frac1a.
\]
When
\[
d=0,
\]
the ratio equals
\[
1/a
\]
for every nonzero \(G\), and \(U_{\rm AM}=\alpha\).

## Verification

The accompanying `verify.py` directly replays the source first- and second-moment recurrences under alternating gradients.

It checks the exact first-moment transient, the bias-corrected second-moment limit, the raw-gradient control, monotonicity of the restoration factor, the zero-damping cancellation, and the numerical crossover scale for the source table values.

The finite computations are transcription guards. The limit formulas and monotonicity are proved algebraically above.

## Relationship to prior work

Wang and coauthors introduced AdaMomentum by replacing the raw gradient in Adam's second raw-moment estimate with its momentumized version. The source explicitly describes this as a twofold exponential moving average and motivates it by the claim that the momentumized gradient supplies more accurate directional information. It also moves the damping term inside the second-moment recurrence.

The inspected source develops convergence and generalization arguments and extensive empirical comparisons. Searches within the full text for alternating or oscillating gradients did not identify a frequency-response statement of the form proved here.

LaProp, proposed earlier by Liu, Wang, and Ueda, analyzes a different coupling between momentum and adaptive normalization. That work shows that adaptive normalization can interact strongly with momentum and studies instability when the two decay parameters are mismatched. It does not analyze AdaMomentum's momentum-squared second moment or imply the exact alternating-gradient restoration factor above.

Focused published-record searches for AdaMomentum alternating-gradient steady states, oscillatory gradients, twofold-EMA frequency response, and periodic-gradient second moments did not identify an implication-equivalent result.

## Limitations

The input is a pure alternating signal and therefore probes one extreme frequency.

The result is an optimizer input-response law, not a fixed-objective convergence theorem.

The raw-gradient control is an ablation with the same damping placement; it should not be confused with every implementation detail of standard Adam.

The result does not claim that restoring high-frequency update amplitude is always beneficial or harmful.

## References

1. Yizhou Wang, Yue Kang, Can Qin, Huan Wang, Yi Xu, Yulun Zhang, and Yun Fu, “Rethinking Adam: A Twofold Exponential Moving Average Approach,” arXiv:2106.11514v1, 2021.
2. Liu Ziyin, Zhikang T. Wang, and Masahito Ueda, “LaProp: Separating Momentum and Adaptivity in Adam,” arXiv:2002.04839v1, 2020.
