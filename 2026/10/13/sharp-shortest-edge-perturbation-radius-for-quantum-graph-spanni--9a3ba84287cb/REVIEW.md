# Review

## Correctness

PASS. Friedlander's connected Kirchhoff metric-graph determinant identity, as stated in Harrison--Weyand [1, Eq. (40)], and the weighted matrix-tree theorem yield the exact cotree polynomial in RESULT.md. Its summands are monotone in every length ratio. Adding a long edge raises the normalized average and adds a long factor to the complement weight of each existing spanning tree, while newly admitted spanning trees add nonnegative error. This establishes complete-graph extremality, and Cayley's count plus edge symmetry gives the displayed sharp polynomial. All boundary quantifiers are handled: the shortest edge is attained, the upper length cap is strict, ties at half integers are excluded, and \(n=2\) is separated. The exact-rational verifier independently checks the finite combinatorial identities, but does not certify the universal proof by enumeration.

## Originality

PASS relative to the inspected sources and searches, with residual indexing risk. Harrison--Weyand [1] has the general determinant identity and a much smaller sufficient radius, not a sharp extremal radius. The follow-up [2] treats one-edge perturbations of selected graphs and explicitly describes the \(n^{-n}\) scale as an expectation; it does not establish the simultaneous-edge, all-graph sharp theorem or fixed-topology tree-inclusion threshold. The comparison is mathematical: their identities are inputs, but their stated perturbation estimates do not imply the exact universal optimum without the cotree monotonicity and edge-addition argument. Searches for synonymous determinant-rounding, graph-cotree, and complete-graph-extremal formulations in published records found no theorem covering the claim.

## Value

PASS. Both sources identify the original length-spread hypothesis as excessively restrictive, and [2] explicitly motivates an improved all-graph window. The result supplies the **largest permissible universal perturbation radius** with its extremal graph and demonstrates the predicted \(n^{-n}\) order, while quantifying the stronger topology-specific radius through uniform spanning-tree edge-inclusion counts. This is a motivated sharp structural cutoff, not a re-tabulation of known eigenvalues or a normalization-only counterexample: every sharpness example actually has a distinguished shortest edge and nonuniform lengths.

## Closest sources and limitations

Primary: Harrison--Weyand, arXiv:2209.01284, Theorem 2 and Eq. (40). Closest follow-up: Harrison--Weyand, arXiv:2406.17965, Section 5 and Appendix A. Known determinant and matrix-tree identities are not asserted to be new. Only connected simple graphs, positive lengths, and standard Kirchhoff matching are covered, with the baseline equal to the actual minimum length; the observable also uses combinatorial degree information. Alternative unindexed equivalent sharp bounds remain a residual originality risk.

Self-review: passed. Independent audit: not yet performed.
