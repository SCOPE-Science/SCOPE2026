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

The accompanying finite census traverses the \(2^{14}\)-element plane-filling section space, checks geometrical nonsingularity by Gröbner unit ideals on every coordinate chart, and determines the ten plane-projective orbits. It then computes the characteristic-two Cartier matrices and verifies the joint \(2\)-rank and \(a\)-number distribution.

`verify_census.py` printed `CENSUS_CARTIER_VERIFY_OK`. The independent `check_points.py` enumerated points over extensions through degree six, reconstructed the zeta numerator and confirmed each \(2\)-rank; it printed `POINT_COUNT_ZETA_VERIFY_OK`.

The enumeration gives exact coverage of this finite family, not a theorem about other field sizes or any independent external certification. The \(a\)-number relies on the Cartier calculation, not the independent point-count check. Independent audit has not been performed.
