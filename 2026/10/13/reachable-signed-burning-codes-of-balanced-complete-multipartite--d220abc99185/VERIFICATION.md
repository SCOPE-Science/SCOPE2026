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

The proof works for every finite connected complete multipartite graph with at least three nonempty parts and any balanced edge signature; it is independent of the finite tests. The exhaustive verifier runs all 99 ordered part-size profiles with 3–7 vertices. For each graph, it explores the legally reachable spread-then-ignite state space and compares terminal colorings to the claimed signed code under all 4,692 balanced gauge signings. It separately checks the exact Hamming covering-radius formula on the all-positive code and computes all 4,692 individual plurality values. All comparisons passed, with 49,320 terminal words considered across signatures.

Reproduce in Python 3 with `python verify_balanced_multipartite.py` from this folder, and compare the displayed summary with `verification_output.txt`. The finite tests cannot certify an infinite theorem or originality. Their role is to challenge the inductive structural proof and each small parity/boundary case. The independent scientific audit is not performed.
