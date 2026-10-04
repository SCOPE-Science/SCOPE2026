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

The verifier implements two independent descriptions: the literal synchronous irreversible \(k\)-threshold process on vertices, and the weighted parking-profile criterion from the proof. It enumerates all ordered complete-multipartite profiles through order \(8\), all thresholds \(1\le k\le N\), all minimum-size subsets, and all seed-count profiles contributing to the claimed exact count.

Replay command:

`python verify.py`

Expected terminal line:

`VERIFY_OK profiles=247 subset_checks=71117 count_checks=1757 max_order=8`

The finite replay is a consistency check. It does not substitute for the infinite proof, and it does not test nonuniform thresholds.
