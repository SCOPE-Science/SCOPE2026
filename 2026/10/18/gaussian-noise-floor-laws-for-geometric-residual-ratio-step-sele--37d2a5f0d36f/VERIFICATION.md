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

# Verification record

The analytic proof uses independent Gaussian endpoint measurements, a strictly positive Gaussian density at zero, the central chi-square/Beta transformation, reciprocal symmetry, and summable Gaussian norm tails. It does not invoke a finite simulation as proof of an infinite family of assertions.

Run `python check_noise_window.py` after installing `requirements.txt`. The check passed 852 distributional algebra, beta symmetry, arctangent-specialization and seeded independent Gaussian sampling comparisons, using NumPy and SciPy. The seed is fixed; empirical CDF tolerances are declared in code.

**Scientific limits:** The positive-moment divergence at the sharp cutoff, the polynomial-tail limit, and almost-sure full-history limit are consequences of the proof, not numerical sampling. The exact-gradient one-step multiplier does not constitute evidence for divergence of an entire adaptive optimization trajectory. An independent audit has not been conducted.
