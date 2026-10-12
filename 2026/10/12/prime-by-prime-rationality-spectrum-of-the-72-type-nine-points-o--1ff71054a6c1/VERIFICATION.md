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

# Reproduction and limits

Run `python3 verify.py` with Python 3.10 or later; no third-party packages are required. The verifier uses exact integer/rational operations, a six-dimensional cyclotomic quotient with an independent cube-root coordinate, and finite-field group operations. It establishes that the published representative lies on the Fermat cubic and the published type-nine factor, and checks the claimed prime-by-prime counts for each prime \(5\le p<1100\). All observed instances agree with the four-case theorem.

The 9-division field equality also uses the explicit 72-point enumeration of Merta--Zięba, a Weil pairing and a primitive coordinate. The ring-theoretic kernel counts are checked by the written proof. The infinite assertion follows mathematically from the proof's CM argument, Frobenius determinant and Chebotarev's theorem; it is not inferred from finite enumeration. Source overlap has been reviewed, but independently certified originality or correctness is not claimed.
