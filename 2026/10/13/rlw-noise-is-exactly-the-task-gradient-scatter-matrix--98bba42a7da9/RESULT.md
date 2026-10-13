# RLW noise is exactly the task-gradient scatter matrix
## Finding

Random Loss Weighting (RLW) samples a new simplex weight vector and uses the corresponding weighted task-gradient aggregate. For every exchangeable simplex weight law, the complete second-order geometry of that extra randomness is determined by the task-gradient disagreement matrix.

Fix
\[
T\ge2
\]
task gradients
\[
g_1,\ldots,g_T\in\mathbb R^d.
\]
Let
\[
\lambda=(\lambda_1,\ldots,\lambda_T)
\]
be an exchangeable random vector satisfying
\[
\lambda_i\ge0,
\qquad
\sum_{i=1}^T\lambda_i=1
\]
almost surely. Define
\[
v=\operatorname{Var}(\lambda_1),
\qquad
Z=\sum_{i=1}^T\lambda_i g_i,
\qquad
\bar g=\frac1T\sum_{i=1}^Tg_i.
\]

Then
\[
\boxed{
\operatorname{Cov}(Z)
=
\frac{vT}{T-1}
\sum_{i=1}^T
(g_i-\bar g)(g_i-\bar g)^\top
}.
\]

Thus the weight distribution controls only one scalar, \(v\). Its entire covariance eigenspace geometry is fixed by the centered task gradients.

The exact noise energy is
\[
\boxed{
\mathbb E\lVert Z-\bar g\rVert_2^2
=
\frac{v}{T-1}
\sum_{1\le i<j\le T}
\lVert g_i-g_j\rVert_2^2
}.
\]

When
\[
v>0,
\]
the covariance range is exactly
\[
\boxed{
\operatorname{range}\operatorname{Cov}(Z)
=
\operatorname{span}\{g_i-\bar g:1\le i\le T\}
}.
\]
Its nullspace is
\[
\boxed{
\left\{
u:
\langle u,g_1\rangle
=
\cdots
=
\langle u,g_T\rangle
\right\}.
}
\]
Therefore RLW's weight-sampling noise cannot perturb any direction on which all tasks have the same directional derivative.

There is also a sharp distribution-free amplitude bound. Every exchangeable simplex law satisfies
\[
\boxed{
0\le v\le\frac{T-1}{T^2}.
}
\]
The upper endpoint is attained if and only if the random weight vector is uniformly one-hot. Hence the constrained-Bernoulli task-sampling variant in the defining paper is the unique exchangeable simplex law with maximal covariance:
\[
\boxed{
\operatorname{Cov}(Z)
=
\frac1T
\sum_{i=1}^T
(g_i-\bar g)(g_i-\bar g)^\top.
}
\]

For two tasks the covariance is rank one whenever the gradients differ:
\[
\operatorname{Cov}(Z)
=
v(g_1-g_2)(g_1-g_2)^\top.
\]
So all exchangeable two-task RLW laws inject their weight noise along the single disagreement direction.

At an equal-weight stationary cancellation,
\[
\bar g=0,
\]
nonzero task gradients can still produce nonzero RLW covariance. Conversely, if
\[
g_1=\cdots=g_T,
\]
the covariance vanishes for every weight law, no matter how random the weights are.

Finally, the extra noise is isotropic on its own support exactly when the centered task gradients form a tight frame for their span. Generic task configurations therefore produce anisotropic rather than isotropic RLW noise.

## Assumptions and scope

The result is conditional on the current deterministic task gradients. Mini-batch sampling noise is not included; the theorem isolates only the extra randomness introduced by sampling RLW weights.

Exchangeability means that permuting the task labels does not change the weight distribution. This includes the defining code path based on identical independently sampled logits followed by softmax, and the constrained-Bernoulli one-task-at-a-time variant.

The theorem requires only a simplex weight vector with a finite second moment. It does not assume a particular neural-network architecture or loss geometry.

The result characterizes covariance and does not claim that second moments alone determine long-run generalization or local-minimum escape.

## Proof

Exchangeability and the simplex constraint give
\[
\mathbb E\lambda_i=\frac1T.
\]
All diagonal covariance entries are therefore the same number \(v\), and all off-diagonal entries equal one common number \(b\).

Since
\[
\sum_i\lambda_i=1
\]
almost surely,
\[
0
=
\operatorname{Var}\left(\sum_i\lambda_i\right)
=
Tv+T(T-1)b.
\]
Hence
\[
b=-\frac{v}{T-1}.
\]
Writing
\[
P
=
I-\frac1T\mathbf1\mathbf1^\top,
\]
we obtain
\[
\operatorname{Cov}(\lambda)
=
\frac{vT}{T-1}P.
\]

