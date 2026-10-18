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

The exact geometric assertion is proved in `RESULT.md` by a complete edge-sweep computation on the fundamental normal cone and a direct spherical vector-area integral. `verify_crofton.py` is a standard-library-only corroborating checker for the finite edge-incidence identities and independent numerical reevaluation of the spherical integral.

Observed command: `python3 verify_crofton.py`

Observed result:

```
VERIFY_OK vertices=12 edges=24 exact_neighbor_signs=24 positive_events=6
p4=0.193059337124398 p6=0.325345782679200 p8=0.481594880196402 expected_sides=6.577071086144008
```

The script's cone tests use integer arithmetic, and the spherical comparisons are floating-point checks at absolute tolerance \(10^{-13}\) or better; the exact symbolic formulas in the proof are not inferred from numerical agreement. The six event counts and the central-crossing count constitute finite exhaustive checks, not a general-purpose proof of an unbounded assertion. The orientation/offset law is analytic. No independent mathematical review, independent certification, or unrelated external verification is claimed.
