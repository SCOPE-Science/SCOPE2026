---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

The proof uses the derivative of multiplication of coprime monic factors, the explicit straightening of the two pure-power coefficient curves, the product ideal describing their transverse local union, and the restriction exact sequence computing depth. The intersection in the étale chart also computes the local dimension and depth at its generic image point.

The unchanged supporting `checks/verify_multiple_root_germs.py` includes finite projective tangent-space spot checks (computed on the affine cone), and finite spot checks of the formula for the Hilbert function of the transverse monomial model. Its additional one-cluster cusp tests and the ranges including \(m=2\) are background, outside the stated result. `checks/check_output.txt` records the outputs, with the dependency in `checks/requirements.txt`. These finite checks do not prove the uniform theorem or the depth computation.
