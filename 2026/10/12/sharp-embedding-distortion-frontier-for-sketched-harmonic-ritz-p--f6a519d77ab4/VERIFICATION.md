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

# Reproducibility and checked limits

Run `python verify.py` using a standard Python 3 installation. The verifier uses exact `fractions.Fraction` arithmetic, forms both harmonic Gram entries from the declared matrices rather than trusting scalar formulas alone, tests the exact critical singular case, and tests the negative harmonic Ritz value for \(\kappa=9\), \(\varepsilon=2/3\). It also generates deterministic full-rank two-column bases in dimension three and verifies positive definiteness of the Hermitian part of the resulting sketched harmonic denominator and the numerator for distortions below the theoretical threshold.

This is a finite computational cross-check. The continuum of distortions, arbitrary finite trial dimensions, all Hermitian positive-definite matrices, and impossibility of extending the universal guarantee beyond the exact threshold are established analytically in the proof, not by these tests. Reproducing checks does not constitute an independent scientific audit.
