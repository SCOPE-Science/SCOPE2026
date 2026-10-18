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

# Verification notes

The proof's critical finite corner integral is

\[
\int_{\substack{y_i\ge0\\2\sum_i y_i\le b}}\prod_i y_i\,dy
=\frac{b_+^{2d}}{4^d(2d)!}.
\]

The factor \(4^{-d}\) arises from replacing the constraint \(2\sum_i y_i\le b\) with a standard simplex, not from a sampling symmetry factor. The independent triangular coordinate densities contribute \(h^{2d}\) under the corner scaling. Maximizing sign vectors are exactly the component-constant assignments, giving \(2^c\) rather than the cube's \(2^d\) for any fixed positive deformation.

Execute `python3 checks/check_distance_tail.py` using Python 3 (standard library only). The script checks exact cut gaps and zero-cut multiplicity in dimensions two through five, an independent numerical integral for the two-dimensional crossover, and the fixed-positive-deformation leading endpoint coefficient. The final line `VERIFY_OK` indicates those finite tests passed. Continuous limits, all-dimensional quantifiers, cut-spectrum distributional reconstruction, and uniformity on compact \(t\)-intervals are established analytically in `RESULT.md`, not certified by finite test cases.

Independent scientific assessment and publication-priority certification have not been performed.
