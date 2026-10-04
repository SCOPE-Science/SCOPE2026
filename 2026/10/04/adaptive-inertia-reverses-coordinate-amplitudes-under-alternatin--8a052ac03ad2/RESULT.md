# Adaptive Inertia reverses coordinate amplitudes under alternating gradients
## Finding

Adaptive Inertia (Adai) uses a global learning rate but chooses a separate momentum coefficient for every parameter from the relative size of its bias-corrected squared-gradient statistic. On a persistent alternating gradient, that rule has an exact frequency-response phase diagram and can reverse coordinate amplitudes.

Consider source-form Adai Algorithm 2 in dimension
\[
d\ge2,
\]
with zero moment states, constant learning rate
\[
\eta>0,
\]
parameters
\[
\beta_0>0,
\qquad
0\le\beta_2<1,
\qquad
0<\epsilon_c<1,
\]
and alternating input
\[
g_t=(-1)^{t-1}G,
\qquad
G_i\ne0
\quad
(i=1,\ldots,d).
\]

Define the mean squared amplitude
\[
\overline V
=
\frac1d\sum_{j=1}^d G_j^2
\]
and each coordinate's relative energy
\[
r_i
=
\frac{G_i^2}{\overline V}.
\]
Then
\[
\frac1d\sum_i r_i=1.
\]

Because each squared gradient is constant in time,
\[
v_{i,t}
=
(1-\beta_2^t)G_i^2.
\]
After the source bias correction,
\[
\widehat v_{i,t}
=
G_i^2
\]
for every iteration. Therefore
\[
\overline v_t=\overline V
\]
exactly, and the source adaptive-inertia coefficient is constant from the first step:
\[
\beta_i
=
\operatorname{clip}
\left(
1-\frac{\beta_0}{r_i},
0,
1-\epsilon_c
\right).
\]
In particular, the entire alternating-gradient response is exactly independent of \(\beta_2\).

For this constant coefficient, the first moment is
\[
m_{i,t}
=
(-1)^{t-1}
\frac{1-\beta_i}{1+\beta_i}
G_i
\left[
1-(-\beta_i)^t
\right].
\]
The source bias correction divides by
\[
1-\beta_i^t,
\]
so
\[
\widehat m_{i,t}
=
(-1)^{t-1}
\frac{1-\beta_i}{1+\beta_i}
G_i
\frac{
1-(-\beta_i)^t
}{
1-\beta_i^t
}.
\]
Consequently the asymptotic parameter-update magnitude is
\[
U_i
=
\eta |G_i|
\frac{1-\beta_i}{1+\beta_i}.
\]

This response is piecewise explicit. Writing
\[
R(r)
=
\frac{U_i}{\eta\sqrt{\overline V}}
\quad
\text{when }r=r_i,
\]
one obtains
\[
R(r)
=
\begin{cases}
\sqrt r,
&
0<r\le\beta_0,
\\[4pt]
\displaystyle
\frac{\beta_0\sqrt r}{2r-\beta_0},
&
\beta_0<r<\beta_0/\epsilon_c,
\\[10pt]
\displaystyle
\frac{\epsilon_c}{2-\epsilon_c}\sqrt r,
&
r\ge\beta_0/\epsilon_c.
\end{cases}
\]

The central branch is strictly decreasing. Indeed,
\[
\frac{d}{dr}
\left[
\frac{\beta_0\sqrt r}{2r-\beta_0}
\right]
=
-
\frac{
\beta_0(2r+\beta_0)
}{
2\sqrt r(2r-\beta_0)^2
}
<
0.
\]
Hence whenever two coordinates lie in the unclipped regime,
\[
\beta_0<r_j<r_i<\frac{\beta_0}{\epsilon_c},
\]
their raw gradient amplitudes satisfy
\[
|G_i|>|G_j|,
\]
but their asymptotic update amplitudes satisfy the reversed ordering
\[
U_i<U_j.
\]

At the source defaults
\[
\beta_0=0.1,
\qquad
\epsilon_c=0.001,
\]
take
\[
G=(2,1).
\]
Then
\[
\overline V=\frac52,
\qquad
(r_1,r_2)=\left(\frac85,\frac25\right).
\]
Both coordinates lie in the unclipped branch, and
\[
(\beta_1,\beta_2^{\mathrm{inertia}})
=
\left(
\frac{15}{16},
\frac34
\right).
\]
The asymptotic update magnitudes are
\[
(U_1,U_2)
=
\left(
\frac{2\eta}{31},
\frac{\eta}{7}
\right).
\]
Thus the coordinate whose alternating gradient is twice as large receives only
\[
\frac{U_1}{U_2}
=
\frac{14}{31}
=
0.4516129032\ldots
\]
times the asymptotic update magnitude.

Clipping creates two outer branches where the response increases as \(\sqrt r\). The amplitude reversal is therefore not a universal ordering law; it is the exact behavior of the broad interior regime in which Adai is genuinely adapting inertia rather than sitting on either clipping boundary.

## Assumptions and scope

The recurrence is Algorithm 2 of the defining Adaptive Inertia paper:
\[
v_t
=
\beta_2v_{t-1}
+
(1-\beta_2)g_t^{\odot2},
\]
\[
\widehat v_t
=
\frac{v_t}{1-\beta_2^t},
\]
\[
\overline v_t
=
\operatorname{mean}(\widehat v_t),
\]
\[
\beta_{1,t}
=
\operatorname{clip}
\left(
1-\beta_0\frac{\overline v_t}{\widehat v_t},
0,
1-\epsilon_c
\right),
\]
\[
m_t
=
\beta_{1,t}\odot m_{t-1}
+
(1-\beta_{1,t})\odot g_t,
\]
followed by the source product bias correction and the global update
\[
\theta_{t+1}
=
\theta_t-\eta\widehat m_t.
\]

