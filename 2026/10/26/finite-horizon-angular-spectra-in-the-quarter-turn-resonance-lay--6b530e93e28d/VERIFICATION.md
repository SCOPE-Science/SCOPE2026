---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

At P=pi/2 and a=(kappa-kappa^{-1})/2, direct conjugated-rotation line geometry gives acute principal-angle increment g_kappa(theta)=P-arctan(a|sin(2theta)|), with period P and Lipschitz constant 2a. The lift of arg(B_kappa e_theta) has derivative (kappa cos²theta+kappa^{-1}sin²theta)^{-1} <= kappa. Replacing one actual step P+t/N by P costs <= kappa|t|/N; the left Riemann sum for g(theta+tu) costs <=a|t|/N, proving the uniform (kappa+a)|t|/N and Hausdorff bounds for every N and real t. Circular unimodality places residual-window extrema at centers 0 and P/2 and yields W=(2/|t|)integral_0^{r/2}[atan(a cos2u)-atan(a sin2u)]du, r=|t| mod P; width vanishes exactly for nonzero integral quarter turns, with nonzero linear-cusp coefficient atan(a)/(|m|P). Full-period cancellation and the same uniform estimate establish the three detuning regimes for delta_N->0. Independent numerical evaluation of both principal-angle formulas and sliding-window width for kappa=1.3,2,4.5 and eight detunings, with 1001 phase samples, corroborated the formulas; the all-N/all-real proof is analytic.

## originality

PASS

Best-of-knowledge new sharp simultaneous finite-horizon/near-resonance regime, not a new definition of angular spectrum or periodic Riemann sums. The 2024/2025 Beyn–Hüls paper covers fixed elliptic matrices and fixed-system convergence; the 2026 Beyn–Hüls paper covers angular maps, including a small-flow-step limit (its Theorem 4.6), not the P+t/N boundary layer or its exact width, collapse set and cusp. Inspection of relevant primary sections found no mathematical implication recovering these statements; overlap with unindexed near-resonance theory remains possible.

## value

PASS

This is a natural singular limit because N->infinity and parameter detuning->0 do not commute at a rational elliptic rotation. The exact complete detuning interval, finite-N uniform rate, resonance-only collapse and cusp coefficient quantify a geometrically motivated transition for the principal-angle observable rather than an arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
