# GaLore can spend an entire refresh block blind to the current gradient
## Finding

GaLore periodically recomputes a low-rank gradient subspace and reuses it between refreshes. Even on the simplest isotropic strongly convex quadratic, that reuse can create exact blocks in which the projected gradient is zero although the full gradient is nonzero.

Let
\[
F(W)=\frac12\lVert W\rVert_F^2,
\qquad
W\in\mathbb R^{m\times m}.
\]
This objective is \(1\)-smooth and \(1\)-strongly convex.

Use the GaLore projection wrapper with plain SGD as the base optimizer, one-sided left projection, scale \(1\), learning rate \(1\), projection rank \(r\), and refresh period
\[
T\ge2.
\]
Assume
\[
m=Kr
\]
for an integer
\[
K\ge2.
\]
Initialize
\[
W_0=\operatorname{diag}(a_1,\ldots,a_m),
\qquad
a_1>\cdots>a_m>0.
\]

At a refresh step, GaLore takes the top \(r\) left singular vectors of the current gradient. Between refreshes it reuses the same projector. With plain SGD, the projected-back update is
\[
W_{t+1}=W_t-P_tP_t^\top W_t.
\]

Then the trajectory is exact. At
\[
t=kT,
\qquad
k=0,\ldots,K-1,
\]
the projector spans
\[
e_{kr+1},\ldots,e_{(k+1)r},
\]
and the single update annihilates precisely those \(r\) diagonal entries.

For every
\[
j=1,\ldots,T-1
\]
and every block before the last,
\[
P_{kT}^\top\nabla F(W_{kT+j})=0
\]
while
\[
\nabla F(W_{kT+j})\ne0.
\]
Therefore GaLore makes exactly
\[
\boxed{T-1}
\]
consecutive no-op parameter updates after each active refresh.

Equivalently,
\[
\boxed{
\frac{\lVert P_{kT}^\top\nabla F(W_{kT+j})\rVert_F}
{\lVert\nabla F(W_{kT+j})\rVert_F}=0
}.
\]
The stale subspace retains none of the current gradient, even though it was the exact top-\(r\) singular subspace at the preceding refresh.

The final nonzero block is removed at
\[
t=(K-1)T,
\]
so GaLore reaches the minimizer after exactly
\[
\boxed{(K-1)T+1}
\]
updates.

By contrast, ordinary full-gradient descent with the same unit step satisfies
\[
W_1=W_0-\nabla F(W_0)=0.
\]
Thus a condition-number-one problem that full-gradient descent solves in one step can require a refresh-limited staircase of
\[
(K-1)T+1
\]
GaLore updates.

For
\[
m=2r,
\]
the contrast is already
\[
1
\quad\text{versus}\quad
T+1
\]
updates, with an exact block of \(T-1\) zero updates in between.

## Assumptions and scope

The theorem concerns the GaLore projection mechanism with plain SGD as the base optimizer. The defining paper presents GaLore as optimizer-independent and gives a generic project-update-project-back wrapper before specializing to Adam.

The projection is the paper's one-sided left projector for a square weight matrix. The scale factor and SGD learning rate are both \(1\).

The refresh period is fixed and satisfies
\[
T\ge2.
\]

The result is deterministic. It does not concern stochastic-gradient noise or optimizer-state transport across subspaces.

The objective is deliberately isotropic, isolating projector staleness from conditioning, stochasticity, and nonconvexity.

## Proof

Because
\[
\nabla F(W)=W,
\]
the initial gradient is diagonal with strictly ordered positive singular values. Hence its top-\(r\) left singular vectors are uniquely
\[
e_1,\ldots,e_r.
\]
Let
\[
P_0=[e_1,\ldots,e_r].
\]
The unit projected SGD update gives
\[
W_1
=
W_0-P_0P_0^\top W_0
=
\operatorname{diag}(0,\ldots,0,a_{r+1},\ldots,a_m).
\]

