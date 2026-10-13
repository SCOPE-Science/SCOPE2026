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

# Verification procedure

Run `python3 verify.py` with Python 3.9 or later and no nonstandard dependencies. The program builds the four-vertex path and its complement from adjacency definitions and calculates their complex matrix exponentials by a scaled Taylor series with repeated squaring; this algorithm is independent of the reversal-sector argument in the proof.

The actual execution returned:

`VERIFY_OK: 12864 direct matrix/closed-form comparisons; 116733 torus bound pairs; analytic density proof required for sharpness.`

The test uses 201 deterministic times, all 16 ordered vertex pairs, and each of the four functions. It also tests all four global upper bounds on a grid of 116,733 independently sampled phase pairs. Numerical comparisons use absolute error below \(2\times10^{-11}\). The finite tests do not certify arbitrarily large times, infinite phase density, or novelty. Those parts rest on the explicit analytic derivation and source comparisons.
