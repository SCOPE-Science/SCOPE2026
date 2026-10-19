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

The proof of the global theorem is analytic and self-contained in RESULT.md. The accompanying `check.py` uses Python's standard library and a fixed seed to test the direct Fourier two-arc formula and bound for 18,000 separated arc pairs, compare connected and antipodal arc families for 2,000 parameter tuples, and check 1,000 piecewise-constant sampled masks using exact Fourier cell-integration factors. Running `python check.py` produced `PASS 21000 deterministic checks, all bounds hold`.

The samples check implementation and normalizations, not exhaustive continuum validity. Weak-* compactness, the bathtub principle, strict endpoint convexity, and the matrix trace identity supply the continuum proof and equality cases. No independent audit or external certification was carried out.
