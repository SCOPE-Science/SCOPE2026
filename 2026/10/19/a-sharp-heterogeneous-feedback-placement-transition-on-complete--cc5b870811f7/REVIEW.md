# Mathematical review: heterogeneous feedback on complete bipartite graphs

## Correctness — PASS

The matrix-tree/rank-two determinant derivation is valid for positive gains and a connected unit-weight graph; the explicit pseudoinverse kernels follow from the four Laplacian eigenspaces. The exact identities for the differences between all four leader-placement orbits have been reconstructed algebraically and verified by rational symbolic computation. The comparison denominators are positive. Strict positivity of the factor in the same-part comparison and the signs of the mixed-orientation comparison reduce the global optimum to just two candidate orbits. The remaining comparison is controlled by a quadratic with negative linear and constant coefficients and (when its leading coefficient is positive) one positive root. The direct diagonal evaluation establishes that the positive threshold strictly exceeds the weaker gain. The seven-vertex onset follows from the integer inequalities. A standalone verifier confirms the rational identities and selected direct inverses; the universal conclusions follow from the analytical inequalities, not numerical sampling.

## Originality — PASS, with limits

Lin–Fardad–Jovanović, arXiv:1302.0450, Sections II–III, formulates arbitrary positive feedback strengths and develops relaxation/greedy methods and low-rank inverse updates, but does not establish a complete bipartite, all-size, all-gain global placement classification. Fitch–Leonard, arXiv:1407.1569, explicitly assumes equal leader feedback strengths and solves cycle/path special cases; the unequal-gain relocation threshold cannot be read off as its equal-gain special case. Clark–Bushnell–Poovendran, arXiv:1208.0946, concerns link disturbances and supermodular selection rather than the specified independent state-noise objective. Related complete-bipartite theorems with three or four leaders, optimal *continuous* gain allocation, and discounted hitting objectives do not imply the two-distinct-leader, prescribed-unequal-gain switching law. Searches for the alternative phrasings of this claim and associated formulas did not locate an equivalent published statement. Searches alone do not establish novelty, and a specialized equivalent calculation outside the inspected literature remains possible.

## Value — PASS

The objective is a physically interpretable steady-state variance and the graphs are basic heterogeneous-degree communication networks. The sharp result gives a complete placement decision with no combinatorial search, discovers a true qualitative relocation transition governed jointly by network imbalance and leader-gain heterogeneity, and identifies the smallest possible seven-vertex instance with a simple exact radical threshold. The effect is not a monotone re-expression of the known equal-gain optimum, since the optimal leader-part allocation changes from two-in-the-small-part to a split design for sufficiently unequal gains. No general-graph or large-leader-count impact is asserted.

## Residual limitations

Only unit-weight complete bipartite graphs with part sizes \(2\le p<q\), two distinct leaders, prescribed positive finite gains and isotropic state noise are proved. Comprehensive bibliographic uniqueness and independent validation remain unestablished. The result has not been extended to weighted graphs or unequal disturbance intensities.

Self-review: passed. Independent audit: not yet performed.