GaLore reuses \(P_0\) for the next \(T-1\) steps. Every remaining nonzero row of \(W_1\) is orthogonal to \(P_0\), so
\[
P_0^\top W_1=0.
\]
The projected gradient is therefore zero, giving
\[
W_2=\cdots=W_T=W_1.
\]

At step \(T\), the refreshed top-\(r\) left singular vectors are
\[
e_{r+1},\ldots,e_{2r}.
\]
That update annihilates the next diagonal block.

Inductively, at refresh
\[
t=kT
\]
all previously selected coordinates are zero and the remaining positive entries preserve their original strict ordering. The refreshed projector therefore selects
\[
e_{kr+1},\ldots,e_{(k+1)r},
\]
the active update kills that block, and the reused projector sees zero compact gradient for the following \(T-1\) steps.

There are exactly
\[
K=m/r
\]
active refresh blocks. The final active update occurs at
\[
t=(K-1)T,
\]
so
\[
W_{(K-1)T+1}=0.
\]

Full-gradient descent with unit step satisfies
\[
W_1=W_0-W_0=0.
\]
This proves the comparison.

## Verification

The accompanying `verify.py` recomputes the top-\(r\) singular subspace at every refresh and replays the project-update-project-back recurrence for several dimensions, ranks, refresh periods, and strictly ordered diagonal initializations.

It checks each active block, every exact no-op interval, the zero current-gradient retention ratio, and the closed convergence time.

The computation is a transcription guard. The theorem is proved by induction above.

## Relationship to prior work

Zhao and coauthors introduce GaLore as a gradient low-rank projection wrapper. Their generic algorithm separates projection, a base optimizer update, and projection back to the original parameter space. Their multi-subspace construction recomputes the projector periodically by SVD.

The defining paper already warns that infrequent subspace changes may leave the algorithm stuck in a region that is no longer important to optimize, and notes that good progress in the designated subspace does not imply good overall performance. It does not give an exact deterministic construction in which the compact gradient is identically zero for the entire remainder of every refresh block, nor the resulting closed convergence-time law.

He and coauthors later observe that for a precomputed low-rank projector there can exist a nonzero gradient whose projection is exactly zero, and they establish deterministic GaLore convergence under additional assumptions. Their general nullspace observation does not establish that GaLore's own top-singular-vector projector can become exactly orthogonal to the next deterministic gradient after one valid update on a condition-number-one quadratic. Their deterministic convergence result is compatible with the finite dead intervals proved here.

Later subspace-tracking and adaptive-switching work motivates more responsive changes of the gradient subspace. Those developments reinforce the relevance of projector staleness, but the inspected public records did not state this exact staircase law.

## Limitations

The base optimizer is plain SGD rather than Adam.

The unit step exposes exact annihilation. Nearby steps produce near-dead rather than exactly dead intervals; that perturbation analysis is not claimed.

The initialization is diagonal with strictly ordered positive entries and
\[
m/r
\]
an integer.

The theorem is a worst-case structural diagnostic, not a prediction of practical language-model training.

## References

1. Jiawei Zhao, Zhenyu Zhang, Beidi Chen, Zhangyang Wang, Anima Anandkumar, and Yuandong Tian, “GaLore: Memory-Efficient LLM Training by Gradient Low-Rank Projection,” arXiv:2403.03507v1, first submitted 2024-03-06; ICML 2024.
2. Yutong He, Pengrui Li, Yipeng Hu, Chuyan Chen, and Kun Yuan, “Subspace Optimization for Large Language Models with Convergence Guarantees,” arXiv:2410.11289v1, 2024; ICML 2025.
3. Sahar Rajabi, Nayeema Nonta, and Sirisha Rambhatla, “SubTrack your Grad: Gradient Subspace Tracking for Memory and Time Efficient Full-Parameter LLM Training,” arXiv:2502.01586, 2025.
