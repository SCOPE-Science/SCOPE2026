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

## Reproducible checks

The package contains `verify.py`. Run `python verify.py` with Python 3 and no third-party dependencies. Its partition kernel evaluates every pair of equivalence relations among five labeled grid cells (or four cells plus the center), rejecting repeated cells. It checks the complete trace superfamily given by full, empty, row-column cross, and two-row-by-two-column rectangle masks.

Observed output of the run from the embedded `verify.py`:

```text
LOCAL_TRACE_GEOMETRY 4 2 PASS
LOCAL_TRACE_GEOMETRY 6 3 PASS
LOCAL_TRACE_GEOMETRY 7 3 PASS
LOCAL_TRACE_GEOMETRY 8 2 PASS
KERNEL five_neighbors partitions 1153 maximum_traces 24 PASS
KERNEL center_plus_four partitions 113 maximum_traces 25 PASS
BASE 4 2 VC 1 nonexistence_tests 10 witness 12 center_chart 34,12 PASS
BASE 5 2 VC 2 nonexistence_tests 35 witness 12,13 center_chart 45,24,34,12 PASS
BASE 6 2 VC 3 nonexistence_tests 126 witness 12,13,14 center_chart 56,25,35,23,45,24,34,12 PASS
BASE 7 2 VC 3 nonexistence_tests 330 witness 12,13,14 center_chart 56,25,35,23,45,24,34,12 PASS
BASE 8 2 VC 4 nonexistence_tests 1287 witness 13,14,25,26 center_chart 78,37,47,13,57,35,45,15,67,36,46,16,25,23,24,12 PASS
BASE 6 3 VC 3 nonexistence_tests 210 witness 123,124,125 center_chart 345,136,146,134,156,135,145,123 PASS
BASE 7 3 VC 4 nonexistence_tests 1287 witness 124,125,136,137 center_chart 267,234,235,124,236,146,156,126,237,147,157,127,136,134,135,123 PASS
VERIFY_OK complete_finite_kernel=PASS small_cases=PASS witnesses=PASS
```

## Mathematical limits

The finite kernel is exhaustive because a labeled selection of at most five distinct grid cells is completely represented by its row and column set partitions; two spare indices per dimension cover every possibly relevant center at Johnson distance at most two. The finite checker does not prove this reduction, Johnson-distance identities, transitivity, or embedding monotonicity; those arguments appear in `RESULT.md`. No independent external validation or formal proof has been performed.
