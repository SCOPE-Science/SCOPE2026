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

# Reproduction and limitations

Run `python3 verify.py` with Python 3.9 or later and no external packages. It reconstructs the linear map on the truncated polynomial ideal over prime fields and checks nullity, order-of-two congruences and explicit non-basis idempotent witnesses under the original quandle product at primes seventeen and thirty-one. Direct exhaustive enumeration verifies all \(3^3\) coefficient vectors for prime three and all \(5^5\) vectors for prime five. No finite sample establishes the universal theorem; the proof uses general group-ring and character arguments. The algebraic-scheme claims have no independent external audit.
