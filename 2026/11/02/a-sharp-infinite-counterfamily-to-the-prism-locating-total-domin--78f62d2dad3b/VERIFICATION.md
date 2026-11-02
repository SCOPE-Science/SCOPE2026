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

Run `python3 verify_prism.py` with Python 3 and no third-party packages.

The verifier constructs the ten distinct length-five cyclic factors of \(B\), \(BQ\), and \(BQQ\), checks total domination and all eligible collision pairs in each, independently tests locating-total domination on the actual complete prism graph for \(n=8,13,\ldots,63\), and exhaustively tests all smaller initial-set sizes at \(n=8\). Its printed marker is `CERTIFICATE_OK` with factor count 10, local eligible-pair count 12, and the covered finite orders.

The crucial all-size step is mathematical: a five-column factor of \(BQ^t\) can involve at most one block interface since block lengths are eight and five; the interface types occur among \(B\), \(BQ\), and \(BQQ\). The local lemma proves no other pair of unselected vertices can share a nonempty fingerprint. The cubic counting lower bound is independent of computation. Finite checks are corroboration and do not establish infinite correctness on their own.

This is not independent validation. Publication priority against unindexed equivalent research remains uncertain.
