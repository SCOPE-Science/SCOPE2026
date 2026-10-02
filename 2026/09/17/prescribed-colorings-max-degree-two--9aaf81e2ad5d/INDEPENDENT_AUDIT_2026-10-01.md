# Independent mathematical audit — Exact prescribed color-class sizes for graphs of maximum degree two

Audit date: 2026-10-01 (UTC) UTC
Disposition: passed

## Correctness
the component lemma for paths and cycles realizes every multiplicity vector bounded by the component independence number. The global max-flow reduction has singleton cuts equal to the independence bound, two-color cuts equal to the total order minus the number of odd-cycle components, and all larger cuts automatic. An independent exhaustive check over every unlabeled path/cycle component multiset through order 9 tested 3,885 graph/partition cases and matched the theorem in every case.

## Originality
Birken's recent skewed Hajnal–Szemerédi theorem gives a sufficient bounded-class condition, not this exact if-and-only-if support description. A related same-day SCOPE result isolates the bipartite maximum-degree-two special case; it does not imply the odd-cycle pair obstruction or the full stable-partition support. Targeted Resultary and web searches found no earlier equivalent characterization.

### equivalent_formulations
No prior source located gives the same two-inequality characterization including odd-cycle components.

Searches: Resultary: maximum degree two graph prescribed color class sizes chromatic symmetric function stable partition support; arXiv:2609.18629; arXiv:2201.07333

Evidence: The theorem is equivalent to an exact stable-partition/monomial-support criterion for Δ≤2 graphs.

### broader_coverage
Closest coverage is weaker or restricted, not dominating.

Searches: Birken arXiv:2609.18629; Matherne–Morales–Selover arXiv:2201.07333; Resultary SCOPE-skewed-hajnal-szemeredi-maximum-degree-two

Evidence: Birken gives skewed-colouring sufficient conditions; the related SCOPE result covers the bipartite Δ≤2 special case; neither implies the full odd-cycle pair constraint.

### exact_database_or_table
Not a known-table recomputation.

Searches: Resultary stable partition support maximum degree two

Evidence: No exact database/table of all feasible profiles was found; the claim is uniform over all finite Δ≤2 graphs.

### claim_vs_prior_implication
The claim is not mechanically implied by the inspected general frameworks.

Searches: Stanley chromatic symmetric function framework; arXiv:2201.07333; arXiv:2609.18629

Evidence: General CSF/Newton-polytope language does not yield the two obstructions; the max-flow proof supplies the missing sufficiency.

### Source inspections
- **Birken, A Hajnal-Szemerédi Theorem for Skewed Colorings** — Primary metadata/abstract inspected; it gives the recent general sufficient prescribed-size theorem motivating the record. Assessment: Compared against the final statement and implication scope.
- **Stanley, A Symmetric Function Generalization of the Chromatic Polynomial of a Graph** — Primary background source for the chromatic symmetric function. Assessment: Compared against the final statement and implication scope.
- **Resultary search** — Searched exact prescribed-coloring, stable-partition, and maximum-degree-two formulations; related records were compared by implication. Assessment: Compared against the final statement and implication scope.

## Scientific value
the theorem gives a complete feasibility criterion for an entire natural graph class, converts it into the exact stable-partition support of the chromatic symmetric function, and settles the maximum-degree-two instance of the motivating prescribed-coloring question.

## Reproducibility
Independent exhaustive enumeration through n=9 covered 189 path/cycle graph types and 3,885 graph/partition cases with no mismatch against the stated inequalities.

## Limitations and residual risks
The theorem is restricted to finite simple graphs of maximum degree at most two. Originality is assessed against the documented searches and inspected recent skewed-coloring work; unrelated formulations could remain under different terminology.
- The originality search can miss older literature phrased in terms of stable partitions rather than prescribed color classes.
