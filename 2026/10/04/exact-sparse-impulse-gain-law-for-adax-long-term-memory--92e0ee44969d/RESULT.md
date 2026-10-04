# Exact sparse-impulse gain law for AdaX long-term memory
## Finding

AdaX replaces Adam's exponentially forgetting second moment by an exponentially amplified long-term memory. A single isolated gradient exposes an exact finite-gain law for that mechanism.

Consider one coordinate of source-form AdaX Algorithm 2 with
\[
\alpha_t=\alpha>0,\qquad 0\le\beta_1<1,\qquad \beta_2>0,
\]
zero initial moments, no active projection, and
\[
g_1=G\ne0,\qquad g_t=0\quad(t\ge2).
\]
This input can be realized in the source online framework by one linear loss followed by constant losses on a sufficiently wide bounded interval.

The moments are
\[
m_t=(1-\beta_1)\beta_1^{t-1}G,
\]
\[
v_t=\beta_2(1+\beta_2)^{t-1}G^2,
\]
and
\[
\widehat v_t
=
G^2\frac{\beta_2(1+\beta_2)^{t-1}}{(1+\beta_2)^t-1}.
\]
Hence
\[
\widehat v_t\downarrow G^2\frac{\beta_2}{1+\beta_2}.
\]
The isolated squared gradient therefore keeps the nonzero asymptotic weight
\[
\frac{\beta_2}{1+\beta_2}.
\]

The update magnitude is
\[
|\Delta x_t|
=
\alpha(1-\beta_1)\beta_1^{t-1}F_t(\beta_2),
\]
where
\[
F_t(\beta_2)
=
\sqrt{
\frac{(1+\beta_2)^t-1}{\beta_2(1+\beta_2)^{t-1}}
}
=
\sqrt{
\frac{1+\beta_2-(1+\beta_2)^{-(t-1)}}{\beta_2}
}.
\]
The sequence \(F_t\) increases strictly from \(1\) to
\[
F_\infty=\sqrt{\frac{1+\beta_2}{\beta_2}}.
\]

Thus
\[
x_\infty-x_1
=
-\alpha\,\operatorname{sgn}(G)\,\mathcal G(\beta_1,\beta_2),
\]
with
\[
\mathcal G(\beta_1,\beta_2)
=
(1-\beta_1)\sum_{t=1}^{\infty}\beta_1^{t-1}F_t(\beta_2).
\]
For fixed \(\beta_2\),
\[
\mathcal G(0,\beta_2)=1,
\]
\[
1<\mathcal G(\beta_1,\beta_2)
<
\sqrt{\frac{1+\beta_2}{\beta_2}}
\qquad(0<\beta_1<1),
\]
and
\[
\lim_{\beta_1\uparrow1}\mathcal G(\beta_1,\beta_2)
=
\sqrt{\frac{1+\beta_2}{\beta_2}}.
\]
Moreover \(\mathcal G\) is strictly increasing in \(\beta_1\).

At the source default
\[
(\beta_1,\beta_2)=(0.9,10^{-4}),
\]
\[
\mathcal G=2.855543514903\ldots,
\]
while the sharp limiting ceiling is
\[
100.0049998750\ldots.
\]

For the Adam second moment displayed in the same source framework,
\[
\widehat v_t^{\rm Adam}
=
G^2\frac{(1-\beta_2)\beta_2^{t-1}}{1-\beta_2^t}.
\]
The corresponding normalized update tail is asymptotic to a positive constant times
\[
\left(\frac{\beta_1}{\sqrt{\beta_2}}\right)^{t-1}.
\]
Therefore Adam's total single-impulse displacement is finite exactly when
\[
\beta_1<\sqrt{\beta_2}.
\]
AdaX removes that impulse-summability restriction for every \(\beta_1<1\), but its finite gain can still be large when \(\beta_2\) is very small.

## Assumptions and scope

The recurrence is the displayed source Algorithm 2:
\[
m_t=\beta_1m_{t-1}+(1-\beta_1)g_t,
\]
\[
v_t=(1+\beta_2)v_{t-1}+\beta_2g_t^2,
\]
\[
\widehat v_t=\frac{v_t}{(1+\beta_2)^t-1},
\]
\[
x_{t+1}=x_t-\alpha\frac{m_t}{\sqrt{\widehat v_t}}.
\]

The theorem uses constant \(\alpha\), one coordinate, inactive projection, and the displayed source recurrence without an added denominator regularizer.

