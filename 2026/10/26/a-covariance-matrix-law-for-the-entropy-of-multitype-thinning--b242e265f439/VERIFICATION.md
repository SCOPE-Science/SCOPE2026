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

# Verification scope
Run `python3 check.py` with Python 3 standard library. The program independently enumerates the bivariate retained-count distribution conditioned on the number of nonzero source vectors. It checks exact-rational means, marginal second factorial moments and joint covariance for 24 values of the aggregation size, verifies the first two monic Charlier identities, and reports normalized joint and marginal KL divergences at six finite sizes. The computation is a finite check, not a proof of convergence. The proof of the infinite limiting law is the global entire-function coefficient estimate and dominated-convergence argument in `RESULT.md`; the KL and total-correlation assertions do not rely on extrapolation from these finite samples. Neither an independent audit nor independent validation has been performed.
