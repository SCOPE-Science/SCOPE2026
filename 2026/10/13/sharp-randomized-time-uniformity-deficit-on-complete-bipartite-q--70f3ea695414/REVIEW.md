# Scientific review: complete-bipartite time-sampling optimality

## Correctness — PASS

The exact polynomial identity \(A^3=abA\) yields every transition probability and reduces arbitrary time distributions to two cosine moments with the exact feasible set \(u^2\le v\le1\). The derived Hessian is positive definite for every total order at least three. For nontrivial parts, monotonicity in \(v\), the derivative cubic, and its boundary sign prove the global optimum, including the balanced threshold. A supporting-hyperplane certificate proves the separate star formula; the two exceptional small graphs are checked directly. The attached standard-library checker independently reconstructs transition entries and verifies closed forms over finite families. Finite checks corroborate, but do not replace, the proof for all part sizes and probability laws.

## Originality — PASS, with residual risk

Baptista, Coutinho, and Marques, arXiv:2308.16378v1, Section 3.1, prove a coarse exclusion for sufficiently large complete bipartite graphs and list the known exact-mixing small examples. Their Section 3.2 constructs randomized exact mixing on the three-vertex path. Those facts are credited, not recycled as novel. Sections 2–4 and concluding discussion in that full primary text were examined for a global optimal Frobenius error, a deterministic-optimality theorem, or a balanced-graph protocol transition; none was found. Coutinho and Guo's 2024 quantum-walk survey develops nearby sampling questions but does not state this quantitative classification. The novelty assessment concerns the sharp loss, optimizer characterization, and threshold, not the known existence of exact averages. The principal residual risk is an equivalent result under general spectral convex optimization terminology.

## Value — PASS

When arbitrary observation-time distributions cannot achieve uniform mixing, an exact optimization criterion is needed to quantify how close quantum transport can come. The theorem answers that question for a fundamental infinite graph family, establishes when randomizing time is provably useless for this criterion, and identifies the nonobvious sharp boundary at which optimal global fidelity requires zero transport across the two parts. This is a complete resource and fidelity classification under a clear physical measurement protocol, not merely a new expression for a familiar special case.

## Boundaries

The theorem addresses a global unnormalized squared-Frobenius loss for the unweighted adjacency Hamiltonian. It gives neither universal optimality for other norms nor exact quantum channel synthesis, and no claim of independent audit is made. The comparison with unindexed or inaccessible literature is necessarily incomplete.

Self-review: passed. Independent audit: not yet performed.
