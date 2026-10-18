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

Run `python verify.py` using Python 3. With SymPy installed, the script evaluates the symbolic derivatives of the equilibrium kernel used in the second-order coefficient calculation. It also runs separate exact-rational finite-type mass-balance and convexity comparisons and numerical root checks for epidemiological parameters and population splits. The actual execution completed successfully with the following terminal result:

`PASS: 5109 symbolic, exact-rational, equilibrium, and numerical checks`

The analytic proof in `RESULT.md`, not the finite test set, establishes the comparison for all positive finite type distributions and all parameter values stated. The script checks formulas but cannot certify publication priority or settle dynamics outside equilibrium. No external or independent audit has been performed.
