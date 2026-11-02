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
The included `verify.py` uses only Python's standard library. From a directory containing that script run `python3 verify.py`.

It performs exact native Zinbiel multiplications over prime fields, not an implementation of the proof's proportional-row counting, and reconstructs all element commutants. It checks the original algebra identity on every basis triple and, for each listed \((q,n)\), enumerates all ordered commuting pairs and triples via adjacency bitsets. Direct counts:

| \(q\) | \(n\) | Commuting pairs | Commuting triples |
| ---: | ---: | ---: | ---: |
| 3 | 2 | 81 | 729 |
| 5 | 2 | 625 | 15625 |
| 5 | 3 | 3625 | 93125 |
| 5 | 4 | 30625 | 2340625 |
| 7 | 3 | 18865 | 938791 |

Expected final line: `VERIFY_OK 5 exhaustive independent pair/triple censuses and centralizer checks`.

Boundary conventions: all zero is counted; the center is the highest-degree basis line; the characteristic is strictly larger than the dimension. The test suite verifies small prime fields, but it does not exhaust extension fields or infinite dimensions. Those cases are covered algebraically by the proof and not separately certified. Independent mathematical audit: not performed.
