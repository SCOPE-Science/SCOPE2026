# Review of exact exhaustive Lempel–Ziv phrase boundaries

**Correctness — PASS.** An infinite two-family block argument derives every phrase start. Each proposed phrase has a demonstrated occurrence of its proper prefix at an earlier starting position and cannot itself occur at an earlier starting position, with overlap permitted. The two phrase lengths telescope exactly, and the small ternary base is checked explicitly. An independent direct parsing implementation agrees for ten alphabet-scale parameter choices through 100,000 symbols. Finite computation is corroboration, not an infinite proof.

**Originality — PASS relative to inspected literature and database records.** The 2006/2007 Constantinescu–Ilie work supplies the general exhaustive-history definition and an asymptotic classification, but not these explicit Cantor-family start indices. Berstel–Savelli concern a distinct Crochemore decomposition. Five targeted database searches found related string-attractor and morphic-word records but no implications covering this exact formula. The full journal text was inspected; the full Berstel–Savelli source could not be read, so any hidden specialization remains an originality risk.

**Value — PASS.** A natural classical morphic family receives its complete infinite exhaustive parsing, not just an asymptotic complexity class. The result distinguishes the ternary Cantor word sharply from all larger parameters and identifies phrase locations and lengths as well as exact finite-stage counts; such information is relevant to the fine combinatorics of LZ compression on automatic sequences.

**Closest literature and limits.** Constantinescu–Ilie, *The Lempel–Ziv Complexity of Fixed Points of Morphisms* (2006/2007), proves only order-class information for this family, while Berstel–Savelli, *Crochemore Factorization of Sturmian and Other Infinite Words* (2006), uses a different parsing rule. This theorem is confined to the exhaustive-history convention and prefixes of the defined infinite fixed points. No independent verification beyond the reproducible calculations and this scientific review is claimed.

Self-review: passed. Independent audit: not yet performed.
