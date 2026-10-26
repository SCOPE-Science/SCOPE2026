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

Run `python3 verify_subdivision_old.py` next to this document with Python 3 (standard library). The test enumerates all subsets in the actual subdivision graph and verifies nonempty, pairwise distinct open-neighborhood signatures together with exactly one selected neighbor at every selected vertex. It independently enumerates perfect codes of the original graph satisfying the minimum-degree condition, builds their images and compares the complete sets of masks.

The checked cases comprise all \(75\) labeled graphs on orders \(1\)–\(4\), plus \(75\) order-five graphs selected deterministically, and cubic \(K_4\), \(K_{3,3}\), and \(Q_3\) (counts \(4\), \(0\), and \(4\)). The proof is the four-step mathematical argument in RESULT.md, and not an assertion that finite testing proves universal correctness. The complexity transfer invokes the published 1988 NP-completeness premise rather than rechecking its underlying reduction. Self-review passed; no independent audit was performed.
