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
The proof is exact for every prime \(p\ge5\); its infinite domain is not certified by finite enumeration. The indispensable steps are the norm-character bound on non-origin lines, the forcing of \(a=b\), and the scalar-exponent analysis for every prime divisor of \(p^2-1\).

The bundled `verify.py` directly enumerates the finite test cases; it is not a mathematical audit. Execute it with `python verify.py` using the standard library. It checks all ordered pairs \((a,b)\) with \(b\ne0\) and every term of the prescribed progression using repeated-squaring multiplicative-order tests. The expected outputs are \(p=5:8\), \(p=7:0\), \(p=11:0\), \(p=17:96\). The script asserts that every solution satisfies \(a=b\).

No numerical tests prove the infinite statement; no external independent audit has been performed.
