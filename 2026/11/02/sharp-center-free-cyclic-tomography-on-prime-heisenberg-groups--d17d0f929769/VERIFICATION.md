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
The standalone `checker.py` generates exact 0–1 coset-incidence matrices over the integer lattice and performs row elimination over the finite field of two elements, without floating-point approximations or third-party libraries. A full-rank reduction modulo two certifies full column rank over the rationals and complex numbers for each tested finite instance.

Executed `python checker.py` from the extracted package. The output confirms all 3, 10, and 35 split subsets at primes 3, 5, and 7, respectively, and one split subset at 11. These finite tests cannot certify the all-prime statement, for which RESULT.md provides an independent analytic proof via irreducible Fourier analysis and prime Fourier minors. The original irreducible classification and general Fourier criterion are published; no external independent mathematical validation of this combined theorem has occurred.
