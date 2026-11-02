# Scientific review of the six- through nine-vertex cycle bound

## Correctness — PASS

The normalization uses only the inequalities \(\operatorname{Var}(|f|)\le\operatorname{Var}(f)\), translation equivariance for nonnegative inputs, and rotation symmetry. The sign expansion of edge variation and the positive-radius/negative-majorant decomposition are identities at fixed input, not relaxations. The primal programs contain every branch and exactly encode the variation unit ball. All \(53860\) rational dual vectors were verified by reconstructing the matrices and testing \(1039232\) integer-scaled dual coordinate inequalities. Weak duality proves the uniform upper bounds, and direct point-mass calculations prove sharpness. Numerical linear programming was used to discover certificates, but is not an assumption of their verification.

## Originality — PASS, qualified

Closest inspected work is González-Riquelme, Kovač and Madrid (arXiv:2603.12462), which explicitly completes four-vertex graphs and tabulates five-vertex cases. Its general graph theorem concerns complete graphs, not cycles. González-Riquelme and Madrid (arXiv:2005.03146) treat complete and star graphs and general lower bounds, and Bober et al. (arXiv:1005.3030) treat the integer lattice rather than finite cycles. A numerical formula \(1-1/n\) in another graph family does not imply the claimed upper bound for the centered operator on \(C_n\). Searches also considered equivalent graph-ball maximal formulations and the existing finite-cycle historical claims; none retrieved the four new upper bounds. Search incompleteness and possible older unindexed special-case computations remain a risk.

## Mathematical value — PASS

This supplies sharp, attained finite-graph variation constants for two complete nontrivial cycle diameter levels: \(C_6,C_7\) of diameter \(3\), and \(C_8,C_9\) of diameter \(4\). This is a natural extension of the documented complete graph-size \(\le5\) census and tests the point-mass sharpness mechanism where several distinct centered ball radii compete. The exact dual certificates resolve the problem for every real-valued input on these graphs; these are not isolated examples or numerical guesses. The result is a finite cutoff, not a theorem for all cycles.

## Limits and prior sources

The checker has been replayed from the included files. Its finite coverage is logically sufficient only because the proof supplies an exhaustive case reduction. General-size cycles, weighted measures and nonunit variation exponents remain untreated. Most relevant primary sources: arXiv:1005.3030, arXiv:2005.03146 and arXiv:2603.12462. The exact date of the first listed source is verified on its arXiv submission-history page.

Self-review: passed. Independent audit: not yet performed.
