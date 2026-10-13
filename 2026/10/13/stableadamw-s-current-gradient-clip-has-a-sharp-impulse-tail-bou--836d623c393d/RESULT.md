# StableAdamW's current-gradient clip has a sharp impulse-tail boundary
## Finding

StableAdamW modifies AdamW by detecting when the current squared gradient is large relative to the second-moment estimate and then reducing the tensor learning rate. This mechanism is designed for a changing learning signal. Its use of the **current** gradient in the detector creates an exact complementary blind spot: after a large gradient disappears, stale first-moment momentum can remain while the clipping statistic is identically zero.

Consider one scalar coordinate with zero weight decay, constant base step
\[
\alpha>0,
\]
numerical floor
\[
\varepsilon>0,
\]
and
\[
0<\beta_1,\beta_2<1.
\]
Use the source bias-corrected recurrence
\[
\widehat\beta_{j,t}
=
\beta_j
\frac{1-\beta_j^{t-1}}{1-\beta_j^t},
\qquad
j\in\{1,2\},
\]
\[
v_t
=
\widehat\beta_{1,t}v_{t-1}
+
(1-\widehat\beta_{1,t})g_t,
\]
\[
u_t
=
\widehat\beta_{2,t}u_{t-1}
+
(1-\widehat\beta_{2,t})g_t^2,
\]
with
\[
v_0=u_0=0.
\]

For the implementation form of StableAdamW, the scalar clipping statistic is
\[
\mathrm{RMS}_t
=
\sqrt{
\frac{g_t^2}
{\max\{u_t,\varepsilon^2\}}
},
\]
and the effective step is
\[
\eta_t
=
\frac{\alpha}{\max\{1,\mathrm{RMS}_t\}}.
\]

Now feed the deterministic impulse history
\[
g_1=G\ne0,
\qquad
g_t=0
\quad
(t\ge2).
\]
Define
\[
c_j(t)
=
\frac{(1-\beta_j)\beta_j^{t-1}}
{1-\beta_j^t}.
\]
Then, exactly,
\[
\boxed{
v_t=c_1(t)G,
\qquad
u_t=c_2(t)G^2.
}
\]

For every
\[
t\ge2,
\]
the current gradient is zero, so
\[
\boxed{
\mathrm{RMS}_t=0
}
\]
and StableAdamW applies no clipping:
\[
\boxed{
\eta_t=\alpha.
}
\]

The magnitude of the normalized momentum part of the parameter update is therefore
\[
|\Delta\theta_t|
=
\alpha
\frac{c_1(t)|G|}
{\sqrt{c_2(t)}|G|+\varepsilon}.
\]
For fixed \(t\), this expression increases with \(|G|\), and its supremum over finite impulse amplitudes is
\[
\alpha R_t,
\]
where
\[
\boxed{
R_t
=
\frac{1-\beta_1}{\sqrt{1-\beta_2}}
\frac{\sqrt{1-\beta_2^t}}{1-\beta_1^t}
\left(
\frac{\beta_1}{\sqrt{\beta_2}}
\right)^{t-1}.
}
\]

Hence the impulse-tail update family is uniformly bounded exactly on one side of a sharp moment-decay frontier:
\[
\boxed{
\sup_{G\ne0,\ t\ge2}
\frac{|\Delta\theta_t|}{\alpha}
<\infty
\quad\Longleftrightarrow\quad
\beta_1^2\le\beta_2.
}
\]

If
\[
\beta_1^2>\beta_2,
\]
then
\[
R_t
\sim
\frac{1-\beta_1}{\sqrt{1-\beta_2}}
\left(
\frac{\beta_1}{\sqrt{\beta_2}}
\right)^{t-1},
\]
so
\[
R_t\to\infty.
\]
Consequently, for every prescribed
\[
M>0,
\]
there are a finite time \(t\) and finite impulse magnitude \(|G|\) such that
\[
g_t=0,
\qquad
\mathrm{RMS}_t=0,
\qquad
|\Delta\theta_t|>M\alpha.
\]

At the exact boundary
\[
\beta_1^2=\beta_2,
\]
the large-impulse envelope has the finite limit
\[
\boxed{
R_t
\longrightarrow
\sqrt{
\frac{1-\beta_1}{1+\beta_1}
}.
}
\]

