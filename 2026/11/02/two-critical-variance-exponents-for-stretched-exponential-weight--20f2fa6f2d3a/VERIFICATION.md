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

Run `python3 verify.py` using the Python 3 standard library. The accompanying `verification_output.txt` is the program's recorded output. The program enumerates all \(\prod_{j=2}^n(j-1)=(n-1)!\) labeled parent-choice trees for each order \(n=2,\ldots,7\), using exact rational attachment probabilities, and checks the exact mean and total path-length variance against the orthogonal-increment formulas. This performs 12 exact-rational equalities.

It additionally evaluates the deterministic variance recurrence through 100,000 and 500,000 arrivals at five specified parameter choices, checking finite diagnostic inequalities and positivity: 20 assertions. Together there are 32 actual asserted conditions. In particular the slow convergence at the logarithmic critical exponent is visible; the numerical checks do not justify extrapolation to infinity.

The infinite-size statements require independent analytical reconstruction of the kernel estimates, the critical power-product estimate, Riemann-sum and harmonic asymptotics, and martingale convergence. They are argued in `RESULT.md`; the code is not an infinite proof and does not certify originality or mathematical value. Independent validation has not been performed.
