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

# Reproducibility checks

Run `python3 verify.py` with ordinary Python 3. The program uses only the standard library and exactly represents expectations as rational numbers. It reconstructs the conditional-gap Dirichlet polynomial moments, enumerates all matchings of up to seven chords, checks means, variances, and mixed covariance, separately enumerates labeled matching pair events to check mixed indicator independence, and confirms the polynomial identities for \(2\le n<200\). The source checked at review returned:

```
PASS: 652 exact assertions, matchings exhaustively enumerated through n=7.
```

The analytical central limit theorem is not established by this finite enumeration; it follows from the independent-chord model, the bounded nondegenerate first Hoeffding projection with covariance \(I_2/45\), the degeneracy variance estimate \(O(n^2)\), and the standard multivariate central limit and Slutsky theorems. No independent audit or external proof certification has occurred.
