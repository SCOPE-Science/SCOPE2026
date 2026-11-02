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

## Reproducibility

The `check.py` file is standalone and uses NumPy, SciPy and mpmath. Run `python check.py` from a directory containing that file. It constructs a Feynman–Kac block moment generator, checks the first four moments through a matrix exponential against the closed-form fourth cumulant for multiple rates, velocities and times, and checks high-precision sign regimes and the unique example crossing. The executed run reported 333 assertions passed and a maximum matrix-formula absolute difference of approximately \(2.73\times10^{-12}\).

The exact proof uses the 2-by-2 resolvent, explicit inverse Laplace transforms, and a twice-iterated weighted-average monotone-ratio argument. Computational tests of finitely many examples are not treated as proofs of the continuum statement. The cited prior 2014 article supplies the general telegraph model and arbitrary-order moment framework; no independent assessment of novelty or correctness has occurred.
