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
The embedded `verify_boston_common_priority_n3.py` is the executable finite certificate for the stated three-student classification.

It implements Boston twice in separate code paths and checks agreement on every profile for \(n\le3\). It verifies directly that no profile is manipulable for \(n=1,2\). At \(n=3\), it enumerates every one of the \(6^3=216\) labeled truthful profiles and every nontruthful strict report for each student. It obtains exactly \(180\) nonmanipulable profiles, \(24\) profiles manipulable only by the middle-priority student, and \(12\) profiles manipulable only by the lowest-priority student.

A second enumeration canonicalizes profiles under all six school relabelings. It verifies \(36\) classes, every orbit of size \(6\), with exactly six manipulable representatives split \(4+2\). For every bad profile it checks that the unique manipulator truthfully receives her third choice and that her profitable reports are exactly the two rankings placing her true second choice first.

Replay:

`python3 verify_boston_common_priority_n3.py`

The first output line must be `VERIFY_OK`.

The computation is exhaustive only for the explicitly stated finite domain. It supplies no claim for larger markets or different priority structures.
