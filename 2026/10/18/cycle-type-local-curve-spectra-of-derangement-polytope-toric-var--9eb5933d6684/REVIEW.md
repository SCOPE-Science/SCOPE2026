# Self-review

## Correctness — PASS
The derivation begins with the derangement vertices and standard alternating-cycle adjacency criterion. It constructs a complete inclusion-exclusion over disjoint directed forbidden-arc cycles, counts proper cyclic runs by compositions, and separately accounts for selections that are entire prohibited cycles. A direct changed-support permutation enumerator checks each coefficient for every cycle type through \(n=8\), and an independent derangement-pair graph enumerator checks adjacency for \(n\le6\), returning `VERIFY_OK`. The dimension and nonsimplicial cutoff follow by integral incidence rank and elementary support-two/support-three lower bounds. Computation is supporting evidence; infinite quantifiers rest on the proof.

## Originality — PASS, qualified
Behrend's full paper establishes the general matching-polytope adjacency criterion, which is explicitly acknowledged, but its inspected adjacency and face-lattice sections do not give the displayed coefficient-extraction formula or its toric local-degree consequences. Davis–Sagan study different pattern-avoiding permutation subpolytopes. Abreu and collaborators count alternating paths and cycles in the polytope of all matchings, but do not give an explicit cycle-type run polynomial for the perfect-matching subface. Current records about rectangular doubly substochastic matching polytopes concern partial matchings and do not entail derangement cycle-type degrees. Targeted searches for the precise objects, aliases and invariant found no covering result. Potentially unindexed equivalent formulas are a residual risk.

## Mathematical value — PASS
A standard adjacency test does not itself provide explicit local incidence statistics over all derangement vertices. The cycle-run formula resolves the natural all-dimensions, cycle-type-refined local curve degrees of this integral family, computes global edge counts, and yields a sharp toric fixed-point nonsmoothness boundary. It is not an isolated small-case computation or a restatement of the general adjacency criterion.

## Limits
The theorem concerns fixed-point curve incidence, not full singular schemes or analytic types. General adjacency and polytope dimension theory remain prior work. Independent expert verification has not been undertaken.

Self-review: passed. Independent audit: not yet performed.
