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

The included `verify.py` computes \(\kappa_0\) directly by the recurrence over every proper divisor of each exponent vector and compares the result against the independent Stirling-coefficient expression. It checks \(1\le r\le12\) and \(0\le k\le6\), 84 configurations in total, with the exact asserted valuation in every case. Run `python3 verify.py` in an extracted package directory. It requires Python 3 standard library only and prints `VERIFY_OK`.

Finite checks are corroborative only. The infinite statement is proven by the generating-series identity and congruence calculation. Full-text novelty exclusion for the related general-formula paper is not claimed. Independent audit: not performed.
