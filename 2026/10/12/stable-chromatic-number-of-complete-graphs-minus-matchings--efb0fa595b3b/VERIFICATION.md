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

# Verification record

The mathematical proof is self-contained: its decisive steps are the at-most-\(n-1\) reachability orientation, the preferred-available-color argument that every envy arc follows that orientation, and the reverse-preference obstruction for two reused missing pairs. The matching-complement chromatic calculation follows from the size-two bound on independent sets.

Running `python3 verify.py` with the Python 3 standard library generated the included `verification_output.txt`. Exhaustive lower-bound checks covered nine graph profiles and all 11,888 proper candidate \((n-2)\)-colorings on those profiles, with a blocking two-cycle in every case. The upper construction was independently exercised on 3,000 fixed-seed arbitrary preference profiles, checking properness and orientation compatibility.

The enumerations do not prove results for orders above their range. No independently conducted audit or external certification is represented by this file.
