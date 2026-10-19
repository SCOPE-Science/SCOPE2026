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

# Reproduction and mathematical limits

The theorem has an analytical proof valid for every integer \(n\ge3\). The independent program `verification.py` computes the two update-neighbor counts directly on the labeled graph and checks the full absorbing-state opinion histogram by exhaustive enumeration for all sizes \(3\le n\le9\). It separately evaluates both closed formulas for every size \(3\le n\le200\), for all possible blue-vertex counts, without floating-point approximations. The program uses integer Lucas arithmetic, integer recurrence for the signed independence polynomial, and exact integer binomial coefficients.

Run `python3 verification.py` using Python 3 with no third-party packages. Observed complete-enumeration total counts are \(4,8,14,22,32,48,76\) at sizes \(3\) through \(9\), respectively. The program reports 40,688 successful comparisons. This finite computation verifies small instances and arithmetic coherence but is not a proof of the universal fixed-state claim. The infinite-family assertion follows from the mismatch-rung propagation, run-composition bijection and transfer-matrix identity detailed in `RESULT.md`.

Independent validation: not performed. No experimental conclusion about random initial conditions or convergence-time distributions is claimed.
