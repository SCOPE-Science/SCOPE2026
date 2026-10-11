---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The source's controlled fifth state equation contains \((1-u_2(t))\beta_{hv}e^{-\mu_v\tau}I_h(t-\tau)S_v(t-\tau)\). Direct first-order product expansion necessarily preserves the survival factor, contains both delayed variations \(\widetilde I_h(t-\tau)S_v(t-\tau)\) and \(I_h(t-\tau)\widetilde S_v(t-\tau)\), and gives the control term \(-\rho_2(t)I_h(t-\tau)S_v(t-\tau)\). The published Eq. (26) instead omits the survival factor, duplicates the \(\widetilde I_h\) term, and evaluates the \(\rho_2\) term at current states. In the adjoint pairing, substituting \(s=t+\tau\) forces advanced coefficients \(\lambda_5(t+\tau)(1-u_2(t+\tau))\beta_{hv}e^{-\mu_v\tau}S_v(t)\) and its \(I_h(t)\) counterpart on \([0,T-\tau]\), incompatible with the printed Eq. (32). The same first variation forces the corrected delayed-state contribution in the \(u_2\) stationarity formula. Therefore the printed Theorem 9 system is not the first-order system of Eq. (23) for general positive delay.

## originality

PASS

The current primary article itself is the decisive comparison: its stated controlled delay term and printed first variation/adjoint/control formulas are algebraically inconsistent in exactly the audited way. Targeted DOI/title searches located the current article but no correction or erratum. Related delayed biological-control papers use different state systems and do not supply the source-specific correction. The claim is therefore an original correction of a live published optimality system, not a restatement of general Pontryagin theory.

## value

PASS

The discrepancy changes the necessary intervention gradient and the advanced costate coefficients in a published delayed epidemic-control theorem. It is therefore a structural correction needed before the feedback characterization can be interpreted as a first-order necessary condition, not a cosmetic notation fix.

The dated certificate retains the supplied scientific assessment, sources and limitations.
