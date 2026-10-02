# Scientific audit — 2026-10-01

## Final claim assessed

Sharp maximum reformulated Albertson index of trees

## Correctness — PASS

PASS. The proof was reconstructed from the definition. With \(x_v=d(v)-1\), the contribution at a vertex is bounded by \(x_v\sum_{u\sim v}x_u\). Summing gives \(\operatorname{RAlb}(T)\le 2\sum_{uv\in E(T)}x_ux_v\). Bipartiteness then bounds the edge sum by \(X_AX_B\), with \(X_A+X_B=n-2\), giving \(2\lfloor (n-2)^2/4floor\). Equality in the local inequality forces every vertex to have at most one non-leaf neighbor; connectedness of the non-leaf core then forces a double star, and maximizing \(2pq\) under \(p+q=n-2\) forces the balanced double star. The exhaustive tree enumeration through order 17 agrees but is not used as proof.

## Originality — PASS

PASS to the best of current knowledge. The complete 2025 Cutinha--D'Souza--Nayak article was inspected. It introduces the reformulated Albertson index, proves sharp lower bounds under additional degree/pendant constraints, and gives general parameter-dependent upper bounds, but not the order-only tree maximum or the balanced-double-star equality characterization. Searches were also made under the equivalent line-graph formulation \(\operatorname{RAlb}(T)=\operatorname{Alb}(L(T))\). No inspected prior theorem implies the exact order-only result.

### equivalent_formulations

Searches: Resultary: reformulated Albertson tree maximum balanced double star line graph irregularity; DOI 10.1080/09728600.2025.2458263; search: Albertson index line graphs of trees balanced double star

Evidence: The 2025 primary article establishes lower bounds for constrained tree classes and general upper bounds, not the claimed order-only maximum. No earlier exact published record was found under the line-graph formulation.

Reasoning: The line-graph identity is equivalent to the assigned statement, so searches covered both index names; no stronger statement was located.

### broader_coverage

Searches: Albertson 1997 irregularity of a graph; DOI 10.1007/s40819-015-0069-z; DOI 10.1080/09728600.2025.2458263

Evidence: Earlier Albertson and composite-graph work supplies the base invariant and graph-operation context; the 2025 paper supplies only parameter-dependent RAlb bounds.

Reasoning: Those results do not mechanically force the order-only quadratic maximum or its unique equality family.

### exact_database_or_table

Searches: Resultary semantic search for exact RAlb tree extremum; published search for maximum reformulated Albertson index of trees

Evidence: No natural numerical database governs the quantified theorem and no earlier exact theorem record was found.

Reasoning: This is an extremal theorem over every tree order, not a table lookup.

### claim_vs_prior_implication

Searches: Cutinha--D'Souza--Nayak 2025 upper-bound section; line-graph Albertson formulation

Evidence: The prior upper bounds depend on order, size and degree parameters and do not specialize to the claimed sharp order-only value.

Reasoning: The local inequality, bipartite weight product, and equality analysis supply additional implications not contained in the inspected prior bounds.

## Scientific value — PASS

PASS. The theorem determines a natural global extremum and unique extremal tree for a newly studied irregularity index, equivalently solving the Albertson maximum over line graphs of trees. The equality characterization is structural rather than a finite computation.

## Source inspections

- **On the minimum reformulated Albertson Index of fixed-order trees and unicyclic graphs with a given maximum degree** — https://doi.org/10.1080/09728600.2025.2458263. Material read: Complete open-access article, including the definitions, tree results, upper-bound section, conclusion and references. Assessment: CLOSEST_PRIMARY_SOURCE_NOT_COVERING_ORDER_MAXIMUM. Evidence: The article proves sharp lower bounds under fixed maximum degree/pendant conditions and several parameter-dependent upper bounds, but no exact order-only maximum or balanced-double-star equality theorem.
- **Published-record search for reformulated Albertson tree maxima** — Resultary semantic search. Material read: Ranked results for reformulated Albertson, line-graph irregularity, tree maximum and balanced double star formulations. Assessment: NO_EARLIER_EXACT_COVERAGE_FOUND. Evidence: No earlier record in the inspected results states or dominates the assigned theorem.

## Limitations and residual risks

The theorem is restricted to trees. The finite enumeration through order 17 is supporting evidence only. An older equivalent result phrased purely as irregularity of line graphs or block graphs remains a residual originality risk.

- Older graph-irregularity literature may contain an equivalent line-graph or block-graph theorem under different terminology.
- The finite verification through order 17 is corroborative only.

## Disposition

**passed**
