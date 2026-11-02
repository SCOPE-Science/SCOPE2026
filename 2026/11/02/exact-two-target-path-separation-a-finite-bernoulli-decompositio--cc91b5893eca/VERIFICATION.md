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

The exact-rational checker `verify_path_cutting.py` is self-contained (Python 3 standard library). It separately constructs the actual stopping-time distribution by an explicit recursive examination of every possible first cut, tracking whether each original target remains. Its independent second calculation constructs generating polynomials from Bernoulli success probabilities \(1/(k+1)\). Across 55 ordered positive arm-length pairs of total sizes \(3\) through \(12\), all probability coefficients agree exactly. The checker also verifies normalization, the exact one-cut mass, the exact expectation and both sharp total-variation equalities; 964 assertions pass. Four additional finite-sum numerical checks compare expectation formulas. No Monte Carlo approximation is needed.

Reproduce: `python3 verify_path_cutting.py` in the directory containing the bundled file.

These finite computations confirm small cases of the claimed identity but are not exhaustive over infinitely many arm lengths. The mathematical proof in `RESULT.md` derives the finite identity without computational enumeration, and separately proves the interior limiting law, endpoint TV approximation, and independent-Bernoulli central limit theorem. No external or independent review was performed.
