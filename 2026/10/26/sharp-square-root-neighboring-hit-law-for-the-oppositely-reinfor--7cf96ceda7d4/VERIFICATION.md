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

`VERIFY.py` performs finite-horizon rational checks of the exact urn-to-elephant time-space shift and Eulerian-number one-time marginals. Invoke `python VERIFY.py` with standard Python 3, no external dependencies. Confirmed the program exits successfully and prints a PASS status.

The infinite-time bounds rely on Bertoin (2022), Theorem 4.1, with its stated uniformity in \(k\le bn\), \(p=0\) factors \(a_{k+1}=k\) and \(A_{k+n}-A_k=\sum_{i=k+1}^{k+n}(i-1)^2\). The separate short-excursion comparison with a symmetric walk provides the needed integrable majorant at small \(n/k\). A geometric excursion count and the growing return epochs complete the analytical proof. These statements require more than finite enumeration and have no machine-verified infinite certificate. Independent scientific audit has not been performed.
