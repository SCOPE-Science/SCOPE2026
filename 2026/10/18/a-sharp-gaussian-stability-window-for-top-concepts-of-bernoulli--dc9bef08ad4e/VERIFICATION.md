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

# Verification and scientific limits

Execute `python3 verify.py` in the directory containing the standalone verifier. It requires only Python's standard library. The script directly evaluates Galois common-attribute sets for **every** object subset in every complete binary incidence matrix under study, then sums the matrix probabilities exactly as rational numbers. It compares the resulting exact expectation with the proposed binomial formula for all 29 finite cases (10,238 incidence matrices in total). The code also evaluates the analytic finite formula at critical sizes. The finite checks passed and are not infinite certificates.

The critical-window and exponentially small expectation assertions are **not** deduced from computing sample sizes. Their proof uses the exact per-column bad-event probability, a uniform threshold bound, a summable Markov–Borel–Cantelli argument valid without cross-size independence, the central limit theorem for an auxiliary symmetric binomial count, and standard binomial large deviations.

All claims require \(p\in(0,1)\), a positive integer number of attributes at each size, and independent equal-probability incidences within each context. The proof does not characterize stability of non-top concepts, heterogeneous or dependent incidence models, or finer random fluctuations of the stability statistic. A related 2022 paper on stability algorithms could only be compared via its public abstract; an earlier implicit reduction to a random coverage threshold is a residual originality risk. No independent external audit has been conducted.
