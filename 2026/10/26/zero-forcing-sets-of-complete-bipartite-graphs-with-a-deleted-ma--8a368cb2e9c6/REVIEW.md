# Scientific review

**Correctness: PASS.** The explicit color-change proof handles every initial configuration in the domain: each bipartition has at most two initially white vertices, matched supports are necessary at size two, and the only two-by-two obstruction is equality of supports. The proof supplies forcing steps in each other case and enumerates all surviving profiles without double counting. A separate exhaustive direct-rule program produced `VERIFY_OK cases=130 initial_colourings=407040`; these finite checks do not prove the infinite assertion.

**Originality: PASS, subject to residual literature risk.** The 2010 zero forcing source defines the ordinary process but does not establish the target deleted-matching polynomial in the inspected material. Boyer et al. (arXiv:1801.08910, Proposition 4) supply the complete bipartite polynomial, recovered at zero deletions, but that statement does not cover the two new low-degree coefficients. Close indexed records on matching-deleted bicliques count other parameters: geodesic subpaths and non-CIS pairs. The thesis arXiv:1311.7672 was accessible only as an abstract; an exact result in its full text or an unindexed source cannot be excluded. Negative searches are not a uniqueness proof.

**Value: PASS.** The natural family permits a controlled deletion experiment with a precise structural and enumerative answer across every admissible part size. The ordinary zero forcing number has two sharp transitions after one and two missing disjoint edges, and the result then fixes all coefficients rather than just the extremum. The crown-graph specialization is a complete all-size enumeration.

**Scope.** Parts have at least three vertices; deleted edges are pairwise disjoint. No assertion covers smaller parts, other deletion patterns, or other forcing variants.

Self-review: passed. Independent audit: not yet performed.
