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
Let
\[
\phi(s)=\frac{e^{s^{1-s}}-1}{e-1}.
\]
The analytic proof establishes
\[
\phi(s)\sim\frac{s}{e-1}
\]
and, after differentiation,
\[
\frac{s\phi'(s)}{\phi(s)}\to1.
\]

The bundled checker evaluates both ratios at progressively smaller survival probabilities. It also checks the second-order expansion
\[
\phi(s)=\frac{s-s^2\log s+s^2/2}{e-1}+O(s^3\log^2s).
\]

For an exact Pareto baseline, the checker numerically inverts \(\phi(s)=u\) and verifies convergence of the transformed-to-baseline extreme-quantile ratio to \((1/(e-1))^{1/\alpha}\).

These computations are reproducibility aids. The general survival, hazard, regular-variation, and moment statements are proved analytically.
