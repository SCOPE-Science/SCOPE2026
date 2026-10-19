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
# Verification summary

The analytical Wigner generating function, sign-polynomial normalization, strict minima, all-degree Sonin energy identity, component count and fold expansion were checked against the complete proof. `artifacts/check.py` was executed in the package directory with the requirements listed in `artifacts/requirements.txt`.

For even orders \(n=4,6,\ldots,24\), exact rational intervals for all derivative roots and polynomial values were computed. The first two minima satisfy strictly \(m_2>m_1\) at each degree through 22 and \(m_1>m_2\) at 24. The separate floating-point checks cover each order \(1\le n\le64\), but are not the basis of the theorem for arbitrary \(n\). Eight direct phase-space Wigner integrals at oscillator orders 0 through 3 agree with the predicted Laguerre formula within \(10^{-24}\) in 30-digit arithmetic. See `artifacts/check_output.txt`.

No claim is made that a finite test certifies an infinite family. No independent external audit or publication-priority certification has been performed.
