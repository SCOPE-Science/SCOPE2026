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

# Verification record

The proof in RESULT.md, not any finite experiment, establishes the mathematical claims. `verify.py` uses SymPy exact rational matrices to check the critical Hessian, its corank and kernel, the left-projected cubic coefficient and multiple explicit attachment examples. NumPy diagnostics test Hessian signatures above threshold, angle-sum inequalities on deterministic samples, and critical long-time relaxation on graphs with and without attached trees. The script includes a triangle as an explicit comparison to existing literature; the proposed theorem applies only to cycles of length at least five.

Execute `python verify.py` in a Python environment with NumPy and SymPy. Successful execution ends with `VERIFICATION_OK`. The sampled finite orbit asymptotics can converge slowly, so the program compares errors only within a declared tolerance and requires improvement across later times. Numerical data do not certify all graphs, parameters, infinite time, or bibliographic originality.

No independent audit or external validation has been performed. The remaining originality uncertainty includes older weak-link XY/Josephson-ring theory and the inability to inspect the complete earlier triangle record beyond its indexed scientific summary.
