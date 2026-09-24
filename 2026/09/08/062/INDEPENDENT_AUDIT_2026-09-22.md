# Independent three-axis audit — 2026-09-24

Reviewer type: separate AI audit. This document records reproducible scientific checks and literature comparison, not a transcript of private reasoning.

## Audited source

- Record: `SCOPE-20260908-062`
- Source path: `2026/09/08/062`
- Inventory source tree: `601a1a1d585fdfa88ea41b820c9470d000197bdf`
- Audited `RESULT.md` blob: `a64c159dc02cd4d123c85e7033ddcc755bdd6c20`
- Claim audited: exactly 13 isomorphism classes, under `S_6`, of maximum intersecting 3-subset families on `[6]`, with 1024 labelled maxima.

## Correctness — PASS

The finite classification was independently rederived from the definitions. The 20 triples of `[6]` form 10 complementary pairs. Two 3-subsets of `[6]` are disjoint iff they are complements, so an intersecting family contains at most one member of each pair; a family of maximum size 10 therefore contains exactly one member from each pair. Conversely every one-from-each-pair transversal is intersecting. Hence there are exactly `2^10 = 1024` labelled maximum families.

A fresh enumeration generated all 1024 transversals, applied all 720 permutations of `[6]`, and canonicalized each family by its lexicographically least image. It produced exactly 13 orbits, with orbit sizes

`6, 6, 12, 20, 20, 60, 60, 90, 90, 120, 180, 180, 180`,

which sum to 1024. This independently confirms the record's headline count and its orbit-size multiset.

## Originality — FAIL

The novelty claim is contradicted by prior literature. Joanna Polcyn and Andrzej Ruciński, **A hierarchy of maximal intersecting triple systems**, Opuscula Mathematica 37 (2017), 597–608, DOI `10.7494/OpMath.2017.37.4.597`, arXiv `1608.06114`, explicitly classify the six-vertex case. On published page 601, immediately before Proposition 1.6, they state that the 20 triples on six vertices split into 10 complementary pairs, that choosing one from each pair gives `2^10` maximal intersecting 3-graphs, and that these contain **13 pairwise non-isomorphic** classes. Proposition 1.6 then lists the 13 extremal isomorphism types. The paper therefore covers the record's central asserted novelty exactly, not merely a stronger asymptotic theorem or an adjacent parameter.

Full text checked: https://www.opuscula.agh.edu.pl/vol37/4/art/opuscula_math_3732.pdf, published page 601, Proposition 1.6 and the paragraph immediately preceding it. Repository page: https://repo.agh.edu.pl/entities/publication/4e1dd6e4-f7c0-47d2-8009-d35dc9be1d99.

Mapping to the record is direct: a maximum intersecting 3-family on `[6]` has 10 edges and is maximal under inclusion; Polcyn–Ruciński's six-vertex maximal intersecting triple systems are exactly these 13 isomorphism classes. The record's sentence that no prior source records the exact count at `(n,k)=(6,3)` is therefore false.

Searches included: `maximum intersecting 3-uniform hypergraphs on 6 vertices 13 isomorphism classes`, `maximal intersecting triple systems n=6 13`, and exact-title/arXiv checks for the covering paper.

## Scientific value — FAIL

After subtracting the prior result, the remaining contribution is an independent brute-force recreation of an already published 13-class classification, with stabilizer/orbit certificates and shifting labels. Those certificates are useful for replay but do not constitute a new regime, theorem, structural explanation, algorithmic improvement, or materially new dataset: the central classification and its complementary-pair reduction are already in the 2017 paper. The residual annotations are routine invariants of a 1024-object finite census and do not support an accepted scientific finding on their own.

## Repair attempt

A repair was considered by narrowing the claim to the explicit representatives, stabilizer orders, orbit sizes, and shifting flags. This does not rescue the record: those are routine certificate-level refinements of the already known 13-type classification and do not supply sufficient independent scientific value for acceptance.

## Final disposition

**FAILED** on originality and scientific value; correctness passes. The record should not remain represented as a validated novel finding. Scientific rejection evidence is published at the source record; archival relocation to the assigned failed-attempt path remains pending and does not affect the scientific verdict.
