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

# Verification record

Run `python verify.py` using Python 3 standard library only. It creates all factors directly and tests the lexicographic proper-suffix definition, independently of the classified-factor construction. It compares complete sets and their factor-length multisets for every one of the 2,401 positive quadruples with each run length at most seven. It computes every four-run composition through length 30 to test extrema, all equality cases and rational generating-function coefficients. Exact `fractions.Fraction` integration of four quadratic polynomials establishes the arithmetic of the two Dirichlet moments used in the analytic proof.

The general proof is given in RESULT.md; bounded brute-force checks are not used to extrapolate to all integers. No independent mathematical audit has been performed. The results are confined to contiguous distinct Lyndon factors of four positive alternating binary runs, with uniform compositions in the probabilistic statements.
