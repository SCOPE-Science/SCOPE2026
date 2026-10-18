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

# Reproducibility and limits

Run the accompanying `verify.py` using the Python standard library. It constructs rational Fourier polynomials of the normal product and independently calculates exact finite-time moments and the matrix recursion, then verifies the centered fourth-moment arithmetic for all inspected finite indices. It also carries out six deterministic numerical logarithmic-integral spot checks. The completed check returned 59 exact rational checks and six numerical comparisons. No numerical integration constitutes a proof of an asymptotic limit.

The all-parameter conclusions rest on the proof in RESULT.md: the logistic/doubling conjugacy; Birkhoff's theorem for the integrable log multiplier; Jensen's cosine integral; the exact doubling transfer identities; a dominant-eigenvalue argument; and finite Fourier pair counting. Exceptional boundary orbits and nonlinear predator-population dynamics are explicitly excluded from the almost-sure normal conclusions. Independent audit has not been performed.
