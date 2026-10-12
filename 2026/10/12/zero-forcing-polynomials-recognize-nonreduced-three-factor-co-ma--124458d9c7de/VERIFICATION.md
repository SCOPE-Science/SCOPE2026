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

The standalone `verify.py` artifact was read from its packaged path before replay.

It constructs the six-type Boolean blow-up with weights
\[
\lambda_1,\lambda_2,\lambda_3,
\lambda_2\lambda_3,\lambda_1\lambda_3,\lambda_1\lambda_2.
\]

Independently, it constructs the co-maximal ideal graph of products of three prime-power chain rings at the ideal level. Ideals are indexed by their chain exponents, and adjacency is computed from the condition that their coordinatewise sum is the whole product ring.

For the triples
\[
(1,1,2),\quad(1,2,2),\quad(2,2,2),
\]
every vertex subset is exhaustively tested for zero forcing. The resulting complete polynomials agree with the factorized formula, including the minimum-set coefficient.

The actual adjacency matrix is row-reduced over the rationals and has rank \(6\) in every test.

For every ordered triple
\[
1\le\lambda_1\le\lambda_2\le\lambda_3\le8
\]
other than \((1,1,1)\), the checker reconstructs the triple from the six root magnitudes using the two-smallest-roots and cube-product formula.

Finally, for the boundary profile
\[
(1,1,3),
\]
all \(64\) possible choices of at most one white representative in each type are checked directly and all force.

Exact replay output:

```text
l=(1, 1, 2): weights=[1, 1, 2, 2, 2, 1], N=9, Z=3, min_sets=8, adjacency_rank=6
l=(1, 2, 2): weights=[1, 2, 2, 4, 2, 2], N=13, Z=7, min_sets=64, adjacency_rank=6
l=(2, 2, 2): weights=[2, 2, 2, 4, 4, 4], N=18, Z=12, min_sets=512, adjacency_rank=6
RECOVERY_CENSUS_OK
ALL_64_PROFILES_FORCE_OK
VERIFY_OK
```

The exhaustive checks are finite corroboration. The arbitrary finite-ring factorization, rank equality, and reconstruction theorem are proved symbolically in `RESULT.md`.
