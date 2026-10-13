# Published Ranger21 has a gradient-centralization singularity in stable Norm Loss
## Finding

The published Ranger21 algorithm combines Gradient Centralization with Stable Weight Decay and Norm Loss. On a natural strongly convex family, those components create an exact first-step singularity.

Consider one \(d\)-coordinate parameter row, with \(d\ge2\), and the \(1\)-strongly convex quadratic
\[
f(\theta)=\frac12\|\theta-b\mathbf1\|_2^2.
\]
Choose
\[
\theta_\delta=c\mathbf1+\delta q,
\qquad
\|q\|_2=1,
\qquad
\mathbf1^\top q=0,
\]
with
\[
|c|\sqrt d>\epsilon_{\rm clipping},
\qquad
|c-b|<\tau_{\rm clipping}|c|,
\qquad
|c|\sqrt d\ne1.
\]
Assume the source moments are initialized at zero, the regularization coefficient satisfies
\[
\lambda>0,
\]
and the first scheduled learning rate satisfies
\[
\eta_1>0.
\]

For every sufficiently small \(\delta\), the source Adaptive Gradient Clipping condition is inactive. The raw gradient is
\[
\nabla f(\theta_\delta)
=
(c-b)\mathbf1+\delta q.
\]
Gradient Centralization subtracts its coordinate mean, leaving exactly
\[
g_1^{\rm GC}=\delta q.
\]

Because the second-moment state starts at zero, the first bias-corrected maximum second moment is
\[
\widehat v_1
=
\delta^2(q\odot q),
\]
and therefore
\[
\boxed{
\operatorname{mean}(\widehat v_1)
=
\frac{\delta^2}{d}.
}
\]

Algorithm 4 defines its combined Stable-Weight-Decay/Norm-Loss vector using the factor
\[
\frac{\eta_1\lambda}
{\sqrt{\operatorname{mean}(\widehat v_1)}}
\left(1-\frac1{\|\theta_\delta\|_2}\right)\theta_\delta,
\]
and then multiplies that vector by \(\eta_1\) again in the parameter update. Hence the norm of the regularization displacement is exactly
\[
\boxed{
\eta_1^2\lambda\sqrt d\,
\frac{|\|\theta_\delta\|_2-1|}
{|\delta|}.
}
\]
Since
\[
\|\theta_\delta\|_2
\longrightarrow
|c|\sqrt d\ne1,
\]
this displacement diverges like
\[
\frac1{|\delta|}.
\]

By contrast, the adaptive-gradient update remains bounded and actually tends to zero. Its numerator is linear in \(\delta\), while the published adaptive denominator contains the numerical safeguard
\[
\epsilon>0.
\]
Therefore no cancellation can remove the regularization blow-up.

At the symmetric point
\[
\delta=0,
\]
Gradient Centralization makes the processed gradient exactly zero. All first-step second moments are then zero, so
\[
\sqrt{\operatorname{mean}(\widehat v_1)}=0.
\]
Because the Norm-Loss numerator is nonzero when
\[
|c|\sqrt d\ne1,
\]
the published Stable-Weight-Decay/Norm-Loss expression is undefined.

A concrete source-default clipping witness is obtained in dimension two with
\[
c=2,
\qquad
b=1.99,
\qquad
q=\frac1{\sqrt2}(1,-1),
\qquad
\tau_{\rm clipping}=10^{-2},
\qquad
\epsilon_{\rm clipping}=10^{-3}.
\]
For all sufficiently small \(\delta\), the clipping ratio is below \(10^{-2}\), so the exact derivation above applies.

The singularity is not intrinsic to Stable Weight Decay itself. Its original published rule places an \(\epsilon\) safeguard in the adaptive decay denominator. A later first-party Flax Ranger21 implementation also wraps the Stable-Weight-Decay/Norm-Loss denominator in a nonzero-denominator safeguard. Those variants are finite at the symmetric point.

## Assumptions and scope

The result concerns the equations in the published Ranger21 paper, specifically Algorithm 4.

Only one parameter row is needed. The task loss is a deterministic smooth strongly convex quadratic.

The proof assumes a positive regularization coefficient and a positive first scheduled learning rate. No claim is made for the degenerate case \(\lambda=0\).

The initial row norm is assumed different from one so that the Norm-Loss factor is genuinely nonzero at the symmetric point.

The clipping hypotheses ensure that Adaptive Gradient Clipping is locally inactive. This is not restrictive for the obstruction: one may choose \(b\) arbitrarily close to \(c\).

The result does not claim that current software implementations inherit the singularity. In particular, a later first-party Flax implementation inserts a nonzero-denominator safeguard absent from the published Algorithm 4.

## Proof

The raw first gradient is
\[
g_1
=
(c-b)\mathbf1+\delta q.
\]
The clipping ratio tends, as \(\delta\to0\), to
\[
\frac{|c-b|}{|c|},
\]
which is strictly below
\[
\tau_{\rm clipping}.
\]
Since
\[
|c|\sqrt d>\epsilon_{\rm clipping},
\]
continuity shows that clipping is inactive for all sufficiently small \(\delta\).

