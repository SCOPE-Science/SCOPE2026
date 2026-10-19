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

Run `python verify.py` using Python 3 and SymPy. The program independently constructs two covariance coefficient sequences: one from the Koopman transition closure, the other from the formal algebraic generating function. It also integrates the original branchwise affine map over exact dyadic cells, checks pole residues and collision constants symbolically, verifies coefficient positivity for selected rational parameters, and compares finite high-lag coefficients against each asymptotic regime.

The checked range consists of nine rational parameter values, coefficients through degree 16, direct integrals for lags 0 through 4, an 81-step positivity check for six parameters, symbolic algebraic identities, and seven lag-500 asymptotic diagnostics; the executed total is 699. All exact comparisons use rational arithmetic; large-lag checks use floating-point arithmetic.

The all-parameter covariance identity and singularity asymptotics are established in the analytical proof of RESULT.md, not by finite enumeration. In particular, no numerical diagnostic certifies an infinite series by itself. A separate independent mathematical audit has not been performed.
