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

Run `python3 verify.py` with Python 3 and its standard library. The verifier constructs all \(2^{n^2}\) binary relations for each \(1\le n\le4\). It directly evaluates the inclusion violation count from row and column masks, obtains the unweighted joint histogram by number of defects and retained pairs, and compares exact rational probabilities to the coefficient formula in the theorem. It also checks the full factorial-moment identities and the pairwise covariance bound in small cases.

Observed final output:

```
n= 1 teams= 2 unweighted_defect_histogram= [2, 0]
n= 2 teams= 16 unweighted_defect_histogram= [12, 4, 0]
n= 3 teams= 512 unweighted_defect_histogram= [374, 132, 6, 0]
n= 4 teams= 65536 unweighted_defect_histogram= [52056, 12632, 840, 8, 0]
VERIFY_OK teams 66066 rational_parameter_cases 20 exact_probability_coefficients 70
```

Finite enumeration checks coefficients for \(p\in\{0,1/3,1/2,2/3,1\}\). It does not test all real probabilities directly (the closed-form identities do), and finite samples do not prove limits as \(n\to\infty\). The infinite claims rest on the exact intersection factorization, the negative pairwise covariance and factorial-moment argument given in `RESULT.md`. No independent validation has been performed.
