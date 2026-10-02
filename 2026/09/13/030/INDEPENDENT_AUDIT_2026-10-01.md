# Independent mathematical audit — SCOPE-20260913-030

Disposition: **PASSED**.

## Correctness
**PASS** — The primary 14-system dataset was independently decoded. Every decoded object satisfies the STS(21) pair condition, and an independently written root-based mitre counter reproduced the full vector 45,51,39,39,27,42,45,35,21,21,42,44,46,45, so the exact minimum is 21 at systems 8 and 9.

## Originality
**PASS** — The Kokkala-Ostergard paper and dataset establish the complete anti-Pasch/Kirkman catalog but the inspected primary material does not state the mitre vector or minimum; targeted Resultary/literature searches found no prior exact value.

### Equivalent formulations
The minimum-mitre statement and the no-5-sparse conclusion are the same finite-catalog fact after anti-Pasch is fixed.

### Broader coverage
The prior classification supplies the universe being audited but does not, in inspected material, cover the exact mitre minimum.

### Exact database or table
The exact table was recomputed from the primary catalog rather than inferred from the saved counts_raw.txt.

### Claim versus prior implication
The catalog plus the definition does not mechanically yield 21 without the finite count performed here.

## Value
**PASS** — The exact minimum directly answers the natural 5-sparsity question inside the complete resolvable anti-Pasch STS(21) catalog and identifies the extremal systems.

## Source inspections
- **Sparse Steiner triple systems of order 21** (doi:10.1002/jcd.21757): Publisher/research-portal abstract and bibliographic record. Assessment: NOT_COVERING_EXACT_MINIMUM. Abstract gives 83,003,869 classes, three 5-sparse systems, and 14 KTS, but no mitre vector.
- **Sparse Steiner Triple Systems of Order 21 dataset** (doi:10.5281/zenodo.3899950): Dataset description/file-format documentation and the 14-system text mirrored in the audited package. Assessment: PRIMARY_DATA_REPLAYED. All 14 decoded systems are valid STS(21); independent mitre counts reproduce the claimed vector and minimum.

## Residual risks
- The publisher full text was not inspected in full during this run; the primary abstract and primary dataset were inspected. A hidden table in the full article could reduce originality, though targeted searches found none.
