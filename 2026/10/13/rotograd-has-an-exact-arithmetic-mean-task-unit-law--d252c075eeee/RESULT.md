# RotoGrad has an exact arithmetic-mean task-unit law
## Finding

RotoGrad normalizes each task gradient before forming the shared backbone direction, but it chooses the common gradient magnitude from the unnormalized task-gradient norms. This creates an exact separation between directional scale invariance and dynamical loss-unit sensitivity.

Fix one RotoGrad state with nonzero current and initial feature-level task gradients
\[
G_k,
\qquad
G_k^0.
\]
Write
\[
U_k=\frac{G_k}{\lVert G_k\rVert_F},
\]
and let the normalized relative-convergence weights be
\[
\alpha_k
=
\frac{\lVert G_k\rVert_F/\lVert G_k^0\rVert_F}
{\sum_j\lVert G_j\rVert_F/\lVert G_j^0\rVert_F}.
\]
The source target magnitude is
\[
C
=
\sum_k\alpha_k\lVert G_k\rVert_F,
\]
and the displayed backbone update is proportional to
\[
C\sum_k U_k.
\]

Now rescale every task objective from the start of training by a fixed constant
\[
s_k>0.
\]
At a matched network and rotation state,
\[
G_k'=s_kG_k,
\qquad
(G_k^0)'=s_kG_k^0.
\]
Therefore
\[
\boxed{U_k'=U_k}
\]
and
\[
\boxed{\alpha_k'=\alpha_k}.
\]

Define
\[
p_k
=
\frac{\alpha_k\lVert G_k\rVert_F}{C}.
\]
Then
\[
p_k>0,
\qquad
\sum_kp_k=1,
\]
and the rescaled target magnitude is
\[
C'
=
\sum_k\alpha_k s_k\lVert G_k\rVert_F
=
C\sum_kp_ks_k.
\]
Hence
\[
\boxed{
\frac{C'}{C}
=
A_p(s)
:=
\sum_kp_ks_k
}.
\]

The backbone update therefore obeys
\[
\boxed{
C'\sum_kU_k'
=
A_p(s)\,
C\sum_kU_k
}.
\]
Its direction is exactly invariant under arbitrary positive independent task rescaling, while its magnitude changes by a weighted arithmetic mean satisfying
\[
\boxed{
\min_k s_k
\le
A_p(s)
\le
\max_k s_k.
}
\]

The other two update channels transform differently. The source head update uses
\[
\nabla_{\phi_k}L_k,
\]
so
\[
\boxed{
\nabla_{\phi_k}L_k'
=
s_k\nabla_{\phi_k}L_k.
}
\]

For direction homogenization, RotoGrad uses a normalized target
\[
V=\frac1K\sum_kU_k,
\]
which is unchanged by positive task rescaling. Its task-specific rotation loss is linear in the rotated feature gradient, and the algorithm treats that gradient as constant when differentiating with respect to the rotation. Therefore
\[
\boxed{
\nabla_{R_k}L_{{\rm roto},k}'
=
s_k
\nabla_{R_k}L_{{\rm roto},k}.
}
\]

Thus independent task-unit changes preserve the instantaneous backbone direction but multiply each task's head and rotation update speeds by its own scale factor. Whenever two corresponding update gradients are nonzero, their relative step-speed multiplier changes by exactly
\[
\boxed{\frac{s_i}{s_j}}.
\]

There is an exact global equivalence for common scaling. If
\[
s_k=s
\]
for every task and the displayed RotoGrad learning rates are changed to
\[
\eta'=\frac{\eta}{s},
\qquad
\eta_{\rm roto}'=\frac{\eta_{\rm roto}}{s},
\]
then the entire source-form discrete trajectory is unchanged: backbone parameters, task heads, rotations, normalized gradient directions, relative-convergence weights, and target directions all coincide step by step.

Conversely, if two tasks with nonzero head gradients have
\[
s_i\ne s_j,
\]
no single scalar change of the common network learning rate can reproduce both task-head updates at that state. Independent task scaling is therefore not dynamically equivalent to one global learning-rate change.

## Assumptions and scope

The theorem concerns the update equations displayed in the defining RotoGrad paper.

Each task is multiplied by a fixed positive scale from the start of training, so its initial gradient and every later gradient acquire the same factor.

All current and initial feature-level task gradients are nonzero, as required by the source normalization.

The exact full-trajectory equivalence uses the source first-order updates. The rotation statement also applies to a differentiable rotation parametrization because multiplying its scalar loss by \(s_k\) multiplies the parameter gradient by \(s_k\).

The independent-scale statement is pointwise at matched states. Differently scaled runs generally cease to be matched after an update because their task-specific learning speeds differ.

## Proof

Positive task rescaling gives
\[
G_k'=s_kG_k.
\]
Therefore
\[
U_k'
=
\frac{s_kG_k}{s_k\lVert G_k\rVert_F}
=
U_k.
\]

Because the same factor multiplies the initial gradient,
\[
\frac{\lVert G_k'\rVert_F}
{\lVert(G_k^0)'\rVert_F}
=
\frac{s_k\lVert G_k\rVert_F}
{s_k\lVert G_k^0\rVert_F}
=
\frac{\lVert G_k\rVert_F}
{\lVert G_k^0\rVert_F}.
\]
Thus every raw relative-convergence score, and hence every normalized \(\alpha_k\), is unchanged.

It follows that
\[
C'
=
\sum_k\alpha_ks_k\lVert G_k\rVert_F
=
C\sum_k
\frac{\alpha_k\lVert G_k\rVert_F}{C}s_k
=
A_p(s)C.
\]
The arithmetic-mean bounds follow because \(p\) is a probability vector.

For the rotation channel, the source target \(V\) is an average of normalized task gradients and is therefore unchanged. The task-specific feature gradient in the rotation loss scales by \(s_k\), while the algorithm treats that feature gradient as constant with respect to the rotation. The entire scalar rotation loss is consequently multiplied by \(s_k\), so its parameter gradient is multiplied by the same factor.

The head-gradient identity is immediate from
\[
\nabla_{\phi_k}(s_kL_k)
=
s_k\nabla_{\phi_k}L_k.
\]

Under a common scale \(s\), every backbone, head, and rotation gradient used by the source update is multiplied by \(s\), while all normalized directions and relative-convergence coefficients are unchanged. Replacing both displayed learning rates by their values divided by \(s\) therefore produces the same next state. Starting from identical states, induction gives identical full trajectories.

Finally, suppose two nonzero head gradients correspond to unequal scales \(s_i\ne s_j\). If one common learning-rate multiplier \(r\) reproduced both original head steps, it would have to satisfy
\[
rs_i=1
\]
and
\[
rs_j=1,
\]
which is impossible. Hence independent scaling cannot in general be absorbed into one global network learning rate.

## Verification

The accompanying `verify.py` samples positive current and initial task-gradient norms, normalized task directions, and arbitrary positive scale factors.

It checks exact invariance of the normalized gradients and relative-convergence weights, the arithmetic-mean backbone multiplier, its min-max bounds, task-specific head and rotation scaling, and the common-scale one-step compensation identities.

It also checks algebraically that unequal task scales cannot be compensated by one common network learning-rate multiplier when two task-head gradients are nonzero.

The computations are transcription guards. The all-state transformation laws and trajectory equivalence are proved analytically above.

## Relationship to prior work

Javaloy and Valera introduce RotoGrad as a joint gradient-magnitude and gradient-direction homogenization method. Their magnitude rule normalizes every task gradient, then sets a common target magnitude \(C\) as a convex combination of the original task-gradient norms. The combination weights use each current norm divided by its initial norm. Their direction block learns task-specific rotations against a target formed from normalized gradients.

The defining algorithm separately updates the backbone using
\[
C\sum_kU_k,
\]
each task head using its own loss gradient, and each rotation using its task-specific rotation loss. The paper emphasizes gradient-scale disparities and the importance of the target magnitude for task step sizes, but the inspected full text does not state the exact transformation of these three update channels under arbitrary changes of task-loss units.

Later work on dual balancing explicitly treats disparities of loss scales and gradient magnitudes as distinct multi-task balancing problems and introduces logarithmic loss transformation plus gradient normalization. That broader motivation is compatible with the present result but does not state RotoGrad's arithmetic-mean multiplier or its task-specific rotation-speed transformation.

Focused published-record searches for RotoGrad loss scaling, task-unit invariance, rotation learning-rate scaling, and an arithmetic-mean transformation law did not identify an implication-equivalent result.

## Limitations

The result concerns multiplicative positive task scaling applied consistently from initialization.

If task scales change during training, the source relative-convergence ratios need not remain invariant because the stored initial norms use different factors.

The theorem isolates deterministic unit transformations and does not claim that loss-unit sensitivity necessarily harms benchmark performance.

The common-scale trajectory equivalence uses reciprocal rescaling of both displayed learning rates; holding either one fixed changes the corresponding dynamics.

## References

1. Adrián Javaloy and Isabel Valera, “RotoGrad: Gradient Homogenization in Multitask Learning,” arXiv:2103.02631v1, first submitted 2021-03-03; ICLR 2022.
2. Baijiong Lin, Weisen Jiang, Feiyang Ye, Yu Zhang, Pengguang Chen, Ying-Cong Chen, Shu Liu, Ivor W. Tsang, and James T. Kwok, “Dual-Balancing for Multi-Task Learning,” arXiv:2308.12029v1, first submitted 2023-08-23.
