---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Starting from g_Q(tu)/|Q|=(1-t/T)(1-qt/T) for T=2sqrt(1+q²), -d(g_Q/|Q|) has probability density [(1+q)-2qt/T]dt/T. The Mellin integral converges at zero iff p>-1, including negative p, and gives rho_p=T[(p+2-pq)/((p+1)(p+2))]^(1/p); logarithmic limiting integration gives rho_0=T e^(-1-q/2). The exact log derivative is -(q-1)((p+1)q-1)/((1+q²)(p+2-pq)); its denominator is positive on p>-1,q∈[0,1], making q=1 the sole reduced minimum when p<=0 and q*=1/(p+1) the sole reduced minimum for p>0. Every maximum is at q=0 or 1. Their log ratio is (log2)/2-log(1+p/2)/p, strictly increasing in p>-1 with the unique zero p=2; differentiation yields crossing slope (log2-1/2)/4, and p=2 substitutions give outer 2/sqrt3 and inner 10/9. The q endpoints each represent four directions and a strict interior q represents eight, so the equality count is exact. SymPy verified the symbolic factorization, limit, identities and sharp contact substitutions. Independent regularized Mellin quadrature (including p=-0.9) and 11 high-precision directional grids corroborated the formulas; neither finite check is used as the infinite-parameter argument.

## originality

PASS

A complete planar-square Euclidean angular-extremum/equality-direction phase diagram is not stated in the inspected general cube, covariance, convexity or integral prior results. However, the complete square radial profile and endpoint values are already implicit/partly explicit in Langharst–Manui–Zvavitch Proposition 34, so priority belongs only to the remaining all-parameter direction classification and transverse crossing, not the moment framework or raw endpoint formulas. The inaccessible original 1998 Gardner–Zhang full text is a named residual risk.

## value

PASS

The radial-mean family has an active sharp-shape problem after the negative-p convexity theorem; the square is the canonical fourfold-symmetric test body, with Euclidean radii and complete equality/contact classes natural invariants. This finding classifies all admissible parameters, locates the single eightfold outer contact at p=2 and the emergence of eight oblique inner contacts for p>0, and gives the nonzero contact-crossing slope. The result is a small but independently usable sharp benchmark for a concrete natural operator rather than an arbitrary parameter sample. Value is limited to the square and does not assert a new general mean-body inequality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