The alternating gradient is a deterministic optimizer input-response diagnostic. It may also be realized by alternating linear sample losses. It is not asserted to be the gradient trajectory of one fixed coercive objective.

All coordinates are assumed nonzero so that the source ratio
\[
\overline v_t/\widehat v_{i,t}
\]
is defined without an extra convention.

The superscript-free \(\beta_i\) in the finding denotes the constant parameterwise inertia produced by this input; it is not the source second-moment parameter \(\beta_2\).

## Proof

For every coordinate,
\[
g_{i,t}^2=G_i^2.
\]
Starting from
\[
v_{i,0}=0,
\]
the scalar second-moment recurrence solves to
\[
v_{i,t}
=
(1-\beta_2^t)G_i^2.
\]
The source bias correction therefore gives
\[
\widehat v_{i,t}=G_i^2
\]
for every \(t\). Averaging over coordinates gives
\[
\overline v_t=\overline V,
\]
so the clipped inertia coefficient is the fixed number
\[
\beta_i
=
\operatorname{clip}
\left(
1-\frac{\beta_0}{r_i},
0,
1-\epsilon_c
\right).
\]

Now solve
\[
m_{i,t}
=
\beta_i m_{i,t-1}
+
(1-\beta_i)(-1)^{t-1}G_i.
\]
Unrolling gives
\[
m_{i,t}
=
(1-\beta_i)
\sum_{j=1}^t
\beta_i^{t-j}
(-1)^{j-1}G_i.
\]
Changing variables converts the sum to a finite geometric series in
\[
-\beta_i,
\]
which yields the displayed exact formula.

Because the inertia coefficient has been constant from the first step, the source product correction is
\[
1-\prod_{z=1}^t\beta_i
=
1-\beta_i^t.
\]
Since
\[
0\le\beta_i<1,
\]
the transient ratio tends to one and the stated limiting amplitude follows.

The piecewise response comes directly from the clipping rule.

If
\[
0<r\le\beta_0,
\]
then
\[
1-\beta_0/r\le0
\]
and the lower clip gives
\[
\beta=0.
\]

If
\[
\beta_0<r<\beta_0/\epsilon_c,
\]
neither clip is active, so
\[
\beta=1-\frac{\beta_0}{r}.
\]
Then
\[
\frac{1-\beta}{1+\beta}
=
\frac{\beta_0}{2r-\beta_0}.
\]

If
\[
r\ge\beta_0/\epsilon_c,
\]
the upper clip gives
\[
\beta=1-\epsilon_c,
\]
and
\[
\frac{1-\beta}{1+\beta}
=
\frac{\epsilon_c}{2-\epsilon_c}.
\]

Differentiating the middle branch proves strict amplitude reversal there. Substitution proves the exact two-coordinate example.

## Verification

The accompanying `verify.py` independently replays the source second-moment, clipping, momentum, product bias correction, and parameter update under alternating gradients.

It checks the exact cancellation of \(\beta_2\), the closed transient first moment, the piecewise limiting response, strict interior amplitude reversal, and the exact default-parameter example.

The finite calculations are transcription guards. The complete formulas and monotonicity are proved algebraically above.

## Relationship to prior work

Xie, Wang, Zhang, Sato, and Sugiyama introduced Adaptive Inertia to separate parameterwise momentum adaptation from adaptive learning rates. Their Algorithm 2 computes a bias-corrected squared-gradient statistic, rescales it by its coordinate mean, and sets parameterwise inertia through a clipped ratio. The paper recommends
\[
\beta_0=0.1,
\qquad
\beta_2=0.99,
\qquad
\epsilon_c=0.001,
\]
and analyzes saddle-point escape, flat-minimum selection, and general convergence.

The inspected full text does not state an alternating-gradient or periodic-input response law. Searches within the paper for alternating, periodic, oscillatory, and frequency terminology did not locate such a result.

The source also distinguishes Adai from an earlier adaptive-momentum method because Adai is parameterwise. The result here depends precisely on that parameterwise ratio: constant coordinatewise gradient energies turn into different fixed inertia coefficients, and the high-frequency response can reverse their amplitude ordering.

Focused published-record searches for Adai alternating gradients, periodic gradients, frequency response, and constant-magnitude oscillation did not identify an implication-equivalent result. The closest returned optimization findings concern different momentum or adaptive-state recurrences and do not imply the piecewise response above.

## Limitations

The theorem concerns a persistent alternating input, which probes the highest discrete frequency rather than a generic stochastic-gradient spectrum.

It is an optimizer input-response law, not a convergence theorem for a fixed nonlinear objective.

Coordinates with zero gradient amplitude are excluded because the source ratio would require an additional zero-division convention.

The outer clipping branches do not exhibit amplitude reversal; the reversal is exact only in the unclipped adaptive-inertia regime.

## References

1. Zeke Xie, Xinrui Wang, Huishuai Zhang, Issei Sato, and Masashi Sugiyama, “Adaptive Inertia: Disentangling the Effects of Adaptive Learning Rate and Momentum,” arXiv:2006.15815, first public version 2020-06-29.
