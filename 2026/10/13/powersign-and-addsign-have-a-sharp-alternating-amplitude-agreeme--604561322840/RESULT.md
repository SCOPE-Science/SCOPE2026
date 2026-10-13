# PowerSign and AddSign have a sharp alternating-amplitude agreement window
## Finding

PowerSign and AddSign use the sign product between the current gradient and an exponential moving average of past gradients as a binary agreement signal. On a persistent sign-alternating input, that signal has an exact amplitude-ratio phase diagram.

Let
\[
m_t=\beta m_{t-1}+(1-\beta)g_t,
\qquad
m_0=0,
\qquad
0<\beta<1,
\]
and let
\[
g_{2n-1}=A>0,
\qquad
g_{2n}=-B<0.
\]
Write
\[
r=\frac AB.
\]

Then
\[
m_{2n}
=
\frac{\beta A-B}{1+\beta}
\left(1-\beta^{2n}\right)
\]
and
\[
m_{2n-1}
=
\frac{A-\beta B}{1+\beta}
-
\frac{\beta A-B}{1+\beta}
\beta^{2n-1}.
\]

These identities give a complete sign classification.

If
\[
\beta\le r<\frac1\beta,
\]
then
\[
\operatorname{sign}(m_t)
=
\operatorname{sign}(g_t)
\]
for every finite step. Thus the current gradient and its EMA are classified as agreeing even though the gradient reverses sign at every iteration.

At the upper boundary
\[
r=\frac1\beta,
\]
every even EMA is exactly zero.

If
\[
r>\frac1\beta,
\]
every odd step agrees while every even step disagrees.

If
\[
0<r<\beta,
\]
every even step agrees. The odd steps begin in agreement and switch exactly once to disagreement. The first strictly disagreeing odd step is
\[
2N-1,
\]
where
\[
N
=
\left\lfloor
\frac{
1+
\log\!\left((\beta-r)/(1-\beta r)\right)/\log\beta
}{2}
\right\rfloor
+1.
\]

For the base source rules,
\[
\mathrm{PowerSign}:
\quad
e^{\operatorname{sign}(g_t)\operatorname{sign}(m_t)}g_t,
\]
and
\[
\mathrm{AddSign}:
\quad
\left(
1+
\operatorname{sign}(g_t)\operatorname{sign}(m_t)
\right)g_t.
\]
Hence agreement multiplies the current gradient by
\[
e
\]
for PowerSign and by
\[
2
\]
for AddSign, while disagreement multiplies it by
\[
e^{-1}
\]
and
\[
0,
\]
respectively.

Outside the central window, the larger-amplitude parity is the agreeing parity and the smaller-amplitude parity is suppressed asymptotically. Inside the window, both parities are amplified.

At the source decay
\[
\beta=0.9,
\]
the all-step agreement window is
\[
0.9
\le
\frac AB
<
\frac{10}{9}
=
1.111111\ldots.
\]
In particular, for the balanced Nyquist signal
\[
A=B,
\]
PowerSign and AddSign reduce exactly, at every step, to
\[
e\,g_t
\]
and
\[
2g_t,
\]
despite maximal sign alternation.

## Assumptions and scope

The result concerns one scalar coordinate and the base PowerSign and AddSign rules without internal time decay.

A positive bias-correction factor on the gradient EMA does not change any sign, so the phase diagram is unchanged whether the EMA is written in corrected or uncorrected magnitude form.

The source's sign convention at exact zero is taken as
\[
\operatorname{sign}(0)=0.
\]

The input is externally prescribed. The theorem is an input-response statement for the agreement primitive and does not claim that a fixed objective generates the alternating sequence.

## Proof

The even subsequence obeys
\[
m_{2n}
=
\beta^2m_{2n-2}
+
(1-\beta)(\beta A-B).
\]
Starting from
\[
m_0=0,
\]
solving this affine recurrence yields
\[
m_{2n}
=
\frac{\beta A-B}{1+\beta}
\left(1-\beta^{2n}\right).
\]

For odd steps,
\[
m_{2n-1}
=
\beta m_{2n-2}
+
(1-\beta)A.
\]
Substituting the even formula gives
\[
m_{2n-1}
=
\frac{A-\beta B}{1+\beta}
-
\frac{\beta A-B}{1+\beta}
\beta^{2n-1}.
\]

The even sign is therefore the sign of
\[
\beta A-B,
\]
except at equality, where every even EMA is zero.

For odd steps, if
\[
r\ge\beta,
\]
the displayed formula is positive for every finite \(n\). If
\[
0<r<\beta,
\]
the limiting odd EMA is negative but
\[
m_1=(1-\beta)A>0.
\]
The odd formula is strictly decreasing in \(n\), so it crosses zero at most once. Solving
\[
m_{2n-1}<0
\]
gives
\[
\beta^{2n-1}
<
\frac{\beta-r}{1-\beta r},
\]
which yields the stated first strictly disagreeing index.

Combining the odd and even signs proves the phase diagram. Substitution into the two source multipliers gives the exact amplification and suppression factors.

## Verification

The accompanying `verify.py` checks the two closed EMA formulas against direct recurrence replay over randomized parameters, verifies all three open sign regimes and both boundary cases, checks the finite odd-step switch index when \(r<\beta\), and confirms the source-default window.

The computations are transcription guards. The phase diagram and switch formula are proved algebraically above.

## Relationship to prior work

Bello, Zoph, Vasudevan, and Le introduced PowerSign and AddSign after finding the product
\[
\operatorname{sign}(g)\operatorname{sign}(m)
\]
repeatedly in automatically discovered optimizer expressions. The paper interprets this product as a binary signal for whether the current gradient and its running average agree on a coordinate.

The base rules use
\[
e^{\operatorname{sign}(g)\operatorname{sign}(m)}g
\]
and
\[
\left(1+\operatorname{sign}(g)\operatorname{sign}(m)\right)g,
\]
and the source experiments use a first-moment decay of
\[
0.9.
\]

The inspected full text gives the optimizer families, internal-decay variants, transfer experiments, and qualitative agreement interpretation. It does not state the exact two-level alternating phase diagram, the \(\beta\)-to-\(1/\beta\) all-step agreement window, or the finite switch index below that window.

Focused published-record searches for PowerSign or AddSign under alternating, periodic, and two-level gradients did not identify an implication-equivalent result.

## Limitations

The theorem isolates the sign-agreement gate rather than complete optimization dynamics.

The balanced alternating signal is a diagnostic input, not a claim about typical minibatch gradients.

Internal decay changes the multiplier magnitudes over time but not the sign-agreement classification derived here.

The result does not assert that amplification inside the central window is beneficial or harmful for a particular learning problem.

## References

1. Irwan Bello, Barret Zoph, Vijay Vasudevan, and Quoc V. Le, “Neural Optimizer Search with Reinforcement Learning,” Proceedings of the 34th International Conference on Machine Learning, PMLR 70:459–468, 2017.
2. Irwan Bello, Barret Zoph, Vijay Vasudevan, and Quoc V. Le, “Neural Optimizer Search with Reinforcement Learning,” arXiv:1709.07417v2, 2017.
