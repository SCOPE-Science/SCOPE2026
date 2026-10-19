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

# Reproducibility and checks

Execute `python3 verify.py` using Python 3 standard library. This verifies the exact seven-state and three-state characteristic-polynomial identities by formal multivariate integer polynomial arithmetic and independently enumerates all binary occupation configurations of \(C_3\square C_n\) for \(n=3,4,5,6\). It compares complete particle-number count distributions against a transfer recursion constructed from the five physical column symbols, giving totals \(17,49,125,323\). It numerically differentiates the explicitly proved Perron root for the reported thermodynamic constants. Analytic arguments in `RESULT.md`, not finite enumerations, establish the all-length generating identity and the normal fluctuation limit.

The procedure does not check arbitrary larger widths, sample physical culling endpoints, or establish uniqueness in the literature. No independent audit has been performed.
