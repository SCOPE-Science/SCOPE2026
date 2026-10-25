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

# Verification and scope

Execute `python3 verify.py` using Python 3.10 or later; no additional libraries or nonlocal files are needed. The actual run completed successfully with 11 exact rational checks, three short-interval reverse-order checks at refined RK4 resolutions, 600 seeded randomized two-treatment comparisons and 60 three-treatment six-permutation comparisons. The exact checks include the sharp \(bK^2=27\) derivative bound and the suppressive \(b=54\) witness with coefficient \(10/441\). The numerical RK4 checks are not interval-arithmetic certificates and cannot prove any all-parameter assertion. The general theorem is proved in `RESULT.md` by an order-preserving coordinate, scalar comparison and Taylor expansion. An independent mathematical audit has not been performed. The inaccessible full text of Kar and Matsuda (2007) prevents a complete originality comparison with that paper.
