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

# Verification scope and replay

The companion `verify.py` is standalone Python 3 code using only standard-library exact integer and rational arithmetic. Execute `python3 verify.py` from the extracted package directory. Its completed result was:

`VERIFY_OK cubic_full_enumerations=11 quartic_full_enumerations=3 smith_triple_checks=11 symbolic_group_checks=100 exact_arithmetic=yes`

Cubic cases: \((p,k)=(2,1),(2,2),(2,3),(2,4),(2,5),(3,1),(3,2),(3,3),(5,1),(5,2),(7,1)\). Quartic cases: \((2,2),(2,3),(3,2)\). Every cubic case independently enumerates all lower-coefficient tuples and roots, enumerates all reduced Vandermonde triples, and compares both to the parity formula. For \(p\in\{2,3,5,7,11\}\) and \(1\leq k\leq20\), the grouped valuation expression is also compared with the closed formula. No randomness or floating-point arithmetic enters any test.

These checks do not enumerate all primes, all degrees or all exponents. Those quantifiers are justified by the finite algebraic proof in `RESULT.md`. No independent audit or outside certification is asserted.
