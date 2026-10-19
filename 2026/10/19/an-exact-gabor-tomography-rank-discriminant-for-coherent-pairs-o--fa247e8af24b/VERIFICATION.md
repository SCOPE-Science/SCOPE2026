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

Execute `python verify_two_chirps.py` with Python 3.9 or later. It uses integer coefficient vectors modulo the degree-\(p-1\) cyclotomic relation for odd prime \(p\). For each tested prime and nonzero slope, all \(p^2\) translation/modulation pairs and all four formal coefficients of the ambiguity polynomial are compared against the closed identity. It also verifies the square magnitude and conjugation of the Gauss sums.

Tested primes: 3, 5, 7, 11, 13, 17 and 19, each at slopes 1 and 2. All 8,184 exact coefficient comparisons passed; details are preserved in VERIFY_OUTPUT.txt.

The rank count, all-prime classification, and the explicit complete unit-amplitude two-chirp construction follow from the symbolic argument in RESULT.md. Finite tests do not certify an infinite statement by enumeration. The result addresses noiseless full complex-linear matrix lifts, not nonlinear necessity or robustness to noisy intensities.
