# Scientific review

## Correctness — PASS

The theorem is established for every positive integer parameter, not extrapolated from small cases. The canonical left/right embedding union bounds the symbol counts; incompatible shared symbols give the essential dichotomy. Exact subsequence conditions around the two middle zeros, plus single-deletion minimality, force matching numbers of exterior ones, yielding a bijection with two bounded binary interleavings. Complementation doubles the disjoint count. A standard ratio bound and Stirling's formula prove the limiting law. The bundled self-contained checker independently tests the enumeration and minimality of the constructed words and compares with exhaustive sets up through the fourth parameter.

## Originality — PASS, with residual priority risk

The 2026 Sopp–Liyanage–Gong–Zhu paper supplies a general enumeration algorithm and structural graph but not the stated closed length spectrum. Lin's 2026 bound on numbers of length-constrained minimal common supersequences is not sharp enough to imply the expression; Fraser's 1995 treatment provides a dynamic-programming characterization; the 2022 Alon–Bourla–Graham–He–Kravitz result concerns shortest common supersequences and general bounds. OEIS A112029 already records the same numerical sum and its asymptotic, so neither the integer sequence nor the underlying arithmetic identity is asserted to be new. The substantive difference is the new word-theoretic classification, the formula for *every length*, and the corresponding geometric limit. An overlooked equivalent specialization remains possible.

## Value — PASS

The paired words are the simplest nontrivial equal-multiplicity strings with reversed run order, a canonical adversarial merge instance. In the newly developed minimal-common-supersequence enumeration setting, the result determines exactly how many irreducible merges of each length exist, identifies every attainable length from shortest to longest, and gives explicit asymptotic concentration near the longest irreducible merge. This offers a closed-form benchmark and structural example that generic enumeration-time bounds do not supply. The question and the invariant are natural before applying the computation.

## Literature and limitations

Primary: arXiv:2603.22591v1 (2026-03-23), arXiv:2609.26650v1 (2026-09-22), arXiv:2209.11882v1 (2022-09-23); also Fraser's 1995 thesis, Chapter 6, and OEIS A112029. The theorem is only for the stated opposite equal-block words. Earlier unpublished or unindexed proofs of the same family may exist; general-purpose enumeration methods can produce finite instances but do not themselves provide the displayed closed-form theorem. The numerical binomial-sum sequence is previously known.

Self-review: passed. Independent audit: not yet performed.
