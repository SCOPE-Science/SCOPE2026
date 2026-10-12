# Two-task CAGrad has sharp common-descent and equalization thresholds
## Finding

For two tasks, CAGrad solves
\[
\max_d\min\{\langle g_1,d\rangle,\langle g_2,d\rangle\}
\quad\text{subject to}\quad
\lVert d-g_0\rVert\le c\lVert g_0\rVert,
\qquad
g_0=\frac{g_1+g_2}{2}.
\]

Assume
\[
a=\lVert g_1\rVert>b=\lVert g_2\rVert>0,
\qquad
\rho=\frac{\langle g_1,g_2\rangle}{ab},
\qquad
-1<\rho<-\frac ba.
\]
The last condition means the average gradient harms task \(2\):
\[
\langle g_2,g_0\rangle=\frac b2(b+a\rho)<0.
\]

Let
\[
G=\sqrt{a^2+b^2+2ab\rho}=2\lVert g_0\rVert.
\]
Define
\[
c_{\rm cd}=-\frac{b+a\rho}{G},
\qquad
c_{\rm bal}=\frac{a^2-b^2}{G(b-a\rho)}.
\]
Then
\[
0<c_{\rm cd}<c_{\rm bal},
\qquad
c_{\rm cd}<1.
\]

For
\[
0\le c<c_{\rm bal},
\]
the unique optimizer is
\[
\boxed{
d^*=g_0+c\lVert g_0\rVert\frac{g_2}{b}
}
\]
and the weaker task controls the minimax value:
\[
\boxed{
\min_i\langle g_i,d^*\rangle
=
\langle g_2,d^*\rangle
=
\frac b2(b+a\rho+cG)
}.
\]
Therefore CAGrad still harms task \(2\) when
\[
c<c_{\rm cd},
\]
is first-order neutral for task \(2\) at
\[
c=c_{\rm cd},
\]
and is strict common descent for
\[
c>c_{\rm cd}.
\]

The balancing transition occurs later. Put
\[
\delta=\frac{g_1-g_2}{2},
\qquad
h=g_0-\frac{\langle\delta,g_0\rangle}{\lVert\delta\rVert^2}\delta,
\]
\[
e=\frac{|\langle\delta,g_0\rangle|}{\lVert\delta\rVert},
\qquad
s=\lVert h\rVert,
\qquad
R=c\lVert g_0\rVert.
\]
For
\[
c\ge c_{\rm bal},
\]
the optimizer is
\[
\boxed{
d^*
=
\left(
1+\frac{\sqrt{R^2-e^2}}{s}
\right)h
}
\]
and
\[
\boxed{
\langle g_1,d^*\rangle
=
\langle g_2,d^*\rangle
=
s^2+s\sqrt{R^2-e^2}>0
}.
\]

Thus “stop harming the weaker task” and “equalize taskwise progress” are different CAGrad events.

Writing
\[
q=\frac ba,
\]
the equalization threshold lies inside the source convergence range precisely when
\[
\boxed{
c_{\rm bal}<1
\iff
\rho<\frac{3q^2-1}{2q}
}.
\]
In particular,
\[
\boxed{
q\le\frac13
\Longrightarrow
c_{\rm bal}\ge1
}
\]
for every non-antiparallel harmful pair. In that regime CAGrad can restore common descent with a convergence-safe parameter, but cannot exactly equalize the two first-order task improvements while keeping
\[
c<1.
\]

There is also a symmetric limit. If
\[
a=b,
\qquad
-1<\rho<1,
\]
then
\[
\boxed{
d^*=(1+c)g_0
}
\]
for every
\[
0\le c<1.
\]
Hence equal-norm two-task CAGrad never rotates the mean direction; it only rescales it.

## Assumptions and scope

The statement is pointwise and first-order. It classifies one CAGrad direction, not a complete nonlinear training trajectory.

The unequal-norm phase diagram is restricted to the regime where the average gradient is harmful to the weaker task.

The gradients are noncollinear. Exact antiparallelity is excluded because the average-gradient ball can degenerate.

“Convergence-safe” means the source range
\[
0\le c<1
\]
under which its smooth average-loss convergence theorem applies.

## Proof

Write
\[
g_1=g_0+\delta,
\qquad
g_2=g_0-\delta.
\]
Then
\[
\min\{\langle g_1,d\rangle,\langle g_2,d\rangle\}
=
\langle g_0,d\rangle-|\langle\delta,d\rangle|.
\]

