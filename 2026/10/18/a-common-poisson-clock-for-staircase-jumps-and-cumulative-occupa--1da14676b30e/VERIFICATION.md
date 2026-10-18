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

Run `python3 verify_staircase.py` in the directory containing that file. The replay output was `PASS: 4996 exact finite identities and seeded stochastic sanity checks`. The checker uses only the Python standard library (`fractions`, `math`, and `random`).

Its rational tests compare the finite generating-function recurrence from the jump kernel with the independent closed polynomial formula at 3 rational probabilities, 4 generating-function arguments and 14 time indices. Other exact tests verify the integrated joint-survival identities for running minima and record-count/occupation covariance terms. Two seeded simulations check the renewal-based path construction and its marked-process comparison for finite observation horizons. The simulation bound is deliberately loose and is **not** a proof of the claimed asymptotic order.

For the infinite theorem, the critical mathematical checks are: (1) exact geometric waits from exponential seeds, independent next uniform multipliers; (2) the pointwise inequality \(|\lambda G-E|\le\lambda(E+1)\), with its special endpoint \(\lambda=1\); (3) \(\mathbb E\sum_j\lambda_j(E_j+1)\le4\); (4) the time comparison \(\Pi(t-10\log t)\le N_n\le\Pi(t+10\log t)\) with probability tending to one uniformly for \(np\to\infty\); (5) the independent exponential marks in this logarithmic band; and (6) the compound-Poisson covariance matrix. These are proved in `RESULT.md`.

The verification is mathematical and computational consistency checking only; it does not certify originality, establish a stronger error rate, or replace independent scientific assessment.
