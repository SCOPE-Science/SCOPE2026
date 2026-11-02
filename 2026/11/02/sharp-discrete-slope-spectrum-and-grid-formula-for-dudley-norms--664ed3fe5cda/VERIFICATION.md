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

# Reproducible checks and limits
Run `python3 CHECKER.py` using Python 3 and its standard library only. The exact-Fraction checker independently enumerates rational vertices of the lifted polytope for seven graphs with two to four vertices (106 boundary vertices in total) and compares all their possible mass maximizers against the claimed parity-grid formula for 18 signed integer profiles per graph. It then compares the path dynamic program with independent brute-force label enumeration for 60 rational signed profiles on paths with 2 to 6 vertices. All tests passed in the recorded run.

The exact graph-wide quantization, constructive realization for every diameter index, and cubic-time path recursion are proved analytically in `RESULT.md`. Finite experiments cannot substitute for those universal statements. The algorithm's arithmetic-operation complexity assumes unit-cost real/rational arithmetic and does not bound intermediate rational bit lengths. Independent scientific validation is not performed.
