---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For m>=2 and positive budget B and alternating edge prices cA,cB, define tau=pi/m, d=cos(tau), Delta=cA+cB+2sqrt(cA*cB)d. Build a centered 2m-vertex planar polygon with squared alternating chord lengths cA,cB, where angular steps 2alpha,2beta and alpha+beta=tau. Rayleigh trace against both columns yields a universal upper bound B/(2mR^2) = 2B sin^2(tau)/(m Delta) for EVERY independently chosen nonnegative conductance vector (even asymmetric). The proposed positive alternating weights a*=B/m(cA+sqrt(cA*cB)d)/(cA Delta), b*=B/m(cB+sqrt(cA*cB)d)/(cB Delta) are budget-feasible and satisfy L(w*)X=Lambda X via tangential-force cancellation. Standard two-vertex Bloch decomposition shows this Lambda is the first positive eigenvalue, even for m=2, so upper bound is attained. Every other optimum makes both planar Rayleigh columns gap eigenvectors; two noncollinear neighbor-chord vectors at each vertex then uniquely determine its incident conductances, proving labelled-edge uniqueness (not merely modulo symmetry). The m=2 equal-weight boundary, strict price sensitivity for m>2, square-root large-cycle ratio and m^-3 gap follow algebraically. Independent eigenvalue/budget computation checked 15 size-price cases and 180 randomly perturbed nonsymmetric feasible conductance assignments, all below the claimed optimal gap. These finite computations do not replace the global proof.

## originality

PASS

Best-of-knowledge PASS for the explicit globally unique two-price alternating cycle solution with unrestricted independent edge conductances, not the generic continuous-time fastest mixing SDP or polygon dual. Sun-Boyd-Xiao-Diaconis already establish continuous-time spectral-gap design, maximum-variance-unfolding dual, uniform price cycles, and 2-dimensionality of optimal cycle configurations; Section5.3 does not state this exact period-two tariff optimizer with labelled-edge uniqueness. Boyd-Diaconis-Parrilo-Xiao solve symmetry-reduced discrete-time SLEM objective; the stochastic-matrix spectral-radius problem is distinct from continuous-time generator gap with conductance price budget. Published mathematical-finding queries yielded no direct same-parameter solution, but unindexed analytic specializations remain a priority risk.

## value

PASS

Two-class alternating tariffs are a natural tractable yet nonuniform spectral resource allocation problem. An explicit unique global allocation over 2m unconstrained independent rates, a sharp spectral-gap value, and a rigorous independence-from-symmetry optimum certificate replace a numerical SDP throughout the infinite family. The four-cycle price-neutral allocation is a meaningful sharp finite-size exception, and the asymptotic square-root price rule explains large-network scaling.

The dated certificate retains the supplied scientific assessment, sources and limitations.
