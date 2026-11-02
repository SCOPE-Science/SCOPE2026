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

# Reproducibility and limits

Execute `python3 verify_multiscale.py` with Python 3 standard library. The program creates exact rational enclosures for four values of the derivative, with cutoff \(K=250\), and asserts the indicated signs. The infinite tail is bounded above by \((1-q)^{K+1}/2\) separately for each coordinate. No floating-point approximation is used to decide any sign; displayed decimals only summarize the results.

The fully general Laplace-transform formula and tail inequality are established analytically in `RESULT.md`. Running code verifies the finite rational certificate, not publication priority or an independent audit. The claim concerns Gaussian endpoint-divergence rate, not total physical entropy production.
