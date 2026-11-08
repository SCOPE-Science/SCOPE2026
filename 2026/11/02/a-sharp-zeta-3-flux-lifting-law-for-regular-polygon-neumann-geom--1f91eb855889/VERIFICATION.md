---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Exact facet radial graph r_N=cos(pi/N)/cos(tau) gives pulled-back normal flux G_N=r_N u_r - tan(tau)u_theta. Since u_r(1)=0 and r_N-1=O(N^-2), G_N=-f' sin(tau)+O_L2(N^-2). On disk Neumann energy is 2pi sum_{n!=0}|g_hat(n)|²/|n|. Facet sawtooth coefficients a_{k,N} satisfy N a_{k,N}->1/k, |a_{k,N}|<=C/(N|k|), and for trigonometric f' sidebands kN+m are disjoint for N>2M, giving 2ζ(3)||f'||². For f' in H^{1/2}, modulation and summation of |k|^-3/2 uniformly control endpoint and density applies. Separate finite Fourier-integral/single-mode checks agree; no claim of total FE Galerkin error.

## originality

PASS

Boffi and Gastaldi (2026) show order h^{3/2} geometric error effects for straight-sided Neumann FEM approximation and some cancellation, not this isolated radially transported flux functional or 2ζ(3) sharp coefficient in the inspected complete primary text. Classical disk harmonic multipliers are used, not asserted new. Other natural-boundary finite-element works and older faceted Neumann homogenization may contain a related calculation; inaccessible full texts are residual risks.

## value

PASS

A natural isolated Neumann geometric consistency mechanism has a precise universal nonzero N^-3/2 norm asymptotic, trace dependence and H^{3/2} endpoint; it is a reusable exact benchmark for curved-to-faceted boundary numerical methods without overclaiming full FEM error.

The dated certificate retains the supplied scientific assessment, sources and limitations.
