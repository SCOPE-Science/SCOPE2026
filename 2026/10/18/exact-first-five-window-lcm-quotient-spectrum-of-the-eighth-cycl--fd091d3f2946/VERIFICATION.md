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

# Reproducibility

With Python 3 and no external packages, run `python3 CHECKER.py` in this directory. Expected terminal line: `VERIFY_OK`.

The program recomputes (rather than assumes) the five exact polynomial resultants, compares their factorization by trial division, verifies complete root lists modulo \(17,97,641\), and certifies the complete list of close pairs. It then evaluates the original product/least-common-multiple definition independently on 160000 test cases, enumerates the 1057009-element period for exact frequencies, and exhibits a nonperiod witness for every maximal proper divisor of each proposed period.

The universal proof is in `RESULT.md`; all infinite quantification, unique least-period arguments, and the CRT counting formula are mathematical deductions rather than extrapolations from the finite tests. No independently commissioned proof review or audit has taken place.
