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
# Direct finite verification

`python3 verify_inverse.py` returned:

`VERIFY_OK: 21 bases, complete four-digit direct-image and fiber enumeration, support, maximum and maximizing multiplicities`

The verification enumerates every input string in bases 2 through 22, with no random sampling. It separately constructs the formula's image dictionary and compares counts for every output. The analytic triangular limit and all-base claims depend on the proof in `RESULT.md`, not on extrapolation from finite tests. Independent scientific audit has not been performed.
