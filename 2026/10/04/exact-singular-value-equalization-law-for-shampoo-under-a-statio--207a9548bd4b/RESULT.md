# Exact singular-value equalization law for Shampoo under a stationary gradient
## Finding

Consider the matrix form of Shampoo with the source initialization
\[
L_0=\varepsilon I_m,
\qquad
R_0=\varepsilon I_n,
\qquad
\varepsilon>0,
\]
and suppose the same nonzero matrix gradient is observed at every iteration:
\[
G_t=G\in\mathbb R^{m\times n}.
\]
This stationary-gradient regime occurs exactly for a linear objective and is also a natural local stress test for the preconditioner.

Let the reduced singular value decomposition be
\[
G=U\operatorname{diag}(\sigma_1,\ldots,\sigma_r)V^\top,
\]
where
\[
\sigma_1\ge\cdots\ge\sigma_r>0.
\]
The source accumulators are then
\[
L_t=\varepsilon I_m+tGG^\top,
\qquad
R_t=\varepsilon I_n+tG^\top G.
\]
The Shampoo direction
\[
P_t=L_t^{-1/4}GR_t^{-1/4}
\]
has the exact reduced SVD
\[
P_t
=
U\operatorname{diag}
\left(
\frac{1}{\sqrt{t+\varepsilon/\sigma_1^2}},
\ldots,
\frac{1}{\sqrt{t+\varepsilon/\sigma_r^2}}
\right)V^\top.
\]

Thus every active singular mode is driven toward the same magnitude \(t^{-1/2}\). The damping parameter does not change the limiting geometry; it gives each mode a transient delay
\[
\tau_i=\frac{\varepsilon}{\sigma_i^2}.
\]
Small singular modes have the longest delay.

Let
\[
\kappa_G=\frac{\sigma_1}{\sigma_r}.
\]
The condition number of the nonzero singular spectrum of the preconditioned direction is exactly
\[
\kappa(P_t)^2
=
1+
\frac{\varepsilon(\kappa_G^2-1)}
{\varepsilon+t\sigma_1^2}.
\]
Therefore, whenever \(\kappa_G>1\), the anisotropy decreases strictly at every step and converges to one.

For any desired spectral condition target
\[
1<K<\kappa_G,
\]
the exact continuous threshold is
\[
t
\ge
\frac{\varepsilon(\kappa_G^2-K^2)}
{(K^2-1)\sigma_1^2}.
\]
For integer iteration counts, the first admissible iteration is the ceiling of the right-hand side, with the usual minimum of one because Shampoo updates begin at \(t=1\).

The normalized direction converges to the partial polar factor:
\[
\sqrt t\,P_t\longrightarrow UV^\top.
\]
The convergence has the exact spectral-norm error
\[
\left\|
\sqrt t\,P_t-UV^\top
\right\|_2
=
1-
\left(
1+
\frac{\varepsilon}{t\sigma_r^2}
\right)^{-1/2}.
\]
The slowest mode is exactly the smallest nonzero singular value.

There is also an exact trajectory consequence on a linear loss. With constant learning rate \(\eta>0\),
\[
W_{t+1}=W_t-\eta P_t.
\]
For each active singular mode,
\[
\sum_{t=1}^T
\frac{1}{\sqrt{t+\tau_i}}
=
2\sqrt T+O(1),
\]
so
\[
\frac{W_1-W_{T+1}}{\sqrt T}
\longrightarrow
2\eta UV^\top.
\]
Thus accumulated Shampoo asymptotically moves in a polar direction even though its state retains the full history of repeated gradients.

## Assumptions and scope

The theorem uses Algorithm 1 of the defining Shampoo paper in the matrix case, including additive accumulation and positive identity damping.

The gradient is assumed constant across iterations. This is exact for a linear loss and isolates the action of the preconditioner from changing gradient geometry.

The rank \(r\) may be smaller than \(\min(m,n)\). The partial polar factor \(UV^\top\) is defined on the nonzero singular subspaces supplied by the reduced SVD.

No momentum, exponential moving average, grafting, delayed inverse-root refresh, or block partitioning is included. Those are later practical variants rather than the source Algorithm 1 analyzed here.

## Proof

From the source recurrence and the stationary gradient assumption,
\[
L_t
=
\varepsilon I_m+tGG^\top,
\qquad
R_t
=
\varepsilon I_n+tG^\top G.
\]
Using the reduced SVD of \(G\), the active eigenspaces of both accumulators are the left and right singular spaces. Therefore
\[
L_t^{-1/4}U
=
U\operatorname{diag}
\left(
(\varepsilon+t\sigma_i^2)^{-1/4}
\right),
\]
and similarly
\[
R_t^{-1/4}V
=
V\operatorname{diag}
\left(
(\varepsilon+t\sigma_i^2)^{-1/4}
\right).
\]
Multiplication gives
\[
P_t
=
U\operatorname{diag}
\left(
\frac{\sigma_i}{\sqrt{\varepsilon+t\sigma_i^2}}
\right)V^\top
=
U\operatorname{diag}
\left(
\frac{1}{\sqrt{t+\varepsilon/\sigma_i^2}}
\right)V^\top.
\]

