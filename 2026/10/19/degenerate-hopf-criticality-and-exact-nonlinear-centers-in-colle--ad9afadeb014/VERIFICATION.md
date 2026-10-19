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

The analytic identity \(x(1-x)P'(x)=(m-(N-1)x)P(x)\) gives \(x(1-x)P'''(p)+2(1-2p)P''(p)=0\), which cancels the entire cubic focus coefficient for both listed risk-feedback laws. The independent reversible-center conclusion uses the involution \((x,r)\mapsto(1-x,r)\) only when \(M=(N+1)/2\).

Run `python verify.py` with Python 3, SymPy and SciPy installed. The executable file contains all required model definitions and does not depend on other files or external data. It independently forms the quadratic and cubic multilinear normal-form tensors and verifies six rational-parameter zero-coefficient cases exactly. It also verifies four numerical first-return checks at the symmetric-group critical point, with absolute return-coordinate errors below \(5\times10^{-13}\).

The script checks finitely many parameter choices only. The universal coefficient statement follows from the displayed symbolic derivative identity, and the continuous family of critical cycles follows from the reversibility/implicit-function argument, not from numeric integration. No global attraction or higher-order classification of asymmetric groups is asserted. Independent audit remains unperformed.
