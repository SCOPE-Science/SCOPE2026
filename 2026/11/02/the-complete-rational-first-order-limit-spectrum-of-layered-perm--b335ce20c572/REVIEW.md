# Review of the complete rational first-order limit spectrum of layered permutations

## Correctness — PASS

The proof identifies the uniform layered-permutation measure with independent fair cuts and interprets TOTO in the first-order binary-word language. The standard aperiodic-automaton equivalence together with a finite rational Markov-chain argument gives rationality of every limit. The family of equally long words \(w_j=0^{t+3}1u_j1\) has no cross-bifix overlap: a suffix of length at most \(t+3\) ends in \(1\) while a corresponding prefix is all zeros; a longer overlap begins within the run of leading zeros and reaches its first one too early. Consequently swapping pattern labels is an involution, yields exact conditional uniformity, and gives the finite-size identity. The disjoint-block bound proves exponential convergence, and direct first-order occurrence definitions give quantifier rank at most \(2\max\{1,\lceil\log_2 b\rceil\}+8\). The `checker.py` corroborates finite instances; it does not certify arbitrary denominators. A standard aperiodicity/Markov-chain theorem is used as an explicit premise.

## Originality — PASS within inspected evidence

Braunfeld–Kukla (2022, arXiv:2111.06307, Lemma 3.5/Theorem 3.6) gives layered first-order convergence and its dyadic Markov construction implicitly rationalizes limits, but not the exact spectrum. Falgas-Ravry et al. (2026, arXiv:2610.34328, Theorem 1.4) give density for a broad class, not universal rational attainment. Berthé–Goulet-Ouellet–Perrin (2025, ICALP 143) derive density formulas for aperiodic languages; this is related, but their inspected theorem does not state the current complete spectrum. A previous rational-attainment calculation for a stricter Fibonacci subclass uses a related disjoint first-occurrence technique; it cannot logically imply the new full-class result. Historical priority under broader coding-language terminology remains a meaningful risk, so the review asserts only best-knowledge originality.

## Value — PASS

This is a complete exact determination of a natural first-order limiting-probability invariant, not a narrow arbitrary slice or a recomputed table. The explicit finite-size symmetry upgrades known density to exact rational attainment, and rational exclusion closes the classification. Its scope is uniform sampling in first-order TOTO; it does not cover nonuniform models or stronger logics.

## Verification limits and sources

Core proofs and finite cross-checks are in `RESULT.md` and `checker.py`. The closest primary sources are arXiv:2111.06307, arXiv:2610.34328, and DOI 10.4230/LIPIcs.ICALP.2025.143. The historical-priority and independent mathematical review questions remain open.

Self-review: passed. Independent audit: not yet performed.
