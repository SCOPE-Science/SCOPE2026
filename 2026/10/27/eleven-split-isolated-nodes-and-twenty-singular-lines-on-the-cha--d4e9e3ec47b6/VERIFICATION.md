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

## Reproducibility and scope
Run `python3 barth_nieto_char3_checker.py`. The finite-field checks independently confirm the 91/46 rational-point counts, singular-stratum counts 20/15/11, and isolated-node Hessian determinants 2 and 1 modulo 3. The general singular-locus statement over the algebraic closure follows from the separate Jacobian proof in `RESULT.md`, not merely from this finite enumeration.

The nonreduced Jacobian structure on the singular lines and semistable reduction are not calculated. No independent scientific audit has been performed.
