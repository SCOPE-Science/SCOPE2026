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

The coordinate model uses the \(k[t]\)-linear endomorphism algebra of \(k[t]/t^n\oplus k[t]/t^2\) for \(n\ge4\). The square equations are derived explicitly in `RESULT.md`; the two parity reductions give the claimed point counts and component decompositions by elementary algebraic-geometry arguments.

Run `python3 check_n2_squarezero.py`. Its coordinate enumeration checks every scalar block parameter for seven cases with \(q=2,3\), and its second matrix construction checks squaring and commutation in ordinary matrices for three cases. Expected markers are `NONHOOK_SQUARE_ZERO_COUNTS_OK` and `MATRIX_MODEL_CROSSCHECK_OK`.

No finite enumeration proves the formula for all finite fields. The universal conclusion rests on the symbolic equations and valuation analysis. No independent expert check, proof-assistant certification, or check of the potentially nonreduced defining scheme is claimed.
