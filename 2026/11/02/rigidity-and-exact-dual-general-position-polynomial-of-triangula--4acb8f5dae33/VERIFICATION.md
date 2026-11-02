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

Compile and run `dual_triangular_verify.cpp` using a C++17 compiler, for example:

```sh
g++ -O3 -std=c++17 dual_triangular_verify.cpp -o dual_triangular_verify
./dual_triangular_verify
```

The checker independently builds \(T_n=L(K_n)\) from pairs of root vertices, constructs adjacency, computes every graph distance by Floyd–Warshall, and scans all \(2^{\binom n2}\) candidate subsets for \(3\le n\le7\). A shortest path is identified by the exact distance equality, and a candidate is rejected whenever a selected internal vertex lies on a shortest path with both endpoints selected or both endpoints unselected. Every survivor is compared to the explicit root-star and four-root-triangle classification. This checks all coefficients, not only extrema.

Observed output when the packaged source was compiled and executed:

```text
n=3 V=3 candidate_subsets=8 admissible=8 coefficient_by_size=0:1 1:3 2:3 3:1
n=4 V=6 candidate_subsets=64 admissible=9 coefficient_by_size=0:1 3:8
n=5 V=10 candidate_subsets=1024 admissible=6 coefficient_by_size=0:1 4:5
n=6 V=15 candidate_subsets=32768 admissible=7 coefficient_by_size=0:1 5:6
n=7 V=21 candidate_subsets=2097152 admissible=8 coefficient_by_size=0:1 6:7
VERIFY_OK
```

The finite checks do not establish the infinite theorem. Its proof uses the exact clique-number and maximum-clique structure of \(K_{n-2}\square K_2\) and the forced-root-star argument in `RESULT.md`. The comparison with ordinary general position uses the published Theorem 4.4 of arXiv:1903.04286, not computational extrapolation. No independent mathematical audit has been conducted.
