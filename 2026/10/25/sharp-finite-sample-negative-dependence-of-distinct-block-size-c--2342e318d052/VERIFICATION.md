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

# Reproducibility

Run `python3 verify.py` in the directory containing the result and the verifier. It uses only the Python standard library, integer arithmetic, and exact rational counting; the recorded output is `VERIFY_OK 50619 exact assertions; 23712 Dyck paths`. The exhaustive Dyck paths are all paths of semilengths two through ten. Block sizes correspond to maximal down-run lengths. The verifier separately checks the binomial mixed-moment formula, cross-covariance signs and the sharp all-size equality examples, together with algebraic ratio-step bounds at additional finite sizes.

The mathematical proof is the Lagrange coefficient extraction and exact monotone-ratio identity in RESULT.md. Finite enumeration alone does not verify the theorem for arbitrary \(n\). This package does not contain or claim independent expert validation.
