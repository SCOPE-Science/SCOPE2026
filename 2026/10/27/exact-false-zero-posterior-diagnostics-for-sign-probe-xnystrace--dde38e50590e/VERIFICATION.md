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

Run `python3 check_xnys.py` using a standard Python installation. The standalone checker uses only the standard library's exact rational arithmetic and exhaustively reconstructs the two-dimensional Nyström active-range projector for all \(2^m\) sign patterns at each integer \(2\le m\le9\) and four positive rational eigenvalue pairs. Expected output: `VERIFY_OK 4080 exhaustive projective-sign configurations`.

The checker verifies exact distributions of \(\widehat T-T\) and \(\widehat Q\), moment identities, and the false-zero event, including the special two-sample case. It does not establish the theorem for arbitrarily large \(m\). The general proof is the projective-sign classification and its exact counting argument in RESULT.md. The implementation of the theoretical estimator uses the Moore–Penrose pseudoinverse; optimized finite-precision variants may behave differently for dependent sign sketches. No independent audit was performed.
