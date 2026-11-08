---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For exact softplus fixed-point equilibrium with 0<q<1, slopes t,s∈(0,1) are freely realizable by biases. A one-unit recurrence yields H1=t(1−t)/(1−qt)^3, derivative zero uniquely at t*=1/[(1−q)+sqrt((1−q)^2+q)], giving asymptotic δ²sup H1→4/27. For triangular W=[[q,0],[q,0]], output second unit has H2=s(1−s)/(1−qt)^2 + q s t(1−t)/(1−qt)^3. Maximizing s gives s*=(1−qt²)/[2(1−qt)] and envelope (1−qt²)^2/[4(1−qt)^4]. Ratio (1−qt²)/(1−qt)^2 strictly increases with t, giving exact supremum 1/[4(1−q)^2] as t→1, not at any finite bias. Two independent copies in 2D multiply to det Hessian sup 1/[16(1−q)^4]. The comparison ratio 4 to the source 1/64 coefficient is architecture-specific, not a new global sharp upper bound. Independently checked derivative/algebra and representative finite q values; actual symbolic verifier source was inspected.

## originality

PASS

Best-of-knowledge PASS for optimization over all scalar and triangular biases and sharp architecture comparison. Standard implicit differentiation and the motivating paper’s generic upper bounds are prior work, and the source explicitly did not optimize universal prefactors. Full original 2026 article unavailable, so possible hidden matching special case remains risk.

## value

PASS

The optimization distinguishes a nontrivial recurrent architectural effect: a saturated first unit enhances curvature transmitted to a second, yielding a factor 27/16 over optimized one-unit inverse-square curvature and fourfold 2D determinant improvement versus the published example at equal norm bounds. Exact constants motivate sharpened universal bounds, without overstating global optimality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
