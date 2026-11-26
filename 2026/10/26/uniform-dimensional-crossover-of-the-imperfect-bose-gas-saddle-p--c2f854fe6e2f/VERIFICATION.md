---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

The verification is analytic. For the reduced equation \(X=\operatorname{Li}_{1-\delta}(e^{-x})\), check DLMF §25.12 Eq. 25.12.12, the uniform bound on its terms of order at least one in \(x\), and the cancellation of the leading poles in \(\Gamma(\delta)\) and \(-\zeta(1-\delta)\). The proof retains the \(O(x)\) remainder when converting the estimate on \(x^{-\delta}\) to a relative error on \(x\).

The uniform expression using the two exact special-function coefficients has relative error \(O(z/(1+\delta X))\), where \(z=[\Gamma(\delta)/(X-\zeta(1-\delta))]^{1/\delta}\). In the elementary expression there is also an \(O(\delta)\) coefficient-truncation error. The sequence \(\delta=e^{-2X}\) shows why a pure \(O(\delta)\) error is insufficient. For the relative power-law endpoint, bound \(\delta^{-1}\log(1-\zeta(1-\delta)/X)\) above and below as in the proof: it vanishes exactly when \(\delta^2X\to\infty\), rather than just \(\delta X\to\infty\). The path \((\delta,X)=(j^{-2},j^3)\) separates these conditions.

The proof concerns the reduced saddle only and supplies no finite-temperature, finite-volume or force-error bound. No finite numerical experiment or formal proof certificate is used.
