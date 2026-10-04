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

The Hamiltonian is rebuilt directly from standard spin-\(1\) matrices in `verify_biquadratic_qutrit.py`.

The checker compares the numerical \(9\times9\) spectrum with the total-spin spectrum, exponentiates the Gibbs state, performs a direct partial transpose, and compares the resulting negativity with the closed formula on deterministic parameter grids.

It also checks
\[
T_c=\frac{3|K|}{\log4},
\]
the zero-field simplification
\[
\mathcal N=\frac{r-4}{r+8},
\]
and positive negativity at large finite fields below threshold.

Finite numerical replay is supplementary to the analytic proof.

No independent audit has been performed.
