# Exact single-impulse gain law for LaProp decoupled momentum
## Finding

LaProp preconditions each current gradient before accumulating momentum. For a single isolated gradient this makes the complete cumulative response exactly solvable.

Take one coordinate with constant learning rate \(\lambda>0\), \(0\le\mu<1\), \(0\le\nu<1\), \(\varepsilon>0\), zero moment states, and
\[
g_1=G\ne0,\qquad g_t=0\quad(t\ge2).
\]
With source bias corrections
\[
c_{m,t}=1-\mu^t,\qquad c_{n,t}=1-\nu^t,
\]
the first preconditioned gradient is
\[
\frac{G}{|G|+\varepsilon},
\]
and all later preconditioned gradients are zero. Hence
\[
m_t=(1-\mu)\mu^{t-1}\frac{G}{|G|+\varepsilon},
\]
so
\[
\Delta\theta_t
=
-\lambda\frac{G}{|G|+\varepsilon}
\frac{(1-\mu)\mu^{t-1}}{1-\mu^t}.
\]
Therefore
\[
\theta_\infty-\theta_1
=
-\lambda\frac{G}{|G|+\varepsilon}\mathcal K(\mu),
\]
where
\[
\mathcal K(\mu)
=
(1-\mu)\sum_{t=1}^{\infty}\frac{\mu^{t-1}}{1-\mu^t}
=
\sum_{t=1}^{\infty}
\frac{\mu^{t-1}}{1+\mu+\cdots+\mu^{t-1}}.
\]

The gain is exactly independent of \(\nu\). For fixed \(\mu<1\), each summand is at most \(\mu^{t-1}\), so the series is finite. For \(t\ge2\),
\[
\frac{\mu^{t-1}}{1+\mu+\cdots+\mu^{t-1}}
=
\frac{1}{1+\mu^{-1}+\cdots+\mu^{-(t-1)}},
\]
which is strictly increasing in \(\mu\); hence \(\mathcal K\) is strictly increasing. Also
\[
\mathcal K(0)=1.
\]
As \(\mu\uparrow1\), the \(t\)-th summand tends to \(1/t\). Arbitrarily long partial sums therefore approach harmonic sums of arbitrarily large size, proving
\[
\lim_{\mu\uparrow1}\mathcal K(\mu)=\infty.
\]

At representative source-recommended momentum values,
\[
\mathcal K(0.8)=2.3892643470829\ldots,
\]
\[
\mathcal K(0.9)=3.0096094482298\ldots.
\]

For comparison, use the zero-damping Adam recurrence in the same notation with \(0<\nu<1\). The same isolated gradient gives
\[
m_t=(1-\mu)\mu^{t-1}G,\qquad
n_t=(1-\nu)\nu^{t-1}G^2.
\]
Its bias-corrected update magnitude is
\[
\lambda
\frac{(1-\mu)\mu^{t-1}}{1-\mu^t}
\sqrt{
\frac{1-\nu^t}{(1-\nu)\nu^{t-1}}
}.
\]
The tail is asymptotic to a positive constant times
\[
\left(\frac{\mu}{\sqrt{\nu}}\right)^{t-1}.
\]
Thus Adam's isolated-gradient total displacement is finite exactly when
\[
\mu<\sqrt{\nu}.
\]
At equality the update tail tends to a positive constant; above equality it grows geometrically.

LaProp therefore removes this momentum/adaptivity summability threshold for an isolated gradient, while retaining a distinct cumulative-memory effect: its impulse gain becomes arbitrarily large as \(\mu\) approaches one even though each individual update remains bounded.

## Assumptions and scope

The LaProp recurrence is
\[
n_t=\nu n_{t-1}+(1-\nu)g_t^2,
\]
\[
m_t=\mu m_{t-1}+(1-\mu)\frac{g_t}{\sqrt{n_t/c_{n,t}}+\varepsilon},
\]
\[
\theta_{t+1}=\theta_t-\lambda\frac{m_t}{c_{m,t}}.
\]
The theorem assumes \(\varepsilon>0\), so the preconditioned zero gradients are well defined even when \(\nu=0\). The Adam comparison is separately stated for zero damping and \(0<\nu<1\).

The input is a sparse optimizer diagnostic, not a trajectory claim for one fixed strongly convex objective. No persistent-noise or global-convergence statement is made.

## Proof

The first step has \(n_1/c_{n,1}=G^2\), hence the normalized input \(G/(|G|+\varepsilon)\). Every later raw gradient is zero, so the momentum state is a homogeneous geometric tail. Division by \(1-\mu^t\) gives the exact update and the series \(\mathcal K\).

Geometric domination proves convergence for fixed \(\mu<1\). The reciprocal-polynomial representation proves strict monotonicity. The harmonic limiting partial sums prove divergence as \(\mu\uparrow1\).

For Adam, solving its first- and second-moment recurrences gives the displayed update. Dividing that update by \((\mu/\sqrt{\nu})^{t-1}\) yields a positive finite limit, so the geometric-series criterion gives the if-and-only-if threshold.

## Verification

The accompanying `verify.py` replays LaProp and Adam directly, compares source recurrences with the closed formulas, checks the numerical gains at \(\mu=0.8\) and \(\mu=0.9\), verifies gain monotonicity numerically, and checks the Adam subcritical, critical, and supercritical regimes.

The numerical work is only a transcription check. Finiteness, monotonicity, divergence, and the Adam threshold are proved analytically.

## Relationship to prior work

Liu, Wang, and Ueda introduced LaProp to decouple momentum from adaptivity. Their Algorithm 1 preconditions the current gradient before accumulating momentum. Proposition 1 proves that each individual LaProp update is bounded independently of \(\mu\), while Proposition 2 gives an Adam bound under the coupling condition \(\mu<\sqrt{\nu}\). The paper also explicitly motivates LaProp by resilience to a single pathologically large gradient.

The inspected full text does not state the total displacement from one isolated gradient, the exact series \(\mathcal K(\mu)\), its strict monotonicity, or its divergence as \(\mu\uparrow1\). Thus the result distinguishes pointwise update robustness from cumulative impulse gain.

Focused published-record and web searches for LaProp impulse response, isolated gradients, cumulative displacement, and equivalent sparse-input formulations did not identify an implication-equivalent result.

## Limitations

The single impulse is intentionally sparse.

The unbounded high-\(\mu\) gain does not contradict the source per-step bound; it is accumulation across infinitely many bounded updates.

The Adam comparison uses zero damping. A positive fixed denominator floor changes Adam's very late tail.

No claim is made that large impulse gain is universally harmful.

## References

1. Liu Ziyin, Zhikang T. Wang, and Masahito Ueda, “LaProp: Separating Momentum and Adaptivity in Adam,” arXiv:2002.04839v1, 2020; revised as arXiv:2002.04839v3, 2021.
