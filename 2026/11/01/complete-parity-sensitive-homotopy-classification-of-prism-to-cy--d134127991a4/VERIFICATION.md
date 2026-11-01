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

The finite verifier `artifacts/verify_prism_targets.py` was executed from this package and its recorded output is included as `artifacts/verification_output.txt`. It independently constructs signed rim and vertical color assignments, checks edge compatibility, and enumerates the entire graph of single-vertex recolorings. It checks the winding counts and the predicted parity splitting for selected source and target sizes, including odd target \(q=3\), even targets \(q=6,8\), and sharp boundary lengths \(n=q\). This is finite corroboration, not a proof for all parameters or of the circle component homotopy types. The latter follows from the printed proof and the sourced component theorem of Fujii et al. and the target-fold equivalence. The \(q=4\) case is proved by folding and is not covered by the signed-increment verifier.
