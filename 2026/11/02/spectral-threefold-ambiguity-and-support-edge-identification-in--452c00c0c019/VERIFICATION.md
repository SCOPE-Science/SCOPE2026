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

Stationary force covariance e^(−c|t|) gives S_X(ω)=2cf²/[(ω²+c²)((p−ω²)²+q²ω²)]. Its numerator and monic cubic in z=ω² are observed. For q²<4p the mechanical quadratic is irreducible over ℝ, so the unique real linear factor marks c, then q,p,f. If q²≥4p, mechanical rates a,b>0 have a+b=q, ab=p; the spectral cubic determines their unordered multiset with telegraph c and each distinct selection c yields exactly one positive realization, including repeated poles. Overdamped causal Green kernel g(t)≥0 has integral 1/p; stationary σ with no flips on any finite interval has positive probability, so essential support R=f/p exactly. Writing U=abc gives R²=Kc/U², K=cf², and identifies c unambiguously. Independently checked three exact aliases with poles 1,2,3 and K=6, discriminants, support inversions and generator stationary moments. Exact-population observables only; no finite-sample inference.

## originality

PASS

Best-knowledge PASS for a complete one-, two-, threefold physical inverse spectrum classification and one-support-edge inverse rule. The physical model and bounded stationary support are prior work and the spectral filtering is standard. A generic linear-system identification/pole-allocation theorem might imply the special classification, and the exact primary physical article was not fully read.

## value

PASS

The example demonstrates a concrete threefold failure of inference even with all second-order data and shows precisely which additional non-Gaussian observable resolves it; this is a motivated physical stochastic identification invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
