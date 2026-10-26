# Self-review

## Correctness — PASS
The theorem's integer domain, normalization, ordered edge indices and inverse-point indices were independently reconstructed from the signed binary-adjacency definition. Parity establishes that each pair of successive time indices is a vertical edge. Four-adic recurrences identify exactly \(2^k\) edges on the dyadic line, and the sign of the leading base-four digit fixes orientation. An induction using the companion sum recurrence gives an exhaustive permutation of the lower heights, permitting exact inversion. The attached verifier reconstructs the sums directly and checks all levels through \(k=7\). Finite tests do not replace the written proof.

## Originality — PASS with residual risk
The directly relevant 2023 full text contains the requisite recurrences and global geometric/counting theorems, but not the stated chronological dyadic height permutation and bit-dilation inverse. The earlier 1981 full paper addresses fractal dimension and global coverage. The 2013 plane-path documentation already provides **general coordinate inversion** and mentions the earlier-known boundary/interior visit multiplicity; neither is claimed new. The new narrowly specified structural result is an explicit closed form and chronological ordering at a canonical self-similar scale, rather than a new assertion that such inversion is possible. Search comparisons with named related sequence tables and current mathematical finding records uncovered no equivalent formula. The 1978 Brillhart–Morton primary text and a 1996 discussion were not fully inspected and may contain an equivalent expression; priority is not certified.

## Mathematical value — PASS
The dyadic frontiers are canonical self-similar cross-sections for the paperfolding walk. Their full ordered crossing permutation is a structural phenomenon (all even lower heights descending, followed by odd heights ascending), not merely a few numerical terms. The exact inverse evaluates the one or two visit times of an arbitrary lattice point on such a line by direct binary-digit arithmetic in logarithmic input length, avoiding traversal of the earlier quadratic-length path. These statements refine how a known plane-filling path fills its frontiers, while leaving arbitrary non-dyadic lines open.

## Limitations and nearest sources
See RESULT.md and AUDIT.json for exact theorem scope, direct comparisons with Rampersad–Shallit (2023), Mendès France–Tenenbaum (1981), Ryde (2013), OEIS A093573 and incompletely accessible Brillhart–Morton papers. Same-model source comparison is not proof of publication priority. This review is not an external validation.

Self-review: passed. Independent audit: not yet performed.
