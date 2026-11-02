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

# Reproducibility and verification

Run `python verify.py` in the same directory as this file, with SymPy installed. The program constructs the nine-state continuous-time generator, its marked exit-rate matrix, stationary law, current and Poisson solution from first principles, rather than importing any predetermined full result. It checks the exact rational current and long-time Fano polynomial, the whole length-two/length-one difference polynomial, both distinct singular rescalings, the limiting derivative and crossover polynomials, and rational test parameter pairs.

The key universal steps additionally use exact positivity and Descartes' rule for \(0<u\le1/10\), intermediate-value sign bracketing, and coercive bounds for the globally optimized small-unpausing profile. These mathematical arguments are supplied in `RESULT.md`; finitely many numerical checks cannot replace them. No independent audit was performed.
