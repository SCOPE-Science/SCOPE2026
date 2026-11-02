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

# Verification and scope

The executable `verify.py` evaluates the Hessian identity symbolically, checks lexicographic Gröbner reductions on four projective charts modulo five, enumerates the fourteen rational Jacobian zeros and their local quadratic ranks, and counts the points of the explicit quartic over `GF(5)` and `GF(25)` using a polynomial quotient implementation. The expected output is embedded in `verification_output.txt` and ends with `VERIFY_OK`. It reports the singular quartic counts `56`, `826` and resolved counts `126`, `1176`.

The arithmetic conclusions for every extension follow from the proved K3 Weil bound and its saturation over the quadratic extension. The checker does not compute arbitrary extension fields or independently certify historical novelty. The existence of rational points on the exceptional smooth conics follows from the finite-field theorem for ternary nondegenerate quadratic forms; the checker verifies their nondegeneracy but does not explicitly enumerate points on each conic.
