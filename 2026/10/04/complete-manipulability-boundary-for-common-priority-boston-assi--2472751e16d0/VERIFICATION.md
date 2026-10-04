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
The embedded `verify_boston3_common_priority.py` is an exact finite replay for the common-priority Boston/immediate-acceptance environment.

The script implements the mechanism twice:
1. a round-by-round application algorithm; and
2. an independent rank-level scan over schools.

The two implementations are required to agree for every truthful and false-report profile tested.

For the \(3\times3\) unit-capacity market, the verifier exhausts all \(6^3=216\) strict preference profiles, each of three potential manipulators, and all five false reports. It verifies:
- exactly \(36\) manipulable profiles;
- exactly \(36\) vulnerable student-profile pairs;
- exactly \(72\) profitable report triples;
- profile, distinguished-student, and report-triple incidences \(1/6\), \(1/18\), and \(1/45\);
- one vulnerable student per bad profile;
- exactly two profitable reports per vulnerable student;
- every gain is from third sincere choice to second sincere choice;
- vulnerable priority ranks split as \(24\) middle-priority and \(12\) lowest-priority profiles;
- exact equality between the enumerated bad set and the analytic if-and-only-if criterion in `RESULT.md`;
- exactly six school-relabeling classes, each of orbit size \(6\).

The verifier separately exhausts the \(2\times2\) common-priority unit-capacity market and finds no profitable report.

Run:

`python3 verify_boston3_common_priority.py`

The first output line must be:

`VERIFY_OK`

The executable proves only the stated finite unit-capacity common-priority boundary. The broader conclusions are those justified by the analytic case proof in `RESULT.md`.
