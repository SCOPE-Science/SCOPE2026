---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

C PASS: Independently used SymPy to expand the supplied four differential equations, verify x+y+z+w is conserved, verify (d/dt)(log x-(1+p)y/q-((1+p)/q+1/s)z)=C-r-Dx exactly, and verify y'+z'=rx-qy and z'=rx-sz. The scalar barrier for Phi implies eventual positive lower bound for x when C>r, hence O(1/T) mean-vector correction for each positive trajectory. At C=r, x'=-x(x+(1+p)y+z)<=-x^2 and stable linear convolution plus slow x decay yield z/x->r/s, y/x->r/q, then (1/x)'->D; logarithmic integral follows from the coboundary. At C<r the per-capita rate tends to C-r. This is an analytic all-trajectory argument, not just a symbolic script.

## originality

PASS

PASS: Boros-Hofbauer Theorem 14 for precisely the normalized four-species equations proves unique positive equilibrium for C>r, bifurcation and coexistence of an attracting equilibrium and two limit cycles, plus permanence. The 22-page arXiv full text was inspected at Eq. (8), Theorem 14 and its proof; it does not determine exact trajectory-independent concentration time means, a bounded finite-time endpoint correction, or the critical full inverse-time and logarithmic cumulative-production laws. The new coboundary identity and threshold asymptotic analysis are additional, not contained in equilibrium/cycle statements. General dynamic ACR results are about pointwise robustness and differ.

## value

PASS

V PASS: This naturally motivated chemical oscillator has coexistence of stable/unstable cycles and equilibria, so their full observable concentration barycenter being identical is not a trivial equilibrium calculation. The O(1/T) endpoint terms identify quantitative mean invariants across basins; the critical universal t^-1 profile and logarithmic cumulative-production centering describe the natural chemical total-mass bifurcation sharply. No paper-sized general theory is required for this specific motivated dynamical theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
