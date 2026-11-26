---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For this deterministic graph ODE, at a stationary point recovery rules out x_i=1; a zero load would propagate to neighbors and contradict B>0, and a zero infection coordinate forces all infection coordinates to vanish. Hence the only branches are disease-free or strictly positive. Dividing the load variables by 1-x_i produces a Laplacian with positive edge weights (1-x_i)(1-x_j); its stationary nullspace on a connected graph is exactly constants. This gives the uniform disease-free load and forces within-part equality on a biclique via strict monotonicity of x/(1-x)^2. Independently, multiplying the two positive infection balances gives c(1-x_L)(1-x_R)=gamma/sqrt(mn); substituting into either balance shows that the infection odds are in the ratio sqrt(n):sqrt(m). Their common positive scale fixes the two loads, with total B an affine function of that scale of strictly positive slope and intercept B_c, so there is precisely one positive equilibrium for B>B_c and none at equality or below. Back-substitution and exact residual checks corroborate this, including star and balanced cases: python3 /workspace/branches/frozen_math_recheck.py 1 ran 96 rational cases; the frozen script was read, not executed. Opposite rankings follow strictly from the explicit odds and opposite ordering of the complementary susceptible fractions, and the loads are affine in B. On the fixed-mass tangent space the linearization is block triangular with infection block B A/(m+n)-gamma I and load block -L on zero-sum vectors. The latter is strictly stable, and the former has largest eigenvalue B sqrt(mn)/(m+n)-gamma. This proves only the stated below/above-threshold local assertions; no conclusion at equality about decay, or about endemic dynamical stability, is needed.

## originality

PASS

The distinct claim is the exact stationary profile and full mass-parametrized stationary classification for unequal bicliques. The defining model, stationary load law, spectral threshold, supercritical stability/uniqueness context, and equal-part solution are prior. In particular, merely reversing the nodal ordering is not distinct from the prior load identity.

## value

PASS

The simplest strongly degree-heterogeneous connected family is a natural test of the conservation-coupled graph ODE beyond the known regular case; it includes stars of arbitrarily many leaves. Exact coordinates and exclusion of hidden asymmetric or boundary stationary branches give an analytical reference for approximations, rather than only restating the spectral threshold or the load identity. No real-world inference follows from this abstract model calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
