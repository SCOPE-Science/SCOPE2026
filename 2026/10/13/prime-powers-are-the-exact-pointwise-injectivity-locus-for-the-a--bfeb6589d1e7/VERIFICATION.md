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

The proof is symbolic. `verify.py` is a regression test for the two explicit mixed-support constructions and the prime-power boundary. It factors every integer from \(2\) through \(10000\) and uses exact rational arithmetic to check the two transform-difference identities and the exclusion \(P=2Q\). The checker does not prove the theorem for all integers; the unbounded proof is in `RESULT.md`.