The source explicitly reports trying the alternative numerator \(v_t^2\) in the RMS detector and finding worse empirical performance. That rejected detector has a useful exact mathematical contrast. Define
\[
\mathrm{RMS}^{(v)}_t
=
\frac{|v_t|}
{\sqrt{\max\{u_t,\varepsilon^2\}}}.
\]
If the effective step is divided by
\[
\max\{1,\mathrm{RMS}^{(v)}_t\},
\]
then for every scalar state,
\[
\boxed{
\frac{\alpha}{\max\{1,\mathrm{RMS}^{(v)}_t\}}
\frac{|v_t|}{\sqrt{u_t}+\varepsilon}
\le
\alpha.
}
\]
Thus the alternative detector closes this scalar stale-momentum amplitude channel exactly, even though the defining paper reports that it performed worse in experiments.

The defining paper's standard choices remain on the bounded side. For example,
\[
\beta_1=0.9
\]
has
\[
\beta_1^2=0.81,
\]
below the paper's examined second-moment values
\[
0.9,\ 0.95,\ 0.98,\ 0.99.
\]
The result is therefore a sharp design boundary, not a claim that the source hyperparameters exhibit the unbounded impulse family.

## Assumptions and scope

The theorem concerns one scalar coordinate, or equivalently a one-coordinate tensor, of source-form StableAdamW.

Weight decay is set to zero so that the statement isolates the adaptive momentum update. Adding decoupled weight decay contributes a separate parameter-proportional term.

The base learning rate is constant. A bounded time-varying schedule simply multiplies the displayed tail law by its current base rate and does not alter the moment-ratio boundary itself.

The gradient sequence is an externally prescribed deterministic impulse. It is an optimizer input-response stress test, not a claim that a smooth fixed objective naturally generates an arbitrarily large single gradient followed by exact zeros.

The numerical floor is strictly positive. Unboundedness is over the family of finite impulse amplitudes and times; for any single fixed finite \(G\), the positive \(\varepsilon\) eventually dominates and the tail update decays to zero.

The statement does not claim that the source's tested hyperparameters are unstable. They satisfy
\[
\beta_1^2<\beta_2.
\]

## Proof

At the impulse step,
\[
\widehat\beta_{j,1}=0,
\]
so
\[
v_1=G,
\qquad
u_1=G^2.
\]

For every later time the input vanishes. Therefore
\[
v_t
=
G
\prod_{k=2}^{t}
\widehat\beta_{1,k}.
\]
The product telescopes:
\[
\prod_{k=2}^{t}
\beta_1
\frac{1-\beta_1^{k-1}}
{1-\beta_1^k}
=
\beta_1^{t-1}
\frac{1-\beta_1}
{1-\beta_1^t}.
\]
Thus
\[
v_t=c_1(t)G.
\]
The same argument for the squared-gradient state gives
\[
u_t=c_2(t)G^2.
\]

Because
\[
g_t=0
\]
for all
\[
t\ge2,
\]
both the ideal source statistic
\[
\sqrt{g_t^2/u_t}
\]
and the implementation-safe statistic
\[
\sqrt{
g_t^2/\max\{u_t,\varepsilon^2\}
}
\]
are exactly zero. Hence clipping is inactive.

The parameter denominator then gives
\[
|\Delta\theta_t|
=
\alpha
\frac{c_1(t)|G|}
{\sqrt{c_2(t)}|G|+\varepsilon}.
\]
For fixed positive coefficients this is strictly increasing in \(|G|\). Taking the supremum as
\[
|G|\to\infty
\]
gives
\[
R_t
=
\frac{c_1(t)}{\sqrt{c_2(t)}},
\]
which simplifies to the displayed formula.

If
\[
\beta_1/\sqrt{\beta_2}>1,
\]
the remaining prefactor converges to the positive constant
\[
(1-\beta_1)/\sqrt{1-\beta_2},
\]
so
\[
R_t\to\infty.
\]
For any target \(M\), choose \(t\) so that \(R_t>M\), then choose a sufficiently large but finite \(|G|\) so that the finite-\(\varepsilon\) ratio still exceeds \(M\).

If
\[
\beta_1/\sqrt{\beta_2}\le1,
\]
then
\[
R_t
\le
\frac{1}{\sqrt{1-\beta_2}}
\left(
\frac{\beta_1}{\sqrt{\beta_2}}
\right)^{t-1}
\le
\frac{1}{\sqrt{1-\beta_2}},
\]
where we used
\[
1-\beta_1^t\ge1-\beta_1
\]
and
\[
\sqrt{1-\beta_2^t}\le1.
\]
So the family is uniformly bounded. This proves the if-and-only-if frontier.