It is an optimizer input-response statement. It does not claim fixed-objective global convergence or characterize persistent stochastic noise.

## Proof

The first-moment formula follows directly because the input vanishes after \(t=1\). The second-moment recurrence has one forcing term, giving
\[
v_t=\beta_2(1+\beta_2)^{t-1}G^2.
\]
Substitution into the bias correction yields the formula for \(\widehat v_t\) and therefore for \(F_t\).

Because
\[
F_t(\beta_2)^2
=
\frac{1+\beta_2-(1+\beta_2)^{-(t-1)}}{\beta_2},
\]
\(F_t\) is strictly increasing and bounded by \(F_\infty\). Absolute convergence of the displacement follows from the geometric factor \(\beta_1^{t-1}\).

Let \(N_r\) be geometric on \(\{1,2,\ldots\}\) with
\[
\Pr(N_r=t)=(1-r)r^{t-1}.
\]
Then
\[
\mathcal G(r,\beta_2)=\mathbb E[F_{N_r}(\beta_2)].
\]
If \(0\le r<s<1\), then
\[
\Pr(N_s\ge t)=s^{t-1}>r^{t-1}=\Pr(N_r\ge t)
\]
for every \(t\ge2\). Thus \(N_s\) strictly stochastically dominates \(N_r\), and strict increase of \(F_t\) proves strict increase of \(\mathcal G\).

At \(r=0\), \(N_r=1\), giving \(\mathcal G=1\). As \(r\uparrow1\), \(N_r\to\infty\) in probability, while \(F_t\) is bounded and tends to \(F_\infty\). Hence
\[
\mathcal G(r,\beta_2)\to F_\infty.
\]

For Adam, substitution of the same impulse into its displayed bias-corrected second moment gives the stated formula. Its update magnitude is
\[
\alpha(1-\beta_1)\beta_1^{t-1}
\sqrt{
\frac{1-\beta_2^t}{(1-\beta_2)\beta_2^{t-1}}
}.
\]
Its ratio to
\[
\left(\frac{\beta_1}{\sqrt{\beta_2}}\right)^{t-1}
\]
tends to a positive constant, so the series is summable exactly when \(\beta_1<\sqrt{\beta_2}\).

## Verification

The accompanying `verify.py` replays AdaX under the isolated-gradient input, checks the closed moment formulas and response kernel, evaluates the source-default gain, verifies monotonicity in \(\beta_1\), and checks the finite, critical, and divergent Adam impulse regimes.

The finite calculations are transcription guards. Summability, strict gain monotonicity, and the sharp limiting gain are proved analytically above.

## Relationship to prior work

Li, Zhang, Wang, and Luo introduced AdaX to replace Adam's exponentially forgetting second moment by exponential long-term memory. Their Algorithm 2 multiplies the old second-moment state by \(1+\beta_2\), applies a matching bias correction, and explicitly motivates the design by sparse and small gradients near optimal points. The source also recalls the Adam condition \(\beta_1<\sqrt{\beta_2}\) in its decreasing-gradient analysis.

The inspected AdaX full text establishes broader convergence and second-moment stability results, but it does not state the isolated-gradient cumulative displacement, the exact gain series, or the sharp ceiling
\[
\sqrt{\frac{1+\beta_2}{\beta_2}}.
\]

Bock and Weiß later gave a fixed-point framework for local convergence of deterministic adaptive optimizers, including Adam and several related methods. The inspected analysis does not provide an AdaX sparse-input gain theorem.

Focused published-record searches for AdaX impulse response, sparse-gradient momentum tails, cumulative displacement, early-gradient asymptotic weight, and equivalent gain formulas did not identify an implication-equivalent result.

## Limitations

The isolated-gradient input is a diagnostic for optimizer memory rather than a typical training trajectory.

The source implementation ecosystem may include numerical regularization not present in the displayed Algorithm 2 recurrence analyzed here.

The sharp gain ceiling is approached as \(\beta_1\uparrow1\); the source default \(\beta_1=0.9\) is far below that worst limit.

The Adam comparison uses the bias-corrected second-moment convention displayed in the AdaX source framework.

## References

1. Wenjie Li, Zhaoyang Zhang, Xinjiang Wang, and Ping Luo, “AdaX: Adaptive Gradient Descent with Exponential Long Term Memory,” arXiv:2004.09740v1, 2020.
2. Sebastian Bock and Martin Georg Weiß, “Local Convergence of Adaptive Gradient Descent Optimizers,” arXiv:2102.09804v1, 2021.
