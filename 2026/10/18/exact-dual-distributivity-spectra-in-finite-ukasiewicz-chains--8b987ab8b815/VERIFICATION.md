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

# Verification instructions and scope

Run `python3 verify.py` using only the standard Python library. The checker represents each chain element as an integer in \(\{0,\ldots,n\}\), calculates the original two operations by `min` and `max`, and independently evaluates the region predicates from the proof. It compares every direct equation result, its dual complement, the simultaneous-locus classification, and all three aggregate formulas for each denominator \(1\le n\le45\).

Observed result:

`VERIFY_OK denominators=1..45 triples=1168560 direct_vs_regions=PASS counts=PASS`

The loop is exhaustive only within the displayed finite denominator range. The arbitrary-denominator claim is established by the algebraic case partition in `RESULT.md`, not by interpolation from experimental values. The count formulas use denominator \((n+1)^3\) for independent uniform draws. No full independent scholarly audit has been performed.
