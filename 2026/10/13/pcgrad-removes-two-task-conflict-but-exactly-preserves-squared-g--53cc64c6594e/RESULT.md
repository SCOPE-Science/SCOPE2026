# PCGrad removes two-task conflict but exactly preserves squared gradient-norm imbalance
## Finding

PCGrad was introduced to remove pairwise gradient conflict in multi-task learning. For two tasks, its projection geometry has an exact consequence that separates directional conflict from gradient-magnitude imbalance.

Let two nonzero task gradients be
\[
g_1,g_2,
\]
and suppose they conflict:
\[
\rho
=
\frac{\langle g_1,g_2\rangle}{\|g_1\|\,\|g_2\|}
\in(-1,0).
\]
Write
\[
a=\|g_1\|,
\qquad
b=\|g_2\|.
\]

On the two-task conflicting branch, PCGrad replaces each task gradient by its projection onto the normal plane of the other and then sums the two projected gradients. Thus its aggregate direction is
\[
d_{\rm PC}
=
g_1+g_2
-
\frac{\langle g_1,g_2\rangle}{a^2}g_1
-
\frac{\langle g_1,g_2\rangle}{b^2}g_2.
\]

The directional derivative of each task along this aggregate is exactly
\[
\boxed{
\langle g_1,d_{\rm PC}\rangle
=
a^2(1-\rho^2)
}
\]
and
\[
\boxed{
\langle g_2,d_{\rm PC}\rangle
=
b^2(1-\rho^2)
}.
\]
Therefore, for every
\[
-1<\rho<0,
\]
the update direction
\[
-d_{\rm PC}
\]
is a strict common first-order descent direction for both tasks, regardless of the ratio
\[
a/b.
\]

More sharply, relative to each task's own steepest first-order progress, PCGrad applies exactly the same angular attenuation:
\[
\boxed{
\frac{\langle g_i,d_{\rm PC}\rangle}{\|g_i\|^2}
=
1-\rho^2
}
\qquad
(i=1,2).
\]
If
\[
\phi=\arccos\rho,
\]
this common attenuation is
\[
\sin^2\phi.
\]

Consequently the ratio of the two infinitesimal task decreases is independent of the conflict angle:
\[
\boxed{
\frac{\langle g_1,d_{\rm PC}\rangle}
{\langle g_2,d_{\rm PC}\rangle}
=
\left(\frac ab\right)^2
}.
\]
Thus PCGrad removes directional conflict but exactly preserves the squared gradient-norm imbalance in first-order task progress.

The aggregate norm is also explicit:
\[
\boxed{
\|d_{\rm PC}\|^2
=
(1-\rho^2)
\left(
a^2+b^2-2ab\rho
\right)
}.
\]
At exact antiparallelity,
\[
\rho=-1,
\]
both projected gradients vanish and
\[
d_{\rm PC}=0.
\]
For a near-antiparallel angle
\[
\phi=\pi-\varepsilon,
\]
normalized task progress obeys
\[
1-\rho^2
=
\sin^2\varepsilon
=
\varepsilon^2+O(\varepsilon^4).
\]
Hence PCGrad's common-descent guarantee degenerates quadratically as the two gradients approach exact opposition.

There is a complementary sharp comparison with ordinary scalarization. Let
\[
d_{\rm sum}=g_1+g_2.
\]
Then
\[
\langle g_1,d_{\rm sum}\rangle
=
a(a+b\rho)
\]
and
\[
\langle g_2,d_{\rm sum}\rangle
=
b(b+a\rho).
\]
Writing
\[
r=\frac ab,
\]
the raw sum is a strict common first-order descent direction exactly when
\[
\boxed{
-\rho<r<-\frac1\rho
}.
\]
At either boundary one task has zero first-order progress. Outside the interval, the task with the smaller gradient norm is harmed to first order by the raw sum.

PCGrad therefore has an exact two-part effect: it extends strict common descent from this finite amplitude-ratio window to every positive norm ratio whenever the gradients are not exactly antiparallel, but it does not equalize first-order task progress. The original squared norm disparity survives unchanged.

## Assumptions and scope

The result concerns exactly two differentiable task losses evaluated at the same parameter vector.

The analysis applies to PCGrad's conflicting branch,
\[
\langle g_1,g_2\rangle<0.
\]
For nonconflicting gradients PCGrad leaves the pair unchanged.

The theorem is first-order. If the parameter update is
\[
\theta^+
=
\theta-\eta d_{\rm PC},
\]
then for differentiable task losses
\[
L_i(\theta^+)
=
L_i(\theta)
-
\eta\|g_i\|^2(1-\rho^2)
+
o(\eta).
\]
No finite-step decrease is asserted without smoothness and step-size assumptions.

The two-task case has no projection-order ambiguity because each gradient has only one other task gradient against which it can be projected.

