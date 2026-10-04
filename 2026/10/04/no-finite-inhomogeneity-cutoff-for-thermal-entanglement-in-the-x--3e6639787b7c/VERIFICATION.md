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

`verify_xxz_inhomogeneity.py` reconstructs the \(4\times4\) Hamiltonian directly from Pauli matrices and computes Gibbs-state concurrence from the Wootters spin-flip spectrum.

The checker compares direct matrix concurrence with the closed formula on a deterministic parameter grid. It separately solves a genuine lower activation threshold in a high-temperature example and verifies the predicted zero/positive sides of that threshold.

For the source's plotted parameter choices
\[
J=1,\qquad B=0.8,\qquad T=0.6,
\]
it checks positive concurrence at large finite inhomogeneity for each listed \(J_z\).

It also verifies convergence of
\[
\frac{|b|}{J}C(T,b)
\]
toward \(1\).

The finite replay is supplementary. The all-parameter topology and reciprocal asymptotic are proved analytically in `RESULT.md`.

No independent audit has been performed.
