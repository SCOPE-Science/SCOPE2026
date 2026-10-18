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

# Verification and limits

Run `python3 verify_cardinality.py` using Python 3's standard library. Recorded result: `CARDINALITY_QUOTIENT_VERIFY_OK 2737`.

The checker compares exact size-overlap reachability against the proposed finite ternary frame for small moduli and cutoffs, verifies the precise positive/negative boundary, constructs depth-one separating valuations for negative cases, and independently enumerates ordinary finite subsets to corroborate the size-interval lemma. The unrestricted theorem follows from the written constructive proof, not from a finite computation. There is no independent mathematical audit or formal proof-assistant certification.
