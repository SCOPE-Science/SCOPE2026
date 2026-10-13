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

Run `python3 artifacts/verify.py` with Python 3. The script uses only the standard library and reconstructs the full finite problem from the cover-weight definition. It verifies the cover-weight histogram, enumerates every normalized size-eight code, confirms all row and column projections are bijections, counts affine versus nonlinear maxima, and computes the orbit partition under translations, row permutations, column permutations, and transposition.

Expected final line:

`VERIFY_OK cover_weight_hist=0:1,1:33,2:231,3:247 normalized_maxima=7622 maximum=8 labeled_maxima=487808 affine_maxima=109952 nonlinear_maxima=377856 natural_group_size=36864 orbits=59 orbit_sizes=128x1,768x2,1152x2,2304x8,3072x1,4608x21,6144x1,9216x9,18432x13,36864x1`

The finite computation proves only the stated binary \(3\times3\) case. No asymptotic or higher-size classification is inferred.
