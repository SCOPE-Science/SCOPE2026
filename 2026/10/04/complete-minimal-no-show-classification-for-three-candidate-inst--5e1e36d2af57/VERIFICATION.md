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
The embedded `verify_irv11_noshow.py` provides an exact finite replay.

The profile-first route enumerates every weak composition into the six strict ballot types for each electorate size from \(1\) through \(11\). For every profile with a unique IRV winner, every nonempty homogeneous abstention group is tested. It verifies zero bad profiles through \(10\) voters and exactly \(60\) bad profiles with \(60\) harmful moves at \(11\).

The event-first route independently enumerates each possible post-abstention profile, ballot type, and group size that reconstructs an \(11\)-voter election. It is required to reproduce the identical harmful-event set.

The replay additionally verifies:
- \(4{,}368\) total anonymous \(11\)-voter profiles and \(4{,}080\) with a unique full-election winner;
- incidences \(5/364\) and \(1/68\);
- every harmful group has size \(2\);
- the abstainers always improve from their last-ranked full winner to their second-ranked post-abstention winner;
- exactly \(10\) candidate-relabeling classes, all of orbit size \(6\);
- the exact two-family normalized classification;
- ballot-type-count strata \(2,5,3\) across the ten classes for three, four, and five distinct ballot types, respectively.

Run:

`python3 verify_irv11_noshow.py`

The first output line must be:

`VERIFY_OK`

The exhaustive computation is finite and is not used to infer claims for larger candidate sets or unrestricted electorates.
