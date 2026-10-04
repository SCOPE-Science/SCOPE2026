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
The exact verifier checks all \(75582\) length-eight and \(167960\) length-nine residue multisets modulo \(16\). It compares direct four-position enumeration with an independent subset-size/residue dynamic program; the methods agree everywhere.

Expected output begins `VERIFY_OK` and reports `bad8=160`, `bad9=0`, `orbits=7`, with orbit sizes `[32, 32, 16, 8, 32, 32, 8]`.

It also rebuilds the affine action and verifies that the seven orbits cover all \(160\) extremals. This computation proves only the finite \(n=4\) claim.
