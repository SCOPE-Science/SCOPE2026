# Scientific review: fixed-content Simon-congruence classes

## Correctness — PASS
The mathematical statement is an exact, all-integer classification for binary linear words with precisely two ones, constant total zero count, and depth at least three, together with explicitly separated depth-one/two cases. Necessity follows from the two-one probes that extract clipped gaps and the one-one probes that extract two boundary flags. Sufficiency is established by exhausting subsequences containing zero, one, or two ones. The closed count follows by inclusion–exclusion on bounded triples, plus exactly four possible exceptional splits. The stabilization and its sharp threshold are derived from that count; no extrapolation from finite experiments is needed. The independent spectrum enumerator checked 10,374 words over 126 distinct depth/length combinations and the critical boundary cases. No external proof assistant or independent formal validation was used.

## Originality — PASS (best-knowledge, with priority risk)
The closest inspected foundational source, Karandikar–Kufleitner–Schnoebelen (2013), analyzes the unrestricted index and obtains necessary inter-marker constraints (Lemmas 3.1–3.2). Those constraints alone do not characterize the two residual boundary flags, nor provide the exact fixed-composition class count. Fleischer–Kufleitner (2018) computes general shortlex representatives and Gawrychowski et al. (2020) give linear congruence testing, neither a closed census of this slice. Fleischmann et al. (2026) concern a different, jumbled equivalence. Targeted searches for the exact formula, alternative gap-truncation signatures, and fixed-Parikh Simon types found no source implying the full claim. A differently named equivalent formula could remain undetected; the 2020 paper was compared at its abstract, not fully inspected.

## Value — PASS
The result answers a natural fixed-content restriction of a major quotient-size question in piecewise-testable language theory. It replaces potentially exponential subsequence spectra with a five-coordinate signature, counts every equivalence class across all zero counts, and proves a sharp finite saturation level and quadratic dependence on observation depth. These structural and exact-enumerative properties are not routine restatements of the general quotient-index bounds.

## Sources, limitations, and risk
The inspected comparison includes arXiv:1310.1278 (full relevant sections and appendix), arXiv:1804.10459 (normal-form sections and algorithms), arXiv:2005.01112 (abstract and bibliographic information), and arXiv:2610.17910v1 (introduction, definitions, algorithmic contributions). The result does not address three or more ones, larger alphabets, classes spanning distinct zero totals, or cardinalities of individual classes. Full historical-priority coverage cannot be certified by literature searches alone.

Self-review: passed. Independent audit: not yet performed.
