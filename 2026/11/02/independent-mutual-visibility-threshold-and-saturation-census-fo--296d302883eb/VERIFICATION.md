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

# Verification of independent mutual-visibility threshold

The supplied `verify_independent_mv.cpp` uses the original graph adjacency to test whether a chosen independent set is mutually visible. It enumerates every potentially feasible choice with at most one selected vertex per path layer and at most two per clique color. The latter restrictions are proved necessary in RESULT.md. For each candidate of size at least the asserted optimum, and for each selected pair, it runs BFS in the graph after deleting all other selected vertices. The pair is visible if and only if this restricted BFS distance equals the original product distance. Thus the finite tests do not reuse the analytic two-block criterion from the proof.

Compile and run:

```
c++ -O3 -std=c++17 verify_independent_mv.cpp -o verify_independent_mv
./verify_independent_mv
```

The recorded `verifier_output.txt` gives all tested parameter cases: \(m\in\{2,3,4\}\), \(2\le L\le2m+3\). The program verifies that the largest cardinality equals the claimed formula, checks that no larger candidate succeeds, and for each \(L\ge2m+1\) in this range checks that the exact number of size-\(2m\) sets is \((m!)^2\binom{L-1}{2m}\). The last line is `VERIFY_OK` only if all those comparisons hold.

**Scope:** these are exhaustive finite enumerations for the specified small graph instances, not a proof for all dimensions. The infinite theorem is established by Steps 1--6 of RESULT.md. Geodesic normalization and endpoint cases \(m=2\), \(L=2\), \(L=2m-1\), \(L=2m\), \(L=2m+1\) are covered in that proof. Independent external mathematical review has not occurred.