The scalar map
\[
\sigma\mapsto
\frac{\sigma}{\sqrt{\varepsilon+t\sigma^2}}
\]
is strictly increasing for \(\varepsilon>0\), so the largest and smallest nonzero singular values of \(P_t\) correspond to \(\sigma_1\) and \(\sigma_r\). Hence
\[
\kappa(P_t)^2
=
\kappa_G^2
\frac{\varepsilon+t\sigma_r^2}
{\varepsilon+t\sigma_1^2}.
\]
Using \(\sigma_1^2=\kappa_G^2\sigma_r^2\) yields
\[
\kappa(P_t)^2
=
1+
\frac{\varepsilon(\kappa_G^2-1)}
{\varepsilon+t\sigma_1^2}.
\]
This is strictly decreasing in \(t\) when \(\kappa_G>1\). Solving \(\kappa(P_t)\le K\) gives the stated threshold.

For the polar limit, each normalized singular value is
\[
\sqrt t\,s_i(P_t)
=
\left(
1+
\frac{\varepsilon}{t\sigma_i^2}
\right)^{-1/2}.
\]
All approach one. The largest deviation from one occurs at \(\sigma_r\), which proves the exact spectral-norm error formula.

Finally,
\[
s_i(P_t)
=
(t+\tau_i)^{-1/2}.
\]
The integral comparison for this decreasing positive sequence gives
\[
\sum_{t=1}^T(t+\tau_i)^{-1/2}
=
2\sqrt T+O(1)
\]
for each fixed \(\tau_i\). Substituting into the SVD expansion of the cumulative update proves the scaled displacement limit.

## Verification

The accompanying `verify.py` constructs random matrix gradients with prescribed singular values, forms the source Shampoo accumulators directly, computes inverse fourth roots by eigendecomposition, and compares the resulting update with the closed-form singular-value law.

It also checks the exact condition-number formula, the target equalization time, the polar-limit error, and the scaled cumulative displacement.

The numerical calculations are transcription guards. The formulas for every iteration and the asymptotic trajectory statement are proved analytically above.

## Relationship to prior work

Gupta, Koren, and Singer introduced Shampoo with separate left and right accumulated second-moment matrices. Their matrix algorithm initializes both factors by positive identity damping and uses inverse fourth roots on the two sides of the current gradient. The paper remarks that the quarter-power construction gives the familiar order \(t^{-1/2}\) step-size decay and analyzes the resulting structured preconditioner through Kronecker products and matrix inequalities.

Bernstein and Newhouse later showed that Shampoo with accumulation disabled maps a single gradient to its semi-orthogonal polar factor and interpreted that idealized update as spectral-norm steepest descent. That result removes historical accumulation before making the polar identification.

More recent work decomposes practical accumulated Shampoo into its Kronecker eigenbasis and eigenvalue scaling and studies grafting, stale eigensystems, and eigenvalue correction. The inspected analysis does not specialize the original additive accumulator to a stationary gradient or give the exact finite-time singular-spectrum equalization law above.

The present finding bridges the source accumulated algorithm and the later polar interpretation: under a stationary gradient, ordinary additive Shampoo approaches the polar geometry continuously, with an exact damping-controlled equalization rate and an exact iteration threshold for any target condition number.

## Limitations

A stationary gradient is a deliberately controlled regime. It does not describe changing singular subspaces during nonlinear training.

The theorem addresses the original additive accumulator. Exponential moving averages have a different stationary limit and require a separate calculation.

Practical Shampoo often adds grafting and updates inverse roots only intermittently; these modify the realized update magnitude or introduce staleness.

The result describes gradient-spectrum equalization, not Hessian conditioning or a global convergence advantage on nonlinear objectives.

## References

1. Vineet Gupta, Tomer Koren, and Yoram Singer, “Shampoo: Preconditioned Stochastic Tensor Optimization,” arXiv:1802.09568v1, 2018.
2. Jeremy Bernstein and Laker Newhouse, “Old Optimizer, New Norm: An Anthology,” arXiv:2409.20325v1, 2024.
3. “Purifying Shampoo: Investigating Shampoo's Heuristics by Decomposing its Preconditioner,” arXiv:2506.03595v1, 2025.
