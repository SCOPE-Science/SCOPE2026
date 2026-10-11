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

# Verification and limits

The complete proof is provided in RESULT.md. The critical analytic checks are: the Green reproducing identity; strict first-shell maximality; uniform \(\ell^{p_*}\) control of near-optimizers; the complex modulus mean-value/Hölder estimate; the two-stage improvement from \(t=O(q^{-1/2})\) to \(t=O(\rho_d^q e^{C\sqrt q})\); and taking the \(q\)-th root. None uses numerical data as a proof of a limit.

`check_lattice_green.py` was executed with a cubic Dirichlet box of radius five and 1331 vertices. The residual maximum was about \(3.05\times10^{-16}\); the source Green value was approximately \(0.241072439473\), normalized nearest-neighbor value about \(0.308644874416\), and maximum remaining shell value about \(0.180595121196\). Ratios of the noncentral \(q\)-th-power Green mass to \(6\rho^q\) for exponents \(8,12,18,24,36\) were approximately \(1.0306435826\), \(1.0033093286\), \(1.0001297576\), \(1.0000051904\), and \(1.0000000084\). These are finite-volume illustrations; there is no rigorous numerical enclosure of the infinite-volume lattice constant in this package.

No independent audit was performed. Publication dates and literature comparisons are limited to identified sources; unindexed equivalent work remains possible.
