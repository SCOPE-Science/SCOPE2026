# Scientific assessment: A six-factor criterion for circular subsequence universality in binary de Bruijn cycles of order five

## Correctness — PASS

The proof establishes a bijection between all binary order-five de Bruijn necklaces and those of the 65,536 four-suffix Boolean feedback maps whose induced 32-state permutation is a single cycle. The checker iterates every map with integer arithmetic, separately reproduces the complete 2,048-necklace set by Euler tours, and compares greedy complete-arch indices with independent earliest-embedding distinct-subsequence dynamic programming at all 32 rotations. Its exact 512/768/768 feedback table proves all class frequencies; the two relevant feedback entries exactly characterize the two circular alternating length-six factors, and both together force a prohibited 2-cycle. The complete finite proof is in RESULT.md, the executable exhaustive enumeration in checker.py. Finite claims only, no infinite inference.

The statement is a finite theorem. The verifier does not sample a subset, infer from a timeout, or claim an infinite extension; exhaustive coverage follows from the bijection between valid sixteen-output feedback maps and order-five binary de Bruijn necklaces. The source includes all definitions, code, and exact target counts, and comparisons use separate constructions of the cycles and of the invariant. Evidence is the self-contained `checker.py` and the finite-exhaustive proof in `RESULT.md`.

## Originality — PASS, with residual uncertainty

Full-text research on de Bruijn cycles, finite-word subsequence universality, arch factorizations, and circular scattered-factor universality was compared at statement/implication level with the exact 2048-cycle rotation spectrum and six-factor iff criterion. The most relevant sources supply the object, enumeration methods, or general arch machinery but not the specific order-five joint spectrum or local six-factor witness. A published general finite-word generating function concerns all words of given length and does not determine this restricted conditional distribution. Previously accessible classifications of BWT-run and palindromic invariants on the same order-five cycles are logically different. Searches do not prove priority; an uncatalogued equivalent finite census remains a disclosed risk.

The closest primary sources are Zhi Xu (arXiv:1004.1216v1), Barker et al. (arXiv:2003.04629), Fleischmann et al. (arXiv:2104.09063), and Gabric–Sawada (arXiv:2005.01638). The first counts/constructs contiguous de Bruijn and multi-shift factors; the second and third develop general scattered-universality and arch methods; the fourth concerns discrepancy. None of the relevant inspected statements supplies the full conditional 512/1536 count, the 23/9 and 28/4 per-rotation profile, or the six-factor criterion. OEIS A169672 documents one cycle only. The 1946 paper is bibliographically verified, but its full text was not examined. Exact source comparisons, equivalences and uncertainties are recorded in `AUDIT.json`. Absence from search results alone is not taken as priority proof.

## Value — PASS

Classical de Bruijn cycles are maximally universal for contiguous five-bit windows, but scattered-subsequence universality of a single circular traversal is a different natural invariant. The exact dichotomy, its sharp index endpoints, and the small six-letter alternating-factor obstruction give a structural recognition criterion across all 2,048 cycles instead of a list of samples. Exact per-rotation class frequencies complete this tractable order-five census and create reproducible benchmarks for subsequence-based sequence analysis. The small rank is mathematically motivated by its classical full necklace count and exhaustive feasibility. No unproved relevance to larger orders or performance application is asserted.

## Scope and limitations

This classification is restricted to binary order-five de Bruijn circles and circular traversals of exactly 32 symbols. The theorem does not assert a new result for all word lengths or alphabet sizes. Exhaustive historical priority and external verification are not asserted. The dated primary source anchoring the classification is arXiv:1004.1216v1 from 2010-04-08; the 1946 foundational paper has only year-level publication evidence.

Self-review: passed. Independent audit: not yet performed.
