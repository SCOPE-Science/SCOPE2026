# PowerGrad is exactly cross-entropy SGD with a reciprocal head–body learning-rate rebalance
## Finding

Consider a multiclass network whose logits have the common form
\[
z=W h_\theta(x),
\]
where \(h_\theta(x)\) is a differentiable feature map and \(W\) is the final linear classification head. Let
\[
\mathcal L(W,\theta)
\]
denote ordinary cross-entropy.

PowerGrad changes the backward softmax probability vector from
\[
p_i(z)
=
\frac{\exp(z_i)}{\sum_j\exp(z_j)}
\]
to
\[
p'_i(z)
=
\frac{p_i(z)^\alpha}{\sum_j p_j(z)^\alpha},
\qquad
0<\alpha\le1.
\]
The transformed probabilities satisfy the exact identity
\[
\boxed{
p'(z)=\operatorname{softmax}(\alpha z).
}
\]

This elementary identity has a stronger optimization consequence. Define the scalar surrogate
\[
\boxed{
\Psi_\alpha(W,\theta)
=
\frac1\alpha
\mathcal L(\alpha W,\theta).
}
\]
Then the complete PowerGrad backward vector field is exactly
\[
\boxed{
\nabla^{\mathrm{PowerGrad}}_{W,\theta}\mathcal L
=
\nabla_{W,\theta}\Psi_\alpha.
}
\]
Thus the modified backward pass is conservative: it is ordinary gradient descent on an explicit scalar objective, even though that objective differs from the loss used in the forward pass.

There is also an exact reparameterization of the optimization dynamics. Put
\[
V=\alpha W.
\]
Suppose PowerGrad uses plain gradient descent or minibatch SGD with head learning rate \(\eta_W\) and feature-body learning rate \(\eta_\theta\), with the same minibatch sequence on both sides of the comparison. Then one PowerGrad step is conjugate to ordinary cross-entropy training in variables \((V,\theta)\) with learning rates
\[
\boxed{
\eta_V=\alpha\eta_W,
\qquad
\eta_\theta^{\mathrm{CE}}=\frac{\eta_\theta}{\alpha}.
}
\]
In particular, if PowerGrad uses one common learning rate
\[
\eta_W=\eta_\theta=\eta,
\]
then its exact ordinary-cross-entropy representation has body-to-head learning-rate ratio
\[
\boxed{
\frac{\eta_\theta^{\mathrm{CE}}}{\eta_V}
=
\frac1{\alpha^2}.
}
\]
For the values
\[
\alpha<1
\]
used to flatten the backward probability distribution, this is an exact reciprocal layerwise learning-rate rebalance: the feature body is accelerated relative to the classifier head by the factor
\[
\frac1{\alpha^2}.
\]

A particularly sharp boundary case occurs when the features are fixed. There is then no \(\theta\)-block, so PowerGrad with step schedule \(\eta_t\) is exactly ordinary cross-entropy SGD under
\[
V_t=\alpha W_t
\]
and the rescaled step schedule
\[
\alpha\eta_t.
\]
Because \(\alpha>0\),
\[
\operatorname*{arg\,max}_c (W_t h)_c
=
\operatorname*{arg\,max}_c (V_t h)_c
\]
for every feature vector \(h\). Thus the matched trajectories make identical class predictions at every iterate.

Under the usual linearly separable fixed-feature assumptions for which ordinary cross-entropy gradient descent converges in direction to the multiclass hard-margin solution, PowerGrad has the same limiting classifier direction. In this setting PowerGrad changes scale and optimization clock, but not the matched decision-boundary trajectory.

## Assumptions and scope

The PowerGrad exponent satisfies
\[
0<\alpha\le1.
\]
The source also discusses the endpoint
\[
\alpha=0,
\]
but the scalar surrogate contains \(1/\alpha\), so the theorem deliberately excludes that endpoint.

The logits are linear in the final head:
\[
z=W h_\theta(x).
\]
The feature extractor may otherwise be nonlinear and nonconvex.

The exact dynamic conjugacy is for ordinary full-batch gradient descent or minibatch SGD, with corresponding batches used in the two parameterizations. Separate constant or time-dependent block learning rates are allowed.

Momentum, Nesterov acceleration, adaptive preconditioners, weight decay, gradient clipping, and other optimizer state transformations are not covered by the stated conjugacy.

The fixed-feature max-margin conclusion is conditional on the standard assumptions required by the cited implicit-bias theorem, including separability and an admissible gradient-descent step regime.

## Proof

For any softmax probability,
\[
p_i(z)
=
\frac{\exp(z_i)}{\sum_j\exp(z_j)}.
\]
Therefore
\[
p_i(z)^\alpha
=
\frac{\exp(\alpha z_i)}
{\left(\sum_j\exp(z_j)\right)^\alpha}.
\]
The common denominator cancels when the powered probabilities are renormalized, giving
\[
p'_i(z)
=
\frac{\exp(\alpha z_i)}
{\sum_j\exp(\alpha z_j)}
=
\operatorname{softmax}(\alpha z)_i.
\]

For a one-hot label vector \(y\), ordinary cross-entropy with logits \(u\) has logit gradient
\[
\nabla_u\ell(u,y)
=
\operatorname{softmax}(u)-y.
\]
Hence the PowerGrad logit pseudo-gradient is
\[
g_z
=
\operatorname{softmax}(\alpha z)-y.
\]

Now write
\[
V=\alpha W.
\]
Ordinary cross-entropy with head \(V\) has head gradient
\[
\nabla_V\mathcal L(V,\theta)
=
g_z h_\theta^\top.
\]
By the chain rule,
\[
\nabla_W
\left[
\frac1\alpha\mathcal L(\alpha W,\theta)
\right]
=
\nabla_V\mathcal L(V,\theta),
\]
which is exactly the PowerGrad head pseudo-gradient.

