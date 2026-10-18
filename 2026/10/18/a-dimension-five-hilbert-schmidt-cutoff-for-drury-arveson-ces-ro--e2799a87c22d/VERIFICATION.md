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

# Reproducibility and verified scope

Run `python3 verifier.py` with standard Python 3. The script checks 600 exact rational identities over dimensions \(2\le d\le5\), input degrees \(0\le m\le5\), and increments \(0\le k,l\le4\). It also checks nonzero action on the constant vector and positivity of the fixed-increment obstruction terms through dimension eight. Expected output: `DRURY_CESARO_COMMUTATOR_EXACT_IDENTITIES_OK cases=600`.

The algebraic checker supports Steps 2–4 of `RESULT.md`; it is not an exhaustive check of all indices. Hilbert–Schmidt convergence and divergence for every dimension are proved by the explicit estimates in Steps 4–5, not inferred from numerical experiments or finite enumeration. Full-text bibliographic comparison of the closest 2026 preprints remains incomplete; independent audit has not been performed.
