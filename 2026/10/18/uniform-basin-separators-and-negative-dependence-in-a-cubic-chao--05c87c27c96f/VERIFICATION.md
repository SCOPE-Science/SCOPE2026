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

# Verification of the analytical result

Run `python verify_basins.py` in the directory containing the accompanying checker. It exhaustively evaluates all fair sign words of length \(0\) through \(4\) at three exact rational values of \(\beta\), and asserts the conditional mean, quadratic-variation and cross-product identities. Its 101 checks use exact integer numerator/denominator arithmetic, including the illustrative \(247/1024\) upper bound on the joint separator probability. The finite checker does not establish an almost-sure limit, a uniform marginal distribution, or an infinite series: those conclusions are proved in RESULT.md via bounded martingale convergence, a simultaneous rational-dense ordering argument, and a controlled telescoping series. Sources: arXiv:2103.03308v1 and arXiv:1611.07248v1. Independent mathematical audit has not been performed.
