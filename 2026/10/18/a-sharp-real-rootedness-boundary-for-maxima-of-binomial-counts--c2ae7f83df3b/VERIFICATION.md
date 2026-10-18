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

The proof in RESULT.md covers every positive integer binomial trial count, every independent sample size at least two, and every interior success probability in the stated cases. The small-parameter obstruction is analytic through coefficientwise polynomial convergence and continuity of complex roots, not simulation.

`checker.py` uses Python 3 standard-library exact integer and rational arithmetic. Running `python checker.py` from the extracted file directory printed `PASS: 2615 exact algebraic/finite checks`. It recomputes all four cubic probability coefficients from binomial CDF powers, checks their explicit polynomial forms, verifies the degree-three discriminant identity as an equality of integer polynomials, checks threshold-bracketing rational values, checks low-order rare-event coefficients for a finite grid of sample sizes, and checks the degree-two discriminant identity and sign on a rational grid.

The checks do not certify the infinite quantifiers on their own; those are justified by the supplied symbolic proof. The literature comparison has unindexed-source and partial-full-text risks, described in REVIEW.md and AUDIT.json. No independent audit has been performed.
