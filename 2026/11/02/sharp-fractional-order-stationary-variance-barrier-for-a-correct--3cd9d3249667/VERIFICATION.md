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

# Reproducibility and limitations

Execute `python verify.py` with Python 3 and the `mpmath` package available. Successful execution prints `VERIFY_OK 696`.

The script checks the fractional Gaussian noise covariance generating function against a separately evaluated finite weighted sum, checks the resulting stationary variance in two equivalent numerical forms, tests rational Padé propagation and strict stability over positive rational step sizes, compares the sharp \(\zeta(-2H)\) asymptotic coefficient at multiple Hurst parameters, and checks the quadratic theta-family coefficient. All results are checked afresh from the supplied source; no precomputed log or external state is required.

The analytic proof in `RESULT.md` supplies the full, all-parameter correctness argument. Finite numerical tests cannot prove the infinite covariance-sum identity, the exact asymptotic limit, strict sign on an interval, or historical novelty. The relevant historical stationary-discretization paper from 2009 was inspectable only through bibliographic abstracts; priority remains subject to examination of that full text. Independent mathematical audit has not been performed.
