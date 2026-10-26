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

# Finite-certificate verification

Run `python3 verify.py` with Python 3 (standard library only). The checker reconstructs Rule 54 from the Wolfram bit convention, independently enumerates the eleven reachable output subset states, and verifies agreement with a finite forbidden-pattern recognizer over fourteen reachable product states. It builds all 109 Boolean pair-state relations and checks closure under each of the two output symbols. It then classifies directed cycles on four vertices by testing lengths one through four, establishes the unique no-loop cyclic element, and proves that its only preimage in the right-product graph is the initial one-letter word `1`.

The ring cross-check enumerates all binary inputs for ring sizes 1 through 12 (8,190 total) and confirms their outputs coincide with the images determined by directed cycles, except for the predicted size-one all-ones target. The exact rational-series consistency check is auxiliary. The unrestricted theorem uses finite-monoid closure and graph theory, not extrapolation from ring testing.

Successful local result: `VERIFY_OK: 11 subset states, 14 language-product states, four minimal forbidden words, 109 relation matrices, period classes 31/77/1, 30 exact rational-series coefficients, 8190 independent ring configurations`.

Scientific limitations: the proof concerns this rule and one image step; it does not enumerate all longer predecessor periods or temporal attractors. No independent audit has yet been performed.
