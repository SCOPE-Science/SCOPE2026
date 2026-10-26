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

# Verification notes

Run `python checker.py` with NumPy, SciPy and SymPy installed. The standalone script checks representative exact rational characteristic polynomials, compares spectral formulas with direct matrix exponentials for 1,500 deterministic sampled positive edge pairs, tests both sides of the explicit unique sign crossing, verifies equal-edge positivity bounds on specified grids and the sharp center-diagonal equality, and checks the near-balance asymptotic at four contrasts. The script reports **18,052 deterministic check units** on successful completion.

The theorem's universal quantifiers, exact sharp parameter boundary, uniqueness of the crossing, and logarithmic asymptotics rest on the self-contained analytical derivations in `RESULT.md`. Finite tests neither certify them independently nor exhaust the parameter domain. Results are in exact arithmetic; observed floating-point signs extremely close to a crossing are not used as proofs.
