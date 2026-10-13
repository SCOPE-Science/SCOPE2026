---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The symbolic proof is valid for every \(n\ge2\) and \(m\ge2\) in the stated domain. The standalone checker `artifacts/verify.py` independently constructs the graph, enumerates all \(3^{1+nm}\) labelings for a bounded test suite, tests the Roman condition directly, and compares the full coefficient vector with the claimed polynomial.

The replay suite uses \((n,m)=(2,1),(3,1),(4,1),(2,2),(3,2),(2,3)\), totaling \(4968\) labelings and reaching order \(7\). The \(m=1\) cases are deliberately included only as boundary stress tests. The checker also verifies minimum weight \(2\), uniqueness of the minimum function, and the total-count specialization at \(x=1\).

A successful replay prints exactly one line beginning with `VERIFY_OK`. This finite computation supports implementation and boundary checking; it is not used as a proof for infinitely many parameter pairs and does not assess originality.
