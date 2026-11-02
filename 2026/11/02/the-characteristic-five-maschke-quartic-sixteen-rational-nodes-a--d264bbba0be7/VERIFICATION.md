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

# Reproducibility

Run `python verify.py` from this directory with ordinary Python 3; no optional dependencies and no network access are required.

The script exhaustively scans the disjoint projective-normalization charts over the 5-element field and 25-element field, represented by \(\mathbb F_5[\theta]/(\theta^2-3)\). For each projective point it compares two independently coded quartic expressions. Confirmed counts are sixteen and 776, split across the four charts as \((12,4,0,0)\) and \((728,44,4,0)\). It enumerates the sixteen singular points, checks the local Hessian determinant \(2\) modulo five, verifies the K3 trace inputs \(70\) and \(550\), and checks the parity formulas algebraically for six illustrative extension degrees. `VERIFY_OK` marks completed checks.

The singular classification over an algebraic closure, irreducibility/normality, existence of the K3 resolution, purity of weight two, and the all-extension point formula are rigorous arguments supplied in `RESULT.md`. The script's six parity checks are not presented as a proof of the infinite statement.

The original 1949 Edge paper was not inspected in full, so exhaustive historical priority has not been certified. No independent audit has been performed.
