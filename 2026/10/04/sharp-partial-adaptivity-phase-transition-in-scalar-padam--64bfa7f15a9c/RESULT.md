# Sharp partial-adaptivity phase transition in scalar Padam
## Finding

Padam interpolates between momentum SGD and fully adaptive AMSGrad through an exponent
\[
p\in[0,1/2]
\]
applied to a historical maximum of second-moment estimates. On the simplest deterministic quadratic, that exponent has an exact dynamical phase transition.

Consider
\[
f(x)=\frac{\lambda}{2}x^2,
\qquad
\lambda>0,
\]
and the zero-momentum, zero-smoothing boundary specialization
\[
\beta_1=\beta_2=0
\]
of the original Padam recurrence. Use a fixed learning rate
\[
\alpha>0
\]
and an adaptive exponent
\[
0<p\le\frac12.
\]
Then
\[
g_t=\lambda x_t,
\qquad
m_t=g_t,
\qquad
v_t=g_t^2,
\]
and the historical maximum is
\[
\widehat v_t
=
\max_{1\le j\le t}g_j^2.
\]
Therefore
\[
x_{t+1}
=
x_t
-
\alpha
\frac{g_t}{\widehat v_t^p}.
\]

Define
\[
M_t
=
\max_{1\le j\le t}|x_j|,
\qquad
a=\alpha\lambda^{1-2p},
\qquad
q_t=\frac{a}{M_t^{2p}}.
\]
The recurrence becomes exactly
\[
x_{t+1}
=
x_t(1-q_t).
\]

The critical radius is
\[
r_p
=
\left(\frac{a}{2}\right)^{1/(2p)}
=
\left(
\frac{\alpha\lambda^{1-2p}}{2}
\right)^{1/(2p)}.
\]

There is a sharp exponent transition at
\[
p=\frac14.
\]

If
\[
0<p\le\frac14
\]
and
\[
0<|x_1|<r_p,
\]
then
\[
q_1>2.
\]
Every iterate overshoots the origin and has strictly larger magnitude than its predecessor, so
\[
|x_t|=M_t.
\]
Moreover,
\[
q_{t+1}
=
\frac{q_t}{(q_t-1)^{2p}}.
\]
For every finite \(t\),
\[
q_t>2,
\]
and
\[
q_t\downarrow2.
\]
Consequently,
\[
M_t\uparrow r_p,
\]
the signs alternate forever, and the parity subsequences converge to opposite nonzero limits:
\[
x_{2j}\to \sigma r_p,
\qquad
x_{2j+1}\to-\sigma r_p
\]
for one sign
\[
\sigma\in\{-1,1\}.
\]
Thus Padam does not converge to the quadratic minimizer from these sufficiently small nonzero initializations. Instead it approaches the symmetric two-cycle
\[
\{-r_p,r_p\}.
\]

At the exact threshold
\[
|x_1|=r_p,
\]
one has
\[
q_1=2,
\]
and the symmetric two-cycle starts immediately.

If
\[
|x_1|>r_p,
\]
then
\[
q_1<2.
\]
The first update cannot create a new historical maximum, so \(M_t\) freezes at \(M_1\), \(q_t=q_1\), and
\[
x_{t+1}=(1-q_1)x_t.
\]
Hence
\[
x_t\to0
\]
geometrically.

The behavior changes qualitatively when
\[
\frac14<p\le\frac12.
\]
Starting from any state with
\[
q_1>2,
\]
the same overshoot recursion applies while \(q_t>2\):
\[
q_{t+1}
=
F_p(q_t),
\qquad
F_p(q)=\frac{q}{(q-1)^{2p}}.
\]
The sequence decreases while it remains above \(2\). It cannot remain above \(2\) forever, because the only possible limiting fixed point is \(2\), but
\[
F_p'(2)=1-4p<0.
\]
Therefore values just to the right of \(2\) are mapped strictly below \(2\). It follows that after finitely many overshoot steps,
\[
q_t\le2.
\]
At that point the historical maximum stops increasing. The recurrence becomes linear forever after. A strict crossing
\[
q_t<2
\]
gives geometric convergence to the minimizer; the exceptional exact hit
\[
q_t=2
\]
produces the symmetric two-cycle.

