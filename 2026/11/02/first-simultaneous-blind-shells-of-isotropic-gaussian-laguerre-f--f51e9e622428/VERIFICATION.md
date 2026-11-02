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

The exact-arithmetic checker in `checks/check_claim.py` recomputes all ten generalized-Laguerre pair resultants, the two exceptional polynomial greatest common divisors, root simplicity, normalization at zero, and the two critical exponents. Run `python checks/check_claim.py` with the dependency from `checks/requirements.txt` installed; it prints an explicit PASS line if every assertion succeeds.

The Fourier-distribution reduction, the Bessel-mode nonexistence argument at and below the endpoint, and construction of nontrivial spherical Bessel solutions above the endpoint are analytical arguments in `RESULT.md`, not machine-certified computations. No external or independent audit has been conducted. The integer dimension, degree cutoff, Fourier convention, positive spectral shell radii, and strictness at the integrability endpoint are essential hypotheses.
