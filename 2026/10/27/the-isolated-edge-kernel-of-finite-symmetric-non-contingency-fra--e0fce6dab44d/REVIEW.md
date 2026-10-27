# Scientific assessment

## Correctness — PASS

For all labelled finite simple undirected frames on a common vertex set and under all **shared** valuations, the proof correctly derives the rowwise homogeneity invariant from \(\Delta p\). It shows that any relation discrepancy can occur only inside isolated two-vertex connected components and that the canonical deletion is complete and uniquely determined. The kernel-fiber matching bijection is reversible. The bivariate enumeration follows by choosing isolated labels and applying the standard exponential formula to the remaining graph components. Edge cases \(n=1,2\), singleton and empty neighbour sets, and the formal rather than analytic interpretation of generating functions are explicit. A standalone exhaustive checker tests all graphs through six vertices and reports `ALL_CHECKS_OK 66771`; all-size correctness rests on the mathematical argument.

## Originality — PASS within inspected evidence

The original component-free graph counting sequence is known: OEIS A093352 already supplies its total-count formula, so that formula is not credited as new. The 2014 and 2015 papers of Fan, Wang and van Ditmarsch supply general non-contingency bisimulation and axiomatics; Ding and Yang (2026) give still broader bundled-modality bisimulations; Sierra Miranda, Wang and Zenger (2026) give the exact source semantics and proof theory. The inspected source material did not state or derive as a displayed result the fixed-domain observational kernel \(\kappa\), its sharp depth-one separator on loop-free symmetric graphs, or the complete modal equivalence-fiber spectrum. The related earlier result on KD45 successor-valuation supports has different frame hypotheses and does not imply the irreflexive symmetric result. General bisimulation methods may provide a route to this specialization, which remains a stated priority risk. The inaccessible full 2014 text and a potentially related 2026 thesis require independent priority examination.

## Value — PASS

This is a natural complete semantic classification of symmetric, irreflexive finite accessibility networks: it identifies precisely which graph edges are unobservable by the entire non-contingency language even under unrestricted valuations, provides a linear-time canonical normalization, proves that modal depth one captures all available relational information, and describes **all** observational class sizes, not an arbitrary single-parameter example. It quantifies the information loss of a well-studied modality on a natural network family. The underlying bare graph-count sequence is acknowledged as known and is not used alone to justify value.

## Sources and limitations

The closest primary literature is *Proof Theory for Non-Contingency Logic* (arXiv:2609.38975v1), *Almost Necessary* (AiML 2014), *Contingency and Knowing Whether* (2015), and *A General Theory of Propositional Modal Bundled Modalities* (EPTCS 447, 2026); the exact univariate graph count is OEIS A093352. The statement concerns same-labelled-world valuation-uniform truth only, not frame validity or isomorphism. Source priority is conditional on the inspected material, especially because the full 2014 PDF and the full 2026 bundled-fragments thesis were not available.

Self-review: passed. Independent audit: not yet performed.
