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
# Reproducibility and validation

The standalone file `verify.py` runs with Python 3.9 or later and only its standard library. From the directory containing it, run `python verify.py`. Its successful output is:

`VERIFY_OK: 30 period, Floquet and circle conditions; 10 polynomial degree checks; 2 nonlinear Poincare returns`

The program forms the interpolation coefficients for distinct positive radii, multiple nonidentical physical periods, and both alternating and uniform attracting profiles, for \(1\le m\le5\). It expands the Cartesian polynomials, measures their maximal monomial degree, tests radial invariance directly in Cartesian variables at non-axis points, integrates each angular period and linearized radial Floquet exponent by Simpson quadrature, and compares exact targeted values. An additional nonlinear Runge–Kutta integration of the angular-coordinate return map verifies two adjacent attracting circles have transverse multipliers agreeing with the construction's prediction as the initial radial displacement tends to zero.

The analytical, all-parameter claims are proved in `RESULT.md`, not inferred from numerical tests. The principal nonstandard steps are the exact arithmetical inversion of the cosine-return multiplier formula and the monic-polynomial divisibility lower bound. In particular, a finite set of interpolation checks does not show universal realizability, and finitely many degrees tested cannot show minimality for all \(m\). No formal proof assistant or external independent audit has been used. The limitations concerning extra periodic trajectories and unavailable historical full text remain.
