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

Run `python3 verify.py` with Python 3.9 or later; the checker uses only the standard library.

The checker directly tests the exterior multiplication map over \(\mathbb F_3\) on representatives with centralizer dimensions \(48,57,58,60,63,64\), and on forty deterministic random odd elements. It independently exhausts the \(2^{20}\) possible \(3\)-vectors over \(\mathbb F_2\) solely to check the dimension-independent incidence trichotomy \(k\in\{0,1,3\}\) and its Gaussian counts at \(q=2\). It also checks exact row totals and the rational commuting-probability formula for \(q=3,5,7\).

Expected successful output:

`ALL_EXTERIOR_SIX_CENTRALIZER_CHECKS_PASSED [992496, 54684, 0, 1395, 0, 0, 1] [('nonzero degree one', 48), ('zero wedge-annihilator trivector', 57), ('one-dimensional wedge-annihilator', 58), ('decomposable trivector', 60), ('pure nonzero five-form', 63), ('zero odd part', 64)]`

The finite characteristic-two computation is not a commutativity test: in characteristic two the entire exterior algebra is commutative, so the theorem explicitly excludes it. Finite computations cannot prove the all-odd-field claim. The proof is the five-step reduction and incidence enumeration in `RESULT.md`.
