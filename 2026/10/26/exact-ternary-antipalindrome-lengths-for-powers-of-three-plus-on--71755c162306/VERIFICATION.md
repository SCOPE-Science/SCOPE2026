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

Exact reproducible check: execute `python3 verify.py`. It enumerates all positive ternary antipalindromes of length at most fourteen without using the carry classification; checks every unordered pair summing to the target; independently verifies all explicit triples. The program exhausts only that finite range. The proof's digit-sum/carry monotonicity, length-gap bound and middle-column contradiction are symbolic and apply to all indices. No independent audit has been performed.
