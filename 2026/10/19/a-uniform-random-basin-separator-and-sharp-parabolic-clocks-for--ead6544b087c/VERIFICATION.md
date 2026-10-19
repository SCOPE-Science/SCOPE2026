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

# Reproducible evidence and scope

Run `python verify.py` with Python 3, NumPy and SymPy. The checker asserts the quadratic endpoint constant `pi**2/5`, the exact fair-coin drift cancellation, inverse-distance coefficient signs at both endpoints, sum of map derivatives, monotonic interval preservation, and six seeded biased-trajectory diagnostic clocks. The observed result in this run was `PASS 18 symbolic, map-order and seeded numerical diagnostics`.

The theorem's pathwise limit, the uniform distribution of the random basin separator, the universal almost-sure statement and the normal fluctuation limit are established by mathematical arguments in RESULT.md (bounded (sub/super)martingale convergence, SLLN, countable order squeezing, classical CLT). The verifier cannot turn finite numerical diagnostics into a proof of such probabilistic infinite-time statements. No independent validation or external certification has been performed.
