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
# Verification

Run `python3 verify.py`.

The verifier uses only the Python standard library and performs complete finite checks:

1. Generate all \(90\) rank assignments with multiplicities \((2,2,2)\).
2. Generate all \(8\) representative permutations for every rank assignment.
3. Compute every defining representative-class Ulam distance twice: once by dynamic-programming LCS and once by an independent relative-permutation LIS algorithm; require the full matrices to agree.
4. Build the minimum-distance-\(3\) compatibility graph.
5. Enumerate maximum cliques with exact Bron--Kerbosch search.
6. Independently prove existence of a five-clique and nonexistence of a six-clique with fixed-size backtracking.
7. Independently regenerate every five-clique by nested adjacency intersections and require the result to equal the \(72\)-maximum census.
8. Recompute every internal distance and require all maxima to be equidistant at distance \(3\).
9. Independently enumerate all perfect matchings and all \(1\)-factorizations of \(K_6\), then match every optimum to exactly one factorization and verify exactly \(12\) optima per factorization.
10. Apply all \(720\) cell-label permutations and reproduce the single \(72\)-element optimum orbit and stabilizer order \(10\).

The replayed terminal line is:

`VERIFY_OK maximum=5 labeled_maxima=72 equidistant=true factorizations=6 optima_per_factorization=12 S6_orbits=1 orbit_size=72 stabilizer=10`

The verification is exhaustive for the stated finite domain and does not establish claims outside it.
