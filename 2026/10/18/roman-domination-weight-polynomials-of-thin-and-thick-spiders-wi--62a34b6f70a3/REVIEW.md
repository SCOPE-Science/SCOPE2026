# Self-review

## Correctness — PASS

Every Roman dominating labeling of a thin or thick spider is partitioned according to whether a label two occurs in its clique and, if not, in its head. The three cases are exhaustive and disjoint. The potentially delicate thick-spider restriction is precise: with exactly one core two, only its non-neighbor foot may not be zero, producing the correction \(nz^2 E^{n-1}\). The other thick-spider subtlety, a single foot two with no core/head two, forces its one unmatched core to be positive. Exact arbitrary-head and join/union rules follow from the same zero-defense definition. The correctness argument works for every finite head and \(n\ge2\); experiments on 264 instances and 8,244,702 functions independently corroborate but do not replace the proof.

## Originality — PASS, qualified

The closest direct source, Das–Santra (2026, arXiv:2609.19240v1), provides minimum Roman weights and a decomposition algorithm for \(P_4\)-tidy graphs; the material inspected does not provide these complete weight distributions or the dependence solely on head order and head polynomial. Abu-Khzam–Fernau–Mann (MFCS 2023, DOI:10.4230/LIPIcs.MFCS.2023.6) counts minimal Roman labelings and hence does not imply counts of all Roman labelings. General weighted MSO/clique-width methods can already guarantee polynomial-time coefficient computation on a bounded-clique-width class; algorithmic existence alone is not claimed as new. The algebraic identities and head-substitution principle give strictly more explicit, structurally interpretable information. Searches compared chain-graph and multipartite Roman polynomials, the alternate meaning of spider as a tree, Roman variants, and general polynomial computation. No implication of the explicit spider formulas from an inspected primary theorem was found. Unindexed and inaccessible specialized literature remains a bibliographic risk.

## Value — PASS

The full degree-\(2|V|\) polynomial encodes exponentially many Roman assignments by their weights rather than only one optimum. The universal head-substitution laws are a nontrivial graph-composition invariant and give direct exact coefficient formulas across all \(P_4\)-sparse graphs, a natural hereditary class. The thick-spider exception with one core defender and one unmatched foot is a genuine local combinatorial obstruction, not a renamed complete-multipartite counting exercise. The result gives reusable algebraic machinery independently of new complexity bounds.

## Limitations and closest coverage

The primary 2026 source already determines minimum-weight cases; the 2023 census counts minimal functions; a general fixed-clique-width logical counting theorem covers generic computability. Those claims are excluded from priority assertions. Specialized full-text coverage may be incomplete. No external or independent mathematical validation has been performed.

Self-review: passed. Independent audit: not yet performed.
