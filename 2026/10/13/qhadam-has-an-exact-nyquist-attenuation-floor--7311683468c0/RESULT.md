# QHAdam has an exact Nyquist attenuation floor
## Finding

QHAdam applies quasi-hyperbolic immediate discounts to both Adam moment estimators. On the highest-frequency constant-magnitude signal, the second-moment discount disappears entirely, while the first-moment discount creates an exact attenuation floor.

Consider one coordinate of the bias-corrected source QHAdam recurrence:
\[
m_t
=
\beta_1m_{t-1}
+
(1-\beta_1)g_t,
\]
\[
\widehat m_t
=
\frac{m_t}{1-\beta_1^t},
\]
\[
v_t
=
\beta_2v_{t-1}
+
(1-\beta_2)g_t^2,
\]
\[
\widehat v_t
=
\frac{v_t}{1-\beta_2^t},
\]
with update
\[
\Delta\theta_t
=
-\alpha
\frac{
(1-\nu_1)g_t+\nu_1\widehat m_t
}{
\sqrt{
(1-\nu_2)g_t^2+\nu_2\widehat v_t
}
+
\varepsilon
}.
\]
Assume
\[
0\le\nu_1,\nu_2\le1,
\qquad
0\le\beta_1,\beta_2<1,
\qquad
\alpha>0,
\qquad
\varepsilon\ge0,
\]
zero initial moment states, and
\[
g_t=(-1)^{t-1}G,
\qquad
G\ne0.
\]

Because
\[
g_t^2=G^2
\]
for every \(t\),
\[
v_t
=
G^2(1-\beta_2^t)
\]
and therefore
\[
\boxed{
\widehat v_t=G^2
}
\]
exactly at every step. The complete QH second-moment term is consequently
\[
(1-\nu_2)g_t^2+\nu_2\widehat v_t
=
G^2.
\]
Thus
\[
\nu_2
\]
and
\[
\beta_2
\]
have no effect at all on the update magnitude for this signal.

Now define
\[
a
=
\frac{1-\beta_1}{1+\beta_1}.
\]
The first moment is
\[
m_t
=
(-1)^{t-1}
aG
\left[
1-(-\beta_1)^t
\right],
\]
so
\[
\frac{\widehat m_t}{g_t}
=
a
\frac{
1-(-\beta_1)^t
}{
1-\beta_1^t
}.
\]

This ratio has an exact parity law. For even \(t\),
\[
\frac{\widehat m_t}{g_t}=a.
\]
For odd \(t\),
\[
\frac{\widehat m_t}{g_t}
=
a
\frac{1+\beta_1^t}{1-\beta_1^t},
\]
which decreases to \(a\) as \(t\to\infty\), and at \(t=1\) equals \(1\).

Therefore the QHAdam numerator always has the current gradient's sign and can be written as
\[
(1-\nu_1)g_t+\nu_1\widehat m_t
=
q_t g_t,
\]
where every even step already has the limiting factor
\[
\boxed{
q_\infty
=
(1-\nu_1)
+
\nu_1
\frac{1-\beta_1}{1+\beta_1}
=
1-
\frac{2\nu_1\beta_1}{1+\beta_1}
}
\]
and the odd-step factors decrease from
\[
q_1=1
\]
to the same limit.

The exact update magnitude is therefore
\[
|\Delta\theta_t|
=
\alpha
\frac{|G|}{|G|+\varepsilon}
q_t,
\]
with
\[
\boxed{
|\Delta\theta_t|
\longrightarrow
\alpha
\frac{|G|}{|G|+\varepsilon}
q_\infty
}.
\]

For fixed
\[
\nu_1,
\]
the limiting factor decreases strictly with
\[
\beta_1.
\]
Its sharp high-frequency floor over
\[
0\le\beta_1<1
\]
is
\[
\boxed{
\inf_{\beta_1<1}q_\infty
=
1-\nu_1
}.
\]
Thus the immediate first-moment discount protects a fixed fraction
\[
1-\nu_1
\]
of the current alternating gradient from arbitrarily slow momentum.

When
\[
\nu_1=1,
\]
QHAdam reduces to Adam in the numerator and the attenuation becomes
\[
\frac{1-\beta_1}{1+\beta_1},
\]
which can approach zero as
\[
\beta_1\uparrow1.
\]
Any
\[
\nu_1<1
\]
prevents that complete high-frequency suppression.

For the paper's WMT16 QHAdam setting
\[
\nu_1=0.8,
\qquad
\beta_1=0.95,
\qquad
\nu_2=0.7,
\qquad
\beta_2=0.98,
\]
the asymptotic factor is
\[
q_\infty
=
0.220512820512\ldots.
\]
The second-moment choices
\[
\nu_2=0.7,
\qquad
\beta_2=0.98
\]
do not affect this constant-magnitude alternating response.

