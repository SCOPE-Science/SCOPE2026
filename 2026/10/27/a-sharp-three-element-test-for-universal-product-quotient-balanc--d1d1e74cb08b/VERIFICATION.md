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

The theorem is proved by a two-point calculation, quaternion subgroup construction, finite abelian primary decomposition, and an all-subsets check for four exceptional group types. No group-enumeration experiment is used to infer the universal group-theoretic conclusion.

The enclosed Python 3 standard-library program `verify.py` can be run as `python3 verify.py`. It evaluates both sets directly, enumerates small example groups, searches subsets of sizes at most three, and reproduces exact cardinalities for the explicit abelian and quaternion witnesses. The program was executed and printed `VERIFY_OK`.

The deterministic computations cover cyclic groups through order sixteen, selected products, elementary abelian two-groups through rank six, dihedral groups through order twenty-four, and the quaternion group. Entire power sets are exhausted only for groups explicitly marked for this in the verifier; no claim of exhaustively testing all finite groups is made.

Limitations: Bibliographic searches do not prove novelty. A full-text check of one generalized-dihedral article was unavailable; its publicly available abstract was compared. Independent audit is not performed.
