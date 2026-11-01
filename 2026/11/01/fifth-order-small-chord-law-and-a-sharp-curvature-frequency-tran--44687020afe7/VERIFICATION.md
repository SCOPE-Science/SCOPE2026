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

The accompanying `verify_curve_tail.py` is a standalone SymPy/NumPy/SciPy program. Run `python verify_curve_tail.py` to reproduce exact symbolic checks of the Frenet frame through the fifth derivative, the symmetric midpoint chord squared to sixth order, series inversion, periodic integral coefficient, harmonic curvature energies, fourth-to-fifth sign threshold, and exact arcsine CDF of a circle. It also computes independent direct quadratures of the chord integral and positive inverse-radius for modes \(n=2,4,5,12\) at two thresholds each. Successful execution prints:

`VERIFY_OK Frenet_series=6 inverse_series=1 exact_fourier=2 circle=1 numerical_cases=8`

The numeric comparisons check the Taylor error scale, not an infinite theorem. The proof of the general asymptotic is in RESULT.md, based on uniform local Taylor remainder and compact embeddedness. No finite-sample convergence guarantee is made, and the asymptotic remainder is not uniform over high-frequency curve families.
