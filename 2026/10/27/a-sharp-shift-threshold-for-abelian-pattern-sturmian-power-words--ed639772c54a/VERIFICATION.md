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
# Verification of the sharp affine-power threshold

Run \(`python3 verify.py`\) with Python 3 standard library. The script rebuilds each finite graph by checking the defining sum relation for every allowed edge, independently detects cycles by union-find, and compares the results with the proposed threshold over a finite family. It then directly checks the complete prescribed cycle vertex sequence for 114 parameter choices.

Expected output, reproduced using the embedded source:

```
FINITE_FOREST_CASES_OK 1056
CYCLE_FORMULAS_OK 114
VERIFY_OK
```

Finite experiments do not prove universal claims. For all bases and shifts, the infinite proof is in RESULT.md: the largest-edge obstruction gives sufficiency, and the explicit cycle proves necessity. The published graph/word equivalence [arXiv:2609.28059v2, Theorem E] and its cycle lower bound (Theorem 7.4) provide the final transfer to Abelian maximal pattern complexity. No independent mathematical audit has been performed.