Therefore
\[
p=\frac14
\]
is the exact boundary between persistent small-initialization overshoot and finite self-stabilization for this Padam boundary model.

## Assumptions and scope

The theorem studies the exact Padam recurrence with
\[
\beta_1=\beta_2=0.
\]
This is a boundary specialization of the algorithmic formula, not a claim about the default hyperparameters used in experiments and not an application of the convergence theorem in the source paper.

The result uses a fixed learning rate. The convergence theory in the follow-up Padam analysis chooses learning rates as functions of the optimization horizon; the fixed-step two-cycle here therefore does not contradict those asymptotic stationarity guarantees.

No denominator epsilon is added, matching Algorithm 1 in the defining Padam paper.

The objective is deterministic and scalar. The result isolates the interaction between the maximum second-moment memory and the partial-adaptivity exponent. Momentum, stochastic gradients, smoothing with positive \(\beta_2\), and coordinate coupling require separate analyses.

## Proof

With
\[
\beta_1=\beta_2=0,
\]
Padam gives
\[
m_t=g_t,
\qquad
v_t=g_t^2,
\qquad
\widehat v_t=\max_{1\le j\le t}g_j^2.
\]
On
\[
g_t=\lambda x_t,
\]
this becomes
\[
\widehat v_t
=
\lambda^2M_t^2.
\]
Thus
\[
\begin{aligned}
x_{t+1}
&=
x_t
-
\alpha
\frac{\lambda x_t}
{(\lambda^2M_t^2)^p}\\
&=
x_t
\left(
1-
\frac{\alpha\lambda^{1-2p}}{M_t^{2p}}
\right)\\
&=
x_t(1-q_t).
\end{aligned}
\]

If
\[
q_t\le2,
\]
then
\[
|1-q_t|\le1,
\]
so
\[
|x_{t+1}|\le|x_t|\le M_t.
\]
Therefore no new maximum is created:
\[
M_{t+1}=M_t.
\]
Hence \(q_t\) remains constant thereafter and the system is exactly linear. If \(q_t<2\), its multiplier has magnitude strictly below one. If \(q_t=2\), its multiplier is \(-1\).

Now suppose
\[
q_t>2.
\]
Then
\[
|1-q_t|=q_t-1>1,
\]
so
\[
|x_{t+1}|=(q_t-1)|x_t|.
\]
If the trajectory has been in the overshoot regime up to time \(t\), then
\[
|x_t|=M_t,
\]
and therefore
\[
M_{t+1}=(q_t-1)M_t.
\]
Using
\[
q_t=\frac{a}{M_t^{2p}},
\]
one obtains
\[
q_{t+1}
=
\frac{a}{M_{t+1}^{2p}}
=
\frac{q_t}{(q_t-1)^{2p}}
=
F_p(q_t).
\]

For
\[
q>2,
\]
one has
\[
F_p(q)<q
\]
because
\[
(q-1)^{2p}>1.
\]

Assume first
\[
0<p\le\frac14.
\]
Then
\[
2p\le\frac12,
\]
and for \(q>2\),
\[
(q-1)^{2p}
\le
\sqrt{q-1}.
\]
Also
\[
q>2\sqrt{q-1},
\]
because
\[
q^2-4(q-1)=(q-2)^2>0.
\]
Hence
\[
F_p(q)
=
\frac{q}{(q-1)^{2p}}
\ge
\frac{q}{\sqrt{q-1}}
>2.
\]
Thus the interval \((2,\infty)\) is forward invariant. Starting from \(q_1>2\), the sequence decreases and remains above \(2\). Let its limit be \(L\ge2\). Passing to the continuous fixed-point equation
\[
L=F_p(L)
\]
gives
\[
(L-1)^{2p}=1,
\]
so
\[
L=2.
\]
Therefore
\[
q_t\downarrow2.
\]
Since
\[
M_t=\left(\frac{a}{q_t}\right)^{1/(2p)},
\]
one has
\[
M_t\uparrow
\left(\frac a2\right)^{1/(2p)}
=
r_p.
\]
Every overshoot changes sign, so the two parity subsequences approach opposite endpoints.

