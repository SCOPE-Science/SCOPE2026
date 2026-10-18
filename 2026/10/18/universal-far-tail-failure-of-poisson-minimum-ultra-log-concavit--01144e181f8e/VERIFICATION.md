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

Run `python3 verify.py`. The script checks the exact finite conditional minimum identity using rational arithmetic and reproduces numerical ULC-defect signs and asymptotic normalization for several Poisson intensities and positive sample-size masses, including positive mass at a larger sample size. It prints `verification: PASS` on successful completion.

Analytic proof obligations are independent of the finite checks: (i) the survival factorization for every positive integer sample size, (ii) the uniform higher-size remainder estimate for small Poisson tails, (iii) the Poisson tail asymptotic, (iv) the resulting positive normalized curvature, and (v) fixed-size endpoint preservation. The proof in `RESULT.md` establishes them for all specified parameters and indices (eventually for the strict inequality). No computer result is used to infer an untested infinite range.
