# Review of the box-corner disagreement theorem

## Correctness — PASS
The rank-one equilibrium formula is valid because \(K+L_0\) is positive definite. Its exact substitution into both fixed-edge and changed-edge energies produces a concave quadratic in the monotone quantity \(t/(1+rt)\), with strictly negative quadratic coefficient whenever the baseline edge contrast is nonzero. Coordinatewise endpoint minimization therefore applies to every variable in an independent box and proves the multivariate conclusion by finite induction. Exact fraction computations verify both the subtle cancellation and the nontrivial mixed-corner example; numerical checks are not used as an infinite proof.

## Originality — PASS (best-knowledge, provisional priority)
The closest inspected work proves convexity of a **sum** of polarization and disagreement (Musco et al., arXiv:1712.09948; Yi–Patterson, arXiv:1911.11338), studies polarization instead of disagreement under changed edges (Rácz–Rigobon, arXiv:2206.08996), or minimizes disagreement while holding current opinions fixed (Chitra–Musco, arXiv:1906.08772). None yields the theorem that the *equilibrium* disagreement alone, optimized with independent box-bounded tie strengths, has an all-endpoint optimum. Prior results on rank-one updates and graph-dependent quadratic forms are acknowledged; novelty is the exact sign/shape cancellation and its simultaneous box-corner implication. Research-record searches for equivalent terms, broader coverage and optimization parameters surfaced no matching statement. A stronger unlocated abstract matrix-optimization theorem remains a residual risk; literature absence is not a proof of priority.

## Value — PASS
This addresses an operationally natural but nonconvex tie-strength design problem and rules out the need for intermediate strengths under independent bounds; its sharp boundary is the explicit counterexample that the optimal endpoint pattern can be mixed and that the response may initially increase before decreasing. It is not merely renaming a familiar objective or sampling a tiny arbitrary case: the statement governs every finite undirected graph, heterogeneous positive stubbornness and every box of ties, and gives a concrete discrete reduction. It does not claim efficient combinatorial optimization under the resulting exponential corner set.

## Scope and risks
Pure equilibrium edge disagreement only; diagonal positive stubbornness; symmetric attractive edges; box-only constraints. Does not extend to jointly constrained edges, edge-cost objectives, directed networks or fixed-opinion administrator subproblems. Publication priority remains subject to external specialist checking.

Self-review: passed. Independent audit: not yet performed.
