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

# Reproducibility and scope

Run `python3 verify.py` in a Python 3 installation with the standard library. The checker uses exact rational arithmetic and tests the following for each \(r\in\{2,3,4,5\}\): all \(n\le3000\) against independent direct factorization and divisor convolution; the adjacent prime-power formula through exponent \(5r+4\); and the fractional-part identity at cutoffs \(30,100,512,1000,3000\). An observed successful run prints `VERIFY_OK`.

These checks are finite and do not establish the asymptotic or certify the Euler products. The infinite proof uses a classical Selberg–Delange theorem for the squarefree weight, a signed convolution with an absolutely summable remainder, regular variation, and the zeta fractional-part integral. No independent audit has been performed.
