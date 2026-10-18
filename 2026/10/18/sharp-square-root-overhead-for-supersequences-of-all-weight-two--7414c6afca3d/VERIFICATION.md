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

# Computational verification

Reproduce with `python checker.py` using Python 3 standard library. The script exhaustively examines every candidate host of each length up to the first successful length for target lengths \(3\)–\(11\), using the definition of a scattered subsequence directly. It checks all weight-two target words in each constructed host for lengths \(3\)–\(160\), and validates disjointness of the selected counting intervals for \(N\le160\). The expected terminal line is `PASS: exact n=3..11, universal construction n=3..160, window disjointness.`

The lower-bound and constructive upper-bound proofs in RESULT.md establish the theorem for all \(n\ge3\). These finite tests do not assert an exhaustive search for unbounded lengths, nor do they independently certify originality.
