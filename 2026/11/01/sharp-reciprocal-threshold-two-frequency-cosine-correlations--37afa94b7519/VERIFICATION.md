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

# Verification and limits

The standalone `CHECK.py` executes entirely with Python 3 standard-library exact integer and rational arithmetic. It independently constructs the common positive and common negative threshold arcs for each pair, intersects these arcs using endpoint arithmetic, and compares that measure against the Fourier/Bernoulli formula. It then performs a finite extremal search including all coprime pairs with larger frequency at most 160 and thresholds through index 52, and checks the Bernoulli difference inequality on a rational grid.

Expected checker output: `CHECK_OK 386617`. The analytical proof in `RESULT.md`, rather than this finite enumeration, establishes the theorem for every integer threshold and unbounded integer frequencies. The check does not verify a result for other thresholds or higher cardinalities. No independent mathematical audit has been performed.