Because
\[
\langle\delta,g_0\rangle=\frac{a^2-b^2}{4}>0,
\]
task \(2\) is the active branch initially. Maximizing its linear functional over the radius-\(R\) ball gives
\[
d^*=g_0+R\frac{g_2}{b}.
\]
Along this branch,
\[
\langle\delta,d^*\rangle
=
\frac{a^2-b^2}{4}
+
\frac{R}{2}(a\rho-b).
\]
It reaches zero exactly at
\[
c=c_{\rm bal}.
\]
The worst progress on the same branch is
\[
\langle g_2,d^*\rangle
=
\frac b2(b+a\rho+cG),
\]
whose zero is exactly
\[
c=c_{\rm cd}.
\]

The ordering follows because
\[
c_{\rm cd}<c_{\rm bal}
\iff
a^2\rho^2-b^2<a^2-b^2
\iff
\rho^2<1.
\]
Also
\[
G^2-(b+a\rho)^2=a^2(1-\rho^2)>0,
\]
so
\[
c_{\rm cd}<1.
\]

After the branch reaches
\[
\langle\delta,d\rangle=0,
\]
both taskwise progress values are equal. On that hyperplane the objective is
\[
\langle g_0,d\rangle.
\]
The projection of the ball center onto the hyperplane is \(h\); the ball-hyperplane intersection has radius
\[
\sqrt{R^2-e^2}.
\]
Moving from \(h\) in the direction \(h/\lVert h\rVert\) maximizes the remaining linear objective, proving the equalized formula.

For the safe-range criterion, direct expansion gives
\[
(1+q^2+2q\rho)(q-\rho)^2-(1-q^2)^2
=
(\rho^2-1)(1+2q\rho-3q^2).
\]
Since
\[
\rho^2-1<0,
\]
one obtains
\[
c_{\rm bal}<1
\iff
1+2q\rho-3q^2<0.
\]
When
\[
q\le1/3,
\]
the required right-hand threshold is at most \(-1\), so no non-antiparallel pair can meet it.

If
\[
a=b,
\]
then
\[
\delta\perp g_0.
\]
For
\[
d=g_0+u,
\qquad
\lVert u\rVert\le c\lVert g_0\rVert,
\]
the objective equals
\[
\lVert g_0\rVert^2+\langle g_0,u\rangle-|\langle\delta,u\rangle|,
\]
which is uniquely maximized by
\[
u=cg_0.
\]

## Verification

The accompanying `verify.py` compares the formulas with the exact scalar CAGrad dual. It checks random harmful configurations, the common-descent crossing, the equal-progress phase, the one-third obstruction, and the equal-norm specialization.

The numerical work is only a transcription guard. The thresholds and branch formulas are proved above.

## Relationship to prior work

Liu, Liu, Jin, Stone, and Liu define CAGrad by the ball-constrained worst-task improvement problem, derive its simplex dual, visualize a two-task case, and prove convergence toward a stationary point of the average loss for
\[
c<1.
\]
The inspected defining full text does not state a closed two-task phase diagram, a sharp parameter where a harmful weaker task first becomes nonharmful, or a separate exact-equalization threshold.

Later direction-oriented multi-objective work develops related neighborhood-regularized formulations. A later two-objective alignment method uses a clipped weighted CAGrad variant. The inspected material from these works does not state the vanilla unweighted thresholds above.

Focused published-record searches for CAGrad common-descent thresholds, equal-progress thresholds, norm-ratio barriers, and equal-norm directional behavior did not identify an implication-equivalent result.

## Limitations

The theorem does not control finite-step nonlinear loss changes at arbitrary learning rates.

The one-third barrier concerns exact equality of first-order progress, not the existence of a common descent direction.

The full two-task geometry when the average gradient already helps both tasks is not classified here.

Clipped and weighted CAGrad variants are outside the claim.

## References

1. Bo Liu, Xingchao Liu, Xiaojie Jin, Peter Stone, and Qiang Liu, “Conflict-Averse Gradient Descent for Multi-task Learning,” arXiv:2110.14048v1, first submitted 2021-10-26; NeurIPS 2021.
2. Peiyao Xiao, Hao Ban, and Kaiyi Ji, “Direction-oriented Multi-objective Learning: Simple and Provable Stochastic Algorithms,” arXiv:2305.18409, 2023.
3. “Reward-free Alignment for Conflicting Objectives,” arXiv:2602.02495, 2026.
