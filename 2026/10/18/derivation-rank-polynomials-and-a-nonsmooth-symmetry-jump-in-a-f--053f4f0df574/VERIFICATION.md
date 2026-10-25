---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The rank count separates characteristic odd/even via 2Xu=2Yv=0. In odd characteristic the 3x3 lower triangular matrix yields the stated rank counts. In characteristic two the 4x3 matrix splits into nonzero-constant and zero-constant slices; the former normalizes a nonzero covector by GL2, the latter uses rank and trace of a 2x2 block, giving sums q^8. The coordinate ring with a0²=b0²=0 and Δ invertible proves reduced dimension 6 vs tangent dimension 8. Boundary q=2 fits and q=3 agrees with symbolic formulas. Script output was not rerun; all-field correctness rests on the symbolic proof, not finite logs.

## originality

PASS

The materially inspected same-algebra primary paper works over characteristic zero and gives automorphism generators, not the finite-field rank distribution or characteristic-two nonreduced scheme; no exact covering table was located in bounded Resultary search. This is a best-of-knowledge finding with residual literature risk.

## value

PASS

The natural length-four complete intersection is a minimal test case for a characteristic-two jump in infinitesimal algebra symmetries. Exact rank-polynomial distributions for all derivations give meaningful fine structure absent from ordinary automorphism-point counts, and the nonreduced group-scheme coordinate ring explains the tangent excess. This is a motivated exact invariant beyond raw code reproducibility.

The dated certificate retains the supplied scientific assessment, sources and limitations.
