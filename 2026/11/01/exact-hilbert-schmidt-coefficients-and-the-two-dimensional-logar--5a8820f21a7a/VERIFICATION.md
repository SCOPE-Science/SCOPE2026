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

# Reproducibility and verification

The attached `CHECKER.py` uses only the Python standard library (`fractions`, `math`) and runs with `python3 CHECKER.py`.

Actual check: `PASS: 577 exact assertions; no finite test is an infinite proof.`

The program independently sums finite normalized monomial matrix coefficients for dimensions \(1\) through \(7\) and output degrees up to \(15\), checks all closed row formulas, checks invariance under coordinates in low dimensions, and confirms the finite critical harmonic-sum identities. Critical finite algebraic identities in the proof use the hockey-stick binomial identity, elementary monomial norms, and the symmetrized finite harmonic sum. Infinite sufficiency and necessity are proved from Hilbert–Schmidt matrix summability and orthogonality, not from extrapolation. The asymptotic endpoint classifications follow by the integral test; they are not verified computationally for all parameters. Independent audit has not been performed.
