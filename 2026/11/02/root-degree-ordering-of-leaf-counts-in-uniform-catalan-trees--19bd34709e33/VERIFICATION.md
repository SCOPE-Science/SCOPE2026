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

The theorem follows from Lagrange inversion, explicit common-support row-ratios, and exact moment extraction. For nonstar adjacent root degrees the row ratio is strictly increasing with the leaf count. Across nonadjacent degrees the successive ratio of row likelihood ratios is \((k-d+1)/(k-e+1)>1\) wherever both are defined. Ordered support intervals and the terminal star row complete all TP2 boundary cases.

`verify.py` independently enumerates plane-tree shapes for \(m=2,\ldots,9\) edges and verifies joint cells, moments, and minors. It uses rational arithmetic for larger-size checks through \(m=100\). The command `python verify.py` passed 15,911 assertions. These finite tests do not establish statements for all sizes; the written proof does.

The listed prior enumerations are substantive historical context; no independent mathematical audit and no exhaustive priority verification have occurred.
