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

# Reproducibility

Execute `python3 verify_occupancy.py` in a directory containing the supplied standalone script. The script uses only the standard library and has no external input.

Exact enumeration traverses the full finite assignment spaces for \((m,n)=(3,4),(3,5),(3,6),(4,8),(5,6)\), computing \(\mathbb E[Y_1]\), \(\mathbb E[Y_4]\), \(\mathbb E[Y_1Y_4]\) and their covariance as rational numbers and comparing each with independently calculated closed-form expressions.

Exact-rational checks test the consecutive quotient of the normalized covariance ratio across \(3116\) sample-size pairs for \(3\le m\le40\); they confirm the unique peak at \(n=2m\), the contiguous positive integer interval, and strict positivity at its peak. Numerical checks at three increasing box counts and five rescaled offsets check convergence toward \(\frac43e^{-4}(1-z^2/2)\).

Observed output from the supplied checker:

```
PASS: 5 exhaustive allocations, 3116 exact-rational quotient checks, 15 numerical limit checks
m=3, positive integer ball counts 5..8
m=4, positive integer ball counts 7..10
m=5, positive integer ball counts 8..13
m=20, positive integer ball counts 35..46
m=100, positive integer ball counts 187..214
```

These finite tests and numeric limits do not prove the all-size theorem. The analytic proof is supplied in RESULT.md. Historical originality has not been independently audited; the 1964 joint-local-normality paper was not available in full text.
