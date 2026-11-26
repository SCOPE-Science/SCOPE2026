---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

Run `python3 verify_braess_benchmark.py` in this directory. This finite exact-rational check compares direct minimum-cost option tests with the equilibrium classification on rational flow grids for benefit levels \(9/8,6/5,3/2,7/4\). It also checks the unique grid optimizer and worst Nash cost at those levels, using grids containing the predicted global optimizer and a worst Nash flow. The continuum claims and the sharp optimizer switch at the irrational value \(4-2\sqrt{2}\) require the analytic proof in `RESULT.md`.

```text
grid B=9/8: optimum 783/256; worst Nash cost 27/8; ratio 32/29
grid B=6/5: optimum 16/5; worst Nash cost 18/5; ratio 9/8
grid B=3/2: optimum 7/2; worst Nash cost 9/2; ratio 9/7
grid B=7/4: optimum 15/4; worst Nash cost 21/4; ratio 7/5
```
