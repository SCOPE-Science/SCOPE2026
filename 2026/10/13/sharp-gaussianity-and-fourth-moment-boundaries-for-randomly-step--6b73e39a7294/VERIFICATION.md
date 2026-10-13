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

# Verification and reproducibility

Run `python3 verify.py` with Python 3.9 or later; only the standard library is required. The script recomputes the two rational step laws and confirms equality of \(\mathbb EH\) and \(\mathbb EH^2\), equal stationary variance \(4/3\), finite fourth moment \(92/15\) for the first law, and multiplier fourth moment \(1261/576>1\) for the second. It verifies that the fourth-moment multiplier for the second law crosses the moment threshold between orders 3 and 4. The script also checks 210 additional rational-parameter combinations for the variance-bias and fourth-cumulant algebra, including deterministic and midpoint cases. The expected terminal line starts `VERIFY_OK`.

This is exact finite arithmetic, not a proof by experiment. The existence and uniqueness of the invariant law, iff Gaussianity statement, the positive fourth-cumulant identity and the complete positive moment range are justified by the mathematical proof in `RESULT.md`; the program cannot certify universal quantifiers or an asymptotic tail exponent. No simulation or external library is necessary. Independent audit is not performed.
