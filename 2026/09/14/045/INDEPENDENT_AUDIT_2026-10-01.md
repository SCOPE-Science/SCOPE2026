# Independent audit — SCOPE-20260914-045

Audit date (UTC): 2026-10-01 (UTC)

## Final claim

The 11 stored pairs (F,l) realize the stated 11 potential rank-matrix/Jordan-degree-type variants for T=(1,3,6,6,6,6,6,3,1) over each of GF(1000000007) and GF(1000000009); no characteristic-zero realization is claimed.

## Correctness

**PASS** — A fresh independent exact modular reconstruction, implemented separately from the package verifier, rebuilt the catalecticants and multiplication-by-powers rank matrices for every one of the 11 stored certificates over both stated primes. For all 22 field/certificate checks it reproduced the Hilbert function (1,3,6,6,6,6,6,3,1), the stored central rank and Delta data, and the complete stored Jordan-degree-type signatures. Thus the finite-field existence claim is verified. This does not establish characteristic-zero realizability, which the record explicitly disclaims.

## Originality

**PASS** — The AAIY source explicitly gives at most 65 potential JDT for the s=6 family and leaves occurrence as an open question. Its Table 6 and Question 4.13 were inspected. The record’s 11 explicit two-prime realizations are not supplied by that classification, and no exact prior database/table of these 11 certificates was found in Resultary or the checked literature.

### Equivalent formulations

Aliases and equivalent formulations were compared against the closest primary sources; the assessment follows implication rather than title matching.

### Broader coverage

The checked broader theorems do not imply the exact final claim under the same hypotheses.

### Exact database or table

The primary s=6 classification lists potential types but does not provide the 11 explicit two-prime realization certificates.

### Claim versus prior implication

The AAIY source explicitly gives at most 65 potential JDT for the s=6 family and leaves occurrence as an open question. Its Table 6 and Question 4.13 were inspected. The record’s 11 explicit two-prime realizations are not supplied by that classification, and no exact prior database/table of these 11 certificates was found in Resultary or the checked literature.

## Value

**PASS** — These are exact finite-field realizations in the minimal k=5 case of a published open occurrence problem, across seven Table-6 rows. Even without characteristic-zero lifting, they provide motivated boundary data about which conjectural Jordan-degree types actually occur in two large characteristics.

## Source inspections

- Jordan degree type for codimension three Gorenstein algebras of small Sperner number — https://arxiv.org/abs/2406.06322 — PARTIAL_COVERAGE: The paper delimits potential types and asks about occurrence; it does not furnish these 11 certificates.
- Jordan types with small parts and Gorenstein Hilbert functions — https://doi.org/10.1016/j.laa.2022.03.013 — NOT_COVERING: General Jordan-type constraints do not imply these explicit k=5 finite-field realizations.
- Published-results semantic search — https://github.com/Resultary/2026/tree/main/2026/9/14/SCOPE045 — NO_STRONGER_MATCH_FOUND: The exact record was the direct match; no distinct published SCOPE result supplied these 11 occurrences.

## Residual risks

- Literature search is best-of-knowledge and cannot exclude an obscure or unindexed source.
- The audit credits only inspected proofs, source material, and fresh computations described above.

## Disposition

PASSED
