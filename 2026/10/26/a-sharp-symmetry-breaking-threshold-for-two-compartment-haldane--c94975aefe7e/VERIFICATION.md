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

# Reproducible verification

Run `python3 verify_haldane.py` using Python 3 and only its standard library. The program checks 1,600 pseudorandom parameter configurations at the fixed seed 3511593, comparing the original two-term kinetic formula with the independent product-coordinate expression at 161 allocations per configuration, and checking every sample against the theorem's proposed global optimum. It also compares finite-difference and exact derivative formulas at nine randomly chosen product values per configuration (where the finite difference lies within the feasible interval). The observed result was:

```
PASS: 1,600 reproducible parameter instances; 257,600 objective comparisons;
      14,400 derivative tests; exact b=2, N=6 case; onset and large-budget asymptotics.
```

The exact rational example \(b=2,N=6\) is checked against \(x_-=3-4/\sqrt5\), optimum \(25/64\), and equal-allocation value \(3/8\). Onset and large-budget approximations are checked at five distinct inhibition parameters.

The classification of *all* positive parameters follows analytically from the strictly decreasing derivative numerator and its factored endpoint sign in `RESULT.md`, not from the finite samples. Float roundoff and finite numerical grids are not certificates of universal positivity, uniqueness, or historical novelty. The comparisons do not simulate time-dependent microbial dynamics.
