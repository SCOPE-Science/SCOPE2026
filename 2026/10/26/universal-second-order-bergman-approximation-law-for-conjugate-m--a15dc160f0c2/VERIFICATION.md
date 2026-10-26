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

The proof relies on the product formula in `RESULT.md`, which is derived directly from the normalized Beta moments. `verify_asymptotic.py` is a Python standard-library-only exact rational check of the first two expansion coefficients and the sharp-peak cancellation for fixed integer orders \(2\) through \(16\), plus independent comparison of the spectral product formula with Beta-moment ratios for integer weights and degrees.

Run `python verify_asymptotic.py`; expected output is two PASS lines ending in `2175 total exact rational tests, including moment identities.`. The checker was run successfully from the packaged source and the output was captured in `verification_output.txt`.

Finite symbolic sampling cannot prove the theorem for all \(m\ge3\) or arbitrarily large real weights. The analytic proof separately establishes the index-tail bound, local uniform differentiated expansions, and localization of all maximizing indices. No external audit has been performed.
