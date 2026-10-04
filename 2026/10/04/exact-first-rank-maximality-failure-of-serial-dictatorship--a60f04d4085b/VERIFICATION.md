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
The embedded `verify_sd_rankmax_3x3.py` provides an exact finite replay.

Serial dictatorship is implemented twice. Rank-maximality is also implemented twice: by direct lexicographic comparison of rank signatures and by an exact steep-base integer score using base \(4\).

The script verifies:
- all four strict \(2\times2\) profiles;
- all \(216\) strict \(3\times3\) profiles;
- all six perfect matchings for every three-agent profile;
- exactly \(54\) failures of serial-dictatorship rank-maximality;
- exact incidence \(1/4\);
- rank-maximal-set-size histogram \(36\) singleton and \(18\) doubleton cases;
- the six signature-transition cells and their counts;
- exactly nine object-relabeling classes, each of orbit size \(6\).

Run:

`python3 verify_sd_rankmax_3x3.py`

The first output line must be:

`VERIFY_OK`

The finite replay proves only the stated two- and three-agent boundary.
