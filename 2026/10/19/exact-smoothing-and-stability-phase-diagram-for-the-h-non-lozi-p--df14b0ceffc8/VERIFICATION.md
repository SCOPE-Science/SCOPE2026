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

# Reproduction

Run `python3 verify.py` with a recent SymPy installation. The checker prints `VERIFY_OK` only if all exact symbolic identities and all numerical branch/return assertions pass. Checked symbolic identities include both strict-threshold difference numerators, the level-function interface values, terminal derivative, and central multiplier product. Its parameter grid spans contracting dissipative cases, near-degenerate branch widths, and cases whose terminal threshold exceeds the published smoothing interval.

The analytical proof is independent of the finite grid: convexity, monotonicity and Schur conditions cover every real parameter in the stated domain. The checker does not certify source novelty or external review. Mathematical assertions at neutral multipliers are limited to linear spectra; no nonlinear stability conclusion is attempted.
