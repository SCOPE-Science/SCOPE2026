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

The general class-counting theorem has a symbolic proof using cyclic vectors, zero-edge Jordan chains, and circular compositions; the finite enumeration below is **not** an infinite proof.

Run `python verify_operator_census.py` in any Python 3 environment. Standard-library only. The script independently enumerates all coordinate vectors in each tested prime field and all stated chain lengths, builds each multiplication matrix, obtains nilpotent Jordan partitions from ranks of powers, and checks the claimed exact histogram. Nonzero cyclic matrices are checked via their product parameter; their module is proved to be cyclic in the accompanying theorem.

Prime-field test ranges are \(q=2\) and \(1\le d\le8\); \(q=3\) and \(1\le d\le6\); \(q=5\) and \(1\le d\le4\); \(q=7\) and \(1\le d\le3\), using one or two coefficient choices. The independent tests total 34 cases. A separate check enumerates the idempotents in two weighted \(2\)-cycles over \(\mathbb F_7\), obtaining counts \(4\) and \(1\), and checks exact equality of their sets of multiplication matrices with multiplicity.

Only prime fields were exhaustively enumerated; arbitrary prime powers and arbitrary cycle lengths are covered by the mathematical proof rather than this script. The tests are self-review, not independent validation; independent audit remains unperformed.
