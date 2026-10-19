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

# Reproducible verification

Run `python verify_prime_tori.py` with Python 3 and NumPy. The checker constructs complex Fourier restrictions and independent real symmetric weighted Laplacians, checks full-rank eigenspace restrictions, matches predicted maximal multiplicities at selected weights, and checks invariance under matrix shifts. The expected output is `PASS: 85 independent modal/full-matrix/multiplicity/shift checks; primes 5,7,11`.

Tested primes are 5, 7, 11, with full Laplacian diagonalization for 5 and 7. These calculations are finite and use floating-point ranks; numerical coincidence cannot certify exact nonresonance or a universal PBH criterion. Exact arithmetic validity follows from the cyclotomic and Fourier proof in RESULT.md. No independent mathematical audit has been conducted.
