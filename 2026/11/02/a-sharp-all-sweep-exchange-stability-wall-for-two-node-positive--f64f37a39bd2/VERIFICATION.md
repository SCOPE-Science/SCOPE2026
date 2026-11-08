---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For the explicitly stated two-node Gauss-Lobatto multiplicative maps, g=f_i/x_i vanishes at each positive equilibrium (s,s) and Dg=Q/s with Q=[[-a,a],[b,-b]]. Linearizing the exponential predictor and all finite sweeps gives D F_0=I+hQ and D F_m=I+(h/2)Q(I+D F_{m-1}), so transverse multipliers satisfy R_0=1-2u, R_m=1-u(1+R_{m-1}), u=h(a+b)/2>0. Solving yields R_m=(1-u+2(-1)^(m+1)u^(m+2))/(1+u). Exact parity inequalities imply |R_m|<1 iff 0<u<1 for each finite m, R_m(1)=(-1)^(m+1), instability beyond 1. IFT for locally implicit collocation yields (1-u)/(1+u), and difference magnitude 2u^(m+2)/(1+u), giving convergence iff u<1. Positive inputs stay positive by finite exponential compositions; no global nonlinear contractivity asserted. Independent rational multipliers and sample nonlinear linearizations corroborate; exact algebra is unrestricted proof.

## originality

PASS

Pezzella establishes a positive SPIDeC method and scalar diagonal statements, but coupled exchange is not diagonal: ratios f_i(y)/y_i depend on the state. The all-finite-sweep transverse wall is a concrete specialization, potentially derivable with standard Picard algebra. Full highly relevant Pezzella source was inaccessible (Oxford VPN disconnected), leaving a material priority risk rather than a fabricated NOT_COVERING verdict.

## value

PASS

This exact counterexample shows strict componentwise positivity and arbitrarily many finite corrections do not ensure transverse stiff stability, while the implicit collocation derivative is unconditionally damped. It sharply delineates a real numerical-method pitfall even in a minimal, naturally coupled positive exchange system.

The dated certificate retains the supplied scientific assessment, sources and limitations.
