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

The analytical proof reconstructs the dual extreme points from the tight-edge criterion, derives the exact squared-normal identity, uses opposite facet constraints to determine the inradius, and characterizes the linear span of contact normals to obtain the complete optimal-center affine dimension. The elementary lattice resonance calculation is exact.

Run `python verify_inball.py` with Python 3.10+, NumPy and SciPy installed. The program checks exact rational dual constraints and tight connectivity for every predicted vertex at 15 finite parameter/dimension pairs. Six configurations with sizes 2 and 3 use NumPy/SciPy halfspace intersections of the original full metric-inequality system as an independent source of dual vertices. For all 15 configurations it tests the exact maximized squared norm and contact multiplicities, and tests the tangent-normal span by numerical linear algebra with an explicit tolerance. The recorded execution ended with `ALL EXACT METRIC AND EUCLIDEAN-INBALL CHECKS PASSED`. Numerical rank checks are not exact-rational certificates and are not the proof of the dimension statement; equation (5) and the block-contrast argument supply the general proof.

The proof covers every integer \(m\ge2\) and every real \(1<t<2\); the finite program is corroboration, not an exhaustive infinite certification. Independent audit has not been performed.
