# Scientific review

## Correctness — PASS
The exact spectrum of every invariant stochastic chain has the four spectral types given in RESULT.md. The first two nonconstant types give a sharp minimax lower bound with a unique cross-weight optimizer. The remaining eigenvalue yields an exact nonempty permitted interval of core-edge weights. Symmetry averaging proves global optimality, and nonnegative averaging proves the all-optimizer edge-use necessities. The exact-rational and numerical verification script passed; finite tests do not prove the infinite-family classification.

## Originality — PASS, residual risk disclosed
Boyd, Diaconis, Parrilo and Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries* (arXiv:0709.0955v1), §5.4.2, is the closest primary source: it gives general complete multipartite spectral blocks and the exact complete-bipartite solution. That bipartite result already explains the optimum value when the independent class is at least as large as the clique; this branch is not claimed new in isolation. For a larger clique, the bipartite optimum is strictly worse, and no inspected primary statement yields the split-graph solution, full invariant optimizer interval, or two sharp edge-support transitions. Jafarizadeh's friendship-graph study concerns triangles sharing one hub, a different topology. The available search is not a proof of novelty; unindexed or inaccessible stronger work remains a material risk.

## Value — PASS
The exact design boundary is not a small numerical improvement: when the clique size increases with a fixed independent class, optimal SLEM approaches zero when clique-internal edges are available but approaches one when they are removed. The exact all-parameter optimizer class explains precisely when such edges must, may or cannot be used.

## Limitations and status
Only symmetric stochastic chains with uniform equilibrium and allowed zero off-diagonal weights are considered. No uniqueness of unrestricted optimizers is claimed. Finite verification supports rather than replaces the analytic proof. No independent validation has been conducted.

Self-review: passed. Independent audit: not yet performed.
