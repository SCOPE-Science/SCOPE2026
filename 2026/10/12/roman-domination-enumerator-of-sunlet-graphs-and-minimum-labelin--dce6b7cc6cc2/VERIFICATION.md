---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For any set T of cycle vertices labeled 2, the leaf/core local feasible pairs are exactly A=z²(1+z+z²) at T, B=z(1+z)² at non-T vertices neighboring T, and C=z²(2+z) otherwise. The full labeled weighted sum over T and trace of the four-state cyclic transfer matrix are identical; the determinant is D(u,z)=1−(A+C)u−Azu²−ABzu³. The formal logarithmic trace/determinant identity establishes the all-n generating function and characteristic recurrence without convergence assumptions. The lowest exponent is n+|T|+q(T), bounded by n+ceil(n/3), and cyclic gap sizes ≤3, plus one uncovered length-4 gap for n≡1 (mod3), yield the claimed multiplicities. Independently enumerated all 3^(2n) labelings for n=3,4,5; they equal the separate mask fiber polynomial (minimum coefficients 3,14,5). Independently checked the n+ceil(n/3) and closed coefficient formula by full T-mask enumeration for n=6..11. These finite tests do not replace the general gap/transfer proof.

## originality

PASS

Prior corona work determines only the Roman domination number; published related path/cycle/complete-base corona and minimal-RDF enumerators have different objects or predicates. No all-n all-weight C_n corona K1 polynomial or exact minimum-label multiplicities were located; the uninspected older primary body is recorded as priority risk.

## value

PASS

A natural parameter for Roman domination on a standard attached-cycle graph family: the all-weight polynomial, rational generating function, third-order recurrence, and exact residue-dependent number of optimum functions, beyond the known minimum weight. The specific full census is meaningful despite the standard transfer-matrix method and a previously known scalar invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