Let \(G\) be the matrix whose columns are \(g_i\). Then
\[
Z=G\lambda
\]
and
\[
\operatorname{Cov}(Z)
=
G\operatorname{Cov}(\lambda)G^\top
=
\frac{vT}{T-1}GPG^\top.
\]
But
\[
GPG^\top
=
\sum_i(g_i-\bar g)(g_i-\bar g)^\top,
\]
which proves the covariance formula.

Taking the trace gives
\[
\mathbb E\lVert Z-\bar g\rVert_2^2
=
\frac{vT}{T-1}
\sum_i\lVert g_i-\bar g\rVert_2^2.
\]
The standard pairwise identity
\[
\sum_i\lVert g_i-\bar g\rVert_2^2
=
\frac1T
\sum_{i<j}\lVert g_i-g_j\rVert_2^2
\]
proves the energy formula.

For \(v>0\), the covariance is a positive scalar multiple of \(AA^\top\), where the columns of \(A\) are \(g_i-\bar g\). Therefore its range is the column span of \(A\), and \(u\) is in its kernel exactly when
\[
\langle u,g_i-\bar g\rangle=0
\]
for every \(i\), equivalently when all \(\langle u,g_i\rangle\) are equal.

For the sharp variance bound, the simplex constraint gives
\[
0\le\lambda_i\le1.
\]
Thus
\[
\mathbb E\lambda_i^2
\le
\mathbb E\lambda_i
=
\frac1T,
\]
so
\[
v
=
\mathbb E\lambda_i^2-\frac1{T^2}
\le
\frac{T-1}{T^2}.
\]
Equality requires
\[
\lambda_i^2=\lambda_i
\]
almost surely for every coordinate, so every coordinate is binary. Because the coordinates sum to one, each realization is one-hot. Exchangeability makes the selected index uniform. The converse is immediate.

The tight-frame statement follows because a positive semidefinite operator is scalar on its range exactly when
\[
\sum_i(g_i-\bar g)(g_i-\bar g)^\top
\]
is a scalar multiple of the orthogonal projector onto the centered-gradient span.

## Verification

The accompanying `verify.py` constructs finite exchangeable weight laws by averaging over all permutations of several simplex vectors. It checks the exact weight covariance, the task-gradient covariance formula, pairwise noise energy, covariance rank and kernel, the sharp one-hot upper bound, and the two-task specialization.

These computations are transcription guards. The identities and sharpness statements are proved algebraically above.

## Relationship to prior work

Lin, Ye, Zhang, and Tsang introduce RLW by sampling random loss weights, normalizing them onto the simplex, and taking the corresponding weighted aggregate gradient. Their analysis explicitly treats the resulting method as doubly stochastic and argues that the extra randomness can improve local-minimum escape and generalization. Their theoretical local-minimum discussion abstracts the randomness as a generic zero-mean noise with bounded intensity.

The defining paper uses several symmetric random-weight constructions. Its constrained-Bernoulli option selects only one task for an update, making it the one-hot endpoint identified by the sharp variance theorem above. The paper does not state the exact covariance matrix of the weight-induced gradient noise, its disagreement-subspace support, or the maximality of the one-hot law among exchangeable simplex distributions.

Kurin and coauthors later compare RLW with specialized multi-task optimizers and explicitly connect random scalarization to stochastic regularization. Their inspected analysis likewise does not resolve the covariance support or show that every exchangeable RLW law has the same second-order eigendirections.

The covariance law also distinguishes RLW from generic additive isotropic noise: random task weights cannot inject variance in a direction where all tasks already agree.

Focused published-record searches for RLW covariance, task-disagreement scatter, weight-noise support, and exchangeable simplex weighting did not identify an implication-equivalent result.

## Limitations

Only weight-sampling noise is characterized. Data mini-batch noise adds another covariance component and can have directions outside the task-disagreement span.

Exchangeability is essential for the universal one-scalar covariance law. Deliberately task-asymmetric random weight distributions can have a more general covariance matrix.

The result is instantaneous and second-order. It does not prove that maximizing RLW covariance improves optimization or generalization.

The tight-frame isotropy criterion describes covariance geometry, not higher moments of the weight distribution.

## References

1. Baijiong Lin, Feiyang Ye, Yu Zhang, and Ivor W. Tsang, “Reasonable Effectiveness of Random Weighting: A Litmus Test for Multi-Task Learning,” arXiv:2111.10603v1, first submitted 2021-11-20.
2. Vitaly Kurin, Alessandro De Palma, Ilya Kostrikov, Shimon Whiteson, and M. Pawan Kumar, “In Defense of the Unitary Scalarization for Deep Multi-Task Learning,” arXiv:2201.04122v1, 2022; NeurIPS 2022.
