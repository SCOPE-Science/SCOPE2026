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

The proof establishes the theorem for all \(q\ge2\) and all \(n\ge1\). The accompanying verifier performs independent finite checks rather than serving as an infinite certificate.

`verify.py` constructs forward children directly from every source by choosing an original symbol and a later insertion point. It separately reconstructs candidate parents from a received word by deletion, then checks equality with the run formula. For \(2\le q\le4\) and \(1\le n\le5\), it exhaustively checks every received word, the maximum inverse degree, the stated equality characterization where applicable, and the total edge formula. It also checks alternating sharpness witnesses and the closed formula on a larger parameter grid.

Limits: finite enumeration does not establish the all-parameter theorem by itself. The mathematical proof in `RESULT.md` supplies the general argument. The verification covers only the exact one-symbol operation specified there.
