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

# Reproducible mathematical checks

The standalone `checker.py` requires Python standard-library modules only. From the directory containing `checker.py`, execute `python checker.py`. It computes the four raw vertex dot products at 12,000 angular quadrature points for 70 explicit and seeded parameter pairs; it does **not** use the theorem's piecewise directional-width formula to construct those projections. The program tests 51 thresholds for every shape, the mean-width perimeter identity, and the strict critical-angle criterion. In the recorded run, every test passed and the largest CDF-quadrature discrepancy was approximately \(9.40\times10^{-5}\). Finite quadrature error is expected near critical levels; no numerical check is relied upon as a substitute for the all-parameter proof.

Exact checks in `RESULT.md`: vertex projections and symmetry reduction; correct inverse-trigonometric sublevel lengths on all three intervals; the inequality \(p<\arctan b<q\) equivalent to \(b>1\), \(ab<1\); and a quadratic Taylor analysis of the extra peak. The separate boundary cases are explicitly stated. No independent mathematical audit or external verification is asserted here.
