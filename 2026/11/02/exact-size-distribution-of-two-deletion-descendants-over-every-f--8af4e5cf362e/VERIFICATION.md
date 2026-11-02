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

The complete proof of the unconditional histogram identity and exact moments is in `RESULT.md`; it uses unique leftmost subsequence embeddings and direct enumeration of difference-run patterns. `check.py` is a standalone standard-library Python 3 verifier. Run `python3 check.py` and compare with `check_output.txt`.

The program exhaustively generated each possible labeled word in 33 parameter cases (281,783 words) and compared the independently enumerated distinct deletion outputs to the local formula. It then compared entire histograms, mean and variance, and carried out 429 exact enumerator-derived moment checks for \(2\le q\le12\) and \(2\le n\le40\). All passed on the actual included program. The symbolic proof is required for arbitrary parameters; finite enumeration cannot certify the infinite statement. No third-party full papers, external validation records, or independent mathematical audits are included.
