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

## Exact checks

The complete standalone script `verify.py` checks integral conic restrictions and elimination factors, the three conic Hessian determinants, four tangent-line restrictions, four line–conic discriminants, incidence exclusion tables and characteristic-seven line equality. It enumerates projective points over 26 prime fields from 7 through 109, confirming the stated rational singular-point counts. The script was executed and returned `VERIFY_OK`.

## Scope of verification

The universal prime-characteristic statements are deduced from exact factorizations and pairwise local intersection multiplicities, not from the finite-field enumeration. The symbolic tests use rational arithmetic; the modular specializations use the exact integral models. Computation of the full singularity scheme or the local Tjurina algebra is not part of this verification. No independent audit or external validation has been performed.
