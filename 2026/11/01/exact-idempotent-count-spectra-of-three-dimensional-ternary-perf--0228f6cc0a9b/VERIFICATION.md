---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For F3 every nonzero coordinate has square one; for any subset S of three basis positions the idempotent equation forces x_j=sum_{i∈S}w_ij. Checking exactly the support constraint bijects nonempty supports with nonzero idempotents. Exhaustive finite domain contains 3^9=19683 matrices and 11232 invertible. Independently evaluated all 27 candidate vectors on each invertible W and independently BFS-tested strong connectivity: labeled histogram 3600,5056,1800,600,120,48,0,8 (k=0..7) and simple 3408,3256,768,72; independently partitioned invertible matrices into all orbits under the exact 48-element S3×(F3*)^3 action, yielding class spectra 78,111,40,15,3,1,0,1 and simple 74,73,17,2. The source census.py separately checks stabilizers and direct orbits, and 249 is attributed to known work. Finite enumeration is complete for the specified field/dimension; not an extrapolation.

## originality

PASS

Wei–Zou 2023 full text Theorem 5.1 gives the unstratified 249-orbit total and monomial action; those are prior and excluded from novelty. Kaygorodov–Martín González–Viruel 2026 full survey gives mean one and open distributions, not the ternary finite histogram. Hu 2026 complex full-support study is not the same F3 invariant. Exhaustive exact table supplies unknown finer natural strata but unindexed tables may conceal it.

## value

PASS

A complete intrinsic class-by-class and labeled distribution for a natural small odd prime field addresses a specific random-idempotent counting question; absent value six, simple threshold three, and exact zero-idempotent frequency are not deducible from the mean-one law or total orbit count. Finite dimension-specific classification is a worthwhile reusable exact benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
