---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Cyclically ordered sampled points generate the polygon hull perimeter as sum of adjacent chords, including collinear cases under the twofold segment-length convention. For any vertex, the nearest enclosing cyclic sample gap (A,B) has joint density N(N-1)/L² (1-(A+B)/L)^(N-2). Let S=A+B and T=A/S: T is independent uniform[0,1], E S=2L/(N+1). The virtual corner loss g_beta(A,B)=S-sqrt(A²+B²+2ABcos(beta)) has exact expectation Lh(beta)/(N+1) using ∫sqrt(c²+s²u²)du. On G=all m edges sampled, the actual chord deficit equals sum of g_beta; on the complement each nonnegative term is at most L, while P(G^c)<=sum_i(1-ell_i/L)^N<=m rho^N. Therefore the stated explicit bound follows, including the rare all-collinear cases. Independently checked angular integral for several beta and a square 10k-repetition Monte Carlo at N=50; observed estimate agrees within its sampling error and must not be mistaken for an exact verification of the exponentially small error term. The all-N proof is the analytic gap argument.

## originality

PASS

Prior random-polytope boundary results calculate facet numbers, volumes or smooth-body perimeter approximation, not this all-convex-polygon angular arctanh coefficient and uniform exponential finite-sample remainder. The full Reitzner–Schuett–Werner paper was read in HTML to compare Theorems 1.1 and 1.2; full Schneider 1988 was unavailable and is a narrow historical risk, but its accessible description concerns smooth-body sampling.

## value

PASS

A motivated first-order quantitative approximation of fixed polygon perimeter by boundary-random inscribed hulls, with explicit corner-angle coefficient and an exponentially small uniform-in-N remainder. Unlike volume/area deficit, perimeter has inverse-linear rather than inverse-square scale. The edge-missing correction is mathematically material: ignoring it would falsely claim an exact finite-N identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
