# Yogi can rectify a balanced alternating gradient into linear drift
## Finding

Yogi was designed to control increases in effective learning rate by replacing the multiplicative second-moment update of Adam with an additive sign-controlled update. On a perfectly balanced alternating gradient, that additive rule can lock its denominator to the input phase and convert zero pairwise gradient sum into nonzero linear parameter drift.

Consider one coordinate of source-form Yogi Algorithm 2 with
\[
m_0=0,
\qquad
v_0=0,
\qquad
0<\beta_1,\beta_2<1,
\qquad
\eta>0,
\qquad
\varepsilon>0.
\]
Use
\[
\operatorname{sign}(0)=0
\]
and prescribe
\[
g_t=(-1)^{t-1}G,
\qquad
G>0.
\]
Thus every adjacent pair is exactly balanced:
\[
g_{2k-1}+g_{2k}=0.
\]

Yogi updates
\[
m_t=\beta_1m_{t-1}+(1-\beta_1)g_t,
\]
\[
v_t
=
v_{t-1}
-
(1-\beta_2)
\operatorname{sign}(v_{t-1}-g_t^2)g_t^2,
\]
and
\[
x_{t+1}
=
x_t
-
\eta
\frac{m_t}{\sqrt{v_t}+\varepsilon}.
\]

Put
\[
s=1-\beta_2,
\qquad
q=\frac1s,
\qquad
N=\lfloor q\rfloor.
\]
If
\[
q\notin\mathbb N,
\]
define
\[
L=NsG^2,
\qquad
U=(N+1)sG^2.
\]
Then
\[
L<G^2<U,
\]
and after the first threshold crossing the second moment enters the exact period-two orbit
\[
L,\ U,\ L,\ U,\ldots.
\]
More precisely,
\[
v_N=L,
\qquad
v_{N+1}=U,
\]
so \(U\) occurs on the parity of \(N+1\).

The first moment has the exact closed form
\[
\boxed{
m_t
=
p(-1)^{t-1}
\left[
1-(-\beta_1)^t
\right]
},
\qquad
p=
\frac{(1-\beta_1)G}{1+\beta_1}.
\]

Define
\[
\Delta
=
\frac1{\sqrt L+\varepsilon}
-
\frac1{\sqrt U+\varepsilon}
>0.
\]
The two asymptotic normalized updates in a gradient pair have unequal magnitudes because their denominators are phase locked. Their pair sum tends to
\[
(-1)^{N+1}p\Delta.
\]
Therefore the parameter satisfies
\[
\boxed{
\lim_{t\to\infty}
\frac{x_t}{t}
=
(-1)^N
\frac{\eta p\Delta}{2}
}
\]
and this limit is nonzero.

Hence a deterministic signal with exactly zero gradient sum on every adjacent pair produces systematic linear parameter motion.

There are two exact suppression mechanisms.

If
\[
q\in\mathbb N,
\]
then the additive second moment reaches
\[
v_t=G^2
\]
exactly after \(q\) steps and stays there. The two gradient parities then use the same denominator, so
\[
\boxed{
\lim_{t\to\infty}\frac{x_t}{t}=0
}.
\]

Likewise, if the diagnostic is instead initialized with
\[
v_0=G^2,
\]
then
\[
v_t=G^2
\]
for all \(t\), for every value of \(\beta_2\), and the linear drift again vanishes.

In ideal real arithmetic, the paper-reported values
\[
\beta_2\in\{0.9,0.99,0.999\}
\]
give
\[
q\in\{10,100,1000\},
\]
so they lie exactly on the no-drift resonance for this diagnostic.

## Assumptions and scope

The gradient sequence is externally prescribed. The theorem is an exact input-response statement for the optimizer recurrence, not a claim that a fixed objective generates this alternating sequence.

The result uses the un-debiased Algorithm 2 recurrence printed in the defining paper, with a constant learning rate.

The denominator is exactly the source form
\[
\sqrt{v_t}+\varepsilon.
\]

The arithmetic resonance statements are exact-real statements. Finite-precision representations and implementation-specific bias corrections may perturb the exact locking behavior.

