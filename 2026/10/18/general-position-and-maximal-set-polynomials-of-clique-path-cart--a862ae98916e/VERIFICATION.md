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

# Computational verification

Compile the standalone C++17 program with `g++ -O3 -std=c++17 -o verify verify.cpp && ./verify` from the same directory. Its output must match `verification_output.txt`.

The program constructs graph adjacency directly, uses breadth-first search to compute shortest-path distances, and marks collinear triples using distance equalities. It then enumerates every vertex subset for 29 graph instances with factor sizes between 1 and 8 and at most 19 vertices, testing 491,210 subsets. For every instance it independently checks the structural feasibility criterion and all coefficients of the all-set polynomial. For seven instances satisfying \(m,n\ge3\), it also checks the exact count of every inclusion-maximal set against the maximal-set polynomial. It reports `VERIFICATION_OK graph_cases=29 subsets_tested=491210 feasible_subsets=4761 maximal_pair_cases=7`.

The unrestricted formulas, classification, and nonpurity conclusion are proved combinatorially in `RESULT.md`. A finite exhaustive computation alone would not prove them. No independent external scientific audit has been performed.
