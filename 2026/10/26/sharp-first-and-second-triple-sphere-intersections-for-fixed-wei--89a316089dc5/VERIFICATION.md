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

A standard-library verifier enumerates the complete four-type profile of three binary centers after translating the first to zero. For each type profile, a finite binomial sum counts exact-radius common neighbors without using the extremal inequalities from the proof. It checks all profiles for \(t=2,3,4,5\) and \(4t\le n\le4t+4\); the observed equality profiles are exactly the pairwise-distance patterns \(2,2,2\) and \(2,2,4\), with the predicted counts.

The execution output records 20 complete grids, 23,340 profile evaluations and 15 independent direct binary-word enumerations. For \(n=12\) and \(t=3\), the predicted top two values are 45 and 32. The exact output ends with `TRIPLE_SPHERE_VERIFY_OK`.

Reproduce using `python3 verify_triple_spheres.py` (no third-party Python packages). The accompanying `verification_output.txt` contains the observed output. No finite experiment establishes the full infinite theorem; the proof in `RESULT.md` does. Independent review is not represented as performed.
