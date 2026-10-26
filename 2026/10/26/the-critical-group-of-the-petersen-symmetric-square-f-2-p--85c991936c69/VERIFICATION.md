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

# Exact computational verification

`verify.py` is a standalone Python 3 program with no third-party dependencies. Run `python3 verify.py` from the extracted package. A successful execution prints `VERIFY_OK` and lists all nonunit Smith factors.

The program checks: the Kneser construction has 10 vertices and 15 edges; the two-token configuration graph has exactly 45 vertices, 120 edges, degree multiplicities 15 at four and 30 at six, and is connected; a 44-by-44 reduced Laplacian has determinant 49253533675382566432014336000 by exact fraction-free Bareiss elimination; traces of all matrix powers through 45 give the stated characteristic polynomial by Newton identities; the determinant agrees with the coefficient of the linear term through the matrix-tree theorem; reductions modulo prime powers give the stated Smith valuation profiles at primes 2, 3, 5, 7 and 19; and all factors form a divisibility chain whose product equals the determinant.

The local Smith computation uses invertible row and column permutations and additions modulo a prime power higher than the determinant valuation. The pivot chosen at each stage has the smallest remaining prime valuation, so its unit part is invertible in the appropriate quotient ring and every row/column clearing step is justified. Total valuation equals the exact determinant valuation, excluding undetected higher factors. This is an exhaustive finite arithmetic computation, not a random or heuristic check.

The package does not contain an independent external review. The computation concerns only the precisely defined finite graph, not an all-graph theorem. The literature check cannot exclude unindexed prior data.
