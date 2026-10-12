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

`verify.py` uses exact rational arithmetic and a small exact multivariate polynomial representation. It reconstructs the \(\alpha\)-permanent from the permutation definition, verifies coefficient-by-coefficient that the unique order-three overlapping defect equals the factored expression used in the proof, and checks all subset pairs for an explicit nonsymmetrizable inverse \(M\)-matrix at several positive rational values of \(\alpha\).

The universal proof does not depend on sampling. The finite exact example only checks implementation consistency and demonstrates coverage outside the symmetrizable class. The four-dimensional sharpness boundary is taken from Sra, arXiv:2609.39979v1, Remark A.2, rather than re-proved computationally here.
