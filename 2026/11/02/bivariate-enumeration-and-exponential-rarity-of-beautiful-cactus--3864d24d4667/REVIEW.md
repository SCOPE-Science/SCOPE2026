# Review: bivariate beautiful-cactus enumeration

## Correctness — PASS

The reduction from the forbidden-induced-subgraph theorem to cactus blocks follows because cactus graphs contain no diamonds and all cycles are induced. An induced net around a triangle is equivalent to the absence of a degree-two vertex in that triangle block, by the cactus block-cut tree. The rooted attachment argument partitions graphs without duplication according to whether the global root alone certifies its unique incident triangle, yielding the exact term \(sx(T-x)^2/2\). All even cycles of length at least six contribute \(tT^5/[2(1-T^2)]\). The nonnegative reformulation (3) permits the standard aperiodic smooth implicit-function singularity transfer; the coefficient and derivative factors have been recomputed from the implicit equation. Exact formal-series arithmetic and independent finite graph enumeration test the directly defined forbidden subgraphs and yield `VERIFY_OK`. These tests corroborate, rather than replace, the general proof.

## Originality — PASS, qualified

Wunderlich's primary full text arXiv:2610.07924v1 (Theorem 1.1 and Sections 5–6) provides the structural forbidden-family characterization but neither the cactus-specific bivariate generating function nor its asymptotic density. Voblyi–Meleshko (2014) develops unrestricted block-cactus enumeration, a broader graph family whose basic block product cannot impose the local degree-two witness requirement. OEIS A091485 counts all triangular cacti, with a demonstrably different order-six count, and Mathar's unlabelled vertex-disjoint-cycle enumeration covers a different model. Mathematical-record searches for equivalent terminology, root-marked formulas, local triangle witnesses and exact counts produced no stronger covering theorem; close results on cactus B-coloring, homology, and chordal graph squares do not imply the new enumerator. Historical priority remains provisional, particularly for older formulas under net-free/cactus terminology.

## Value — PASS

The beautiful graph class was recently characterized by induced obstructions, creating a natural quantitative gap. The complete bivariate enumerator determines all labelled counts refined by two intrinsically distinguished cycle types, rather than isolated small orders. It exposes why block-wise filtering is insufficient, supplies concrete exact data, and proves that beautiful cacti are exponentially rare among all cacti. The rarity rate and correction term are natural structural outputs of the triangle-witness constraint, not arbitrary numerical slices.

## Limitations and closest literature

The classification is relative to Wunderlich's theorem and the asymptotics to standard analytic-combinatorics transfer. The numerical constants are approximate. Finite direct graph verification stops at six vertices; series verification at nine. No claim is made about all beautiful graphs or unlabelled cacti. Absolute historical priority and independent mathematical validation are not certified.

Self-review: passed. Independent audit: not yet performed.
