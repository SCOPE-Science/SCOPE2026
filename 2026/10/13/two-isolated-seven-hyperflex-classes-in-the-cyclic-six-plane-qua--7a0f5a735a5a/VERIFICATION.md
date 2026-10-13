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

The exact symbolic verifier `verify.py` reconstructs the Hessian of the specified plane quartic over the rational coefficient ring, proves the affine polynomial reduction, and checks the resultant, discriminant, boundary flex and triple-root exclusion identities. Run with Python 3 and SymPy using `python verify.py`.

The proof, not a numerical experiment, determines all geometric points by splitting into the unique point at infinity, the four affine points with the first coordinate zero, and the six-point fibers over the roots of the Hessian cubic. The quartic is smooth on the stated domain by its displayed partial derivatives. The double-root criterion uses the exact cubic discriminant, and the distinction of isomorphism classes uses the cited primary classification.

Not checked: positive characteristic, arbitrary genus-three quartics, exhaustive unpublished literature, or independent external validation. This is self-review only.
