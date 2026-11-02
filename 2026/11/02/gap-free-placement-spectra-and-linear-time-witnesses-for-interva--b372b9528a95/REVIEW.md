# Scientific assessment

## Correctness — PASS

The claim is quantified over all finite simple degree-two topologies with interval-valued approval counts. Reduction to unary/pairwise interval constraints retains every feasible placement. Two-state path/cycle dynamic programming computes both extremes in linear time. In the switching proof, same-direction changes cannot violate an interval, while opposite-direction changes create directed implications. Every strongly connected block of the implication graph is an alternating-sign path or even cycle and hence changes occupancy count by at most one. Reverse condensation order preserves all constraints and the integer intermediate-value argument proves the full size spectrum. The seven-vertex counterexample satisfies all three exact-one equations and has exactly two solutions of sizes one and three. Standalone finite verification agrees for 10,843 exhaustive constraint instances, 1,150 randomized incidence instances, and one 10,000-site construction. These tests are corroborative; the structural proof covers unbounded sizes.

## Originality — PASS, with priority limitations

Knop and Schierreich (arXiv:2302.13997, Section 3) solve arbitrary approval sets on degree-two networks by a cardinality-indexed dynamic program, which neither states gap-free counts nor yields the claimed linear-time construction for positive lower bounds. Schierreich (arXiv:2308.09501, Section 4) proves a linear-time result for upper-bound-only approvals, a downward-closed special case. The implication-exchange interpolation and general interval algorithm are not derived by the cited statements without an additional argument. Relevant primary texts and several distinct literature searches for interval neighbor-count housing, binary constraint cardinality spectra, aliases and stronger coverage were compared. A previously published equivalent characterization in specialized constraint-satisfaction literature remains possible and requires independent priority review.

## Mathematical value — PASS

In exact-cardinality housing, a gap between feasible population sizes changes whether a planner can realize a prescribed intake. The theorem proves no such gaps are possible on path/cycle topologies even when positive lower bounds destroy downward monotonicity. The linear algorithm constructs a housing of every admissible intake size; its exchange blocks explain the phenomenon structurally. The seven-vertex example shows precisely why the degree restriction matters. This improves a motivated tractability boundary rather than enumerating an arbitrary finite slice.

## Sources and scope risks

Primary-source comparisons: https://arxiv.org/abs/2302.13997 and https://arxiv.org/abs/2308.09501. Residual risks: a semantically equivalent result under a different binary-CSP formulation, and reliance on the single-interval approval hypothesis. No claim about general degree-three computational hardness is new here.

Self-review: passed. Independent audit: not yet performed.
