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

Run `python3 verify.py` in the directory containing `verify.py`; it uses only the Python standard library. The checker reports `VERIFY_OK` after independently evaluating exact integer trace masks for all one- through four-edge support graph types, exhaustively listing all such types on at most eight nonisolated vertices, checking their labeled embedding multipliers, and enumerating every subset of up to four graph vertices for triangular graphs of sizes \(2\le n\le10\).

Completed local execution returned:

```
REPRESENTATIVES 1 types 1 trace_table=PASS
REPRESENTATIVES 2 types 2 trace_table=PASS
REPRESENTATIVES 3 types 5 trace_table=PASS
REPRESENTATIVES 4 types 11 trace_table=PASS
GRAPH_TYPES_COMPLETE 19 PASS
LABELED_MULTIPLIERS PASS
SHATTER_COUNTS 2 [1, 0, 0, 0, 0] PASS
SHATTER_COUNTS 3 [1, 3, 0, 0, 0] PASS
SHATTER_COUNTS 4 [1, 6, 0, 0, 0] PASS
SHATTER_COUNTS 5 [1, 10, 45, 0, 0] PASS
SHATTER_COUNTS 6 [1, 15, 105, 420, 0] PASS
SHATTER_COUNTS 7 [1, 21, 210, 1190, 2625] PASS
SHATTER_COUNTS 8 [1, 28, 378, 2800, 9520] PASS
SHATTER_COUNTS 9 [1, 36, 630, 5796, 23310] PASS
SHATTER_COUNTS 10 [1, 45, 990, 10920, 50400] PASS
VERIFY_OK candidate_subsets 265023 trace_table=PASS class_completeness=PASS orbit_sizes=PASS exact_coefficients=PASS
```

For the infinite result, the essential logical step is the exact support reduction: every query edge uses at most two outside vertices, so every trace family stabilizes after two outside vertices. Together with the mathematically complete list of support types, the finite mask table is exhaustive for every \(n\). The separate assertion that no set of size at least five is shattered uses an explicitly cited published theorem. Enumeration through dimension ten is corroboration, not a proof of that published theorem. Neither external review nor independent external validation has been performed.
