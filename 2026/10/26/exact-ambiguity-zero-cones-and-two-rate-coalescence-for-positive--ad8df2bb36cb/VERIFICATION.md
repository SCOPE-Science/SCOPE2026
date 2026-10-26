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

# Reproduction and verification limits

Run `python CHECKER.py` after installing `mpmath` from `requirements.txt`. The checker was executed against this same standalone source, and its recorded output is supplied as `CHECK_OUTPUT.txt`. It tests three direct oscillatory Gaussian integrals against the independently assembled closed form at 55-decimal precision; tests four distinct interior-ray roots against both the exact formula and the first exponential phase correction; verifies the two endpoint-ray coefficient tests; and checks representative parameters in each coalescing-width regime.

These are finite numerical tests, not numerical proofs of the full cone, the infinite zero count, or the limiting power laws. Analytic justification is in `RESULT.md`, Steps 1–5. The tests require the real angular-frequency convention used there. Nonstandard steps needed by the proof are the exact Gaussian identity (checked independently by direct integral at sample points), exterior-sector exponential domination, cosine-root uniqueness at large index, the first-root bracket, and the small-width equal-amplitude tangency estimate.
