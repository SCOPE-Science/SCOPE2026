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

Run `python3 checker.py` using Python 3 standard library. The checker verifies the four complete vertex-colour atom probabilities for two explicitly biased colours, all 16 truth-table subset sums, four nested sample formula reductions, and exact pointed/uniform agreements for every directed edge and colour assignment on n=1,2,3 (loops included). The expected output ends in `ALL_CHECKS_OK`.

The infinite result is justified by the complete structural induction in `RESULT.md`, not by finite tests. Repeated comparisons may have exact ties: the proof treats that case separately using Boolean equivalence. Exact error constants depend on the finite formula, positive edge probability and nonzero expectation gaps; no universal rate uniform over arbitrary formula size or biases is asserted. All confirmation here is self-review; independent audit has not been performed.
