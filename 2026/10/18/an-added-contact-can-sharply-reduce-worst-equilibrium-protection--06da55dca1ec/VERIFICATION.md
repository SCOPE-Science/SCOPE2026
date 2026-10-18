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

The exact formulas were checked via the standalone `verify.py` file included with this result, using Python's standard library and enumerating all independent and maximal independent vertex subsets. The checks cover family indices 2 through 6, confirming that the independence number is \(2k-1\) in both graphs, while independent domination rises from 2 to \(k+1\). A separate loop checks all connected labelled graphs on two through five vertices and every missing-edge insertion: 1, 4, 38 and 728 connected graphs respectively; no insertion increases independent domination. Each edge and label is constructed explicitly from the stated graph family.

The mathematical proof handles every integer \(k\ge2\), so these finite tests are corroboration only. The implementation does not simulate SIS dynamics, certify novelty, or supply independent mathematical verification. Its exact combinatorial enumeration uses no floating-point arithmetic.
