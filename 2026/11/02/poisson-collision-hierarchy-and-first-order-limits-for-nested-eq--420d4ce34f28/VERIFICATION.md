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

# Reproduction and scope

Run `python3 checker.py` with Python 3.10+ and no third-party dependencies. Successful execution prints `ALL_CHECKS_OK` with the test counts.

The program enumerates 270592 fair colour assignments on four finite nested equivalence structures and compares their full joint critical-profile distribution to an independent exact multinomial calculation using `fractions.Fraction`. Seven further cases compare mixed factorial moments with independent-Poisson predictions. Sixteen exact-model threshold computations cover two critical intensities. These tests exercise small finite identities; they are not an infinite exhaustive check. The general convergence of probabilities and first-order assertions follows from the mathematical proof in `RESULT.md`. Independent external validation has not been performed.
