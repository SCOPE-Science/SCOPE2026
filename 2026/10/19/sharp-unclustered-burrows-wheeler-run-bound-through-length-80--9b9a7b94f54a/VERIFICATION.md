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

# Verification scope
Execute `python3 verify.py` alongside `witnesses.json`. The complete 67-case table is finite, and verification uses exact integer/string operations. It checks occurrence-ranked LF cycles, reconstruction, an independent direct Burrows–Wheeler transform from sorted circular rotations, primitive period exclusion, and cyclic run counts. The expected terminal line is recorded in `output.txt`. These checks establish the upper bounds exactly for the stated lengths; the general lower bound is mathematical and is proved in the cited prior work. There is no inference beyond length 80 and no claim of independent scientific auditing.
