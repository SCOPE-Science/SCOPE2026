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

# Reproduction and scope

The self-contained checker `check_matching.py` is a Python 3 program using only standard-library `math` and `itertools`. Run it with `python3 check_matching.py`. In the recorded execution it printed:

`PASS: 120 curvature/assignment/crossover/gain configurations and asymptotic comparison`

The tests include \(r\in\{1,2,5,10\}\), \(\sigma\in\{0.4,1,2.3\}\), exhaustive permutations in dimensions 2–4, finite-difference crossover bisection, the exact curvature-zero formula, and a dimensionless moderate-distance check of the asymptotic gain ratio. The implementation evaluates the Gaussian absolute-moment excess over distance using an `erfc`-based tail formula to avoid catastrophic cancellation at large distances.

The mathematical proof independently establishes the all-\(n\), all-\(\sigma>0\), all-integer-\(r\ge1\) assignment results under the stated geometry. Computations verify representative instances but are not exhaustive, and do not certify the global historical novelty of the theorem or independence of its review.
