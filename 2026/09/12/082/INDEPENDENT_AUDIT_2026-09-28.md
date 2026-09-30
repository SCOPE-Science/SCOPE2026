# Independent audit — 2026-09-29

**Record:** `2026/09/12/082`  
**Disposition:** **passed**  
**Audited tree:** `4bca34f418cf59392364c3a9c3c9fb723ea1213c`

## Correctness
The structural implication rank 18 => ternary self-duality is exact because the incidence Gram matrix is 0 mod 3. The archived sweep has exactly 1458 uniquely named rows, all reporting RANK 18 MINWEIGHT 6. The representative and six additional spread-out samples were independently parsed and each satisfies row/column sums 15, pairwise row intersections 6, and GF(3)-rank 18. The 3^18 meet-in-the-middle verifier source was inspected; its packed ternary addition and exhaustive 9+9 split cover all information vectors and exclude zero.

## Originality
The exact 1458-matrix Goethals-Seidel data set is a concrete reproducibility artifact, but broad novelty should not be claimed: later/nearby literature classifies very large families of symmetric 2-(36,15,6) designs and computes their ternary codes. The record already avoids monomial-equivalence and isomorphism claims.

## Scientific value
The explicit matrices, per-design sweep ledger, and independent minimum-distance verifier form a useful finite dataset showing that full ternary rank need not imply extremality.

## Findings
- No substantive research-file correction is required.
- The sweep log has 1458 lines and 1458 unique filenames, with result sets rank={18}, minweight={6}.
- Representative plus six distributed samples independently satisfy the design equations and GF(3)-rank 18.

## Independent checks
- Parsed 1458-line sweep: no malformed rows, 1458 unique names, all rank 18/minweight 6.
- Independently checked representative and six distributed matrices for design equations and rank.
- Inspected exhaustive 9+9 ternary meet-in-the-middle implementation and C17 generator rank.

## Limitations
- The connector interface did not make a single bulk download of all 1458 matrices available, so this audit inspected the exhaustive sweep ledger/verifier and a distributed sample rather than re-running the C verifier on every matrix.

## Sources
- https://arxiv.org/abs/2209.13468
- https://arxiv.org/abs/2403.03381
- https://arxiv.org/abs/2303.05056
- repository:2026/09/12/082/artifacts/sweep_results.txt
- repository:2026/09/12/082/artifacts/minweight36.c
