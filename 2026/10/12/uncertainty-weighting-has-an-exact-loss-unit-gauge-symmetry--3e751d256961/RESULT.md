# Uncertainty weighting has an exact loss-unit gauge symmetry
## Finding

Homoscedastic Uncertainty Weighting learns one log-variance per task,
\[
s_i=\log\sigma_i^2.
\]
The source regression term and its simplified classification term share the form
\[
a_i e^{-s_i}L_i(\theta)+\frac12s_i,
\]
with a task-type constant \(a_i>0\).

Let
\[
q_i>0,
\qquad
L_i'(\theta)=q_iL_i(\theta),
\qquad
s_i'=s_i+\log q_i.
\]
Then
\[
e^{-s_i'}L_i'
=
e^{-s_i}L_i,
\]
and therefore
\[
\boxed{
F'(\theta,s')
=
F(\theta,s)+\frac12\sum_i\log q_i.
}
\]

The difference is constant. Hence
\[
\boxed{
\nabla_\theta F'(\theta,s')=\nabla_\theta F(\theta,s)
}
\]
and
\[
\boxed{
\nabla_{s_i'}F'(\theta,s')=\nabla_{s_i}F(\theta,s)
}.
\]

Thus task-loss rescaling is exactly equivalent to translation in log-variance coordinates. Stationary points correspond by
\[
\boxed{
(s_i')^\star=s_i^\star+\log q_i
}
\]
or
\[
\boxed{
(\sigma_i')^2=q_i\sigma_i^2.
}
\]

The symmetry extends to the full optimization path. Consider a deterministic first-order optimizer whose updates depend on gradients and optimizer state but not directly on the absolute value of \(s_i\). If
\[
\theta_0'=\theta_0,
\qquad
s_{i,0}'=s_{i,0}+\log q_i,
\]
with identical optimizer states, then
\[
\boxed{
\theta_t'=\theta_t,
\qquad
s_{i,t}'=s_{i,t}+\log q_i
}
\]
for every step. This includes plain SGD, momentum SGD, and Adam when the uncertainty parameters are not subjected to weight decay, clipping, or other absolute-value operations.

No learning-rate correction is needed, even for independent task rescaling.

The initialization shift is essential. If the numerical uncertainty initialization is held fixed after changing loss units, the run starts with the exact mismatch
\[
-\log q_i
\]
relative to the symmetry-related state.

For squared regression, changing physical target units by
\[
c_i>0
\]
multiplies the squared loss by
\[
q_i=c_i^2.
\]
The corresponding uncertainty standard deviation transforms as
\[
\boxed{
\sigma_i'=c_i\sigma_i.
}
\]

## Assumptions and scope

The theorem concerns the source objective after parameterizing
\[
s_i=\log\sigma_i^2.
\]

The task-scale factors are fixed positive constants.

The source classification expression is obtained using a simplifying approximation; the theorem applies exactly to that displayed simplified training objective.

The trajectory statement requires translation-equivariant uncertainty-parameter updates. Weight decay on \(s_i\), clipping, box constraints, or other direct functions of the absolute log variance break the optimizer-level conjugacy.

The theorem does not claim that using the same numerical uncertainty initialization after changing task units produces the same transient training path.

## Proof

Write
\[
F(\theta,s)
=
\sum_i
\left[
a_i e^{-s_i}L_i(\theta)+\frac12s_i
\right].
\]
The rescaled objective is
\[
F'(\theta,s')
=
\sum_i
\left[
a_i e^{-s_i'}q_iL_i(\theta)+\frac12s_i'
\right].
\]
With
\[
s_i'=s_i+\log q_i,
\]
the data term is unchanged and
\[
\frac12s_i'
=
\frac12s_i+\frac12\log q_i.
\]
This proves the constant-offset identity and therefore the gradient identities.

For the trajectory statement, suppose at step \(t\) that the model parameters agree, the log variances differ by the fixed vector \((\log q_i)_i\), and the optimizer states agree. The gradient identity supplies identical gradient inputs. Translation-equivariance gives identical increments in the log variances, while the model updates are identical. Induction proves the relation for all steps.

For squared regression, unit scaling by \(c_i\) multiplies each squared residual by \(c_i^2\), so the log-variance shift is \(2\log c_i\), equivalent to \(\sigma_i'=c_i\sigma_i\).

## Verification

The accompanying `verify.py` checks the constant objective offset and exact analytic gradient identities under arbitrary independent positive task rescaling.

It then replays Adam on the original and rescaled objectives from symmetry-related log-variance initializations and confirms identical model trajectories with a fixed log-variance translation.

A separate check verifies that reusing the same numerical log-variance initialization after nontrivial rescaling is not the symmetry-related state.

## Relationship to prior work

Kendall, Gal, and Cipolla derive uncertainty-weighted multi-task objectives with inverse-variance task terms and logarithmic uncertainty regularization. They explicitly motivate tasks with different units and scales and state that, in practice, the network predicts
\[
s=\log\sigma^2
\]
for numerical stability.

The inspected defining full text does not state the exact taskwise action
\[
L_i\mapsto q_iL_i,
\qquad
s_i\mapsto s_i+\log q_i,
\]
nor the resulting full trajectory conjugacy.

Later analytical work derives pointwise optimal uncertainty weights and documents substantial inertia when learned uncertainty parameters start from poor initialization. That is consistent with the stationary transformation law above but does not state the exact shifted-initialization equivalence of the coupled model-and-uncertainty dynamics.

Recent scale-mismatch experiments report that standard Kendall-style weighting can degrade when losses are rescaled while conventional initialization is retained. The theorem does not contradict that observation: changing loss units without translating the uncertainty initialization starts from a different gauge representative, and later work shows that uncertainty parameters can adapt slowly.

Focused published-record searches for log-variance gauge symmetry, independent task-rescaling conjugacy, and shifted-initialization trajectory equivalence did not identify an implication-equivalent result.

## Limitations

Absolute-value regularization or constraints on the uncertainty variables break optimizer-level conjugacy.

The theorem applies to multiplicative loss rescaling, not additive offsets.

The classification statement concerns the source's simplified approximate objective.

The result establishes a structural invariance and initialization rule, not empirical optimality, calibration, or fast adaptation.

## References

1. Alex Kendall, Yarin Gal, and Roberto Cipolla, “Multi-Task Learning Using Uncertainty to Weigh Losses for Scene Geometry and Semantics,” arXiv:1705.07115v1, first submitted 2017-05-19; CVPR 2018.
2. Lukas Kirchdorfer, Cathrin Elich, Simon Kutsche, Heiner Stuckenschmidt, Lukas Schott, and Jan M. Köhler, “Analytical Uncertainty-Based Loss Weighting in Multi-Task Learning,” arXiv:2408.07985v1, 2024.
3. Lukas Kirchdorfer and coauthors, “Investigating Uncertainty Weighting for Multi-Task Learning: Insights and Analytical Alternative,” International Journal of Computer Vision, published 2025.
