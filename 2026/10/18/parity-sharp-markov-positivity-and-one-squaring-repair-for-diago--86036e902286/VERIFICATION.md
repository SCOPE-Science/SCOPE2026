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

# Reproduction and evidentiary limits

Run `python verify.py` in this directory with Python 3 and SymPy. Its independently reconstructed Padé polynomials are checked against gamma-integral coefficients through degree 9. Rational matrix-function evaluations on balanced, uniform and asymmetric reset-chain examples compare the actual Padé matrix polynomial/inverse with the projector formula, verify stochastic row sums and check one and two binary squarings. The cubic coefficient and \([3/3]\) derivative identities are symbolic. The recorded run reported `VERIFIED: 681 exact symbolic/matrix checks`.

These checks cover tested finite dimensions, polynomial degrees, and rational steps, not all parameters. Infinite and all-degree statements follow from the gamma integral, rank-one spectral decomposition, and exact sign analysis in RESULT.md. Matrix arithmetic is idealized exact, with no conditioning, finite-precision error or independent certification claim. Mathematical priority remains provisional despite checking relevant sections of the accessible full texts of two older general Runge–Kutta positivity papers; exhaustive priority and independent certification were not performed.
