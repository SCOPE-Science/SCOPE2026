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
The embedded `verify_coombs10_noshow.py` provides an exact finite replay.

Every anonymous three-candidate profile through \(10\) voters is generated as a weak composition into the six strict ranking types. Every positive homogeneous abstention group present in each profile is tested.

Two independently coded Coombs implementations must agree for every participating and post-abstention profile:
1. a closed three-candidate implementation using first-place majority, unique last-place elimination, and the final pairwise contest;
2. a literal iterative elimination implementation.

A second traversal starts with each possible post-abstention profile and adds homogeneous voter groups. It is required to recover exactly the same standard no-show event set as the profile-first traversal.

The replay verifies:
- no standard no-show event through \(9\) voters;
- exactly \(12\) bad profiles at \(10\);
- one profitable event per bad profile, always one abstainer;
- \(3003\) total anonymous ten-voter profiles and \(2412\) unique-outcome profiles;
- incidence \(4/1001\) among all profiles and \(1/201\) among unique-outcome profiles;
- exactly \(2\) candidate-relabeling classes of size \(6\);
- normalized classes \((1,0,2,3,4,0)\) and \((1,1,2,3,3,0)\).

The script separately imposes exactly two identical abstainers and verifies no event below \(13\) voters, followed by exactly \(18\) bad profiles at \(13\), in \(3\) candidate-relabeling classes represented by \((2,0,2,4,5,0)\), \((2,1,2,4,4,0)\), and \((2,2,2,4,3,0)\).

Run:

`python3 verify_coombs10_noshow.py`

The first output line must be:

`VERIFY_OK`

All claims are finite three-candidate statements; the verifier makes no inference about larger candidate sets.
