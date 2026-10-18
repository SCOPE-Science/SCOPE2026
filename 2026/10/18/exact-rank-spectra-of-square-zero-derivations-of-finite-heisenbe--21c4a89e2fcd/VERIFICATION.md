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

# Reproducible checks

Invoke `python3 verify.py` with Python 3 and no additional third-party packages. Its expected final line is `VERIFY_OK_HEISENBERG_SQUARE_ZERO_DERIVATION_RANKS`.

The program builds all matrices in the symplectic Lie algebra for \((m,q)=(1,2),(1,3),(1,4),(1,5),(2,2),(2,3)\). For each square-zero matrix it enumerates all central linear functionals satisfying the required annihilation equation, constructs the full Lie derivation, multiplies its matrix by itself, computes its rank by row reduction, and checks every coefficient against the claimed formula. The field \(\mathbb F_4\) uses polynomial arithmetic modulo an irreducible binary quadratic; the other tested fields are prime fields.

It also enumerates all symmetric matrices of dimensions \(1,2,3\) over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\) and compares nonsingular totals against the relevant congruence-form formulas.

Observed successful checks include \(1+45T+330T^2\) for \((m,q)=(2,2)\), \(1+320T+8400T^2\) for \((m,q)=(2,3)\), and the separate formula evaluation \(1+189T+6930T^2+45360T^3\) for \((m,q)=(3,2)\).

These checks do not exhaust all dimensions or field orders and do not constitute an independent scientific audit. The all-parameter theorem depends on the written proof and the classical form-classification inputs.
