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

# Reproduction and boundaries

Run `python verify.py` with Python 3, NumPy, SciPy and mpmath. In the reviewed package this command printed `PASS 378 assertions`; the captured output is `verification_output.txt`.

The checker independently evaluates the parabolic-cylinder derivative ratio, verifies the exterior Ornstein–Uhlenbeck differential equation, solves the implicit eigenvalue equation at 60-digit precision, compares asymptotic formulas for several fixed low modes and penalty values, and discretizes the conjugated Schrödinger operator on a 20,001-point interior grid. It does not enumerate every penalty or eigenvalue index, nor does a numerical remainder comparison prove a uniform estimate. The infinity-range proof uses the explicit gamma quotient, analytic expansions, matching conditions and Sturm oscillation in `RESULT.md`.

The recorded output is reproducibility evidence, not independent audit or proof of historical priority.
