# Independent mathematical audit — SCOPE-20260917-2226d8f07ffd

Final disposition: **passed**.

## Correctness
**PASS.** For three colours on a path or cycle, a successful initially uncoloured set must be independent; on a path it cannot contain endpoints. Relative to a final proper colouring, each uncoloured degree-two vertex must be tight, meaning its two neighbours have distinct colours. Encoding a path colouring by ±1 increments modulo 3 turns each selected tight vertex into one equality of two adjacent increments; independence makes these constraints disjoint. This gives the stated binomial coefficient formula. On a cycle, suppressing each selected tight vertex reduces to a proper colouring of a cycle of length n-j, giving the stated cycle factor. A fresh definition-level exhaustive enumeration independently reproduced every path coefficient for n≤6 and every cycle coefficient for n≤6, including P3=6p^2(1-p).

## Originality
**PASS.** The full 29-page Farr v1 PDF was inspected. It gives general properties, a two-colour bipartite theorem, and small connected examples through four vertices; its displayed K1,2 three-colour value is 6p^2(1-2p), while the direct count gives 6p^2(1-p). The paper does not give the path/cycle family formulas. A later public 2026-09-19 maximum-degree-two record explicitly states that this 2026-09-17 record was committed earlier and already contained the core formulas; the later record treats its own formulas as an alternate derivation/refinement. Thus later overlap is not earlier prior art.

## Value
**PASS.** Paths and cycles form the complete connected class of maximum degree two, and three colours are the only forcing regime not already reduced to elementary one/two-colour or high-colour behavior. Closed coefficient formulas, recurrences, and exact minimum-domain consequences therefore give a natural complete classification rather than an arbitrary finite slice.

## Source inspections
- **G. E. Farr, The forced colouring function of a graph, arXiv:2609.17108v1** — Full 29-page PDF inspected. Section 3 gives general properties and small examples; Proposition 6 displays the K1,2 three-colour value 6p^2(1-2p) and values for P4 and C4. No path/cycle family theorem appears in the inspected paper. Consequence: Closest primary source supplies definitions and small anchors but not the audited family formulas.
- **Exact forced-colouring functions for paths and cycles (public research record, 2026-09-18)** — Full result inspected; it states the same path and cycle formulas and gives an independent-set proof. Consequence: Subsequent overlap dated after the audited record.
- **Exact forced-colouring functions at maximum degree two (public research record, 2026-09-19)** — Full result inspected; its provenance section explicitly identifies the audited 2026-09-17 record as the earlier source of the core formulas. Consequence: Subsequent record confirms chronology and adds refinements rather than defeating the audited record’s originality.

## Originality comparison
- **Equivalent formulations.** Searches: forced 3-colouring path recurrence; forced colouring independence polynomial paths cycles; forcing-domain counts maximum degree two. Evidence: The primary source contains only small examples; later records use equivalent independent-set and transfer-matrix formulations. Reasoning: Equivalent recurrence and independence-polynomial forms were compared, not only titles.
- **Broader coverage.** Searches: forced colouring maximum degree two all colours; path cycle forced colouring formulas. Evidence: Later 2026-09-18 and 2026-09-19 public records cover the same formulas and broader all-colour packaging. Reasoning: Those records are subsequent, and the 2026-09-19 record explicitly documents the audited record as earlier.
- **Exact database or table.** Searches: Farr 2609.17108 path cycle formula; forced colouring P_n C_n exact coefficients. Evidence: Farr v1 Proposition 6 gives only graphs through four vertices and no family table/formula. Reasoning: Direct full-text inspection of the most plausible primary source supports the non-coverage conclusion.
- **Claim versus prior implication.** Searches: Farr bipartite lambda=2 theorem; high-colour degree bound forcing. Evidence: Those results settle lambda=2 or the elementary high-colour regime, not lambda=3 path/cycle coefficients. Reasoning: The audited lambda=3 formulas require the tight-vertex/independent-set structure and are not mechanical corollaries of the source’s general endpoint identities.

## Residual risks
- The source paper and the audited record were separated by only two days, so unindexed parallel work remains possible.
- The later public records now duplicate and refine the formulas; catalog users should prefer the provenance-aware later synthesis for some applications.

## Limitations
Specific to maximum degree at most two and to the nontrivial three-colour case. The source paper is very recent. Later public records restate and extend the same formulas, but one explicitly records that this 2026-09-17 record was the earlier source of the core formulas.
