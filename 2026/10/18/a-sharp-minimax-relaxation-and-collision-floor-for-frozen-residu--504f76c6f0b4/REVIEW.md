# Scientific review: frozen residual-weighted Kaczmarz batches

## Correctness — PASS

For independent frozen row choices, multinomial marginals give the exact conditional squared-error moment (equation (1) in `RESULT.md`). The cubic-simplex extremal lemma is proved, not numerically assumed: holding a pair sum fixed makes the objective affine in the pair product, and a support-minimal maximizer must be equal on its positive support. Convexity across reciprocal support sizes restricts global maximizers to the uniform distribution or a vertex. Their exact quadratic envelope yields the unique relaxation in both regimes, the sharp strict contraction window, and the positive one-batch concurrency limit. The computations in `verify.py` independently enumerate multinomial counts and check rational arithmetic; they are corroboration rather than the proof of the infinite parameter claim. Boundary cases \(d=2\), \(k=1\), equality in the phase inequality, zero residual, and \(\beta=2/k\) are explicitly handled.

## Originality — PASS, subject to bibliographic limitations

The primary 2026 residual-weighted Jacobi paper analyzes one-step concentration and asynchronous stochastic updates. Its collision discussion and the subsequent 2026 Kaczmarz study provide the motivation but not the sharp, all-dimension, frozen-batch minimax law. The classical minibatch averaging paper gives relaxation bounds and fixed row-probability designs; its result does not directly imply the state-dependent residual sampling extremal lemma or the collision floor. The closest related numerical statements were compared by model, update semantics, parameters, and implication, not keywords alone. Directly related formulas in unindexed studies cannot be ruled out, and independent literature validation remains absent.

## Value — PASS

The theorem gives an exact design rule for the snapshot-collision regime rather than a generic concentration bound. It identifies a nontrivial phase change in the unique minimax step, a sharp universal safety range, and a gap that persists between residual-adaptive and uniform sampling even as the batch size grows indefinitely. The relevant application is assessing when residual-greedy sampling and parallel frozen reads work against each other; the result is not represented as a real-machine speedup theorem.

## Closest literature and limitations

E. Coleman, arXiv:2606.01232 (first public submission 2026-05-31), Sections 3–6; E. Coleman, arXiv:2607.08313 (first public submission 2026-07-09), Sections 2–6; L. Tondji and D. Lorenz, DOI:10.1007/s11075-022-01473-x, Sections 1, 4 and 5. These sources develop adaptive sampling, snapshot interference, and minibatch averaging, respectively. Their results do not explicitly determine the exact state-dependent worst-case one-batch relaxation across all dimensions and batch sizes. The claim is restricted to orthogonal identity systems, exact arithmetic, iid within-batch row draws and additive corrections from a common frozen residual. It does not cover live reads, non-orthogonal rows or the best long-run rate under repeated batches.

Self-review: passed. Independent audit: not yet performed.
