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

# Reproducibility and proof boundary

Run `python3 artifacts/verify.py` with Python 3 standard library. The script constructs all pair-sum fibers for \(t\mapsto(t,t^2)\) on \(\mathbb Z/p^3\mathbb Z\), derives their Gaussian-integer fourth-moment energy independently of the stated block-convolution factorization, checks equality packets with independently assigned middle-digit phases, and rejects a nonextremal amplitude/frequency pattern.

Observed execution:

`VERIFY_OK Gaussian_integer_fiber_cases=23 exact_extremizer_packets=15 strict_nonextremizers=3 spectral_deficit_checks=23`

For primes \(3,5,7\), the fiber/block identity and fourth-power extremizer identities use exact integer arithmetic. Random test coefficients are Gaussian integers from a fixed seed. Frequency-side deficit checks evaluate complex roots of unity numerically with declared tolerances, whereas the corresponding symbolic formula is established algebraically in the proof.

These finite checks are not an exhaustive verification of all functions, phases, or primes. The universal proof follows from exact character orthogonality, uniqueness of roots of a unit discriminant modulo odd prime powers, complete convolution-fiber classification and finite Fourier Parseval. No numerical optimization, heuristic search output, or external certificate is required for the theorem.
