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

The mathematical proof is exact and does not depend on finite computation. The packaged checker performs three independent regression checks using exact arithmetic only:

1. It verifies the normalized determinant/geometric-sum identity as an identity in \(\mathbb Z[u,v]\) for every \(2\le m\le60\).
2. It checks the equivalence between the two-gcd criterion and uniform distribution over every divisor for all \(44,551\) pairs with \(3\le N\le300\) and \(2\le m<N\).
3. For all failing cases through \(N=150\), it constructs explicit three-column subgroup witnesses and verifies the exact row-alias congruences, covering \(4,654\) cases.

Actual replay output from `verify_three_row_family.py`:

`IDENTITY_OK m=2..60`

`UNIFORMITY_OK pairs=44551`

`WITNESS_OK cases=4654`

`VERIFY_OK`

Limit: these finite sweeps are regression tests and do not certify the infinite theorem by enumeration. The infinite statement is established by the determinant, conjugation, and geometric-sum argument in `RESULT.md`.
