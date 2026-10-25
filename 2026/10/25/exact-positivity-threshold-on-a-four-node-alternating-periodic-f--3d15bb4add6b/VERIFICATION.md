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

The nodal transition is defined by \(P_\tau=(M+\tau K)^{-1}M\), with the assembled matrices given in `RESULT.md`. The common denominator is positive for all \(a,b>0\) and \(\tau\ge0\). The opposite-node entries are governed by the strictly increasing polynomial \(q(\tau)=72\tau^2+12ab\tau-ab(a+b)^2\), whose unique positive root is the exact threshold. `verify.py` checks the displayed identities using exact rational arithmetic for representative parameter values. These finite checks are supplementary; the proof in `RESULT.md` establishes the universal claim. The scope is limited to four periodic nodes with alternating edge lengths. The closest 2015 heat-equation article's full text could not be retrieved, and independent audit has not been performed.
