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

# Verification and reproducibility

The theorem is proved for all odd primes by exact inequalities on ordered cosine values, an everywhere-positive Laurent-coefficient construction, and the Fourier involution. No numerical threshold enters these arguments.

The standalone script `check_support.py` uses the Fourier convention stated in `RESULT.md`, computes the positive Laurent coefficients, recomputes the transform at every residue, verifies its polynomial factorization, and checks zero and positive counts. It exercises 502 admissible pairs across the odd primes 3, 5, 7, 11, 13, 17, 19, 23, 29, and 31, with 90-digit `mpmath` precision and an absolute tolerance of \(10^{-56}\). The script additionally computes the second transform for the swapped orientation. Run with `python check_support.py` after installing `requirements.txt`.

The script passed with the output `PASS: 10 odd primes; 502 admissible support pairs checked.` Numerical testing does not certify unseen primes. Both root placement and coefficient positivity hold for every allowed integer parameter in the analytic proof. Independent validation has not been performed.
