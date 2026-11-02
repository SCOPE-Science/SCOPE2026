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

The proof in `RESULT.md` establishes the exact infinite-horizon threshold analytically by three mechanisms: (i) a two-moment lower bound and reflection-principle upper bound for one pulse, (ii) a uniformly positive reflecting heat kernel between distinct pulses, and (iii) the equivalence of infinite-product positivity to series summability. The sharp half-line pulse crossover follows by Laplace inversion and a Gaussian right-boundary excursion estimate. The power-law boundary is an elementary exponent test on that exact series.

Run `python3 verify.py` in a directory containing the extracted `verify.py` file. It requires Python 3 standard library only. The program independently computes one-pulse removal using Robin–Neumann eigenfunctions and compares it with the half-line complementary-error-function calculation, tests the spectral Robin boundary equations, the proved envelope, monotonicity in reaction rate and selected algebraic phase-boundary cases.

The verifier was executed against the embedded source and passed **254 deterministic finite numerical/algebraic check groups**. This count is finite and does not certify the infinite-horizon iff theorem; the complete proof of that theorem is in `RESULT.md`. The numerical comparisons include explicit absolute floating-point tolerances and are not presented as exact-rational certificates.

Scientific limits: finite interval, a positive uniform reflecting gap, positive finite pulse rates, and initially uniform spatial distribution. Any generalization to overlapping pulses or vanishing gaps requires additional argument. No independent validation or mathematical audit has been performed.
