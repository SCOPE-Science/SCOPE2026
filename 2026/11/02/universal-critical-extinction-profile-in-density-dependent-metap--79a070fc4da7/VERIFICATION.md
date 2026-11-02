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

# Verification

The analytic steps proving the all-patch claim appear in `RESULT.md`; the finite executable verifies only an exact example and diagnostic convergence rates. All hypotheses and normalized Perron vectors are explicit.

Run `python3 verify_critical_metapopulation.py` in a Python 3 installation with no third-party dependencies. Exact `Fraction` arithmetic verifies the two-patch Perron equations, left/right normalizations, eigenvalue-one matrix, nonpositive quadratic coefficients, positive curvature \(75/49\), critical limiting vector \((28/75,7/25)\), and the separate effect of nonconstant dispersal. Direct iteration with \(200000\) updates checks the numerical trend (not an infinite-time proof). The program was run on the embedded source before release and prints `PASS`.

For the general result, the proof does **not** presume that the nonlinear map is monotone in population density: only the pointwise inequality \(F(x)<Mx\) on nonzero vectors is required. It does not assert any error bound uniform over all initial populations or patch dimensions. Bibliographic coverage of some plausible general spectral-threshold sources remains abstract-level only; this is an originality limitation, not a proof step.
