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
The embedded `verify_stable_marriage_orbits.py` is a complete exact verifier.

It enumerates all \(6^6=46656\) strict three-by-three preference profiles, checks all six perfect matchings per profile for blocking pairs, and then performs two independent quotient calculations:

1. orbit partition using generators of independent \(S_3\) relabelings on the two sides plus side exchange;
2. Burnside fixed-point counting for all \(72\) group elements, stratified by the number of stable matchings.

The two routes both return \(491,161,17\) classes. Orbit sizes reconstruct the published labeled totals \(34080,11484,1092\). The script also verifies the unique orbit-size-\(12\) representative in the three-stable stratum.

Replay with:

`python3 verify_stable_marriage_orbits.py`

Expected leading output:

`VERIFY_OK`
