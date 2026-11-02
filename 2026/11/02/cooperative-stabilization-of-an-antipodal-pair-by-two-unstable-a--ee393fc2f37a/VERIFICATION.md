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

# Reproducibility and limits

Run `python3 check.py` using Python's standard library from the directory containing the script. The saved terminal output is `checker_output.txt`.

The program evaluates the exact-softmax two-head map, tests the exact rational attention weights and radial gain, uses centered differences in six tangent directions to compare the full Jacobian against the derived block matrix, and confirms the isolated-head growing symmetric modes. Twenty-four seeded nearby nonlinear configurations decay numerically. The exact asymptotic theorem does not rest on those finite trajectories: the proof is the analytic differentiation and contraction argument in `RESULT.md`.

Numerical centered differences have discretization and rounding error. The rational identities in code use `fractions.Fraction`; they are cross-checks, not a general symbolic proof. Only local attraction near the displayed fixed point is claimed. Independent audit: not performed.
