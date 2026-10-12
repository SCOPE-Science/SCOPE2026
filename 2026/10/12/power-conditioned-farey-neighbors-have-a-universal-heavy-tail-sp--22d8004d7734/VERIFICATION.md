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

## Reproduction

Execute `python3 verify.py` with any recent Python 3 interpreter; this is a standalone standard-library arithmetic check. It enumerates all ordered Farey neighbors by the classical recurrence, filters denominators by exact powers, and compares against direct coprime power pairs, with 45 test triples. It also computes sample count ratios to the beta-function leading term at order 10,000,000.

Observed run: `BIJECTION_OK tests=45 all_ordered_Farey_pairs_matched`; large-order counts are 1303766, 66126, 66126, 3336 at exponent pairs (2,2), (2,3), (3,2), (3,3), respectively.

## Mathematical limits

Finite enumeration verifies examples only. The infinite results use the explicit Farey bijection, Möbius grid estimate, beta integral, and two endpoint-cusp expansions in RESULT.md. The t-asymptotic concerns the limiting law after N tends to infinity; t and N are not interchanged. A separately authored independent audit has not been performed.
