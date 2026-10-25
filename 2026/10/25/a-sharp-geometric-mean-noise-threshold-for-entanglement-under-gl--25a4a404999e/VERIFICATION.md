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

# Verification of the two-qubit stationary entanglement threshold

## Analytic checks

The exact resolvent of the stated linear Markovian Lindblad-plus-reset generator provides a normalized positive density matrix. Both partial-transpose branches were considered. The second branch is impossible by a nonnegative pointwise Gram-like expression and Cauchy–Schwarz averaging. The first branch reduces identically to the displayed quartic divided by a strictly positive denominator. Coefficient sign analysis and Descartes' rule prove the unique-reset-boundary statement for every positive parameter value. The strong-reset concurrence expansion is obtained by expanding the exact density matrix, not by numerical fitting.

## Reproducible computation

From the directory containing `checker.py`, execute `python checker.py` using Python 3 with NumPy and SymPy installed. The file is entirely self-contained apart from those packages. It performs symbolic cancellation, exact checks of the quartic coefficients, and independent \(16\times16\) Liouvillian solves of the stationary density matrix for 350 random parameter configurations. It verifies density-matrix normalization and positivity, compares direct Wootters concurrence to the \(X\)-state expression, tests both PPT branches, checks an additional 250 parameter sets against quartic-root structure, and tests 80 symmetric-rate cases and four highly asymmetric configurations. Execution returned `PASS 3646 algebraic and finite-dimensional checks`.

## Scope of evidence

Numerical checks establish reproducibility over tested finite parameter sets; they do not certify an infinite parameter domain. That domain is covered by the algebraic resolvent identity, positivity argument, and polynomial sign proof. The result does not establish finite-time entanglement, stability under arbitrary Hamiltonian perturbations, or independent priority in the literature. Independent audit remains not performed.
