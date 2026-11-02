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
# Verification details

`python3 verify.py` runs with the Python 3 standard library, using `fractions.Fraction` for exact rational Gauss–Jordan inversion of the grounded Laplacian assembled directly from the original graph. The verified output is:

```text
FINITE_CHECKS_OK spectral=154,optimizer_cases=35,subsets=399
```

The script compares the analytical inverse-square formula with direct matrix inversion for every allocation count with \(2\le m\le8\) and \(1\le k\le m\), checks no mixed allocation minimizes in those test cases and checks the sign of the cubic against the two pure allocations. It also exhaustively tests 399 actual leader subsets on smaller graphs, not just symmetry representatives. The edge case in which one follower class is empty is included.

An independent symbolic rational simplification establishes that the difference of the pure-type costs equals the cubic divided by \(k^2m^2(m+1)^2\); the public proof reproduces the corresponding algebra directly. The asymptotic expansion is proved analytically from the cubic. Computation does not certify the theorem outside the tested finite range. Independent external mathematical audit has not been performed.
