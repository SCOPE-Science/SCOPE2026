# Independent three-axis audit — 2026-09-23

Source: `2026/09/08/034`; audited source-tree SHA `80776f3a73196a8ebed9b76dcf3a0bf2dcded635`; `RESULT.md` blob `ebd15c8d03639381bd0444e33559298fd883bbf4`.

## Claim checked
For `S_n`, `n=6,7,8`, the record claims that the Kronecker-square multiplicity vector of an irreducible character determines its partition label up to conjugation, with no other collisions, and supplies the lexicographically first separating constituent for every pair of conjugacy classes (15+28+66=109 separators).

## Correctness — passed
I independently recomputed the complete character tables from the Frobenius coefficient formula rather than using the record's Murnaghan–Nakayama artifacts. For every conjugacy class I verified character orthogonality, then formed all exact Kronecker-square coefficients by the class-sum inner product. The resulting numbers of distinct square vectors are exactly 6, 8 and 12 for `n=6,7,8`, and each fiber is exactly a partition/conjugate-partition pair, with the expected self-conjugate singletons. Using the record's ascending lexicographic partition order gives exactly 15, 28 and 66 first separators. The displayed `n=6` example `{(4,2),(2^2,1^2)}` versus `{(3,3),(2^3)}` first separates at `(3,2,1)` with multiplicities `(2,0)`. Conjugate invariance follows independently from `chi_{lambda^t}=sgn*chi_lambda`, whose square is unchanged.

## Originality — passed relative to checked literature
Searches targeted “Kronecker square determines partition”, “irreducible character square conjugate partitions”, tensor-square fingerprints, collisions, and square-root uniqueness. Pak–Panova–Vallejo (arXiv:1304.0738) and related Saxl literature study constituents/positivity in tensor squares, not equality/collision of complete square vectors for this finite range. Searches for a theorem asserting the same `n=6,7,8` separation or the 109 lex-first certificates found none. The result is therefore novel relative to the literature checked; this is not a guarantee of absolute priority.

## Scientific value — passed
The result gives an exact small-rank boundary for a natural character-recognition question, and the 109 minimal constituent certificates are more reusable than merely asserting pairwise distinctness: they provide a deterministic fingerprint test and compact regression dataset for character/Kronecker implementations. The calculation is exhaustive, exact-integer and independently reproducible.

No repair was needed. Relevant comparison literature was available on arXiv/OA; no Oxford fallback was needed. This is an independent AI audit, not a human/expert or Lean attestation.
