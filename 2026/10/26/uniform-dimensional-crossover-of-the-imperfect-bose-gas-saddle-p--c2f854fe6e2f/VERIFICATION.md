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

The analytic check uses the reduced stationary-point equation \(X=\operatorname{Li}_{1-\delta}(e^{-x})\), the NIST DLMF polylogarithm expansion, and the Laurent expansions of \(\Gamma(\delta)\) and \(\zeta(1-\delta)\). The two \(1/\delta\) poles cancel; the remaining equation is solved for \(x^{-\delta}\). The two limits \(\delta X\to0\) and \(\delta X\to\infty\) are derived explicitly in the proof.

Limits: the finite-\(\beta\) saddle correction and finite-volume terms are not controlled; the asymptotic formula is not asserted for arbitrary \(D/\lambda\), boundary conditions, or the ideal gas. No independent audit or independent validation has been performed.
