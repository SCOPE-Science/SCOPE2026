# Independent audit — 2026-10-01

## Final claim

For every connected complete multipartite graph \(K_{n_1,\ldots,n_r}\), the solid-locating-dominating and self-locating-dominating codes have the complete structural classifications, minimum numbers, minimum-code counts, and code-size generating functions stated in RESULT.md.

## Correctness — PASS

For an omitted vertex \(u\) in part \(V_i\), the proof identity \(I(C;u)=C\setminus C_i\) makes the DLD comparison exact: same-part omissions collide and distinct-part ordered differences are precisely the relevant part-code sets. This yields the complement classification and the elementary-symmetric enumerator. The SLD characterization forces an omitted part to contain no codeword, hence to be a singleton, and a second omitted singleton is impossible; deleting the unique singleton works exactly when all other parts are non-singletons. Boundary cases \(p\le1\) and \(s
e1\) are treated. A fresh replay of the actual verifier returned `VERIFY_OK types 58 checks 16168`, matching all histograms and minima.

Checked sources:
- Junnila--Laihonen--Lehtilä, On regular and new types of codes for location-domination, Discrete Applied Mathematics 2018, DOI 10.1016/j.dam.2018.03.050, full accessible article text inspected.
- Junnila--Laihonen--Lehtilä--Puertas, On Stronger Types of Locating-dominating Codes, DMTCS 2019 / arXiv:1808.06891.
- Published-record semantic search for self/solid locating domination on complete multipartite graphs.
- Fresh exhaustive replay of the package verifier on all 58 complete multipartite types through order eight.

Residual risks:
- The finite replay is corroborative; the all-size formulas rest on the displayed partwise proof.

## Originality — PASS

Best-of-knowledge originality passes. The defining 2018 primary article was inspected in accessible full text: it introduces the two code notions and develops rook graphs and binary Hamming spaces, not complete multipartite graphs. The later structural paper and semantic searches did not produce an equivalent complete-multipartite classification or enumerator.

### Equivalent formulations

Searches:
- Resultary query: self locating dominating solid locating dominating complete multipartite graphs
- Full-text inspection of the 2018 defining article

Evidence:
- The assigned finding is the only exact semantic hit.
- The defining paper explicitly focuses its exact graph-family results on rook graphs and binary Hamming spaces.

Reasoning: Equivalent formulations are the complement-selection description, the two domination numbers, and the cardinality enumerators; no earlier equivalent statement was located.

### Broader coverage

Searches:
- 2018 defining paper
- 2019 stronger-types paper
- 2023 location-code follow-up

Evidence:
- The inspected prior work develops general characterizations and other families but does not dominate the arbitrary complete-multipartite classification.

Reasoning: General definitions and characterizations do not mechanically imply the closed formulas without the partwise neighborhood analysis.

### Exact database or table

Searches:
- Semantic search for complete multipartite SLD/DLD formulas and code counts

Evidence:
- No independent database/table or published record with the same complete family formulas was located.

Reasoning: The exact enumerators are structural formulas, not recomputations of a known table.

### Claim versus prior implication

Searches:
- Comparison of the 2018 full text with the audited theorem

Evidence:
- The prior definitions supply the predicates only; the audited classification needs the identity \(I(C;u)=C\setminus C_i\) and its consequences.

Reasoning: No inspected prior theorem implies the final claim as a special case.

### Source inspections

- **On regular and new types of codes for location-domination** — Defines the invariants but does not cover complete multipartite graphs. Material read: Accessible full article text including Definitions 5 and 6 and the sections on rook graphs and binary Hamming spaces. Method: Primary full-text inspection. Evidence: The article states its main exact graph-family focus as rook graphs and binary Hamming spaces.

Checked sources:
- Junnila--Laihonen--Lehtilä, On regular and new types of codes for location-domination, Discrete Applied Mathematics 2018, DOI 10.1016/j.dam.2018.03.050, full accessible article text inspected.
- Junnila--Laihonen--Lehtilä--Puertas, On Stronger Types of Locating-dominating Codes, DMTCS 2019 / arXiv:1808.06891.
- Published-record semantic search for self/solid locating domination on complete multipartite graphs.
- Fresh exhaustive replay of the package verifier on all 58 complete multipartite types through order eight.

Residual risks:
- Differently indexed later work on complete multipartite graphs remains a best-of-knowledge risk.

## Scientific value — PASS

Complete multipartite graphs are a canonical graph family, and the theorem gives not only two minimum parameters but the full valid-code structure and exact enumerators. The partwise identity is reusable for related locating-code variants, so this is a natural complete classification rather than an arbitrary finite slice.

Checked sources:
- Junnila--Laihonen--Lehtilä, On regular and new types of codes for location-domination, Discrete Applied Mathematics 2018, DOI 10.1016/j.dam.2018.03.050, full accessible article text inspected.
- Junnila--Laihonen--Lehtilä--Puertas, On Stronger Types of Locating-dominating Codes, DMTCS 2019 / arXiv:1808.06891.
- Published-record semantic search for self/solid locating domination on complete multipartite graphs.
- Fresh exhaustive replay of the package verifier on all 58 complete multipartite types through order eight.

Residual risks:
- The result is restricted to complete multipartite graphs.

## Conclusion

The unchanged final claim passes correctness, best-of-knowledge originality, and scientific value.
