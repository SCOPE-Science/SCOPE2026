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

# Computational verification and scope

Run `python3 verify.py` with Python 3 and no external dependencies. The file reconstructs the finite field from a monic irreducible polynomial, checks multiplicative inverses, enumerates all coefficient pairs, tests the two quartics for squarefreeness and disjoint branch divisors using polynomial gcds, multiplies the quotient polynomial, constructs the actual Cartier/Hasse matrices, then obtains the stable rank from three Frobenius twists. It compares the resulting rank and \(a\)-number with the theorem.

The directly enumerated rank counts, in the order \(2,3,4\), are \((1,2,0)\) for \(q=3\), \((1,12,38)\) for \(q=9\), \((1,50,624)\) for \(q=27\), and \((1,156,6086)\) for \(q=81\). Execution produced `VERIFY_OK`.

The unbounded assertions are proved symbolically in `RESULT.md` through disjoint branch-cover geometry, prime-to-three Jacobian decomposition, invertibility of the two-dimensional Hasse block, and finite-field inclusion–exclusion. Computations over four fields cannot independently prove those symbolic steps for all fields. No external or independent audit has been performed.
