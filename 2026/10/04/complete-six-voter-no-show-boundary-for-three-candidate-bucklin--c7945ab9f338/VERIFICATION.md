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
The embedded `verify_bucklin6_noshow.py` is an exact finite replay using only the Python standard library.

It generates every anonymous three-candidate profile through six voters as a weak composition into the six strict ranking types. For each profile it tests every positive homogeneous abstention group and evaluates whether the abstainers strictly prefer the post-abstention winner.

Two winner implementations are checked against one another on every full and reduced profile. One follows literal Bucklin rank depths; the other uses the three-candidate identity that, absent a strict first-place majority, the depth-two winner is the unique candidate with the fewest last-place votes.

A second traversal begins from post-abstention profiles and adds homogeneous groups. Its event set must equal the profile-first event set exactly.

The replay verifies zero no-show events through five voters and exactly eighteen at six voters, with eighteen distinct bad profiles, one abstainer in every event, three candidate-relabeling classes of size six, the normalized family \((1,t,0,3,2-t,0)\) for \(t\in\{0,1,2\}\), and incidence fractions \(3/77\) and \(6/139\).

Run:

`python3 verify_bucklin6_noshow.py`

The first line must be:

`VERIFY_OK`
