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

The full symbolic proof is in `RESULT.md`; the executable `verify.py` performs independent bounded checks on additive-semigroup membership rather than treating the classification predicate as its own oracle. Execute `python3 verify.py` to check every admissible multiplicity-five Kunz vector of genus at most 60, including all 32,065 such vectors, direct pseudo-Frobenius tests and direct minimal-generator tests. Exactly 88 of these semigroups satisfy the consecutive-pseudo-Frobenius criterion; 57 have embedding dimension four. Independent arithmetic interval counts were checked for every parameter sum from 2 through 1000. The program prints `VERIFY_OK` when every assertion succeeds. Numerical enumeration is not claimed as an exhaustive proof for arbitrary genus, and the published classification is not independently audited.