The paper also recommends initializing the second moment from squared gradients evaluated on a reasonably large initial minibatch. The theorem isolates why matching the constant squared-gradient level removes the phase-locking drift on this diagnostic.

## Proof

Because
\[
g_t^2=G^2
\]
for every \(t\), the Yogi second moment is a one-dimensional bang-bang recurrence with step
\[
sG^2.
\]
Starting from zero, it increases by this amount until it first crosses \(G^2\).

If
\[
q=N\in\mathbb N,
\]
then
\[
v_N=NsG^2=G^2.
\]
The sign term is then zero, so \(v_t=G^2\) forever.

If
\[
q\notin\mathbb N,
\]
then
\[
v_N=NsG^2=L<G^2
\]
and the next update gives
\[
v_{N+1}=(N+1)sG^2=U>G^2.
\]
The following step subtracts exactly \(sG^2\), returning to \(L\). Hence the exact two-cycle follows by induction.

For the first moment, seek an alternating particular solution. With
\[
p=\frac{(1-\beta_1)G}{1+\beta_1},
\]
the exact solution satisfying \(m_0=0\) is
\[
m_t
=
p(-1)^{t-1}
\left[
1-(-\beta_1)^t
\right].
\]
Thus the odd and even first moments converge respectively to \(p\) and \(-p\).

In the nonresonant second-moment cycle, if \(N\) is even then odd times use \(U\) and even times use \(L\). If \(N\) is odd the assignment reverses. Consequently
\[
\frac{m_{2k-1}}{\sqrt{v_{2k-1}}+\varepsilon}
+
\frac{m_{2k}}{\sqrt{v_{2k}}+\varepsilon}
\longrightarrow
(-1)^{N+1}p\Delta.
\]
The transient error is a linear combination of powers of \(\beta_1\), hence is absolutely summable across pairs.

Each parameter pair changes by minus \(\eta\) times this normalized-update sum. Summing the constant limiting pair increment plus the absolutely summable transient gives
\[
x_t
=
(-1)^N
\frac{\eta p\Delta}{2}\,t
+
O(1),
\]
which proves the slope.

In either suppression case the denominator is eventually constant. The normalized pair sums then decay geometrically because only the first-moment transient remains. Their cumulative sum is bounded, so the linear slope is zero.

## Verification

The accompanying `verify.py` checks the exact first-moment formula, the resonant locking case, both parities of the nonresonant second-moment cycle, the predicted long-run parameter slope, and suppression by second-moment initialization at \(G^2\).

The finite computations are transcription guards. The period-two state and asymptotic drift are proved analytically above.

## Relationship to prior work

Zaheer, Reddi, Sachan, Kale, and Kumar introduce Yogi as an additive adaptive method intended to control growth of the effective learning rate. Their Algorithm 2 gives the sign-controlled second-moment recurrence used here and their discussion emphasizes that the increment magnitude depends only on the current squared gradient.

The source proves nonconvex stochastic convergence under its assumptions and discusses practical initialization. It specifically notes that zero second-moment initialization can create very large initial learning rates and proposes initializing the second moment from gradient squares on a reasonably large minibatch.

The inspected full text does not analyze alternating or periodic gradients, does not state a phase-locked two-cycle under a balanced input, and does not derive linear parameter drift under an exactly zero pairwise gradient sum.

Focused published-record searches for Yogi under alternating gradients, periodic inputs, zero-mean gradients, second-moment cycles, and linear drift did not identify an implication-equivalent result.

## Limitations

The input is a diagnostic sequence rather than a fixed-objective trajectory.

The result concerns one coordinate and the source recurrence without debiasing.

Exact resonance depends on exact arithmetic and on the zero initialization used in Algorithm 2.

The theorem identifies systematic drift but does not claim that the drift is harmful or beneficial for a particular stochastic optimization problem.

## References

1. Manzil Zaheer, Sashank J. Reddi, Devendra Sachan, Satyen Kale, and Sanjiv Kumar, “Adaptive Methods for Nonconvex Optimization,” Advances in Neural Information Processing Systems 31, 2018.
