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

# Verification procedure
The accompanying `verify.cpp` is a standalone C++17 finite enumerator with no libraries beyond the standard library. Its first traversal uses a Gray-code one-bit update; its second uses an independently structured binary recursion. Both enumerate all \(134217728\) spin subsets, group them by cardinality, compute the exact cut maximum and its number of optimizers, and check the totals against \(\binom{27}{k}\). They agree for every one of the \(28\) sectors.

The checker reconstructs the simple graph from the three geometric line classes, verifies \(27\) vertices, \(216\) edges and parameters \((27,16,10,8)\), evaluates explicit optimal-subset witnesses, compares them with the eigenvalue-derived bound, checks spin-reversal symmetry, tests direct edge sums during enumeration, and verifies the zero-field and critical-field multiplicities.

Run `c++ -std=c++17 -O2 -Wall -Wextra -pedantic verify.cpp -o verify && ./verify`. A successful execution begins with `VERIFY_OK vertices=27 edges=216 subsets_per_graph=134217728 independent_enumerations=2`, and reports zero-field multiplicity `1037376` and critical multiplicities `630444`, `138000`, `10035`, `208` at the four positive field thresholds. All computations use exact integers.

# Limits
This program certifies a finite exhaustive calculation and checks stated witnesses; the inequality for all subsets is proved algebraically in `RESULT.md`. Two agreement paths do not constitute an independent external audit. There is no claim about positive-temperature or infinite-lattice behavior.
