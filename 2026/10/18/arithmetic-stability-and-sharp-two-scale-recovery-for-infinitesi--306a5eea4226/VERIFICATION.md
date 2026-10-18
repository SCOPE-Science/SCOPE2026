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
# Verification of the infinitesimal chord-tomography theorem

The analytic argument establishes the general theorem. The accompanying `check.py` gives reproducible, supplementary calculations using only the Python standard library. It evaluates exact rational expressions for the displayed pair of offsets, checks a finite collection of rational denominator combinations, tests the two-scale square identity on exact rational samples, and independently verifies the chord derivative against central finite differences of actual radial-curve intersections.

To reproduce the checks, run `python3 check.py` and require the final output `FINITE_CHORD_TOMOGRAPHY_CHECKS_OK`. The finite checks do not enumerate all rationals or irrational angles; infinite validity follows from the divisor argument and the torus-character theorem. The finite-difference calculation is not a proof of differentiability, which is established by the implicit-function argument in RESULT.md. The unique Fourier multiplier normalization is \(2\cos(m\alpha)/\sin\alpha\), so squared frame bounds use its square and unnormalized \(L^2(S^1)\) norms.

Scientific limits: only derivatives of chord length at the unit disk are controlled. No assertion is made of a stable nonlinear inverse, a global equality theorem for arbitrary bodies, or an independent scientific audit. Literature comparison remains nonexhaustive for older work whose full text was unavailable.
