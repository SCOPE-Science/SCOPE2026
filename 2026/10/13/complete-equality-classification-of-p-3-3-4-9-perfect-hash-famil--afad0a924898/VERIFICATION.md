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

Run `python3 verify.py` with a standard Python 3 interpreter.

The script builds all \(64\) columns in \(\{0,1,2,3\}^3\) and all \(8640\) forbidden triples. Because coordinatewise symbol translations act transitively on columns, a hypothetical size-\(10\) family can be normalized to contain \(000\). A complete increasing backtracking search excludes that target and separately enumerates every normalized size-\(9\) maximum.

The script then applies all \(64\) coordinatewise translations and deduplicates to the complete literal maximum set. It verifies the incidence equation, applies every element of the explicit natural group \(S_4^3times S_3\) to a representative, checks that this orbit is exactly the complete maximum set, and directly verifies the coordinate-multiplicity and Hamming-distance profiles for every maximum.

A separate mixed-integer cross-check of the maximum was performed during review. The packaged script is the dependency-free exhaustive replay used as evidence for the final claim.

Expected terminal line:

`VERIFY_OK vertices=64 bad_triples=8640 maximum=9 normalized_maxima=648 labeled_maxima=4608 natural_group=82944 orbits=1 orbit_size=4608 stabilizer=18 coordinate_profile=3,2,2,2x3 hamming_profile=2x18,3x18 representative=000,011,022,103,131,213,232,323,330 normalized_sha256=74042c890175057526b3ca0c4ffac26bb9ceea6fb2ee4358512c4bc55ce06b80 labeled_sha256=0cb0593cb7333638b2d7b8a8616bc92ba8c2cd3c2a29c65b06d9004e97235da3`
