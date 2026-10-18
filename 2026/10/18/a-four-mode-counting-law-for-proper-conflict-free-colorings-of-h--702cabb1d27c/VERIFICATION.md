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

Run `python3 verify_sunlet.py` from the directory containing the file. The program uses the Python standard library; `verification_output.txt` is its actual recorded output. It tests all thirty pairs with \(3\le q\le7\) and \(1\le a\le6\) for equality of direct and coefficient-extraction local weights; all 96 triples with \(3\le q\le6\), \(1\le a\le4\), \(3\le n\le8\) for trace-versus-recurrence equality; and 27 core-coloring enumerations with \(3\le q\le5\), \(1\le a\le3\), \(3\le n\le5\). Ten further direct full-graph cases evaluate the open-neighborhood PCF condition explicitly, over 1,496,305 ambient assignments. No numerical tolerance is used. These checks are finite and do not establish the general theorem without the proof. The general step is the invariant subspace decomposition in `RESULT.md`.
