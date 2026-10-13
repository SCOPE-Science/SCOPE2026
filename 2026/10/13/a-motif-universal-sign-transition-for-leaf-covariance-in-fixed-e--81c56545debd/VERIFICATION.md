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

Run `python3 check.py` from the same directory as this document with Python 3 and no additional packages. The code constructs each unlabeled motif's distinct labeled embeddings, checks its automorphism multiplicity, enumerates all simple labeled host graphs for \(n=4,5,6\), groups graphs by edge count, and compares \(163\) exact-rational observed covariance values to the proved formula. It then checks the sign classification for \(867049\) exact-rational cells (including both \(R>1\) and \(R\le1\)) and checks the exact triangle integer threshold through \(n=1000\). The same command completed with `PASS` outputs.

This verification does not exhaust infinitely many graphs or motif types, and it does not certify literature novelty. Those limits are addressed by the mathematical proof and by the separate literature-comparison review.
