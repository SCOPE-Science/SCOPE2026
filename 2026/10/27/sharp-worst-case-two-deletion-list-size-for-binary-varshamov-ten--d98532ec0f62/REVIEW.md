# Three-axis mathematical assessment

## Correctness — PASS
The proof applies to all integers \(n\ge2\), all binary VT checksum residues and all received words of length \(n-2\). The sharp upper bound follows by counting disjoint sets of intermediate words, proving that at most two of the sets can be singletons, and exhibiting the all-zero exact sharp witness. The key nonstandard assertion is the distinctness of the integer checksum increments for canonical two-symbol same-run insertions; the proof handles both inserted symbols and the interval bounds, and finite enumeration independently checks it. The complete all-length claim is proved symbolically; no finite census is used as its proof.

## Originality — PASS
The closest accessible 2017 primary source establishes a general upper bound of \(n\) lists for two deletions from a VT class; the 2026 source establishes averaged bounds, not a sharp individual maximum. Relevant record queries and historical claim statements revealed no implication equivalent to the exact \(\lfloor n/2\rfloor+1\) theorem. Single-deletion uniqueness and two-insertion ball counts are classical, not new. An unindexed equivalent remains a residual priority risk.

## Value — PASS
The exact worst-case ambiguity of two deletions is a natural operational invariant, directly motivated by existing VT list-decoding and recent average-list research. The bound is sharp for every length and closes a factor-of-two upper-bound gap, without claiming better complexity or extending to arbitrary alphabets.

## References and limits
Primary comparisons: Wachter-Zeh, arXiv:1701.02612 Section VI; Banerjee–Con–Wachter-Zeh–Yaakobi, arXiv:2610.15767 Section IV. Scope is binary, exactly two deletions, maximum over checksum classes. Priority relative to all unindexed literature and independent validation remain unresolved.

Self-review: passed. Independent audit: not yet performed.
