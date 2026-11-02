# Scientific review

## Correctness — PASS

For a selected vertex in the four-cube, at least two of its four neighbors must also be selected; every unselected vertex must have a selected neighbor. The program checks these exact necessary-and-sufficient conditions for every one of the \(65,536\) candidate masks. In the five-cube the proof establishes the exact layer predicate \(P(A)\land P(B)\land R(A)\subseteq B\land R(B)\subseteq A\). The program examines every one of the \(65,966,884\) ordered pairs of the \(8,122\) feasible layer masks and independently checks each minimum pair using original-graph neighbor tests. Its conclusions \(8,428\) and \(16,1830\) are exhaustive finite results. Coordinate flips and adjacent coordinate swaps generate all hypercube automorphisms, so the orbit calculation is also complete. No infinite-dimensional statement is inferred from these finite certificates.

## Originality — PASS, provisional historical priority

Tepeh, *On \(k\)-limited domination: complexity and Cartesian products* (arXiv:2606.22428, first public 2026-06-21), explicitly records the two relevant \(k=2\) hypercube cells as unknown in the accessible original Table 3 and states the regular-graph equivalence with \((1,t)\)-domination. Prior \(k=1\) hypercube values provide upper bounds for our problem but do not imply optimality for \(k=2\). Similarly, the published exact \(k=d-1\) values concern total domination and cannot imply the values for the smaller allowed parameter here. Subsequent Sierpiński and cubic-graph studies address different graph families or different parameters. Searches against relevant research records and accessible historical claims found no stronger covering statement or table. The most important residual risk is that uninspected revisions or independent unindexed literature might contain an equivalent classification.

## Mathematical value — PASS

The primary motivating paper specifically identifies the missing hypercube region as a natural direction; the two results fill the first two adjacent blank cells in its displayed table. Moreover, the six complete orbit types and the counts \(428\) and \(1,830\) characterize optimizer degeneracy under the full symmetry of these central regular graphs. These exact natural invariant values and structural minimizer profiles are not forced by a known bound or by the existence of the standard coordinate-halfcube construction. The work does not claim a general theory in arbitrary dimension.

## Limitations and closest literature

The definitive claim concerns the exact two finite cubes only. The 2026-06-21 primary paper's first-version full-text transcription and the relevant portions of later primary sources were compared; some potential later full versions and historical appendices were not accessible. The independent correctness and priority assessments are outstanding.

Self-review: passed. Independent audit: not yet performed.
