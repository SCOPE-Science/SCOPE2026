# M-SVAG has an exact coherent-alternation attenuation law
## Finding

M-SVAG combines an exponential gradient average with an online estimate of gradient variance and then attenuates the average according to an estimated signal-to-noise ratio. On a deterministic period-two input, those two filters have an exact closed response.

Consider one coordinate with
\[
0<\beta<1
\]
and a deterministic alternating gradient
\[
g_t=(-1)^tG,
\qquad
G\ne0.
\]
Let the exponential first and raw-second moments be bias corrected as in the practical source algorithm. Then
\[
\widehat v_t=G^2
\]
for every \(t\), while
\[
\boxed{
\frac{\widehat m_t}{g_t}
=
\frac{1-\beta}{1+\beta}
\frac{1-(-\beta)^{t+1}}{1-\beta^{t+1}}.
}
\]

The practical M-SVAG variance correction uses
\[
\rho_t
=
\frac{(1-\beta)(1+\beta^{t+1})}
{(1+\beta)(1-\beta^{t+1})}
\]
and
\[
\widehat s_t
=
\frac{\widehat v_t-\widehat m_t^2}{1-\rho_t}.
\]
Writing
\[
r=\frac{1-\beta}{1+\beta},
\]
one has
\[
\widehat m_t/g_t\to r,
\qquad
\rho_t\to r,
\]
and therefore
\[
\boxed{
\widehat s_t\longrightarrow
G^2(1+r)
=
\frac{2G^2}{1+\beta}.
}
\]

Thus the practical corrected variance estimator remains strictly positive on a perfectly deterministic coherent alternation.

The source M-SVAG attenuation factor is
\[
\widehat\gamma_t
=
\frac{\widehat m_t^2}
{\widehat m_t^2+\rho_t\widehat s_t}.
\]
Its exact asymptotic value is
\[
\boxed{
\widehat\gamma_t
\longrightarrow
\frac{r}{1+2r}
=
\frac{1-\beta}{3-\beta}.
}
\]

Multiplying by the momentum response gives the complete update-direction gain relative to the current gradient:
\[
\boxed{
\frac{\widehat\gamma_t\widehat m_t}{g_t}
\longrightarrow
\frac{r^2}{1+2r}
=
\frac{(1-\beta)^2}
{(1+\beta)(3-\beta)}.
}
\]

For a constant gradient \(g_t=G\), the bias-corrected moments satisfy
\[
\widehat m_t=G,
\qquad
\widehat v_t=G^2,
\qquad
\widehat s_t=0,
\qquad
\widehat\gamma_t=1.
\]
Hence the displayed factor is the exact asymptotic Nyquist-to-DC gain of this one-coordinate practical M-SVAG response.

At
\[
\beta=0.9,
\]
the momentum-only alternating gain is
\[
\frac1{19},
\]
the additional variance-adaptation factor is
\[
\frac1{21},
\]
and the full M-SVAG gain is
\[
\boxed{\frac1{399}}.
\]
The corrected variance estimate tends to
\[
\boxed{\frac{20}{19}G^2}.
\]

## Assumptions and scope

The gradient sequence is externally prescribed and deterministic. It is a frequency-response diagnostic, not a claim about a fixed objective trajectory.

The theorem uses the practical M-SVAG estimator with one shared exponential coefficient for the first and raw-second moments and the source finite-sample correction factor \(\rho_t\).

The defining analysis motivates the estimator under a local-stationarity model in which recent stochastic gradients are treated as samples from an approximately common distribution. A persistent sign alternation violates that modeling assumption. The positive limit of \(\widehat s_t\) should therefore be interpreted as a model-mismatch diagnostic, not as the true variance of a random input.

The first source step has a special zero-variance convention. It does not affect the asymptotic result.

## Proof

The uncorrected first moment is
\[
m_t
=
(1-\beta)\sum_{j=0}^{t}\beta^{t-j}g_j.
\]
For \(g_j=(-1)^jG\),
\[
m_t
=
(1-\beta)(-1)^tG
\sum_{k=0}^{t}(-\beta)^k.
\]
After division by the bias factor \(1-\beta^{t+1}\),
\[
\frac{\widehat m_t}{g_t}
=
\frac{1-\beta}{1+\beta}
\frac{1-(-\beta)^{t+1}}{1-\beta^{t+1}}.
\]

Because
\[
g_j^2=G^2
\]
for every \(j\), the bias-corrected raw second moment is exactly
\[
\widehat v_t=G^2.
\]

As \(t\to\infty\),
\[
\widehat m_t^2\to r^2G^2
\]
and
\[
\rho_t\to r.
\]
Therefore
\[
\widehat s_t
\to
\frac{G^2-r^2G^2}{1-r}
=
G^2(1+r).
\]

Substitution into the M-SVAG attenuation factor gives
\[
\widehat\gamma_\infty
=
\frac{r^2G^2}
{r^2G^2+rG^2(1+r)}
=
\frac{r}{1+2r}.
\]
Multiplying by
\[
\widehat m_t/g_t\to r
\]
proves the full update gain.

For a constant gradient, bias correction makes both moments equal their constant targets at every step, so the corrected variance is zero and the attenuation factor is one.

## Verification

The accompanying `verify.py` reconstructs the practical bias-corrected M-SVAG moments and source variance correction.

It checks the finite-time first-moment formula, exact raw-second-moment identity, asymptotic corrected variance, attenuation factor, full alternating-gradient gain, constant-gradient DC response, and the exact \(\beta=0.9\) factors \(1/19\), \(1/21\), and \(1/399\).

The computations are transcription guards. The infinite-time limits are proved algebraically above.

## Relationship to prior work

Balles and Hennig introduce stochastic variance-adapted gradients as an online signal-to-noise correction for stochastic optimization. Their practical M-SVAG algorithm estimates the variance from moving first and raw-second moments, applies a finite-sample correction, and multiplies the moving gradient by a variance-adaptation factor.

The same source states that its local-stationarity assumption is most plausible when stochastic noise dominates systematic changes of the gradient. The coherent alternating input studied here deliberately probes the opposite boundary.

The source experiments compare M-SVAG with momentum SGD and use a shared exponential coefficient of \(0.9\), but the inspected full text does not state a period-two response, a Nyquist attenuation law, or the exact \(1/399\) gain.

Focused published-record searches for M-SVAG alternating gradients, periodic gradients, high-frequency response, and variance-adaptation frequency behavior did not identify an implication-equivalent result.

## Limitations

The theorem is one-coordinate and deterministic.

It does not claim that alternating gradients are typical stochastic-gradient noise.

The result concerns the practical source estimator and does not analyze convergence on a full stochastic objective.

The gain law is asymptotic; finite-time transients are given by the exact moment formula but are not separately optimized.

## References

1. Lukas Balles and Philipp Hennig, “Dissecting Adam: The Sign, Magnitude and Variance of Stochastic Gradients,” arXiv:1705.07774v1, first submitted 2017-05-22; ICML 2018.
2. Official M-SVAG reference implementation, `lballes/msvag`.
