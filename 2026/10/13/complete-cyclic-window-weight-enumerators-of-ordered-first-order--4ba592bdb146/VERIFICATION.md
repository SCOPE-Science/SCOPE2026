---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For each nonconstant binary affine truth table in increasing integer position order, its least active variable index t yields B=2^t sized constant blocks in opposite paired blocks. The higher affine bit pattern g(s) determines exactly j cyclic 1-to-0 transitions, giving j zero runs length2B and H-2j runs length B. The binary carry parity map from high coefficient bits to u_h is invertible over F2, making v enumerate 0..2^q-1 and j=ceil(v/2). Thus the endpoint/interior multiplicities mu_q(j) are 1/2 as stated, with extra factor2 for the affine constant; the two constant words contribute 1+z^N. This reconstructs the exact W_{m,b} formula for every m>=1,1<=b<=2^m, and the derived pair and minimum-b formulas. Independent truth-table evaluation, completely separate from the stated formula, checked all cyclic widths for each m=1..6. The analytical carry argument, not finite trials, proves the unlimited quantifiers.

## originality

PASS

Shi/Zhu/Helleseth provide the generic zero-run relation for any cyclic word, not the exact run-length distribution of these integer-ordered binary affine truth tables. Luo/Ezerman et al 2024 use a field-power/extended cyclic coordinate order; at m=3,b=2 their construction has minimum 6 while this order has 5, so Hamming code equivalence cannot transfer their b-symbol result. Resultary queries for first-order RM, Hadamard, natural-order b-symbol enumerators and zero-run distribution returned unrelated code families. The new all-m/all-b carry-induced multiplicity law is not logically implied by generic run transforms, subject to residual unindexed coordinate-specific literature.

## value

PASS

The first-order Reed–Muller/Hadamard code is canonical and cyclic b-symbol weights are intrinsically coordinate-order-sensitive. Computing all coefficients, not merely a minimum, for EVERY dimension and cyclic read width is a substantive natural family classification. The surprising uniform fourfold nonzero interior symbol-pair multiplicities and the binary-carry mechanism supply reusable exact structural content.

The dated certificate retains the supplied scientific assessment, sources and limitations.
