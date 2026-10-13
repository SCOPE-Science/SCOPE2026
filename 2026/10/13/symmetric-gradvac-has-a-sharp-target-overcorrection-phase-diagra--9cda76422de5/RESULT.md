# Symmetric GradVac has a sharp target-overcorrection phase diagram
## Finding

Gradient Vaccine (GradVac) alters a task gradient so that its cosine similarity with another task's original gradient reaches a chosen target. When the same two-task correction is applied in both ordered directions, the two modified gradients do not in general have that requested cosine with each other.

Let
\[
g_1,g_2\ne0
\]
be noncollinear and let
\[
c
=
\frac{\langle g_1,g_2\rangle}
{\lVert g_1\rVert\lVert g_2\rVert}
\in(-1,1).
\]
Assume both ordered GradVac corrections are active with the same target
\[
\tau\in(c,1).
\]
Write
\[
\theta=\arccos c,
\qquad
\gamma=\arccos\tau,
\]
so
\[
0<\gamma<\theta<\pi.
\]

The source law-of-sines correction makes
\[
\cos(g_1',g_2)=\tau
\]
and symmetrically
\[
\cos(g_2',g_1)=\tau.
\]
However, the angle between the two modified gradients is
\[
\boxed{
|\theta-2\gamma|
}.
\]
Therefore their final mutual cosine is
\[
\boxed{
C(c,\tau)
=
\cos(\theta-2\gamma)
}
\]
or, entirely in cosine variables,
\[
\boxed{
C(c,\tau)
=
c(2\tau^2-1)
+
2\tau
\sqrt{(1-c^2)(1-\tau^2)}
}.
\]

This expression is independent of
\[
\lVert g_1\rVert
\quad\text{and}\quad
\lVert g_2\rVert.
\]

The final alignment has a sharp nonmonotone phase diagram. As the requested target \(\tau\) increases from the current cosine \(c\),

\[
C(c,\tau)
\]
increases strictly until
\[
\boxed{
\tau_\star
=
\cos\!\left(\frac{\theta}{2}\right)
=
\sqrt{\frac{1+c}{2}}
},
\]
where
\[
\boxed{
C(c,\tau_\star)=1
}.
\]
Thus the unique target that makes the two modified gradients exactly parallel is the cosine of the original half-angle.

For still larger targets,
\[
\tau>\tau_\star,
\]
the final mutual cosine decreases strictly. In the singular target limit,
\[
\tau\uparrow1,
\]
one has
\[
\boxed{
C(c,\tau)\longrightarrow c
}.
\]
Geometrically, each modified gradient approaches the other task's original direction, so the two directions are asymptotically swapped and their mutual angle returns to the original value.

There is also a sharp target-satisfaction threshold. Apart from the inactive boundary \(\tau=c\), the final mutual cosine equals the requested target only when
\[
\boxed{
\tau_{\rm eq}
=
\cos\!\left(\frac{\theta}{3}\right)
}.
\]
Hence
\[
\boxed{
c<\tau<\tau_{\rm eq}
\Longrightarrow
C(c,\tau)>\tau
}
\]
and
\[
\boxed{
\tau_{\rm eq}<\tau<1
\Longrightarrow
C(c,\tau)<\tau
}.
\]

Thus a stronger pairwise target does not monotonically increase the similarity of the two gradients that are ultimately aggregated. Beyond the bisector target, stronger vaccination reduces their final mutual alignment.

## Assumptions and scope

The claim concerns exactly two nonzero noncollinear task gradients.

Both ordered GradVac corrections are assumed active and use the same target cosine. This is the symmetric two-task case when both tasks are included in the GradVac set.

Each ordered correction uses the other task's original gradient, matching the source two-task construction and contemporary implementations.

The endpoint
\[
\tau=1
\]
is excluded because the source law-of-sines coefficient is singular there; only its limit is used.

The theorem is pointwise. It does not claim that the adaptive EMA target will always enter the decreasing branch during training, nor that such entry necessarily harms empirical performance.

## Proof

Choose coordinates in the plane spanned by the gradients. Put \(g_1\) on angle \(0\) and \(g_2\) on angle \(\theta\).

For one ordered GradVac correction, the source formula is equivalent to
\[
g_1'
=
g_1
+
\frac{\lVert g_1\rVert}{\lVert g_2\rVert}
\frac{\sin(\theta-\gamma)}{\sin\gamma}
g_2.
\]
By the source law-of-sines construction, \(g_1'\) lies between the original directions and has angle \(\gamma\) from \(g_2\). Its absolute direction is therefore
\[
\theta-\gamma.
\]

Applying the same rule in the reverse ordered pair gives \(g_2'\) at angle
\[
\gamma
\]
from \(g_1\). Consequently the final mutual angle is
\[
|(\theta-\gamma)-\gamma|
=
|\theta-2\gamma|.
\]
This proves
\[
C(c,\tau)=\cos(\theta-2\gamma).
\]

Using
\[
\cos\theta=c,
\quad
\cos\gamma=\tau,
\quad
\sin\theta=\sqrt{1-c^2},
\quad
\sin\gamma=\sqrt{1-\tau^2},
\]
and
\[
\cos(2\gamma)=2\tau^2-1,
\qquad
\sin(2\gamma)=2\tau\sqrt{1-\tau^2},
\]
gives the closed cosine formula.

As \(\tau\) increases, \(\gamma\) decreases strictly from \(\theta\) to \(0\). The final angle
\[
|\theta-2\gamma|
\]
therefore decreases strictly from \(\theta\) to \(0\) while
\[
\gamma>\theta/2,
\]
and then increases strictly from \(0\) back to \(\theta\) while
\[
\gamma<\theta/2.
\]
This proves the unique maximum at
\[
\gamma=\theta/2,
\]
equivalently
\[
\tau_\star=\cos(\theta/2).
\]

For exact target satisfaction, require
\[
|\theta-2\gamma|=\gamma.
\]
In the active range
\[
0<\gamma<\theta,
\]
the nontrivial solution is
\[
\gamma=\theta/3.
\]
The other solution
\[
\gamma=\theta
\]
is the inactive boundary \(\tau=c\). The sign comparisons on either side follow from the strict monotonicity of cosine on \([0,\pi]\).

## Verification

The accompanying `verify.py` generates random noncollinear gradient pairs with arbitrary norm ratios and random active targets. It reconstructs both source law-of-sines corrections and checks:

- each ordered corrected gradient has exactly the requested cosine with the other original gradient;
- the final modified-pair cosine equals the closed formula and is independent of norm ratio;
- the bisector target yields exact parallelism;
- the one-third-angle target is the unique nontrivial active target where final and requested cosines agree;
- targets above the bisector eventually reduce final mutual alignment.

The computations are transcription guards. The phase diagram is proved geometrically above.

## Relationship to prior work

Wang, Tsvetkov, Firat, and Cao introduce GradVac to set adaptive gradient-similarity goals. Their pairwise formula modifies one task gradient so that it reaches the requested cosine with another task's original gradient. They allow arbitrary pairwise targets and use EMA variables to set those targets.

The defining paper gives the one-sided law-of-sines derivation and a two-task convergence argument in which both task gradients are altered. It does not state the cosine between the two simultaneously modified gradients, the bisector target that makes them parallel, or the nonmonotone return toward the original cosine for extreme symmetric targets.

Contemporary GradVac implementations likewise process each task against original partner gradients and aggregate the modified task gradients. Their documentation describes the ordered-pair correction but does not state the final two-sided cosine phase diagram.

Focused searches of published records for symmetric GradVac, final modified-gradient cosine, target overshoot, target crossing, and bisector behavior did not identify an implication-equivalent result.

This theorem concerns the composition of two valid one-sided corrections. It does not contradict the source construction: each ordered correction individually reaches its stated target against the corresponding original partner gradient.

## Limitations

The result treats the symmetric two-task case. With more than two tasks, later pairwise corrections can change a task gradient repeatedly and order effects enter.

The target is held fixed during the single analyzed update. The EMA dynamics that generate targets over multiple training steps are outside scope.

The theorem characterizes gradient geometry rather than finite-step loss decrease or training convergence.

The target endpoint
\[
\tau=1
\]
is considered only as a limit.

## References

1. Zirui Wang, Yulia Tsvetkov, Orhan Firat, and Yuan Cao, “Gradient Vaccine: Investigating and Improving Multi-task Optimization in Massively Multilingual Models,” arXiv:2010.05874v1, first submitted 2020-10-12; ICLR 2021.
2. TorchJD documentation, “GradVac,” documenting ordered-pair correction against original partner gradients and aggregation of the modified task gradients.