For the feature parameters,
\[
\nabla_\theta\mathcal L(V,\theta)
=
J_\theta h_\theta^\top V^\top g_z.
\]
Therefore
\[
\frac1\alpha\nabla_\theta\mathcal L(V,\theta)
=
J_\theta h_\theta^\top W^\top g_z,
\]
which is exactly the gradient obtained by backpropagating the PowerGrad logit pseudo-gradient through the original forward head \(W\). This proves
\[
\nabla^{\mathrm{PowerGrad}}\mathcal L
=
\nabla\Psi_\alpha.
\]

For the dynamic conjugacy, a PowerGrad update is
\[
W^+
=
W-\eta_W\nabla_V\mathcal L(V,\theta),
\]
\[
\theta^+
=
\theta
-
\frac{\eta_\theta}{\alpha}
\nabla_\theta\mathcal L(V,\theta).
\]
Multiplying the first identity by \(\alpha\) gives
\[
V^+
=
V
-
\alpha\eta_W
\nabla_V\mathcal L(V,\theta).
\]
This is precisely ordinary cross-entropy gradient descent or SGD with the displayed block learning rates.

If the features are fixed, only the \(V\)-equation remains. Induction over the shared minibatch sequence proves
\[
V_t=\alpha W_t
\]
for every iteration when the initial states satisfy the same relation. Positive scaling preserves every logit ordering, proving the prediction identity.

Finally, any directional convergence theorem for the matched ordinary cross-entropy linear-classifier trajectory transfers immediately because multiplying all classifier weights by the positive constant
\[
1/\alpha
\]
does not change their normalized direction.

## Verification

The accompanying `verify.py` independently reconstructs the PowerGrad transform on random multiclass examples.

It checks that powering and renormalizing softmax probabilities is identical to applying softmax to scaled logits. For a nonlinear one-hidden-layer feature map, it compares the analytic PowerGrad head and feature gradients with centered finite differences of
\[
\Psi_\alpha(W,\theta)
=
\alpha^{-1}\mathcal L(\alpha W,\theta).
\]
It then checks the exact one-step change-of-variables identity with separate head and feature learning rates.

Finally, on a fixed random feature matrix it runs many minibatch SGD steps from matched initializations and verifies at every step that
\[
V_t=\alpha W_t
\]
and that both classifiers have identical predicted classes.

The numerical checks are transcription guards. The identities for all dimensions, datasets, and differentiable feature maps follow from the chain-rule proof above.

## Relationship to prior work

Das, Mondal, Lall, Joshi, and Dutta Roy introduced the PowerGrad Transform as a deliberately altered backward pass. Their method raises softmax probabilities to a power, renormalizes them, and substitutes the result into the backward cross-entropy gradient while leaving the forward pass unchanged. Their analysis emphasizes smoothing of the gradient profile and empirical fitting behavior.

The identity
\[
p'(z)=\operatorname{softmax}(\alpha z)
\]
is closely related to standard temperature scaling: temperature scaling applies softmax to rescaled logits and, for positive temperature, preserves the predicted class. Temperature scaling itself is established prior work and is not claimed as new here.

The new structural statement is that the **entire** PowerGrad parameter vector field, including the feature extractor below the final linear head, is the gradient of the explicit surrogate
\[
\alpha^{-1}\mathcal L(\alpha W,\theta),
\]
and that its plain-SGD dynamics are exactly conjugate to ordinary cross-entropy with reciprocal head/body learning-rate rescaling. The inspected PowerGrad source does not state this conservative-surrogate identity or the
\[
1/\alpha^2
\]
relative learning-rate factor.

For fixed separable features, classical implicit-bias results for multiclass cross-entropy gradient descent imply convergence toward a max-margin direction. The present finding does not reprove that theorem; it shows that the matched PowerGrad trajectory inherits it exactly by positive head rescaling.

Focused searches for PowerGrad together with temperature reparameterization, conservative surrogate gradients, classifier-head rescaling, and reciprocal layerwise learning rates did not identify an implication-equivalent published statement.

## Limitations

The exact optimizer conjugacy is specific to plain gradient descent and minibatch SGD. Optimizers with momentum or adaptive state generally do not commute with the same parameter rescaling without a separate state transformation.

The theorem does not say that PowerGrad is ineffective in deep networks. On the contrary, for
\[
\alpha<1
\]
it identifies a potentially substantial and exact change in the relative optimization speed of the feature body and classification head.

The fixed-feature equivalence is a boundary case. Once the representation is trainable, the reciprocal block learning-rate change can alter the learned features even though the modified backward field remains conservative.

No statistical generalization improvement is asserted. The result is an optimization-geometry characterization of the source backward rule.

## References

1. Bishshoy Das, Milton Mondal, Brejesh Lall, Shiv Dutt Joshi, and Sumantra Dutta Roy, “Altering Backward Pass Gradients improves Convergence,” arXiv:2111.12495v1, first submitted 2021-11-24.
2. Chuan Guo, Geoff Pleiss, Yu Sun, and Kilian Q. Weinberger, “On Calibration of Modern Neural Networks,” arXiv:1706.04599v1, first submitted 2017-06-14; ICML 2017.
3. Daniel Soudry, Elad Hoffer, Mor Shpigel Nacson, Suriya Gunasekar, and Nathan Srebro, “The Implicit Bias of Gradient Descent on Separable Data,” arXiv:1710.10345v1, first submitted 2017-10-27.
