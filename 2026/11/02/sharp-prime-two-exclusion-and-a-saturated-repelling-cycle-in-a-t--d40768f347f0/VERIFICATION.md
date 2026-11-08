---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For primitive two-cycle p≠q, δ=p-q and η=tanh(αp)-tanh(αq), subtract returns (T-2)δ=T Mη. Strict monotonicity gives δ·η>0 while η·Mη=(17/10)||η||²>0, forcing T>2 for all α. For T>2 and α>=10, c=(T-2)/T, midpoint m, half-difference w, write Banach map G(m,w) with limiting pair (b,v), v=(0.7,2.7). The ±1/20 closed box is invariant by sigmoid saturation; Lipschitz<=216e^-6<1; thus a unique box cycle with p positive and q negative and quantified error. Derivative deviates from -(T-1)I by at most 10.8 Tα exp(-.6α/c), giving minimum expansion rho_T=1+(T-2)(1-108e^-6)>1 for both steps, so hyperbolic repulsion follows. Independently checked all three numerical constants and inspected 21-parameter high-precision verifier.

## originality

PASS

The exact model, weights, bias and numerical bifurcation curves are published by Buscarino–Famoso–Fortuna (2023); no general all-α T<=2 two-cycle impossibility or constructive T>2 saturated repeller and uniform expansion was found in the inspected open full article. Qualified novelty for this structural sharp frontier, not for the numerical map or Banach theorem.

## value

PASS

Proves a sharp global finite-period obstruction and a rigorously existing but forward-simulation-invisible repelling cycle in a natural neuron model, separating step-size, gain, and stability regimes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
