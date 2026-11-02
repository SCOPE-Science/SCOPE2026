# Review of strict geodesic unimodality on weighted trees

## Correctness — PASS

For every finite tree with positive conductances and one grounded vertex, the edge comparison follows from the rooted electrical Green matrix: its block on the opposite component changes by an exact rank-one \(r\mathbf1\mathbf1^\mathsf T\) term. The resulting difference \(J(v)-J(u)=r\mathcal B(u,v)\) has no hidden normalization. For two consecutive oriented edges, decomposing into the three intervening components gives a *strictly positive* formula for the increase of \(\mathcal B\), so one-dimensional signs along every tree path cannot change from positive to negative. This proves every local minimum is global and all minimizers are a single vertex or one adjacent pair. A postorder/preorder dynamic program computes exact objective values in linear arithmetic time. Exact matrix calculations were checked independently over 3,798 grounded inverses; finite tests were not used in place of proof.

## Originality — PASS, subject to residual risk

Fitch and Leonard (arXiv:1407.1569, first publicly posted July 7, 2014) identify information-centrality optimality for single leaders in first-order noisy consensus; its tree criterion is a sum of resistances, not the squared Green trace. Patterson, McGlohon and Dyagilev (arXiv:1412.6595) treat inverse-trace leader selection on paths and cycles by general minimum-cost path algorithms. Mackin and Patterson (arXiv:1905.09156) derive inverse-square second-order coherence and general submodular greedy selection, but their inspected treatment gives neither the strict tree-geodesic signed-gradient law nor this exact linear-time all-weighted-tree result. A closely related dissertation was identified by search but full-text retrieval failed; its exact implication cannot be excluded. No claim of exhaustive publication priority is made.

## Mathematical value — PASS

This is a general structural theorem for every finite positively weighted tree rather than a new parameter choice on a known small graph. It shows that a natural second-order network objective has no spurious neighbor-local optima, classifies all ties, and reduces exact single-leader selection to linear-time arithmetic without matrix inversions. The squared criterion is genuinely distinct from the standard first-order median criterion: on the resistance-weighted five-vertex path with edge resistances \(100,1,1,1\), the unique second-order optimum is vertex \(1\), not the first-order centroid vertex \(2\). The signed-edge-gradient property is stronger than a numerical experiment and applies even when the objective is not discretely convex.

## Closest literature and limitations

Only one ideal leader, trees and the inverse-square trace are proved. The higher-order coherence literature provides the target performance measure and approximation algorithms, not the structural law. Specialized material, including E. Mackin's thesis *Network Design for Optimal Performance under Consensus Dynamics* (institutional repository access refused), remains a residual originality risk. Independent audit and external validation have not been performed.

Self-review: passed. Independent audit: not yet performed.
