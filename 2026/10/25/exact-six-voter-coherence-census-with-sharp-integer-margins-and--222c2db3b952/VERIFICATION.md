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

Run `python3 checker.py` with Python 3 standard library. The script prints `ALL_CHECKS_OK` and the exact four-block, coherent/incoherent, radius and orbit counts. It enumerates all \(\binom{20}{4}\) possible four-triple families before filtering, all \(1024\) selectors, all zero-sum integer perturbations with coordinate bounds \(1,2,3\), all \(64\) coalitions for every proposed weight representation, and all \(720\) voter permutations. Its loops are finite, bounded and exhaustive. The core hand-checkable defect in the named six-point example is the incidence identity \(\mathbf1_{123}+\mathbf1_{145}+\mathbf1_{256}+\mathbf1_{346}=(2,2,2,2,2,2)\). The accepted result has self-review only; independent audit has not been performed. Historical threshold-function tabulations remain a stated priority risk.
