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

The analytic proof is the controlling evidence. The accompanying `verify.py` performs the following independent replay checks:

1. expands the exact polynomial identity obtained by substituting the candidate common root of \(Q_\lambda\) and \(D_\lambda\);
2. verifies that the critical quartic has one coefficient sign change and opposite exact rational signs at \(2.102815\) and \(2.102816\);
3. computes the positive root to high precision;
4. reconstructs the upper nonsymmetric branch at several values \(\lambda>\lambda_c\) and checks the original two fixed-point equations numerically;
5. checks that the same branch condition is negative at a sample point below \(\lambda_c\).

The replay does not use finite sampling to prove the global phase count. Global uniqueness of the positive critical root follows from Descartes' rule, and the branch count follows from the analytic quadratic reduction and sign argument in `RESULT.md`.

Scientific limit: this verification concerns the translation-invariant boundary-law system only and does not test extremality or non-translation-invariant Gibbs measures.
