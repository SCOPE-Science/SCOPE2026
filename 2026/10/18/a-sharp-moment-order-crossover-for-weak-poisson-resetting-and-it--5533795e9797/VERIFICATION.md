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

# Verification and reproducibility

Run `python3 check_moments.py` using Python 3 with no third-party dependencies. The program checks exact rational generator identities, strict ordering of finite stationary even moments, critical-moment root evaluations, and the sharp growing-order constant at decreasing reset sizes. Its completed run reported **110659 deterministic finite checks passed**. It additionally verifies the exact finite example \(M_4^{P}/M_4^{G}=32/47\) at \(\lambda=1\), \(\gamma=1/2\), and \(s=1/4\).

The script is a finite diagnostic, not an infinite proof or an independent audit. The real-order moment boundaries are proved by positive exponential-functionals and a unit-interval moment argument. The growing-order result is proved with a uniform binomial expansion and controlled logarithmic summation. No simulation output is treated as establishing novelty.
