# DEAM backtracking saves exactly one stale step after a full reversal
## Finding

DEAM chooses its momentum weight and a backtrack coefficient from the angle between the previous normalized momentum direction and the current gradient. At a full directional conflict, the source rule uses a fixed current-gradient weight and sends half of the previous parameter increment backward.

This mechanism has an exact scalar reversal latency.

Assume a long prehistory with constant gradient
\[
g=+G,
\qquad
G>0,
\]
so that immediately before the regime change
\[
m_0=G,
\qquad
\widehat v_0=G^2,
\qquad
\Delta_0=-\eta
\]
for a constant learning rate
\[
\eta>0.
\]
Now reverse the gradient permanently:
\[
g_n=-G,
\qquad
n=1,2,\ldots.
\]

As long as the previous momentum still points in the old direction, the discriminative angle is
\[
\theta=\pi.
\]
The source DEAM rules then give
\[
\beta=\frac1K,
\qquad
K=\frac{10(2+\pi)}{2\pi},
\qquad
d=-\frac12.
\]
Set
\[
a=1-\beta,
\qquad
x_n=\frac{m_n}{G},
\qquad
y_n=\frac{\Delta_n}{\eta}.
\]

Because the gradient magnitude remains \(G\), the running second-moment maximum remains
\[
\widehat v_n=G^2.
\]
During the full-opposition phase,
\[
\boxed{
x_n=2a^n-1
}
\]
and
\[
\boxed{
y_0=-1,
\qquad
y_n=-\frac12y_{n-1}-x_n.
}
\]

For the source value of \(K\),
\[
x_1,\ldots,x_5>0,
\qquad
x_6<0,
\]
while
\[
y_1,\ldots,y_4<0,
\qquad
y_5>0.
\]

The post-reversal desired descent direction is positive, because the new gradient is negative. Therefore:

\[
\boxed{
\text{DEAM makes exactly four stale parameter updates after the reversal.}
}
\]

The fifth parameter update already points in the new descent direction even though
\[
m_5>0,
\]
so the momentum itself is still stale.

If the backtrack term is suppressed while retaining the same angle-adaptive momentum,
\[
\Delta_n^{\rm no\;backtrack}
=
-\eta\frac{m_n}{G}.
\]
Since
\[
m_1,\ldots,m_5>0,
\qquad
m_6<0,
\]
the no-backtrack variant makes exactly five stale parameter updates.

Hence
\[
\boxed{
\text{the source }d=-1/2\text{ backtrack saves exactly one stale step.}
}
\]

The first reversed update is still stale:
\[
\frac{\Delta_1}{\eta}
=
2\beta-\frac12
\approx
-0.255594.
\]
So even a perfect \(180^\circ\) conflict signal does not reverse the parameter motion immediately.

## Assumptions and scope

The statement concerns one scalar coordinate under the source DEAM update rule.

The pre-reversal state is the steady state induced by a persistent constant gradient \(+G\). The post-reversal gradient is externally prescribed as the persistent equal-magnitude value \(-G\).

The learning rate is held constant over the short reversal window.

The result uses the source full-conflict branch
\[
\beta=1/K
\]
and
\[
d=-1/2.
\]
The small same-direction momentum-weight parameter does not enter until the stored momentum has changed sign.

The theorem is an exact filter-response statement for an abrupt gradient regime change, not a convergence theorem for a parameter-dependent gradient field.

## Proof

At full conflict, the source momentum recursion is
\[
m_n
=
(1-\beta)m_{n-1}
+
\beta(-G).
\]
With
\[
m_0=G
\]
and
\[
a=1-\beta,
\]
subtracting the fixed point \(-G\) gives
\[
m_n+G
=
a(m_{n-1}+G).
\]
Therefore
\[
m_n+G
=
2Ga^n,
\]
so
\[
x_n
=
\frac{m_n}{G}
=
2a^n-1.
\]

The equal gradient magnitude keeps the second-moment maximum equal to \(G^2\). Thus, while the angle remains \(\pi\),
\[
\Delta_n
=
-\frac12\Delta_{n-1}
-
\eta\frac{m_n}{G}.
\]
Dividing by \(\eta\) gives
\[
y_n
=
-\frac12y_{n-1}-x_n.
\]

The closed form is
\[
\boxed{
y_n
=
\frac23
-
\frac{2a^{n+1}}{a+1/2}
+
\frac{a-5/2}{3(a+1/2)}
\left(-\frac12\right)^n.
}
\]

For
\[
\beta
=
\frac{2\pi}{10(2+\pi)},
\]
the elementary enclosure
\[
3.14159<\pi<3.14160
\]
gives
\[
0.12220305<\beta<0.12220321.
\]
Interval evaluation of the exact recurrences yields
\[
0.04231730<x_5<0.04231821,
\]
\[
-0.08505721<x_6<-0.08505626,
\]
and
\[
-0.11437342<y_4<-0.11437207,
\]
\[
0.01486783<y_5<0.01486940.
\]
The earlier \(y_1,y_2,y_3\) are also strictly negative. Hence the update sign changes between steps four and five while the momentum sign changes between steps five and six.

Without backtracking, the normalized increment is simply
\[
-y_n^{\rm momentum}
=
-x_n,
\]
so its sign changes only when \(x_n\) does, between steps five and six.

## Verification

The accompanying `verify.py` reconstructs the exact scalar DEAM reversal recurrence using the source constant
\[
K=\frac{10(2+\pi)}{2\pi}.
\]

It checks the momentum and parameter-increment closed forms, verifies the four-versus-five stale-step counts, certifies the sign margins with the rational enclosure
\[
3.14159<\pi<3.14160,
\]
and confirms that the second-moment maximum remains constant under the equal-magnitude reversal.

The computation is a transcription guard. The latency result is proved from the recurrence above.

## Relationship to prior work

Bai, Ren, and Zhang introduce DEAM with an angle-adaptive momentum weight and a backtrack term. At a \(180^\circ\) conflict, their rule sets the backtrack coefficient to \(-1/2\). Their geometric explanation says this moves the parameter back toward the midpoint of the preceding update and helps correct zig-zag motion.

The inspected defining full text does not give a multi-step response law after a persistent gradient reversal, nor a count of how many parameter updates retain the stale direction.

The later journal version retains the same motivation: the discriminative angle configures momentum, while the backtrack term restricts redundant updates and provides an anticipatory correction. Its accessible text likewise does not state an exact reversal latency.

The present result isolates that intended correction mechanism under the strongest possible directional signal. It shows that the backtrack does help, but in a sharply quantifiable way: it advances the parameter sign reversal by exactly one step relative to the same adaptive-momentum rule without backtracking.

Focused published-record searches for DEAM gradient-reversal latency, permanent \(180^\circ\) conflict, alternating or reversed-gradient response, and exact backtrack timing did not identify an implication-equivalent result.

## Limitations

The post-reversal gradient is externally prescribed and constant.

The theorem uses equal pre- and post-reversal gradient magnitudes.

The result analyzes the source scalar recurrence and does not claim that every neural-network training trajectory will exhibit a four-step stale interval.

The source paper's broader convergence and empirical claims are not reassessed here.

## References

1. Jiyang Bai, Yuxiang Ren, and Jiawei Zhang, “DEAM: Adaptive Momentum with Discriminative Weight for Stochastic Optimization,” arXiv:1907.11307v1, first submitted 2019-07-25.
2. Jiyang Bai, Yuxiang Ren, and Jiawei Zhang, “Adaptive momentum with discriminative weight for neural network stochastic optimization,” International Journal of Intelligent Systems, 2022, DOI:10.1002/int.22854.
