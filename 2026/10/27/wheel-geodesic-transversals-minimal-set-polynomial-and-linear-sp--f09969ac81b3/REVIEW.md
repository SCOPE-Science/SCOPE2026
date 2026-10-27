# Mathematical review

## Correctness: PASS

The finite wheel is diameter two and every edge extends into a two-edge geodesic, so all maximal paths are explicitly accounted for. Omission of the hub is equivalent to an omitted rim clique, giving the second branch. With the hub selected, cyclic gap lengths \(0,1,2\) characterize all transversals. The six allowed adjacent gap pairs characterize essential rim selections, and the additional hub-essentiality argument completes inclusion minimality for \(n\ge6\). The trace matrix and the \(n/k\) rooting correction are justified; the range and minimum counts follow by exact combinatorial arguments. Exhaustive vertex-subset checks verified the complete minimal polynomial through rim length twelve and the all-set polynomial through rim length ten. No finite computation is used in place of the general proof.

## Originality: PASS with priority risks

The geodesic-transversal definition and complexity, the scalar wheel transversal number, and the general join-factor dichotomy are established in the 2021–2022 sources and are not claimed. A review of the relevant full foundational preprint and the full join-product preprint (especially its join theorem and wheel discussion), together with indexed mathematical findings and searches for maximal shortest-path cover aliases and cyclic three-path cover enumeration, did not identify the complete two-polynomial, minimality-spectrum, and exact minimum-set census. The 2021 published wheel-value article was accessible through indexed sections but not fully available during this comparison; an unindexed equivalent hypergraph enumeration remains a risk. The claim stands or falls on the exact strengthened census and gap statement, not on the known minimum.

## Mathematical value: PASS

The scalar optimum conceals two qualitatively different inclusion-minimal families. The transfer-matrix theorem enumerates all minimal configurations for every rim length, while the extremal spectrum has a growing missing interval of \(\lceil n/2\rceil-4\) consecutive cardinalities. The minimum-set multiplicities change with the rim length modulo three. These are structurally motivated refinements of an established geodesic-hitting problem, not arbitrary parameter slices; the results can be used to study nonuniqueness, redundancy, and extremal nonoptimal transversals.

## Limits and evidence

Primary references are listed in `RESULT.md`. The provided `verify.py` uses graph-shortest-path semantics, not the proof's path-case split, to test all vertex subsets for the checked finite orders. It also tests the two symbolic coefficient formulas. Residual originality risk is a possible earlier cyclic 3-path-cover census or inaccessible full 2021 historical text. No independent validation is asserted.

Self-review: passed. Independent audit: not yet performed.
