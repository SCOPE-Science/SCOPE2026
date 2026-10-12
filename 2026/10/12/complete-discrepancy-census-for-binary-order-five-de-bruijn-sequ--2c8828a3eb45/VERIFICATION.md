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

Run `python3 verify.py` beside `certificate.json`.

Engine A exhausts Eulerian cycles in the binary de Bruijn graph \(B(2,4)\), rooted at the unique edge \(\mathtt{00000}\). Engine B independently grows binary words from \(\mathtt{00000}\) while forbidding repeated length-\(5\) factors and checks circular closure. The two complete cycle sets must agree.

For every cycle, one discrepancy routine uses the range of the signed prefix walk and a second routine scans every circular factor explicitly. Their values must agree object by object.

The verifier checks the total \(2048\), the complete histogram \(5:224\), \(6:688\), \(7:912\), \(8:224\), the \(224\)-cycle minimum-layer digest, and the full list of \(60\) complement/reversal orbit representatives and sizes.

Independent audit has not been performed.
