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

# Verification record

The scientific argument appears in `RESULT.md` and the self-contained exact-arithmetic code in `checker.py`. Execution on the embedded code gave:

```
VERIFY_OK
units 12 signed_rank_one 18 total 31
multiplications_checked 961
maximum_signed_incidence_projective_pair_count 9
actual_support_pairings [[1, 0, 1], [0, 1, 1], [1, -1, 0]]
```

The checker computes the closure of the explicitly generated unit group, all signed rank-one outer products and all ordered products. It also enumerates the finite signed-projective patterns via exact rational solutions, independently supporting the combinatorial lemma. The checker is not an exhaustive enumeration of all finite matrix semigroups. The global upper bound is proved mathematically from a completely \(0\)-simple minimal ideal, the rational scalar-group constraint, and the planar finite-group constraint. These structural facts and the full explicit example are explained in `RESULT.md`.

The inspected 2026 primary literature provides the general bound and its minimal-ideal framework, rather than a known exact dimension-two value. Historical priority is not independently established. Independent audit has not been performed.
