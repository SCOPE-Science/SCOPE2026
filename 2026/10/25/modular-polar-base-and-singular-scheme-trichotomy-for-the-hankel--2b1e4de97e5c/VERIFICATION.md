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
# Reproduction and limits

Run `python check_hankel_permanent.py` with Python 3 and SymPy; it prints `VERIFY_OK` when the exact symbolic checks and finite-field spot checks succeed. The checker is included with the calculation.

The polynomial automorphism and its inverse, the equality with the normal form, the reversal symmetry, the Jacobian generators, and the characteristic-three polar-curve substitution are checked symbolically. Equality of the transformed Jacobian ideals is tested modulo several primes. Exhaustive rational point searches over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\) check the expected support; they are not proofs of algebraic-closure support or infinite-characteristic statements.

The proof in `RESULT.md` supplies the global boundary check, reducedness at the extra characteristic-three point, and complete-intersection argument, all independent of finite enumerations. The specific local Artin lengths follow directly from \((U,V,W,t^5)\) or \((U,V,W,t^6)\). Independent audit has not been performed.