The claim does not say that PCGrad fails to improve training. It isolates what the projection step does and does not change in local two-task geometry.

## Proof

Let
\[
c=\langle g_1,g_2\rangle=ab\rho.
\]
The two projected gradients are
\[
\widetilde g_1
=
g_1-
\frac{c}{b^2}g_2
\]
and
\[
\widetilde g_2
=
g_2-
\frac{c}{a^2}g_1.
\]
By construction,
\[
\langle g_2,\widetilde g_1\rangle=0
\]
and
\[
\langle g_1,\widetilde g_2\rangle=0.
\]
Because
\[
d_{\rm PC}=\widetilde g_1+\widetilde g_2,
\]
we obtain
\[
\langle g_1,d_{\rm PC}\rangle
=
\langle g_1,\widetilde g_1\rangle
=
a^2-
\frac{c^2}{b^2}
=
a^2(1-\rho^2),
\]
and symmetrically
\[
\langle g_2,d_{\rm PC}\rangle
=
b^2(1-\rho^2).
\]
For
\[
-1<\rho<0,
\]
both quantities are strictly positive, so
\[
-d_{\rm PC}
\]
is a common first-order descent direction.

Dividing each identity by the corresponding squared gradient norm proves equal relative attenuation. Dividing the two identities proves the squared norm-ratio law.

For the aggregate norm,
\[
\|\widetilde g_1\|^2
=
a^2(1-\rho^2),
\qquad
\|\widetilde g_2\|^2
=
b^2(1-\rho^2),
\]
and direct expansion gives
\[
\langle\widetilde g_1,\widetilde g_2\rangle
=
-ab\rho(1-\rho^2).
\]
Therefore
\[
\|d_{\rm PC}\|^2
=
(1-\rho^2)
\left(
a^2+b^2-2ab\rho
\right).
\]
At
\[
\rho=-1,
\]
each gradient is a negative scalar multiple of the other, so both orthogonal projections are zero.

For the raw sum,
\[
\langle g_1,g_1+g_2\rangle
=
a^2+ab\rho
=
ab(r+\rho),
\]
which is positive exactly when
\[
r>-\rho.
\]
Similarly,
\[
\langle g_2,g_1+g_2\rangle
=
b^2+ab\rho
=
b^2(1+r\rho),
\]
which is positive exactly when
\[
r<-1/\rho
\]
because
\[
\rho<0.
\]
Combining the inequalities proves the sharp scalarization window.

## Verification

The accompanying `verify.py` constructs randomized conflicting vector pairs and compares the source PCGrad projection rule with all three exact identities.

It separately generates prescribed norm ratios and conflict cosines to test the raw-sum common-descent window, its two boundaries, the exact antiparallel null direction, and the quadratic near-antiparallel attenuation.

The finite computations are transcription guards. The identities and if-and-only-if window are proved algebraically above.

## Relationship to prior work

Yu and coauthors introduced PCGrad after identifying a three-part detrimental configuration involving conflicting gradient directions, gradient-magnitude disparity, and high curvature. Their algorithm projects a task gradient onto the normal plane of another task gradient when the pair conflicts, and their two-task analysis gives the explicit projected aggregate and convergence guarantees.

The source appendix contains aggregate factors proportional to
\[
1-\cos^2\phi
\]
and notes slow behavior near exact opposition. It does not state the taskwise identities above, the angle-independent squared gradient-norm ratio of task progress, or the exact amplitude-ratio window in which ordinary summation already gives common descent.

Javaloy and Valera later separate negative transfer into gradient-magnitude and gradient-direction effects and propose RotoGrad to address both. That distinction is consistent with the present exact calculation: PCGrad's two-task projection resolves directional conflict locally, but the first-order progress ratio remains exactly tied to the original gradient magnitudes.

Focused published-record searches for taskwise PCGrad progress, norm-ratio invariants, common-descent amplitude windows, and near-antiparallel slowdown did not locate an implication-equivalent statement.

## Limitations

The theorem is local and first-order.

It treats two tasks; with three or more tasks, PCGrad's sequential projections and randomized task order introduce additional geometry.

The squared progress ratio concerns directional derivatives, not normalized percentage loss reduction or long-horizon training performance.

Near antiparallel gradients produce arbitrarily small common first-order progress, so common descent alone does not imply a useful rate.

## References

1. Tianhe Yu, Saurabh Kumar, Abhishek Gupta, Sergey Levine, Karol Hausman, and Chelsea Finn, “Gradient Surgery for Multi-Task Learning,” arXiv:2001.06782v1, 2020; NeurIPS 2020.
2. Adrián Javaloy and Isabel Valera, “RotoGrad: Gradient Homogenization in Multitask Learning,” arXiv:2103.02631v1, 2021; ICLR 2022.
