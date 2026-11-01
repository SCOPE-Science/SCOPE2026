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

The analytical proof establishes the exact norm formula, dual polar support, nonattainment obstruction, the finite-budget lower certificate, the continuous upper construction, and the matching limit coefficient. No independent external audit is claimed.

Execute the standalone `check_projection_regularization.py` using Python 3. The accompanying script imports only the standard library. The checker derives the root, regularization coefficient, scalar truncated-profile roots for \(K\in\{20,40,80,160,320,640\}\), sample norm bounds, sample Lipschitz inequalities, moment normalizations, and polar support identities. Its successful execution printed `Numerical assertions passed: 31047`.

Finite numerical tests are not exhaustive and do not replace the analytic proof. The regularization limit is over real \(K\to\infty\); no finite experimental cutoff is used as a proof.
