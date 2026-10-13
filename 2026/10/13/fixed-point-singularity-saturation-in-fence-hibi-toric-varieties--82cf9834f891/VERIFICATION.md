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
The companion checker constructs the alternating fence directly.

For \(1\le n\le9\) it exhaustively enumerates all permutations and all subsets. It verifies that the number of linear extensions is the Euler zigzag number \(E_n\) and that the number of order ideals is \(F_{n+2}^{\mathrm{Fib}}\).

For \(1\le n\le16\) it enumerates all independent sets of the path, constructs the active facet normals at the corresponding chain-polytope vertices, and checks that the smooth torus fixed points are exactly all vertices for \(n\le2\) and exactly \(\varnothing,\{1\},\{n\},\{1,n\}\) for \(n\ge3\). The four stable families have determinant of absolute value one; every other vertex for \(n\ge3\) has more than \(n\) active facets.

Finally, the checker generates Euler zigzag and Fibonacci numbers through \(n=100\), verifies the strict crossover between \(n=4\) and \(n=5\), and checks the recurrence inequality used in the infinite proof.

The exhaustive computations are finite regression evidence only. The all-parameter proof is in `RESULT.md`.
