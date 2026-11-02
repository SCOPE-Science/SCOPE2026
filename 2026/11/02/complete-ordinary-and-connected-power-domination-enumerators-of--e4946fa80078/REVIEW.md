# Scientific assessment

## Correctness — PASS

Closed-neighborhood observation leaves precisely the cells in completely unused rows and columns. If both dimensions of this residual rectangle are at least two, no observed vertex has exactly one unseen neighbor; if either is one, every missing cell can be forced immediately. This necessity-and-sufficiency argument establishes the infinite structural characterization and one-step bound. Inclusion-exclusion and the connected bipartite exponential formula then count all labeled sets, and the minimum cases are enumerated directly. All ordinary coefficients were checked on eight actual graph instances (107336 nonempty subsets); all connected coefficients were checked on six instances by an independently implemented recurrence. Exact boundaries, including both dimensions equal to two and the empty set, were considered. Computations support but are not substituted for the proof.

## Originality — PASS, with residual risk

The 2018 power-domination-polynomial paper (arXiv:1805.10984) defines the enumerator and computes other families; its inspected full HTML does not give the present rook-graph polynomials. The 2017 connected-power-domination paper (arXiv:1712.02388) introduces the connected variant but treats complexity and other graph families. The 2016 Cartesian-product literature gives the known ordinary scalar minimum, and Ganesamurthy--Jeyaranjan--Srimathi (arXiv:2205.05274v1, Theorem 10) independently establish the corresponding connected scalar minimum; neither supplies an inspected complete coefficient classification. The all-cardinality structural criterion, both polynomials, one-wave property and minimum-set multiplicities are distinct from those earlier scalar bounds. Equivalent descriptions in terms of the line graph \(L(K_{m,n})\) and row/column support were searched, as were related mathematical research-record claims. No directly covering formula was identified; prior bibliographies or inaccessible full-text sections could contain a related identity, so publication priority is not independently certified.

## Mathematical value — PASS

The result determines two complete graph polynomials on a natural two-parameter graph family motivated by placement and connectivity of monitoring devices. It refines a previously known single-number extremum into the distribution of all feasible placements, reveals that propagation never requires more than one wave, gives a sharp universal success threshold for large placements, and quantifies the reduction from all minimum placements to connected minimum placements. These are exact structural and enumerative results, not reparametrizations of the previously known minimum value.

## Limits and closest literature

The connected polynomial is expressed through coefficients of the standard bipartite connected-graph EGF, and is not claimed to be a small elementary expression for arbitrary dimensions. The inspected full texts cover the two foundational preprints and the 2022 connected-product treatment; the publisher-hosted 2016 Cartesian-product paper was accessible only intermittently as indexed text, leaving a named priority risk. The finite verifier is a consistency test, not a proof for arbitrary dimensions.

Self-review: passed. Independent audit: not yet performed.