Gradient Centralization subtracts the coordinate mean. Since
\[
\mathbf1^\top q=0,
\]
the mean of the raw gradient is
\[
c-b.
\]
Thus
\[
g_1^{\rm GC}
=
\delta q.
\]

The published second-moment recurrence starts from zero:
\[
v_1
=
(1-\beta_2)\delta^2(q\odot q).
\]
At the first step its running maximum equals \(v_1\), and bias correction divides by
\[
1-\beta_2.
\]
Therefore
\[
\widehat v_1
=
\delta^2(q\odot q).
\]
Averaging coordinates and using
\[
\|q\|_2^2=1
\]
gives
\[
\operatorname{mean}(\widehat v_1)
=
\frac{\delta^2}{d}.
\]

Algorithm 4's Stable-Weight-Decay/Norm-Loss vector is
\[
d_1
=
\frac{\eta_1\lambda}
{\sqrt{\operatorname{mean}(\widehat v_1)}}
\left(1-\frac1{\|\theta_\delta\|_2}\right)\theta_\delta.
\]
The parameter update subtracts
\[
\eta_1d_1.
\]
Therefore
\[
\|\eta_1d_1\|_2
=
\eta_1^2\lambda
\frac{\|\theta_\delta\|_2-1}{\sqrt{\operatorname{mean}(\widehat v_1)}}
\]
in absolute value, which simplifies to
\[
\eta_1^2\lambda\sqrt d\,
\frac{|\|\theta_\delta\|_2-1|}{|\delta|}.
\]

Meanwhile the first positive-negative-momentum numerator is proportional to
\[
\delta q.
\]
The adaptive update divides each coordinate by a denominator containing the strictly positive source constant
\[
\epsilon,
\]
so its norm tends to zero with \(\delta\). The full first-step displacement is therefore unbounded in norm.

At
\[
\delta=0,
\]
the same calculation gives
\[
\widehat v_1=0.
\]
The stable-decay denominator vanishes exactly, whereas
\[
\left(1-\frac1{\|\theta_0\|_2}\right)\theta_0\ne0
\]
by the nonunit-norm assumption. Hence the published formula is undefined.

## Verification

The accompanying `verify.py` evaluates the two-dimensional witness with source-default clipping parameters.

It checks that clipping is inactive near the symmetric line, that centralization produces the predicted antisymmetric residual, that the bias-corrected second-moment mean is exactly proportional to \(\delta^2\), and that the regularization displacement obeys the predicted inverse-\(|\delta|\) scaling.

It separately checks that adding a positive denominator safeguard makes the same regularization term finite at the symmetric point.

The computation is only a transcription check. The singularity and asymptotic blow-up are proved algebraically above.

## Relationship to prior work

Wright and Demeure present Ranger21 as a composition of eight optimizer enhancements. The published algorithm applies Adaptive Gradient Clipping, then Gradient Centralization, then adaptive moments, and finally a combination of Stable Weight Decay and Norm Loss. The paper emphasizes the compatibility and synergy of the components.

The original Stable Weight Decay source uses an adaptive denominator with an explicit numerical \(\epsilon\) safeguard. Ranger21's published Stable-Weight-Decay/Norm-Loss formula omits that safeguard even though its ordinary adaptive update retains one.

The original Norm Loss source derives the radial factor
\[
\left(1-\frac1{\|w\|_2}\right)w
\]
as the gradient direction that softly pushes a weight vector toward unit norm. That factor is nonzero on the family used here.

A later first-party Flax Ranger21 implementation explicitly applies a nonzero-denominator helper to the Stable-Weight-Decay/Norm-Loss denominator. It also states that the implementation follows code updated since the publication. This practical safeguard is consistent with, but does not itself state, the strongly convex singular family or the inverse-distance blow-up proved here.

Focused searches for Ranger21 together with Gradient Centralization, Stable Weight Decay, zero second moments, denominator singularities, and strongly convex quadratics did not identify an implication-equivalent published analysis.

## Limitations

This is a well-definedness and local robustness result for the published mathematical algorithm, not a claim that maintained Ranger21 software currently divides by zero.

The exact singular family lies in the mean-gradient direction removed by Gradient Centralization. The stronger inverse-distance statement shows that the issue is not confined to the single exactly symmetric point.

The example isolates one parameter row and one optimization step. It does not assess the empirical accuracy results reported for Ranger21.

The natural repair is already suggested by the surrounding literature and later implementation: apply a positive numerical safeguard to the Stable-Weight-Decay/Norm-Loss denominator.

## References

1. Less Wright and Nestor Demeure, “Ranger21: a synergistic deep learning optimizer,” arXiv:2106.13731v1, first submitted 2021-06-25.
2. Zeke Xie, Zhiqiang Xu, Jingzhao Zhang, Issei Sato, and Masashi Sugiyama, “On the Overlooked Pitfalls of Weight Decay and How to Mitigate Them: A Gradient-Norm Perspective,” arXiv:2011.11152v1, first submitted 2020-11-23.
3. Theodoros Georgiou, Sebastian Schmitt, Thomas Bäck, Wei Chen, and Michael Lew, “Norm Loss: An efficient yet effective regularization method for deep neural networks,” arXiv:2103.06583v1, first submitted 2021-03-11.
