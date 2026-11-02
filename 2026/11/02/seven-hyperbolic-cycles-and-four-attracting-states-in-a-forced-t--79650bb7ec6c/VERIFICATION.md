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

The included `verify_hyperbolic.py` is an executable directed-interval replay, requiring Python 3, `mpmath` 1.3 or newer, and adjacent `centers.json`. It checks eight rational endpoint trajectories, event isolating brackets, transverse velocity signs, six new displacement signs, full-interval excursion-time bounds, central antisymmetric return signs, and strict Floquet multiplier windows.

Numerically enclosed Floquet windows (coarse safe rational bounds) are \((0.99,1)\), \((1.5,1.53)\), and \((0.33,0.34)\) for the three nonsymmetric representative intervals, and \((1.003,1.006)\) for the central antisymmetric solution. The three symmetric partners have identical multipliers by the exact half-period involution identity.

The checker relies on the rigorous transverse itinerary/no-extra-crossings result in Hu–Chen, arXiv:2610.19586v1, Appendix A.3, for the enclosing shooting intervals. Its own interval checks do not independently redo that global itinerary proof. All enumerations concern only the seven exhibited orbits, not the totality of periodic solutions. There is no independent audit.
