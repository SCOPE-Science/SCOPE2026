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

# Reproducible checks and scientific scope

The Python 3 file `verify.py` is standalone and contains no external dependencies. Run `python verify.py` in the directory holding it. The observed completion message was `PASS 3086 exact checks`, including comparisons to an independently implemented complete enumeration of uniform vertex rankings on all unlabeled tree shapes through seven vertices and separate path/star tests through eight vertices. A 39-by-39 degree-pair grid checks the algebraic distance-two identity and positivity of the local kernel with rational arithmetic.

The mathematical proof is in `RESULT.md`: only neighborhood overlaps at graph distances zero, one, and two contribute, and two beta-integral identities determine the exact pair covariances for arbitrary positive integer endpoint degrees. Finite verification does not replace the all-order proof. There is no claim of a joint limit law, independent audit, or automated theorem certification.
