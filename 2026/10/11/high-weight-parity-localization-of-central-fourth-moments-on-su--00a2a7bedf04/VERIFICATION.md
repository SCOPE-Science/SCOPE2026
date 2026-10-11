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
# Reproducible verification

Run `python3 verify.py` with Python 3's standard library. The script checks exact finite Clebsch–Gordan product sums against the independent four-index expansion for 216 Gaussian-integer coefficient examples, using eight different finite offset sets and three base weights for each. It also checks the exact rational optimized \(C(e,o)\) formula against its stationary point across all eight examples.

The proof in RESULT.md covers all finite offset sets and arbitrarily large integer weights. Finite checks do not establish the infinite claim. There has been no independent audit.
