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

# Reproducible mathematical checks

Run `python verify.py` with Python 3 and SymPy available. The program independently reconstructs the symmetric stationary covariance, checks every entry of the Lyapunov equation and the antisymmetric current identity, computes the EPR from its Gaussian definition, and verifies the closed rate, derivative, baseline difference, stability polynomial and limiting value as exact symbolic identities in both model parameters. It additionally checks the illustrative rational-parameter example. This checker was run on the packaged source and printed its PASS message.

The all-parameter monotonicity and baseline-crossing results are proved analytically in `RESULT.md` using strict positivity and affine sign factors, not numerical sampling. The calculations assume \(h>0\) and \(k\ge0\); exact formulas also have formal extensions outside this physical domain which are **not** interpreted as stationary EPR when stability is absent.

The independent scientific and publication-priority audits are not performed.
