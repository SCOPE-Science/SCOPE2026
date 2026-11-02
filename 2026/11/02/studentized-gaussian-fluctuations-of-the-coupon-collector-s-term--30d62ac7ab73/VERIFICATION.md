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

# Verification of the mathematical claim

Run `python3 checker.py` with Python 3 and no third-party libraries in the directory containing these two files. The checker independently computes exact singleton probabilities by absorbing a finite chain of unseen and singleton types and by integrating the proposed physical-time joint density as a finite Gamma integral. It compares every possible singleton count for \(n=2,\ldots,10\), normalizations, the harmonic expectation, and the published variance identity: 90 exact rational assertions in total.

The analytic proof in `RESULT.md` additionally establishes: (i) the all-\(n\) shifted-binomial law by Poisson independence; (ii) a uniform compact-window conditional Berry--Esseen bound; (iii) conditional characteristic-function convergence jointly with the completion maximum; and (iv) the exact mean-square relation \(\mathbb E(M_n-T_n/n)^2=H_n/n\) needed to transfer the random centering to discrete collection time.

The checker cannot certify distributional convergence, asymptotic independence, general historical priority, or any unspecified model. Independent audit has not been performed.
