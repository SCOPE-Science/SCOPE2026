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

# Verification steps and limits

The proof is self-contained in `RESULT.md`. Run `python3 verify.py` in this directory (Python 3.10 or newer). The script constructs all nonempty antichains of nonempty subsets on carriers of sizes one through three; these uniquely represent proper upward-closed local neighborhood families. It evaluates all subsets of the Cartesian product as Boolean events, then compares both converse implications with their stated antichain criteria, checks forward mixing, and compares the observed pair counts with the formulas.

An actual local replay of the embedded script returned:

```
PASS: 529 ordered local-family pairs, 175682 pair/valuation tests
PASS: one-order and two-order exact counts, including (3,3)=(203,131)
PASS: both-order failures first possible on carriers of size 3 by 3
```

The finite replay cannot establish the result for arbitrary finite carrier sizes; that follows from the minimal-neighborhood argument and inclusion-exclusion proof. The result does not treat infinite carriers, empty local neighborhood families, or those admitting the empty set as a neighborhood. No independent verification has been performed.
