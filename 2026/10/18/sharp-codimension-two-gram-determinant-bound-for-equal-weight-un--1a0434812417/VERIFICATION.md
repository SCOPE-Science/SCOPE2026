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

Execute `python3 check_exact.py` with standard Python 3. It evaluates all full-size Gram principal minors for the explicit three-line complementary frame in sizes \(m=6,9,12\) using `fractions.Fraction` and integer combinatorics. It checks the exact squared determinant \(3m^{n-2}/n^n\) and the factor \(3(m-1)/(2m)\) relative to the usual Cauchy--Binet bound. The expected terminal marker is `EQUAL_LEVERAGE_CODIMENSION_TWO_EXACT_CHECKS_OK`.

The executable checks only finite equality examples, not every real tight frame. The universal proof uses an orthogonal-completion/Jacobi-minor identity, the elementary circle convex-hull lemma, and an equality-case argument, reproduced in `RESULT.md`. The uncomputed exact optimum for nonmultiples of three, possible unindexed prior literature, and the lack of an independent external audit are explicit limits.
