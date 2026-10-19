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

The general statement is proved by normalizing a full-support perfect evolution-algebra structure matrix, deriving the full-support invertible-matrix count, determining fixed points for the three subgroup types of \(S_3\), and dividing the exact stabilizer strata by orbit size. This is a proof for all prime powers, not an inference from finite tests.

Execute `python3 artifacts/check_automorphism_profile.py`. The program enumerates normalized matrices and their six permutation stabilizers over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7,\mathbb F_8,\mathbb F_9\), using explicit finite-field quotient arithmetic. It returned `ALL_EXACT_CHECKS_PASSED 7 finite fields` on the reviewed source. All divisions by orbit size are verified to produce integers.

The source program is self-contained and uses only the standard Python library. Finite-field tests do not establish infinite-family correctness. Literature comparisons cannot rule out every unindexed or older equivalent formulation. Independent external validation has not been performed.
