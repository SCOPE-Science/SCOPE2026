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

# Verification notes

The proof uses the exact law of an \(n\)-risk maximum, including the no-claim atom \((1-p)^n\). Its positive density and log-density-ratio derivative have no baseline-dependent factors after cancellation. The sign of the derivative is the sign of a scalar function whose sole varying factor, the product of two single-risk distribution functions, is strictly monotone. Hence the endpoint checks are exhaustive over the *entire* continuum of survival values, and the zero-atom comparison separately closes the gap between positive and zero observations.

The accompanying `verify.py` uses only the Python standard library, rational fractions, and fixed finite enumerations. Execute `python verify.py` from the extracted package. It compares both derivative formulas at 70,400 exact-rational parameter-and-survival points, checks the endpoint-and-atom classification for 6,400 parameter sets, and records three checks for the sharp integer transition in one example. Its recorded execution printed `PASS: 76803 exact-rational identities/order checks`.

The diagnostic tests are finite and cannot establish the universal theorem. Correctness relies on the human-readable algebra and monotonicity argument in `RESULT.md`. The literature comparison includes an openly accessible source explicitly proposing likelihood-ratio comparisons, relevant prior stochastic-order results, and a named full-text access risk; it does not establish independent priority certification.
