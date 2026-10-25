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
# Reproducibility and mathematical checks

`verify.py` uses the actual graph adjacency rather than the column-classification theorem to decide whether a subset and its complement are simultaneously locating-dominating. For each \(4\le n\le8\), it checks every bitmask on \(2n\) vertices, constructs every legal single-transfer edge, and compares the independent outputs with the stated coefficient polynomial, component orders, and edge formula.

Run `python3 verify.py` with Python 3; the expected last line is `VERIFY_OK oracle_masks= 87296 infinite_formula_cases=5`. Per-order outputs give \(112,332,904,2340,5856\) admissible ordered bipartitions and \(240,840,2520,6944,18144\) reconfiguration edges for \(n=4,5,6,7,8\), respectively. A separate boundary check at \(n=3\) verifies that the graph then consists of twenty isolated configurations, which explains the stated domain.

The exhaustive computations establish only these finite cases. The complete proof for arbitrary \(n\ge4\) is based on row-neighborhood trace comparison, domination exceptions, explicit pattern enumeration, Boolean-cube connectivity and level-by-level edge counting; all definitions and hypotheses are given in `RESULT.md`. Nothing here establishes independent audit or global historical priority.
