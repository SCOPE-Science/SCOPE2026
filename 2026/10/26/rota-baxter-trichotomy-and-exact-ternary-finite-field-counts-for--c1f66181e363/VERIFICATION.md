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
# Reproducibility and mathematical checks

The accompanying `verify.py` directly evaluates the Rota–Baxter identity on every ordered pair of standard basis vectors of each tested algebra. It separately tests each branch of the abstract criterion by adjoint and Gram-matrix identities; a mismatch raises an exception. In dimensions two and three over small prime fields, every candidate matrix is enumerated rather than sampled. The dimension-three checks include both values of the quadratic norm \(B(u,u)\), two nonisometric diagonal forms over \(\mathbb F_3\), and weights \(0\) and \(1\). They confirm totals \(33\) and \(66\), and zero-weight square-zero counts \(9\) and \(15\).

Further tests enumerate the exact rank-one parametrization for \(q=5\) and \(q=7\), including both norm types, verify the predicted counts, and directly check representatives of the third branch in dimensions two and four. Run `python3 verify.py`; successful output ends in `VERIFY_OK`.

The infinite-field trichotomy and the prime-power formulas are proved mathematically in `RESULT.md`, not inferred from the finite checks. Unchecked computational regimes include nonprime finite fields, dimensions higher than four, and all possible weights outside the illustrated small fields. These are verification limits, not unproved restrictions on the stated theorem.
