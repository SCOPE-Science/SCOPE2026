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

# Reproducibility and scope

Execute `python3 check_idrank.py` with Python 3 standard library. The checker independently constructs all partitions of \(2n\) points via restricted-growth tuples, filters full-domain rank-\(n-1\) diagrams, composes diagrams by gluing rows, classifies idempotents, and computes the closure of the proposed minimal generating family within the maximal proper rank layer. It verifies the full rank layer for \(n=3,4,5\) and the \(n=2\) right-zero case. The expected completion message is `CHECKER_OK`.

Recorded exact layer sizes are \(36,360,3600\) for \(n=3,4,5\), respectively; exact numbers of rank-\(n-1\) idempotents are \(9,18,30\); generator counts are \(6,12,20\). This finite computation cannot establish the theorem at arbitrary \(n\). The general proof uses the rank-preserving diagram lemma, the established transformation-tournament generating theorem, and the published singular-partition factorization. Independent audit: not performed.
