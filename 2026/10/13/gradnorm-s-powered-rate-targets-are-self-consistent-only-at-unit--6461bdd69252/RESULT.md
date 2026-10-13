# GradNorm's powered-rate targets are self-consistent only at unit asymmetry
## Finding

GradNorm defines each task's desired weighted gradient norm by multiplying the current mean gradient norm by a powered relative training rate. Because the rates are normalized before exponentiation, that powered target vector generally no longer has the same mean as the actual gradient vector.

Consider one GradNorm step with
\[
T\ge2
\]
tasks. Let the unweighted shared-layer gradient magnitudes be
\[
a_i
=
\lVert\nabla_W L_i\rVert_2
>
0,
\]
and assume positive task weights
\[
w_i>0,
\qquad
\sum_{i=1}^{T}w_i=T.
\]
Then the weighted gradient norms are
\[
G_i=w_i a_i,
\qquad
\bar G
=
\frac1T\sum_{i=1}^{T}G_i.
\]

GradNorm's relative inverse training rates satisfy
\[
r_i>0,
\qquad
\frac1T\sum_{i=1}^{T}r_i=1.
\]
For source asymmetry parameter
\[
\alpha>0,
\]
the desired gradient norms are
\[
\tau_i
=
\bar G r_i^\alpha.
\]
Define
\[
M_\alpha
=
\frac1T\sum_{i=1}^{T}r_i^\alpha.
\]

The GradNorm auxiliary loss
\[
L_{\rm grad}
=
\sum_{i=1}^{T}|G_i-\tau_i|
\]
obeys
\[
\boxed{
\frac{L_{\rm grad}}
{\sum_{i=1}^{T}G_i}
\ge
|1-M_\alpha|
}.
\]

This lower bound is sharp over positive task weights for every fixed positive vector
\[
(a_1,\ldots,a_T)
\]
and every positive rate vector with mean one.

Therefore the source targets can all be attained simultaneously exactly when
\[
\boxed{
M_\alpha=1
}.
\]

For heterogeneous training rates, strict Jensen inequalities give the complete phase diagram
\[
\boxed{
0<\alpha<1
\Longrightarrow
M_\alpha<1
},
\]
\[
\boxed{
\alpha=1
\Longrightarrow
M_\alpha=1
},
\]
and
\[
\boxed{
\alpha>1
\Longrightarrow
M_\alpha>1
}.
\]

Hence, within the source algorithm's range
\[
\alpha>0,
\]
the only asymmetry value whose powered heterogeneous targets are exactly self-consistent is
\[
\boxed{\alpha=1}.
\]

This is a structural statement about the target construction, not a claim that GradNorm training fails. A positive residual can still act as a restoring force.

The inconsistency has a canonical correction. Among targets that preserve the source ratios
\[
\tau_i:\tau_j
=
r_i^\alpha:r_j^\alpha
\]
and retain mean
\[
\bar G,
\]
the unique choice is
\[
\boxed{
\tau_i^\star
=
\bar G
\frac{r_i^\alpha}{M_\alpha}
}.
\]
For arbitrary positive gradient magnitudes \(a_i\), these corrected targets are exactly realizable under the source weight normalization by choosing
\[
\boxed{
w_i^\star
=
T
\frac{r_i^\alpha/a_i}
{\sum_{j=1}^{T}r_j^\alpha/a_j}
}.
\]

The source uses
\[
\alpha=0.12
\]
in its toy experiments and
\[
\alpha=1.5
\]
in its main NYUv2 experiments. Whenever the task rates are heterogeneous, both values produce a strictly positive structural target mismatch.

## Assumptions and scope

The result is instantaneous: it analyzes the compatibility of GradNorm's target gradient norms at one training step.

All unweighted task gradient norms \(a_i\) are assumed positive, and the theorem is stated while the task weights remain positive.

The rates \(r_i\) use the source normalization, so their arithmetic mean is exactly one.

The theorem does not model the subsequent network-parameter update or assert that a nonzero \(L_{\rm grad}\) prevents good empirical performance.

The source treats the target terms as constants when differentiating \(L_{\rm grad}\) with respect to the task weights. The present statement concerns the self-consistency of the targets when they are formed from the current mean gradient norm, not the local derivative after detachment.

## Proof

Summing the actual gradient norms gives
\[
\sum_{i=1}^{T}G_i
=
T\bar G.
\]
Summing the source targets gives
\[
\sum_{i=1}^{T}\tau_i
=
\bar G
\sum_{i=1}^{T}r_i^\alpha
=
T\bar G M_\alpha.
\]

By the triangle inequality,
\[
L_{\rm grad}
=
\sum_{i=1}^{T}|G_i-\tau_i|
\ge
\left|
\sum_{i=1}^{T}(G_i-\tau_i)
\right|.
\]
Therefore
\[
L_{\rm grad}
\ge
T\bar G|1-M_\alpha|.
\]
Dividing by
\[
\sum_iG_i=T\bar G
\]
proves the lower bound.

