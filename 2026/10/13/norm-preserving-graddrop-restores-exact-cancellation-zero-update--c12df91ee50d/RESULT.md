# Norm-preserving GradDrop restores exact cancellation zero-updates
## Finding

Gradient Sign Dropout (GradDrop) is motivated by cancellation among conflicting task gradients. The defining paper proves a zero-set property for the pure masked update, but also says that many experiments renormalize the final gradient norm. The public Lingvo implementation enables this norm preservation by default.

Let
\[
g=\sum_{i=1}^{T}g_i
\]
be the ordinary aggregate gradient and let
\[
\widetilde g
\]
be the raw masked GradDrop aggregate. The norm-preserving implementation returns
\[
\boxed{
\widehat g=
\widetilde g
\frac{\lVert g\rVert_2}
{\lVert\widetilde g\rVert_2+\varepsilon}
}
\]
with
\[
\varepsilon>0.
\]
Hence
\[
\boxed{
\lVert\widehat g\rVert_2
=
\lVert g\rVert_2
\frac{\lVert\widetilde g\rVert_2}
{\lVert\widetilde g\rVert_2+\varepsilon}
\le
\lVert g\rVert_2
}.
\]

In particular,
\[
\boxed{
g=0\Longrightarrow\widehat g=0
}
\]
for every mask realization, even when the individual task gradients are nonzero.

For the scalar pair
\[
g_1=a,
\qquad
g_2=-a,
\qquad
a>0,
\]
the source purity is
\[
P=\frac12.
\]
Pure GradDrop with zero leak and identity activation therefore returns
\[
\widetilde g=+a
\]
or
\[
\widetilde g=-a
\]
with equal probability. Thus the pure method is nonzero almost surely, as required by the defining stable-point proposition. But
\[
g_1+g_2=0,
\]
so norm preservation multiplies either raw outcome by zero and returns
\[
\boxed{\widehat g=0}.
\]

Therefore the added norm-preserving postprocessing restores every exact ordinary-gradient cancellation as a zero-update point. Near cancellation it also forces
\[
\lVert\widehat g\rVert_2
\le
\left\lVert\sum_i g_i\right\rVert_2,
\]
so the conflict-induced stochastic escape amplitude vanishes with the ordinary summed-gradient norm.

## Assumptions and scope

The claim concerns the paper-described norm-preserving postprocessing and the inspected public Lingvo implementation.

The incoming original gradient is the ordinary aggregate of the same task losses supplied to GradDrop, as in standard multitask use.

The all-dimensional zero-set statement is independent of mask details. The scalar example uses the source identity activation only to show that the unrescaled mask is genuinely nonzero at exact cancellation.

The result does not say that pure unrescaled GradDrop violates its theorem. The obstruction is introduced by the additional global norm rescaling.

## Proof

The implementation first forms the masked sum \(\widetilde g\). When norm preservation is active it multiplies this vector by
\[
\frac{\lVert g\rVert_2}
{\lVert\widetilde g\rVert_2+\varepsilon}.
\]
Taking Euclidean norms gives the displayed inequality because
\[
\frac{\lVert\widetilde g\rVert_2}
{\lVert\widetilde g\rVert_2+\varepsilon}
\in[0,1).
\]
If
\[
g=0,
\]
the scale factor is zero, proving the all-dimensional statement.

For the two-task scalar example, the positive and negative absolute masses are both \(a\), so the source purity formula gives \(P=1/2\). A single mask sample keeps either the positive task or the negative task, making the raw aggregate \(+a\) or \(-a\). The norm-preserving factor is zero in both cases.

## Verification

The accompanying `verify.py` implements the source scalar purity mask and the inspected norm-rescaling formula. It checks exact two-task cancellation, randomized multidimensional cancellations, the universal norm bound, and a near-cancellation family.

The computations are transcription guards. The theorem itself follows directly from the exact rescaling identity.

## Relationship to prior work

Chen and coauthors define GradDrop by selecting one sign at each position and masking task gradients of the opposite sign. Their Proposition 1 proves that the pure GradDrop update is zero only when every constituent task gradient is zero.

The same paper states that many experiments renormalize final gradients so that the Euclidean norm remains constant through GradDrop, while noting that this step is not practically required. The main theorem is stated for the pure GradDrop update and does not analyze the zero set after this extra rescaling.

The supplemental material derives expectation and variance formulas for the unrescaled one-dimensional mask. It likewise does not analyze the subsequent global norm rescaling.

The public Lingvo implementation makes the composition explicit: `keep_gradnorm_constant` defaults to true, and the final transformed gradient is multiplied by the original incoming gradient norm divided by the transformed norm plus a numerical regularizer.

Focused published-record searches for GradDrop norm renormalization, exact cancellation, zero updates, and stable-point guarantees did not identify an implication-equivalent result.

## Limitations

The finding targets the norm-preserving variant, not pure GradDrop.

Other gradients, optimizer states, or regularizers outside the GradDrop layer can still move a full training system when this layer returns zero.

The result characterizes the exact zero set and a near-cancellation norm bound, not the empirical frequency of such cancellations.

No benchmark-performance claim is made.

## References

1. Zhao Chen, Jiquan Ngiam, Yanping Huang, Thang Luong, Henrik Kretzschmar, Yuning Chai, and Dragomir Anguelov, “Just Pick a Sign: Optimizing Deep Multitask Models with Gradient Sign Dropout,” arXiv:2010.06808v1, first submitted 2020-10-14; NeurIPS 2020.
2. Supplemental material for “Just Pick a Sign: Optimizing Deep Multitask Models with Gradient Sign Dropout,” NeurIPS 2020.
3. TensorFlow Lingvo, `lingvo/core/graddrop.py`, public GradDrop implementation.
