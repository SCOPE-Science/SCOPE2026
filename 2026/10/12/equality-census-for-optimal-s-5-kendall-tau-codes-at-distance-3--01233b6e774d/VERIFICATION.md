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

Run `python3 verify.py` with a standard Python 3 interpreter. The verifier reconstructs the metric by two independent methods, checks all \(7140\) unordered pairs, proves nonexistence of a normalized size-\(21\) clique, enumerates all \(532\) normalized size-\(20\) maxima, expands them to all \(3192\) labeled maxima, rechecks every maximum, and recomputes the natural order-\(240\) orbit partition.

The verifier also confirms the published 2016 example and its orbit size. It does not attempt to determine the full abstract automorphism group of the compatibility graph.

Expected final line:

`VERIFY_OK vertices=120 pair_checks=7140 maximum=20 normalized_maxima=532 labeled_maxima=3192 natural_group=240 orbits=24 orbit_sizes=6x1,30x3,48x2,60x4,120x5,240x9 paper_example_orbit=120 normalized_sha256=502486838fdc6f3400e2372677ebb1ebf733bf9bdef71b690d7fad3c84d82eb2 labeled_sha256=018236d2efcea3622ecab4ccd90d7334de08a6074a5669452884c2d8d500d2b3`
