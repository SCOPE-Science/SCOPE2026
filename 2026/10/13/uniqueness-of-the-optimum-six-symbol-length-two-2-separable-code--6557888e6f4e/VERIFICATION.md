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

The proof has two independent layers.

First, the analytic argument proves the sharp \(16\)-edge upper bound and classifies equality by pair counting. In an equality case the six block sizes must be \( (3,3,3,3,2,2)\); their fourteen covered point-pairs leave one pair uncovered, and the blocks are forced by the three perfect matchings of \(K_4\). Completing the two size-two blocks through a new point and adding the missing-pair triple yields the Fano plane.

Second, `artifacts/verify_q6_separable.py` performs an exhaustive finite replay. It enumerates all row-sorted \(6\times6\) binary matrices subject to the no-two-common-columns condition, checks targets \(16\) and \(17\), canonicalizes maxima under row/column relabeling and transpose, verifies the descendant definition directly, counts labeled matrices, and verifies Fano completion.

The recorded output is:

`VERIFY_OK vertices=36 target17=0 row_multisets16=90 maximum=16 labeled_maxima=64800 natural_group=1036800 orbits=1 orbit_size=64800 stabilizer=16 degree_profile=2,2,3,3,3,3x2 representative=00,01,12,13,20,22,24,31,33,34,40,43,45,51,52,55 normalized_sha256=7066d2210363d8e996ead3ef3c7d4fbb92b87a8685f71e0ee8de8b25c069dd6b`

The exhaustive search is finite and complete for the stated \(6\times6\) domain. No claim is made beyond this finite parameter set.
