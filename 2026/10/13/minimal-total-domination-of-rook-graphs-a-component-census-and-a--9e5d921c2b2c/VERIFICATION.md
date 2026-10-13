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
# Verification

The component proof in `RESULT.md` establishes the general theorem for all integer board dimensions at least two. The reproducible artifact `verify.py` uses exact rational arithmetic to expand the three component-generating series, and independently enumerates all selected sets on ten boards, retaining a set exactly when deleting any chosen square violates ordinary **total** domination. Executing `python3 verify.py` gave:

```
VERIFY_OK board_shapes= 10 brute_subsets= 124752 prior_table_totals= 7
POLY 2 4 [(2, 4), (4, 8)]
POLY 3 3 [(3, 6), (4, 45)]
POLY 3 4 [(3, 4), (4, 93)]
POLY 4 4 [(4, 80), (5, 96), (6, 192)]
POLY 4 5 [(4, 65), (5, 244), (6, 1920)]
POLY 5 5 [(5, 410), (6, 5700), (8, 1200)]
```

A second separately coded necessary-and-sufficient edge-local criterion in `structural_test.py` agrees with deletion-based minimality across all subsets of \(2\times2\), \(2\times3\), \(2\times4\), \(3\times3\), \(3\times4\), and \(4\times4\) boards (zero disagreements). The script also checks published ungraded totals for the seven sizes \((3,3),(3,4),(4,4),(4,5),(5,5),(5,6),(6,6)\). These finite tests check code and illustrations, not a quantified infinite statement. No separate verification or independent audit has been performed.
