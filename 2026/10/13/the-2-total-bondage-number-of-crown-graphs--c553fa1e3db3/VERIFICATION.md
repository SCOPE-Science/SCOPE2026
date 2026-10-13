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

The theorem is established analytically in `RESULT.md`. The finite checker is corroborative only.

`verify.py` performs three independent checks:

1. It exhausts every edge-deletion set below \(2n-3\) for \(n=3,4\) that leaves no isolated vertices and confirms that the total domination number remains \(4\).
2. It exhausts all labeled proper set families in the pair-cover lemma for \(n=3,4\) and confirms the sharp lower bound \(2n-3\).
3. It checks the explicit \(2n-3\)-edge construction for every \(3\le n\le40\), including absence of isolated vertices, failure of every shore pair to dominate, and explicit dominating triples on both shores.

The recorded output is:

`ALL CHECKS PASSED`

The finite ranges are not asserted to prove the infinite statement. No independent audit or independent validation has been performed.
