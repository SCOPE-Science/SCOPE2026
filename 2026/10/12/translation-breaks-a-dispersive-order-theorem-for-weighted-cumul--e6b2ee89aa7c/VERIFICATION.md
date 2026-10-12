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

The public theorem statement and defining equation were checked directly in the cited 2026 source. The accepted counterexample uses only exact formulas.

For \(X\sim\operatorname{Uniform}(0,1)\) and \(Y=X+2\), the quantile functions satisfy \(Q_Y(p)-Q_Y(u)=Q_X(p)-Q_X(u)\) for every pair of quantile levels, so the dispersive-order premise holds. With \(w(x)=e^{-x}\), direct substitution into the defining integral yields
\[
\Phi_{Q_Y}^{w}(u)=e^{-2}\Phi_{Q_X}^{w}(u).
\]
The integral defining \(-\Phi_{Q_X}^{w}(u)\) is strictly positive for each \(0<u<1\); therefore \(\Phi_{Q_X}^{w}(u)<\Phi_{Q_Y}^{w}(u)\), contrary to the published conclusion.

The older unweighted primary source was inspected in full around its stochastic-order comparison. It includes endpoint information when using the dispersive-to-stochastic implication, consistent with the location obstruction exposed here.

No claim is made about a maximal corrected hypothesis, convergence, estimation, or any empirical consequence beyond the exact theorem refutation. Independent audit has not been performed.