## Assumptions and scope

The recurrence is the bias-corrected QHAdam update in the defining paper.

The parameter ranges
\[
0\le\nu_1,\nu_2\le1
\]
are the interpolation regime relevant to the algorithm's immediate-discount interpretation.

The gradient sequence is an externally prescribed input-response diagnostic. It need not arise from a single fixed objective.

The result uses a constant gradient magnitude and alternating sign. This is the real Nyquist-frequency input.

The theorem concerns the QHAdam update before any additional weight decay or clipping not present in the displayed source rule.

## Proof

Unrolling the first moment gives
\[
m_t
=
(1-\beta_1)
\sum_{j=1}^{t}
\beta_1^{t-j}g_j.
\]
For
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
The finite geometric sum yields
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
Dividing by the bias-correction factor and by \(g_t\) gives the exact ratio.

If \(t\) is even, then
\[
(-\beta_1)^t=\beta_1^t,
\]
so the bias-correction factors cancel and
\[
\widehat m_t/g_t=a.
\]
If \(t\) is odd, then
\[
(-\beta_1)^t=-\beta_1^t,
\]
giving the stated larger ratio. Its monotone decrease follows because
\[
x\longmapsto
\frac{1+x}{1-x}
\]
is increasing for \(0\le x<1\), while
\[
\beta_1^t
\]
decreases with odd \(t\).

For the second moment,
\[
v_t
=
(1-\beta_2)
\sum_{j=1}^{t}
\beta_2^{t-j}G^2
=
G^2(1-\beta_2^t).
\]
Bias correction therefore gives
\[
\widehat v_t=G^2.
\]
Substitution into the quasi-hyperbolic second-moment interpolation gives \(G^2\) exactly.

The limiting numerator factor is
\[
q_\infty
=
(1-\nu_1)+\nu_1a.
\]
Differentiating with respect to
\[
\beta_1
\]
gives
\[
\frac{\partial q_\infty}{\partial\beta_1}
=
-\frac{2\nu_1}{(1+\beta_1)^2}
\le0,
\]
with strict inequality when
\[
\nu_1>0.
\]
Taking
\[
\beta_1\uparrow1
\]
proves the sharp floor
\[
1-\nu_1.
\]

## Verification

The accompanying `verify.py` directly replays the source QHAdam moment recurrences under alternating gradients.

It checks the exact first-moment transient, the parity law after bias correction, exact erasure of \(\nu_2\) and \(\beta_2\) from the denominator, the limiting attenuation factor, and the WMT16 numerical value.

The finite calculations are transcription guards. The formulas and sharp floor are proved analytically above.

## Relationship to prior work

Ma and Yarats introduced quasi-hyperbolic momentum as a weighted average between a current gradient and a momentum estimate, then applied the same immediate-discount idea to both moment estimators of Adam to obtain QHAdam.

Their paper explicitly interprets
\[
\nu_1
\]
as controlling how much immediate unbiased gradient enters the update relative to the momentum estimate. It motivates this as a way to reduce the staleness introduced by slow momentum. For QHAdam's second moment, the paper also notes that lowering
\[
\nu_2
\]
can tighten a worst-case per-step update bound.

The inspected full text derives general update bounds and extensive parameter sweeps, but it does not state the response to a persistent alternating constant-magnitude gradient, the exact parity law, or the fact that
\[
\nu_2
\]
and
\[
\beta_2
\]
are completely erased on this signal.

The paper's WMT16 case study uses
\[
(\nu_1,\beta_1,\nu_2,\beta_2)
=
(0.8,0.95,0.7,0.98).
\]
The exact theorem here shows that its highest-frequency constant-magnitude response is controlled only by the first-moment pair.

Focused published-record searches for QHAdam alternating gradients, high-frequency attenuation, periodic inputs, and immediate-discount frequency response did not identify an implication-equivalent result.

## Limitations

The constant-magnitude alternating signal is an extreme high-frequency diagnostic.

The theorem does not imply that changing
\[
\nu_2
\]
or
\[
\beta_2
\]
is irrelevant on general stochastic gradients; only this constant-magnitude signal erases them exactly.

The result concerns the optimizer's input response rather than convergence on a fixed nonlinear objective.

The source allows broader real values of the immediate discounts, while the sharp-floor interpretation here is restricted to the interpolation range
\[
[0,1].
\]

## References

1. Jerry Ma and Denis Yarats, “Quasi-hyperbolic momentum and Adam for deep learning,” arXiv:1810.06801v1, 2018; ICLR 2019.
