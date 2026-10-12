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

The theorem is established by the complete symbolic proof in RESULT.md, not by finite testing. The standalone standard-library checker `verify.py` computes the Dirichlet inverse using a convolution recurrence, verifies the independent multiplicative prime-power formula, computes Jordan totients both by divisor sums and Euler factors, and checks the inequality and equality case for all indices \(1\le n\le4000\) and parameters \(2\le k\le7\). It reports `VERIFY_OK` and 24,000 evaluated pairs. A separate symbolic argument uses the exact Euler product \(\zeta(2)^2/\zeta(4)=5/2\) and exhausts squarefree, cube-divisible, and cube-free nonsquarefree positive composites. Infinite coverage is wholly proof-based; no finite test is treated as an exhaustive infinite certificate. External independent audit remains unperformed.