It remains to prove sharpness. Normalize
\[
x_i=\frac{G_i}{\bar G},
\qquad
s_i=r_i^\alpha.
\]
Then
\[
\frac1T\sum_i x_i=1,
\qquad
\frac1T\sum_i s_i=M_\alpha.
\]

If
\[
M_\alpha<1,
\]
choose
\[
x_i=s_i+(1-M_\alpha).
\]
Then every \(x_i\) is positive, its mean is one, and
\[
\sum_i|x_i-s_i|
=
T(1-M_\alpha).
\]

If
\[
M_\alpha>1,
\]
choose
\[
x_i=\frac{s_i}{M_\alpha}.
\]
Again every \(x_i\) is positive, its mean is one, and
\[
\sum_i|x_i-s_i|
=
T(M_\alpha-1).
\]

If
\[
M_\alpha=1,
\]
take
\[
x_i=s_i,
\]
giving zero residual.

For any such positive normalized vector \(x\), define
\[
w_i
=
T
\frac{x_i/a_i}
{\sum_jx_j/a_j}.
\]
Then
\[
w_i>0,
\qquad
\sum_iw_i=T,
\]
and
\[
G_i=w_i a_i=Cx_i
\]
for one common constant \(C>0\). Since the mean of \(x_i\) is one,
\[
\bar G=C.
\]
Thus the lower bound is attained.

For heterogeneous \(r_i\), strict concavity of
\[
x^\alpha
\]
on the positive half-line when
\[
0<\alpha<1
\]
gives
\[
M_\alpha<1.
\]
At
\[
\alpha=1,
\]
the source normalization directly gives
\[
M_1=1.
\]
For
\[
\alpha>1,
\]
strict convexity gives
\[
M_\alpha>1.
\]

Finally, any target preserving the source ratios must have the form
\[
c\,r_i^\alpha
\]
for a common scalar \(c\). Requiring its mean to equal \(\bar G\) forces
\[
c=\frac{\bar G}{M_\alpha},
\]
proving uniqueness of the corrected target. Substituting the displayed \(w_i^\star\) verifies exact realization.

## Verification

The accompanying `verify.py` checks the lower bound and its sharp constructions on randomized positive task-gradient magnitudes, heterogeneous rate vectors, and asymmetry values below, at, and above one.

It also verifies the Jensen phase diagram numerically and confirms that the mean-renormalized powered target is exactly realizable under positive task weights summing to \(T\).

The computation is a transcription guard. The lower bound, sharpness, and consistency criterion are proved analytically above.

## Relationship to prior work

Chen, Badrinarayanan, Lee, and Rabinovich define the weighted task gradient norm
\[
G_i
=
\lVert\nabla_W(w_iL_i)\rVert_2,
\]
its taskwise average \(\bar G\), and a relative inverse training rate \(r_i\) normalized to have mean one. Their target is
\[
\bar G r_i^\alpha,
\]
and their auxiliary \(L_1\) loss moves each actual norm toward that target. The targets are detached when differentiating with respect to task weights, and the task weights are renormalized after each update to sum to the number of tasks.

The defining paper explains \(\alpha\) as the strength of the restoring force, discusses \(\alpha=0\) as equal-gradient normalization, uses \(\alpha=0.12\) in the toy study, and uses \(\alpha=1.5\) in its main real-data experiments. The inspected full text does not compare the sum of the powered targets with the sum of the actual gradient norms, state the Jensen consistency transition at \(\alpha=1\), or give the sharp unavoidable normalized residual above.

Later scale-invariant multi-task work explicitly argues that learned gradient-balancing weights such as GradNorm's do not guarantee scale invariance throughout training and replaces them with direct gradient normalization. That broader critique does not state the powered-rate target mass mismatch, the exact lower bound
\[
|1-M_\alpha|,
\]
or the unique mean-preserving correction.

Focused published-record searches for GradNorm target inconsistency, powered-rate mean mismatch, an \(\alpha=1\) self-consistency threshold, and unavoidable GradNorm auxiliary loss did not identify an implication-equivalent result.

## Limitations

The theorem is about target compatibility, not downstream generalization or convergence.

The exact sharpness statement assumes positive unweighted gradient norms and positive task weights.

The corrected target is an algebraic consistency repair. No claim is made here that replacing the original GradNorm target by the corrected target improves empirical performance.

The source's \(\alpha=0\) discussion is also mass-consistent, but its algorithm specifies choosing \(\alpha>0\); the phase statement above follows that algorithmic range.

## References

1. Zhao Chen, Vijay Badrinarayanan, Chen-Yu Lee, and Andrew Rabinovich, “GradNorm: Gradient Normalization for Adaptive Loss Balancing in Deep Multitask Networks,” arXiv:1711.02257v1, first submitted 2017-11-07; PMLR 80, 794–803, 2018.
2. Baijiong Lin, Weisen Jiang, Feiyang Ye, Yu Zhang, Pengguang Chen, Ying-Cong Chen, Shu Liu, and James T. Kwok, “Dual-Balancing for Multi-Task Learning,” arXiv:2308.12029v1, 2023.
