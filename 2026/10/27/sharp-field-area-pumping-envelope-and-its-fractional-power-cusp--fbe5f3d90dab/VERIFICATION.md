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

The analytic claim uses an exact source curvature, superlevel-set rearrangement, elementary radial integration, local boundary expansion, and a large-area angular integral expansion. Finite numerical checks are corroboration rather than proof.

Run `python verification/check_heat_envelope.py` from the package root using a standard Python 3 installation; there are no third-party dependencies. The program passed 114 finite assertions on replay, covering numerical quadratures for three fixed positive gap ratios, the cap identity, strict monotonicity, a local fractional-power coefficient, the derivative of the optimized flux with respect to area, and stretched-exponential tail comparisons.

There is no finite enumeration of all contours and no independent audit. The result concerns the infinitely slow geometric response and excludes physical finite-period optimality and the zero-gap degeneracy.
