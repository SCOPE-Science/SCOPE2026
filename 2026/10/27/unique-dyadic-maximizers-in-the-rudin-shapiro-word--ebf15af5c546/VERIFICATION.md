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

The proof derives the block-sum recurrence and the \(G_k\) matrices by induction, then derives the unique legal maximizing pair and the unique maximizing offset. The bundled `verification.py` was executed from its package path and passed its finite checks for \(2\le k\le20\). This finite check is supplementary and does not replace the induction proof. No independent audit or external validation was performed. The older 1985 paper's full text could not be obtained in this run, and this is retained as a literature risk.
