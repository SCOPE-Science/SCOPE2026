# Scientific review: exact constrained de Bruijn discrepancy census

## Correctness — PASS

The domain is the 48-edge, 24-vertex proper-word overlap graph at alphabet size three and order five, with precisely one rotation class per Eulerian circuit rooted at the unique edge `01010`. The proof establishes that each color occurs sixteen times; this makes maximum cyclic pairwise imbalance equal to the range of each of three integer prefix-balance walks. The edge-simple rooted DFS enumerates all such circuits. Independently, all 16,777,216 pairings of two incoming with two outgoing edges at each vertex are tested, and those defining one 48-cycle give an equivalent complete enumeration by a distinct construction. Both yield exactly 23,700, 420,924, and 341,808, summing to 786,432. A direct interval-and-factor checker verifies one witness of each discrepancy. Neither a sampled search nor a timeout is used to justify exhaustiveness. Critical computation paths are included.

## Originality — PASS, subject to residual priority risk

Chen–Liang–Wu (arXiv:2309.02841v1, 2023), Definition 2, Theorems 1–3, establish the restricted-cycle Eulerian correspondence and exact **total count** but do not classify the cyclic discrepancy spectrum. The present histogram strictly refines their total count rather than restating it. Álvarez et al. (arXiv:2407.17367v1, 2024) define this multicolor discrepancy and construct ordinary full de Bruijn cycles with small discrepancy, but a length-243 cycle realizing repeated-adjacent factors cannot imply the length-48 adjacency-hopping census. Gabrić–Sawada (arXiv:2005.01638v2) cover binary ordinary cycles; Alhakim (arXiv:2206.04408v1) covers preference-generated full nonbinary de Bruijn cycles. Neither determines the present distribution. Chen–Sima–Milenkovic (arXiv:2501.12921v2) explicitly identify adjacency-hopping cycles with Kautz sequences, but their Section VI optimizes orthogonality of collections and does not tabulate single-cycle discrepancies. Search matches and related results were compared by mathematical implication. Residual risk: exact constrained discrepancy values could appear in a nonindexed specialized table or unpublished literature; searching does not exclude that possibility.

## Value — PASS

The unrestricted total 786,432 masks a genuine design variable: how uneven each pair of colors can become in arbitrary consecutive windows. The first three orders have uniform discrepancy across all cycles, whereas order five splits into three classes. Their exact cardinalities, particularly the 23,700 optimizers, provide a complete natural finite cutoff for selecting low-imbalance cyclic patterns within the non-repetitive structured-light coding model motivating the 2023 paper. The statement provides an exact new invariant, not a routine recomputation of the known total, and does not claim an extrapolation to arbitrary order.

## Scope and remaining risk

The classification identifies cycles only by rotation; color permutations and reversal are counted separately. The exhaustive census is confined to ternary order five and relies on ordinary integer arithmetic in the provided C++17 implementations. Independent external evaluation and exhaustive global literature priority review have not occurred.

Self-review: passed. Independent audit: not yet performed.
