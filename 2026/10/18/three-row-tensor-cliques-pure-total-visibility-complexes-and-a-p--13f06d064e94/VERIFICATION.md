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

# Reproducible mathematical checks

The program `check_total_visibility_K3Kn.cpp` builds the direct-product adjacency from scratch, determines each pair's common neighbors, and for every \(n=3,4,5,6\) enumerates all subsets. It tests the required unobstructed common neighbor for **every** nonadjacent pair; it does not call the row-support criterion to decide feasibility. It independently builds polynomial coefficients and checks all inclusion-maximal configurations. All checks passed for \(299520\) examined subsets (\(200653\) valid sets) with \(3576\) observed facets in aggregate. Output is supplied in `verification_output.txt`.

Build with a C++17 compiler:

```sh
c++ -std=c++17 -O2 -Wall -Wextra -pedantic check_total_visibility_K3Kn.cpp -o check_total_visibility_K3Kn
./check_total_visibility_K3Kn
```

The code is a finite experiment, not an infinite certificate. The exact all-size formula and facet result follow from common-neighbor geometry and a disjoint count. The probability limit follows from analytic binomial-to-Poisson convergence and explicit bounds, not a Monte Carlo run. No independent audit has been performed.
