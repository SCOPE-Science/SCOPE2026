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

# Reproducibility and checks

Execute `python3 verify_reversal.py` with Python 3 (standard library only). The run performed on the accompanying exact program returned `PASS 4188 finite arithmetic assertions`.

The program checks several hundred independent random three-spin Gibbs parameter choices, including varied unrelated local fields; independently enumerated four-, five-, and six-spin positive weights; the exact two-root example with conditioned positive associations; the one-root large-three-body-coupling regime; and the all-field zero-association case.

The infinite-dimensional-in-\(N\) statement is justified analytically by two facts: summation over any number of spectator spins leaves each selected-pair unnormalized probability affine in the single varied field's exponential, and covariance sign is the sign of a determinant of that two-by-two marginal. It is not inferred from the finite checks. The three-spin threshold discriminants and boundary cases have separate algebraic proofs.

Independent audit has not been performed. The novelty comparison is a best-knowledge literature assessment and is not a certification of priority.
