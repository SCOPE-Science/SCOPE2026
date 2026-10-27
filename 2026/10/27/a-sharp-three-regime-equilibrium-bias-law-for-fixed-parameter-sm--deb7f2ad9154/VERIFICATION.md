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

Run `python3 verify.py` with Python 3.9+ and no third-party packages. The expected success line is `VERIFY_OK 1011`. The program directly uses the monotone scalar root, reconstructs the full joint equilibrium, replays positive-parameter memory and primal residuals for several gains and steps, compares all three singular asymptotic formulas, checks the two-client equal-curvature cancellation, and checks the sufficient local-stability hypotheses on representative parameters.

A script run on the assembled scientific content succeeded with `VERIFY_OK 1011`. The mathematical proof in `RESULT.md` rather than the finite tests establishes existence, uniqueness, infinite-range error bounds, and local stability. This has not undergone independent external validation.