At
\[
\beta_2=\beta_1^2,
\]
the exponential ratio equals one and the remaining factors converge to
\[
\frac{1-\beta_1}{\sqrt{1-\beta_1^2}}
=
\sqrt{
\frac{1-\beta_1}{1+\beta_1}
}.
\]

For the alternative \(v_t^2\) detector, set
\[
D_t=\sqrt{\max\{u_t,\varepsilon^2\}}.
\]
If
\[
|v_t|\le D_t,
\]
then clipping is inactive but
\[
\frac{|v_t|}{\sqrt{u_t}+\varepsilon}
\le
\frac{|v_t|}{D_t}
\le1.
\]
If
\[
|v_t|>D_t,
\]
clipping multiplies the base step by
\[
D_t/|v_t|,
\]
and the normalized update becomes
\[
\alpha
\frac{D_t}{\sqrt{u_t}+\varepsilon}
\le
\alpha.
\]
This proves the exact scalar cap.

## Verification

The accompanying `verify.py` reconstructs Algorithm 2 using the source bias-corrected recurrence.

It checks the closed impulse formulas against direct iteration for randomized \(\beta_1,\beta_2,G\), verifies that the source RMS statistic is exactly zero on every zero-gradient tail step, tests bounded and unbounded sides of the sharp frontier, and checks the exact boundary limit.

It also implements the source-discussed \(v_t^2\)-numerator alternative and verifies its scalar \(\alpha\)-cap over randomized states.

The finite computations are transcription guards. The arbitrary-time and arbitrary-amplitude statements are proved symbolically above.

## Relationship to prior work

Wortsman and coauthors introduce StableAdamW specifically to address loss spikes caused by an out-of-date AdamW second-moment estimator. Their Algorithm 2 computes
\[
\mathrm{RMS}_t
=
\sqrt{\mathbb E[g_t^2/u_t]}
\]
per tensor and divides the base learning rate by
\[
\max\{1,\mathrm{RMS}_t\}.
\]
Their implementation replaces the denominator in that detector by
\[
\max\{u_t,\varepsilon^2\}.
\]
The paper also explicitly asks why the detector uses the current squared gradient rather than squared momentum, reports trying \(v_t^2\), and says that choice performed worse.

Those statements provide both the mechanism and direct motivation for the present stress test, but the inspected paper does not state the zero-gradient clipping bypass, the exact impulse response, or the sharp
\[
\beta_1^2=\beta_2
\]
boundary for uniform tail amplitude.

The boundary is mathematically related to classical Adam analysis. In the proof of Reddi, Kale, and Kumar, controlling first momentum by the square-root second moment produces a denominator involving
\[
\beta_2-\beta_1^2.
\]
Thus the importance of
\[
\beta_1^2<\beta_2
\]
for ordinary Adam moment coupling is prior knowledge and is not claimed as new by itself.

What is additional here is the StableAdamW-specific implication: its **current-gradient** RMS gate is exactly inactive throughout the zero-gradient tail, so it does not repair that moment-ratio channel; moreover, the alternative momentum-numerator detector that the source says it tested would cap the scalar normalized momentum update exactly.

Focused searches for StableAdamW zero-gradient tails, stale momentum, impulse responses, clipping blind spots, and equivalent moment-ratio formulations did not identify a published statement with this combined result.

## Limitations

This is an optimizer input-response theorem, not a fixed-objective convergence or divergence theorem.

The exact amplitude classification is scalar. For a multi-coordinate tensor, the source clip averages the detector over coordinates, so cross-coordinate effects require a separate analysis.

The unbounded side concerns a family of larger finite impulses as the observation time grows. A fixed finite impulse decays eventually because the positive numerical floor dominates.

The source's reported settings lie on the bounded side of the frontier.

The theorem does not argue that the momentum-numerator detector should replace the published detector in practice; the defining paper reports that the momentum-numerator version performed worse empirically.

## References

1. Mitchell Wortsman, Tim Dettmers, Luke Zettlemoyer, Ari Morcos, Ali Farhadi, and Ludwig Schmidt, “Stable and low-precision training for large-scale vision-language models,” arXiv:2304.13013v1, first submitted 2023-04-25; NeurIPS 2023.
2. Sashank J. Reddi, Satyen Kale, and Sanjiv Kumar, “On the Convergence of Adam and Beyond,” arXiv:1904.09237v1.
