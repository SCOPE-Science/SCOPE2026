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

# Verification of exact endpoint norms

Run `python3 check_projection.py` from the package directory using the Python standard library. The source is embedded alongside the result. This script calculates all rows of the degree-zero-plus-one weighted projection kernel by exact fractions and checks that the claimed extremal corner attains the largest absolute row sum. It independently evaluates the closed binomial mean-absolute-deviation formula, the finite binomial-tail identity, the fair-bias parity formula and monotonicity on a rational grid.

The extracted script was executed successfully: **1,866 exact-rational assertions passed** for all vertices in dimensions 2 through 7, each at seven bias values. Strict monotonicity on twenty grid values was also checked in each dimension. Numerical experiments cannot establish the theorem's universal and limiting statements. Those conclusions depend on the convex-order proof, exact binomial identities and asymptotic arguments in RESULT.md.

No Lean, formal proof assistant, independent expert examination or historical-priority certification was performed.
