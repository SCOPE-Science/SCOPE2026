# Review of the exact string-attractor profile of the powers-of-two word

## Correctness — PASS

The claimed minimum is proved by a constructive upper bound and independent lower bounds. The upper bound partitions factors into zero-only, one-one, and multiple-one cases, and supplies explicit attracting positions for either half of each dyadic length block. The projection lemma shows that appending zeros before the next one cannot reduce the minimum: any factor of the dyadic prefix covered across the appended part either is a zero power or has a single one, and can be moved to a distinguished prior zero position. On the dyadic prefixes, nonoverlapping uniquely occurring factors yield the exact baseline lower bounds. For even depth past the half-block threshold, a new zero-only factor forces a further position disjoint from all earlier witnesses. All boundary cases are dealt with separately. The standard-library `verify.py` independently checks factor coverage, lower-certificate occurrence regions, and exact small minima and returns `VERIFY_OK`. Finite checks supplement, not replace, the proof.

## Originality — PASS (qualified)

The decisive comparison is with Schaeffer and Shallit, arXiv:2012.06840, §6, Theorem 8, whose **same-word, same-range, same-numerical bounds** are already established as *upper bounds*. The text after that theorem specifically identifies matching lower bounds as requiring another argument. The present result proves these missing matching lower bounds for **every** prefix length, yielding the full exact minimum profile. This is not a change of terminology or a recomputation of the known upper construction. Restivo–Romana–Sciortino, arXiv:2206.00376, Example 3 and Figure 1, supplies only the logarithmic-order classification for the exact word; that asymptotic equivalence cannot determine thresholds or sharp constants. Mantaci et al., arXiv:1907.04660, concern different finite families; the 2023 simple-Parry and 2025 beta-integer word studies involve different objects. Searches for matching lower-bound proofs, equivalent terminology and explicit profile sequences did not reveal a covering publication. This search is not proof of priority, and an unindexed equivalent remains a residual risk.

## Mathematical value — PASS

The exact minimum size for a canonical sparsely supported automatic word is a motivated, previously explicitly incomplete profile, not an arbitrarily selected finite computation. The result closes the gap left by the known explicit attractor constructions, explains the exact powers-of-four jump locations, and supplies a reusable non-overlap certificate and trailing-run projection method. It resolves the natural all-prefix question, strengthening a broad logarithmic asymptotic statement to complete integer-valued enumeration.

## Scope and residual risks

The proof uses the precise zero-based indexing and linear-prefix definition of string attractors. It does not address every smallest attractor or other automatically generated words. The closest source explicitly provided an upper bound but not the new lower bound; an unpublished or differently indexed matching lower bound remains possible. Computational evidence covers only finite prefixes, while the written combinatorial argument is infinite.

Self-review: passed. Independent audit: not yet performed.
