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

Run `python verify.py` using Python 3 and its standard library. It enumerates all candidate finite-dimensional matrices satisfying the defining Rota–Baxter equation, both over the fields of sizes two and three, at sizes one through four. Independently, it enumerates every Prüfer-coded rooted labeled tree and nonroot coloring through size five and obtains matrix rank from the proved tree statistic. A third exact-rational implementation calculates the marked rooted-tree functional-equation coefficients and checks the full polynomial at evaluation points sufficient to identify all coefficients through degree five. It verifies the exact mean formula against the complete finite enumerations. The expected terminating line is `VERIFY_OK`.

The computations are exhaustive only at the stated finite sizes. The code is not a general symbolic proof; the general kernel-basis argument, labeled exponential formula, and covariance bound are provided in RESULT.md. No independent audit has been performed.
