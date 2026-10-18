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

# Reproducible calculations

Run `python3 verify_cubic.py` with standard Python. The checker uses `fractions.Fraction`, `itertools.permutations`, and `itertools.product`, with no simulation and no external packages. In the current calculation it reported:

`PASS 96 exact rational assertions; d=3..6 one-step, d=3/4 multi-step, and quartic obstruction`

For dimensions 3, 4, 5, 6 the checker exhausts all coordinate shuffles for several explicit doubly stochastic kernels and three zero-sum test inputs. It verifies selected products over all shuffles in every layer at dimensions 3 and 4, all tested regular-degree formulas, and the two distinct fourth-power ratios 11/21 and 2/3. Its finite range is **not** a verification of an infinite or all-dimension mathematical assertion; the elementary symbolic argument in RESULT.md supplies that proof. Bibliographical priority and independent validation remain unperformed.
