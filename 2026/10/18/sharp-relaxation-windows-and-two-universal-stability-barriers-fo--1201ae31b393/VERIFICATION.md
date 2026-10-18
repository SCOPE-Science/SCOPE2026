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

Run `python verification.py` in the same directory using Python 3 and SymPy. The script checks the exact recurrence matrix, trace and determinant, all three Schur/Jury expressions, the sharp endpoint collision, the nontrivial double eigenvalue \(-1\), the robust-cutoff polynomial, and the true weak-concavity modulus and Jacobian for the smooth example. It also evaluates 1,000 seeded independent original-update versus matrix/spectral-window trials and 200 additional seeded tests under changes of the physical proximal stepsize. The recorded completed execution printed:

`PASS: exact scalar and nonlinear-Jacobian identities; 1000 independent direct-step/Jury comparisons; 200 physical-scale matches; rational boundary tests; two universal thresholds`

The infinite parameter inequalities and nonlinear instability are established analytically in `RESULT.md`. Finite sampling is not an exhaustive mathematical proof and the checker does not claim independent verification. The algebraic derivation assumes exact real arithmetic; floating-point experiment comparisons use only slack-tested nonboundary data. No external training data, downloaded references, or independent audit artifacts are needed to execute the checker.
