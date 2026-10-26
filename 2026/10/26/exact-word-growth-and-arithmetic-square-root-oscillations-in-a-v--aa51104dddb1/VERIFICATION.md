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

Run `python verify.py` with Python 3.9 or later from a directory containing the supplied standalone script. Only the Python standard library is needed.

The script builds the two exact word-count recurrences and independently counts all binary subsets on each interval of 1 through 18 sites, deciding admissibility directly from the parity of the valuation of every pair difference. It compares all 36 resulting counts, verifies the fourfold identity for integers 1 through 1000, confirms the exact integer doubling sequences from both initial conditions through depth eight, and checks floating-point bounds for the two displayed growth constants. These numerical enclosures are ordinary floating-point checks, not an interval-arithmetic certificate; strict separation also follows from elementary analytic bounds and can be independently proved without those computations.

Actual execution returned `VERIFY_OK: exhaustive independent binary-mask counts for n=1..18`, followed by exact-recursion confirmations and constants 1.316957896924817 and 1.246450480280461. The infinite mathematical assertions rely on the direct parity decomposition, elementary hyperbolic-cosine identity, monotone growth inequalities and invariant-measure argument in RESULT.md, not finite computation or software certification. The historical-novelty review is not an independent mathematical audit.
