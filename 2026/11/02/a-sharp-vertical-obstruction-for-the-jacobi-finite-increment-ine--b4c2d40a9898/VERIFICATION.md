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

# Analytical and computational verification

The universal proof is self-contained except for well-established Jacobi identities, the fixed-angle Darboux formula in DLMF §18.15(i), and the published sufficient inequality of Nikolov (2026). The critical derivative asymptotic is derived by applying Darboux directly to the shifted-parameter Jacobi polynomial through the **exact** differentiation formula; no uncontrolled differentiation of an \(O(\cdot)\) remainder is used. For fixed \(\alpha,\beta>-1\), the four residues modulo four yield the exact negative liminf when \(\alpha<1/2\), while the endpoint term survives at \(\alpha=1/2\). The new diagonal classification invokes published sufficiency and newly proved necessity as separate implications.

The embedded standalone `CHECK.py` was executed using `python CHECK.py` in an environment with NumPy and SciPy. It reported `JACOBI_ORIGIN_CHECKS_OK 257`. It compares finite-degree origin derivatives with independently computed symmetric finite differences, compares the Darboux leading terms with their polynomial values using explicit absolute-remainder tolerances, and tests signed failure below the threshold. The finite consistency tests are not claimed as an infinite proof or external audit.

Scientific limits: the necessary boundary criterion is not claimed sufficient, and the proof is for fixed real parameters; the first public cited source is dated 2026-06-24. Independent validation has not been performed.
