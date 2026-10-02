# Mathematical audit — 2026-10-01

## Final claim assessed

Exact total strong Roman domination of complete multipartite graphs

## Correctness — PASS

PASS. The proof correctly separates optimal labelings according to whether a whole part is positive. In the full-positive-part case, totality and the defender requirement force the one-part strategy \(A=m+1+\lceil(N-m-1)/2\rceil\). Otherwise every zero vertex must see a positive defender outside its part; reducing to two defender parts yields the exact integer minimization in the package, and the one-unit saving occurs precisely in the stated odd--odd parity case when a third non-singleton part supplies the needed positive neighbor. Explicit constructions attain both lower bounds. A separate direct label enumeration agrees with the formula on representative small multipartite graphs, while the repository verifier exhausts all part-size types through the stated ranges.

## Originality — PASS

PASS to the best of current knowledge. The complete 19-page Nazari-Moghaddam--Soroudi--Sheikholeslami--Yero paper introducing total strong Roman domination was inspected. It establishes general bounds, characterizes several equality cases, and studies trees, but gives no complete-multipartite exact formula. Targeted searches for total strong Roman domination plus complete multipartite graphs found the introducing paper and neighboring variants, but no prior theorem matching the assigned parity-sensitive formula. Resultary likewise returned the assigned theorem as the exact match.

### equivalent_formulations

Searches: Resultary: total strong Roman domination complete multipartite parity formula; web: total strong Roman domination complete multipartite

Evidence: No earlier exact complete-multipartite formula was found. The complete defining paper contains general bounds and tree results but not this multipartite optimization.

Reasoning: Rephrasing the label optimization in terms of zero counts per part gives the same theorem; no inspected source carries out that optimization.
### broader_coverage

Searches: arXiv:1912.01093 complete 19-page text; later total/strong Roman literature search

Evidence: The introducing paper's theorems are general upper/lower bounds and special equality characterizations, none of which determines the parity-sensitive exact value for arbitrary part sizes.

Reasoning: No inspected broader theorem mechanically implies both competing strategies and the parity saving.
### exact_database_or_table

Searches: Resultary semantic search for exact total strong Roman numbers of complete multipartite graphs

Evidence: No table or earlier exact record was located.

Reasoning: The statement is a quantified family theorem, not a finite tabulation.
### claim_vs_prior_implication

Searches: Nazari-Moghaddam et al. full paper; assigned multipartite structural proof

Evidence: The prior definitions and bounds do not force which parts can support optimal defenders or the odd--odd one-unit saving.

Reasoning: The partwise structural lower bound and matching constructions provide additional information beyond the prior general theory.

## Scientific value — PASS

PASS. Complete multipartite graphs are a standard test class for domination parameters, and the optimum is not a single immediate degree bound: it has two competing structural strategies and a genuine parity correction controlled by a third non-singleton part. The closed formula covers complete graphs, stars, bicliques and all multipartite orders uniformly.

## Source inspections

- **On the total and strong version for Roman dominating functions in graphs** — https://arxiv.org/abs/1912.01093. Material read: Complete 19-page primary preprint, including all general bounds, equality characterizations and the tree section. Assessment: PRIMARY_SOURCE_NOT_COVERING_MULTIPARTITE_FORMULA. Evidence: No exact complete-multipartite theorem appears in the paper.
- **Published-record and literature search for complete multipartite total strong Roman domination** — Resultary and targeted literature search. Material read: Ranked published findings and indexed primary literature under the exact parameter and graph class. Assessment: NO_EARLIER_EXACT_COVERAGE_FOUND. Evidence: Searches located the introducing paper and related Roman variants, not the claimed exact multipartite formula.

## Limitations and residual risks

The formula is for connected complete multipartite graphs under the standard total strong Roman definition. It does not classify all optimal labelings beyond the structural cases used in the proof, and it makes no claim for isolated-vertex graphs.

- The total strong Roman literature is relatively young and indexing is uneven; a later poorly indexed multipartite specialization remains possible.

## Disposition

**passed**