Now assume
\[
\frac14<p\le\frac12.
\]
While \(q_t>2\), the sequence decreases. If it never crossed below or onto \(2\), it would again have to converge to the only fixed point \(2\). But
\[
F_p'(2)=1-4p<0.
\]
By continuity, there exists a right neighborhood of \(2\) on which
\[
F_p(q)<2.
\]
A decreasing sequence converging to \(2\) would eventually enter that neighborhood and cross below \(2\), a contradiction. Hence a finite crossing
\[
q_t\le2
\]
must occur.

This proves the phase transition and all stated cases.

## Verification

The accompanying `verify.py` checks the exact reduction from Padam to the scalar max-memory recurrence, the overshoot map, the invariant-above-two property for representative exponents at and below the critical value, finite crossing above the critical value, and the limiting critical radius.

The script also directly simulates the original specialized Padam recurrence and checks agreement with the reduced recurrence. Numerical experiments are not used to prove the infinite-time dichotomy; the exact inequalities and fixed-point argument above establish it.

## Relationship to prior work

Chen, Liu, Sun, and Hong introduced Padam as a partially adaptive method interpolating between momentum SGD and AMSGrad. Their Algorithm 1 uses
\[
\widehat v_t=\max\{\widehat v_{t-1},v_t\}
\]
and divides the momentum by
\[
\widehat v_t^p.
\]
They emphasize
\[
p\in[0,1/2],
\]
note that \(p=1/2\) recovers AMSGrad, and use values such as \(p=1/8\) in experiments. The inspected source does not analyze the exact deterministic scalar max-memory recurrence or a small-initialization two-cycle.

A follow-up convergence analysis by Zhou et al. proves nonconvex stationarity guarantees for Padam and highlights
\[
p\in[0,1/4]
\]
as a favorable theoretical range under sparse gradients. Its prescribed learning rates depend on the optimization horizon. The inspected text does not give a fixed-step scalar phase transition at \(p=1/4\).

The exponent \(1/4\) therefore appears in both the existing convergence literature and the exact scalar dynamics here for different mathematical reasons. In the present recurrence it is the sharp boundary where the overshoot map
\[
q\mapsto\frac{q}{(q-1)^{2p}}
\]
changes local orientation at the fixed point \(q=2\).

## Limitations

The theorem is deliberately a boundary-model diagnosis. Positive momentum and positive second-moment smoothing can alter the dynamics substantially.

The exact persistent two-cycle result assumes a fixed learning rate and no denominator epsilon. Adding either time decay or epsilon changes the scalar recurrence.

For
\[
p>\frac14,
\]
the theorem allows isolated resonant initial conditions that land exactly at \(q=2\) and therefore enter an exact two-cycle. The generic finite-crossing case is strict and converges geometrically after the historical maximum freezes.

The theorem does not claim practical nonconvergence of the default Padam training recipe. Its value is to isolate a sharp mechanism created by partial normalization plus historical maxima.

## References

1. Jinghui Chen, Dongruo Zhou, Yiqi Tang, Ziyan Yang, Yuan Cao, and Quanquan Gu, “Closing the Generalization Gap of Adaptive Gradient Methods in Training Deep Neural Networks,” arXiv:1806.06763v1, 2018.
2. Dongruo Zhou, Jinghui Chen, Yuan Cao, Yiqi Tang, Ziyan Yang, and Quanquan Gu, “On the Convergence of Adaptive Gradient Methods for Nonconvex Optimization,” arXiv:1808.05671v1, 2018.
