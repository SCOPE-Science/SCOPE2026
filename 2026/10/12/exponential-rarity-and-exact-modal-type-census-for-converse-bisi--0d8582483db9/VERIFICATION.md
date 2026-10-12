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

The companion `verify_converse_rigidity.py` was run with Python 3 and completed successfully. Its exhaustive tested cases were \((q,a,h)=(2,2,0),(2,2,1),(2,2,2),(2,2,3),(2,3,2),(2,1,2),(3,3,1),(3,2,1),(3,4,1)\). For each coloring, the script refines the partition using the color and **both** sets of child-successor and parent-successor equivalence classes until stable. It independently tests the local forward-subtree-type criterion and compares the count of discrete two-way quotients with the closed formula. Output:

```text
CHECK q=2 a=2 h=0 tested=2 rigid=2
CHECK q=2 a=2 h=1 tested=8 rigid=4
CHECK q=2 a=2 h=2 tested=128 rigid=16
CHECK q=2 a=2 h=3 tested=32768 rigid=256
CHECK q=2 a=3 h=2 tested=2187 rigid=864
CHECK q=2 a=1 h=2 tested=1 rigid=0
CHECK q=3 a=3 h=1 tested=81 rigid=18
CHECK q=3 a=2 h=1 tested=16 rigid=0
CHECK q=3 a=4 h=1 tested=256 rigid=96
VERIFY_OK 9 parameter_cases 35447 exhaustive_colorings; independent greatest-bisimulation refinement
```

The enumeration is exhaustive only within these declared finite parameters. It is not a proof of the infinite-height or asymptotic claims, which are derived separately in `RESULT.md`. The verifier requires only Python's standard library.
