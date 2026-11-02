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

Run `python3 verify_symbolic.py` and `python3 verify_primefield.py` with Python 3 and SymPy. The first script checks the quartic discriminant identity, Cartier coefficients, \(D_5\) coordinate transformation, quadratic discriminant criterion, and resultant. Its expected output is `EXACT_PICARD_D5_AND_6_2_BOUNDARY_OK`. The second script independently enumerates all \(125\) coefficient triples over \(\mathbb F_5\), computes a polynomial gcd to identify the smooth quartics, constructs the Cartier coefficient matrix, and checks ranks from its third power. Its expected output contains `GF5_EXHAUSTIVE_DIRECT_CARTIER_OK`, with \(84\) smooth rank-two, \(16\) smooth rank-zero and \(25\) singular cases.

The proof of geometric irreducibility, normality and Weil multiplicities uses algebraic arguments given in `RESULT.md`; a finite-field census is not an infinite-field proof. No independent audit or external validation has been performed.
