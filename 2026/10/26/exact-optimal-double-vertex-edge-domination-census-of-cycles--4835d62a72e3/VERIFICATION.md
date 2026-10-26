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

# Reproducibility and limits

Run `python verify.py` with Python 3. The program separately (a) enumerates vertex subsets and checks actual graph-edge closed-neighborhood unions for \(3\le n\le18\), including exclusion of all smaller cardinalities and the asserted optimum gap types, and (b) evaluates the weighted closed-walk trace of an independently defined eight-state sliding-window transition system for \(5\le n\le80\). Both agree with the formula and the program prints `PASS`.

The closed-walk trace weights each appended bit and accepts exactly windows with at least two selected vertices; its proof of equivalence to feasible labeled cycle configurations is separate from the selected-vertex gap proof. These finite checks are neither exhaustive over all cycle lengths nor an independent mathematical audit. The paper's infinite claims are proved in `RESULT.md`.
