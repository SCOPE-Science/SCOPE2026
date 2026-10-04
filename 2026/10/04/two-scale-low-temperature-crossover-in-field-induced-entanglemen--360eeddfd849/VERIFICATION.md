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

`verify_three_qubit_xxx_boundary_layers.py` reconstructs the periodic three-spin \(XXX\) Hamiltonian, forms the Gibbs state, traces out one spin, and computes Wootters concurrence.

The direct matrix result is compared with the analytic reduced-state formula over a deterministic grid.

The script also checks the unique activation threshold, convergence of
\[
\frac{B_*(T)}
{\sqrt6\,T e^{-3J/(2T)}}
\]
to \(1\), the five-point saturation scaling profile
\[
C\!\left(T,\frac{3J}{2}+sT\right)
\to
\frac{2}{3(2+e^{2s})},
\]
and the fixed-high-field Arrhenius law.

The numerical replay is supplementary. The all-parameter asymptotic statements are proved analytically in `RESULT.md`.

No independent audit has been performed.
