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

The source-code checker `verify.py` is standalone Python 3. It verified 922 nonempty admissible antichains in the 6-by-6 exponent grid by exact rational comparison, testing strict equality only for the appropriate complete degree layers. It also compared computed maximizing layers with independent finite evaluations for five prime pairs and twelve exponents, and bracketed the critical exponent. Output: `VERIFIED rational_antichains 922 grid_side 6 prime_pairs 5 exponent_tests 12 critical_2_3 0.460671603873383`.

This is a bounded calculation, not an exhaustive proof over unbounded exponents. The proof of the unrestricted theorem is in RESULT.md; numerical approximation of the threshold is not relied on to certify the qualitative phase transition.
