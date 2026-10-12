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

The proof uses the exact finite magnetization-sector expansion of the Curie--Weiss partition function. After division by the fully magnetized contribution, the one-spin-flip sector has relative factor \(e^{-2(n-1)\beta/n}\), and for \(n\ge4\) the two-spin-flip sector has relative factor \(e^{-4(n-2)\beta/n}\). At each limiting zero \(\theta_{n,k}\), the derivative of \(\cos(nx)\) is nonzero, so a local implicit branch exists and its coefficients are obtained by Taylor expansion.

The special cases are checked from exact reduced equations: \(n=2\) gives \(\cos(2x)=-e^{-\beta}\); \(n=3\) gives \(\cos(3x)+3e^{-4\beta/3}\cos x=0\); and \(n=4\) gives \(\cos(4x)+4e^{-3\beta/2}\cos(2x)+3e^{-2\beta}=0\). The factor \(3\), rather than the generic paired coefficient \({4\choose2}=6\), is the source of the halved \(n=4\) second correction.

`verify.py` evaluates the exact finite sum and bisects the relevant real zeros for representative \(n\). It checks the scaled leading displacement and selected second-order residuals against the analytic coefficients. These finite evaluations do not prove the asymptotic statement and are included only as a reproducibility check.

No claim is made about estimates uniform in \(n\), about general interaction graphs, or about independent validation.
