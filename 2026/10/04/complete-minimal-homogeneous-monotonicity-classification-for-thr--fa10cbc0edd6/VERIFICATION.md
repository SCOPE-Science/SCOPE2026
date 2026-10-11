---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The symbolic lower-bound argument was reconstructed: a harmful homogeneous raise must move the old winner to first place and switch the eliminated candidate; the first-choice inequalities force at least 17 voters, and equality forces totals 6,5,6 with exactly two changed voters. Resolving the two possible donor rankings gives exactly the two stated families. An independent exhaustive enumeration of all anonymous 17-voter profiles and homogeneous winner-raising moves reproduced 252 harmful events on 252 profiles, 42 candidate-relabeling classes all of orbit size 6, and no event below 17.

## originality

PASS

Best-of-knowledge originality survives the broader prior characterizations. Miller proves a general necessary-and-sufficient criterion for vulnerability to upward monotonicity failure, and Brandt--Matthäus--Saile establish minimal voting-paradox instances, but neither inspected source gives the homogeneous same-ballot boundary classification at 17 voters, the forced first-choice vector, the two normal-form families, or the exact 252/42 census. The audited theorem requires an equality-case analysis under the stronger homogeneous-change constraint rather than merely restating vulnerability.

## value

PASS

This is a natural complete classification at the known sharp boundary of a canonical voting paradox. It determines all equality cases, orbit counts, and the exact homogeneous move structure rather than merely recomputing a single witness or probability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
