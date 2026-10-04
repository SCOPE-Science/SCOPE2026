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

Run `python3 verify_census.py`. A successful replay prints `VERIFY_OK`, the total \(788035\), rank counts \(0:11635\), \(2:122320\), \(4:654080\), the identity-containing zero count \(10795\), the remaining zero count \(840\), and the reduced maximal-rank fraction \(1792/2159\).

The verifier uses only exact bit arithmetic. It enumerates each three-space exactly once in reduced-row-echelon form and constructs \(L_U\) by two independent formulas: direct expansion of all \(24\) standard-polynomial monomials and a grouped characteristic-two expansion. The program aborts if the two operator matrices disagree for even one space.

The verification establishes the stated finite census. It does not by itself establish novelty in the literature or any extension to \(q>2\), larger \(n\), or other \(k\).
