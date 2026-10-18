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

# Reproducibility and validation limits

The accompanying standalone file `cuboctahedron_perimeter_checker.py` uses Python 3.10+ and SymPy. It reconstructs all twelve cuboctahedron vertices and twenty-four edges; intersects those edges with independently chosen central planes; constructs the resulting planar convex hull using the monotone-chain algorithm; and checks the theoretical directional perimeter against 2,400 independent numerical constructions. Representative symmetry-wall planes are checked separately. Exact symbolic differentiation verifies the two second-derivative identities and the rational inequalities used in the all-direction proof. A bisection check brackets the unique interior minimizer.

The independent numerical geometry comparisons passed all 2,400 test directions, with maximum absolute perimeter discrepancy \(3.56\times10^{-15}\). The symbolic curvature-free derivative, positivity, and boundary checks passed, as did the narrow numerical enclosure \(0.5150605280<t_*<0.5150605281\) of the unique minimizer. These checks can be reproduced by running the attached script.

The global assertion is proved analytically by the inequalities given in `RESULT.md`. Finite tests do not certify untested directions, and the checks are not independent external mathematical validation.
