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

The complete symbolic eigenpair, complex normal-form coefficient, amplitude reduction, and sharp minimum were checked using the included `check.py`, run directly from this package. SymPy confirms the identities as exact functions of a positive symbolic parameter, not through finite sampling.

Separate direct integrations at fixed exponents \(\gamma=1.5,2,3\) and positive offsets from Hopf corroborate the limiting coefficient but are neither an exhaustive parameter check nor a proof. They are finite-amplitude tests, so the observed estimates have nonzero asymptotic bias.

The result is local to nondegenerate Hopf bifurcation with \(\gamma>1\); no independent audit or external certification has been performed.
