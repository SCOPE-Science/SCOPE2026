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

`artifacts/verify.py` checks the invariant-tensor coefficients \(\alpha,\beta\), the contractions for \(\mathbb E(\operatorname{tr}PH)^2\) and \(\mathbb E L''(0)\), and the resulting \(q(q-n)\) Hessian factor with exact rational arithmetic over a grid of admissible dimensions and integer \(q\)-values. Replay from the packaged artifact returns `VERIFY_OK`.

The script does not prove orthogonal invariance of Haar measure, Gaussian integration, or originality. Those inputs are handled in the mathematical proof and literature comparison. The finding is local and second-order; no higher-order conclusion at \(q=n\) is verified.
