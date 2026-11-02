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

# Verification of the finite S5 depth census

The proof supplies the complete universal argument: all-event common-knowledge unfolding depth equals maximum connected-component graph diameter; attaining the \(n-1\) bound forces an induced spanning path; equivalence-class transitivity restricts each agent to a matching on this path; and a bijection with consecutive-disjoint nonempty agent subsets yields the exact recurrence.

Run `python checker.py` (Python standard library only). The checker independently generates each set partition as an equivalence relation, forms all ordered tuples and computes the resulting graph diameter directly. It compares these exhaustive counts to a separate implementation of the combinatorial recurrence. Cases covered: one agent on two through five worlds; two agents on two through six; three agents on two through five. The checker also checks every extremal graph has precisely \(n-1\) undirected edges when \(n\ge3\). It outputs `ALL_CHECKS_OK` on success. Finite testing is corroborative, not an infinite-size certificate.

No third-party paper is reproduced. The checked object is a classical finite S5 frame; nontrivial intuitionistic-order frames, complete depth distributions, and historical priority are outside this verification. Independent audit is not performed.
