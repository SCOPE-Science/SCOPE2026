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

# Verification notes

Run `python3 verify.py` using Python 3 standard library. It reconstructs each iterate independently for \(2\le m\le13\), counts missing strings using the next-position deterministic subsequence automaton, checks absence at length \(K_m\), checks the predicted exact SAS count and explicit candidates, and exhaustively enumerates all SAS for \(m\le5\). The twelve tested values are \(m=2,\ldots,13\). The end marker is `VERIFY_OK`. This finite computation does not establish the infinite statement; the proof in RESULT.md does. No external independent audit was performed.
