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

`verify.py` reconstructs the complete finite problem from definitions. It generates all \(64\) binary words of length six, computes asymmetric distance for every pair, and performs an exact maximum-clique enumeration of the compatibility graph. It then generates the matching/transversal family independently and checks equality with the complete extremizer list.

Expected output:

`VERIFY_OK maximum=12 labeled_maxima=30 matchings=15 maxima_per_matching=2 coordinate_orbit=30 stabilizer=24 nodes=118645`

The computation is exhaustive for this finite domain. It does not establish any analogous statement for other block lengths or error radii. The literature comparison is separate from the finite verification and retains the access risk described in REVIEW.md.
