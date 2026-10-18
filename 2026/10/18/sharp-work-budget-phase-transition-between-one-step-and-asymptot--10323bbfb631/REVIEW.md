# Self-review

## Correctness — PASS

The claim is reconstructed with its full two-dimensional consistent-system assumptions, four masks, independent sampling, real unit row vectors, cost premium \(w>2\), and equal expected work \(0<c\le1\). The first objective is the top eigenvalue of an expected squared-error projector. The second is the Perron spectral radius of the exact covariance map, and the proof explicitly justifies its relationship to the root of the worst-initial-error finite-horizon expectation. The two objective functions are strictly minimized at balanced singleton probabilities for each fixed batch mass, then become affine functions of batch probability with different slope zeros. The rational example and stronger two-step reversal follow from exact projector algebra. `verify.py` executed from the packaged source, with finite rational and grid checks; the proof handles all real parameters and endpoints independently.

## Originality — PASS, subject to disclosed coverage risk

The closest accessible motivating manuscript is Xie–Yang, arXiv:2511.09872, particularly Theorem 5.1, Remark 5.2 and Appendix B. It states a joint-distribution optimization problem and develops general upper bounds, not the present exact two-target work-budget minimax classification. Its variable-size batches are nonempty, whereas the present model explicitly includes a zero-cost idle event. Mutný–Dereziński–Krause (2020) analyzes determinantal batch-size/cost decisions, not this four-mask exact horizon conflict. The same authors' October 2026 coordinate-descent paper, arXiv:2610.04685, is strongly relevant but only its abstract could be examined; potential stronger coverage cannot be excluded and must be revisited if its full text becomes available. Existing single-row rate identities and random projection results are ingredients, not the asserted new finding. Originality is not independently certified.

## Value — PASS

The paper-motivated choice of a joint batch distribution becomes a sharp natural optimization problem when updates have different work costs. The new classification is complete within that setting, with a nonempty parameter wedge in which two mathematically exact performance objectives prescribe incompatible optimizers. For \(w=4,c=1,r=3/5\), the optimal one-step policy achieves \(3/4\) rather than \(4/5\), but the singleton policy has asymptotic factor \(17/25\) rather than \(3/4\); the singleton policy overtakes by draw two and remains better thereafter. This supplies a rigorous small-dimensional stress test of myopic sampler objectives, not merely a recomputation of a known numerical table.

## Scope and residual risks

The result assumes a consistently solvable real two-row system, exact orthogonal projections, a fixed iid joint distribution, permitted idle updates, an abstract full-batch premium, and expected rather than hard cost budgeting. It does not prove wall-clock optimality, performance on higher-rank systems or adaptive samplers, or an equivalent statement for all stochastic coordinate schemes. A highly relevant 2026 full text remains uninspected and older equivalent formulations may exist. The scientific proof and verification are not an independent audit.

Self-review: passed. Independent audit: not yet performed.
