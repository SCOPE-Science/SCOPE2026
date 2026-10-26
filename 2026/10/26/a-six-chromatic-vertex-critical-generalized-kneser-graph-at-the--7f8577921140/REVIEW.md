# Scientific review of the first isolated-cycle Kneser boundary

## Correctness — PASS

The graph is defined by an unambiguous list of independent three-subsets of a nine-cycle plus an isolated vertex. Direct exhaustive enumeration independently regenerates 57 vertices and 498 edges (30 cycle-only triples, 27 triples containing the isolate, and 138 plus 360 disjointness edges). An explicit six-coloring gives the upper bound. Two separately implemented exhaustive five-color searches, in Python and C++, rule out all assignments modulo renaming of unused colors in exactly 122153 recursive states. A six-orbit certificate gives five-colorings after every vertex deletion; all 57 deletions are checked by transporting the six witnesses using explicitly verified dihedral symmetries. No infinite inference is made from these finite checks. The three-clique witness and ten-label size bound establish clique number three. Risks: any software proof depends on the correctness of the transparent enumeration logic and runtime; this is not independent validation.

## Originality — PASS (bounded)

Arana, Haxell, Kaiser, and Stehlík, arXiv:2610.17884 (2026-10-13), expressly leave cycle plus isolated vertex cases beyond their asymptotic theorem as open. Their Theorem 1.2 settles a shorter-cycle exclusion, Theorem 1.4 proves an asymptotic condition without resolving the first length-nine case at parameter three, and Conjecture 1.3 predicts tightness. The present six-color obstruction closes that exact first boundary, and the additional six-vertex-orbit deletion certificate establishes criticality. Schrijver's 1978 vertex-critical theorem applies to independent triples from a single cycle, a different graph. Broader published searches and published-record comparisons showed no equivalent explicit 57-vertex criticality classification. The 2026 paper mentions unspecified computational checks; prior unpublished enumeration, alternative formulations, and unindexed results remain possible.

## Value — PASS

The result settles the smallest length at the sharp obstruction boundary of an explicitly open 2026 conjecture for the first nonclassical set size. It adds full vertex-criticality, a strict clique-versus-chromatic gap, and a compact six-orbit reproducible certificate. It is a natural extremal cutoff rather than an arbitrary small graph statistic; it does not assert the full conjecture or a downstream theorem.

## Closest literature and limits

The closest primary reference is the introduction and Theorems 1.2/1.4 in Arana–Haxell–Kaiser–Stehlík (arXiv:2610.17884). The classical one-cycle criticality result is Schrijver (1978). The result is finite and machine-assisted; no general cycle-length or higher-parameter statement is proved. Independent mathematical assessment and complete historical-priority review remain outstanding.

Self-review: passed. Independent audit: not yet performed.
