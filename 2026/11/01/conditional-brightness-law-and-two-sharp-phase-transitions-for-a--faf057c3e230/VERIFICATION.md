---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

The eight octahedral facets have area sqrt(3)/2 and normals (±1,±1,±1)/sqrt(3), so Cauchy projection gives B=(1/4)Σ|±a±b±c|=max(2a,a+b+c) for sorted 0≤c≤b≤a. On a fixed largest-coordinate sphere section, the permitted azimuth is [phi0,π/4], phi0=acos(a/sqrt(1-a²)) below 1/sqrt(2), else zero. Haar area d a d phi makes this angle uniformly distributed after conditioning; with Ψ=π/4−phi, b+c=sqrt(2(1-a²))cos Ψ. Pushforward yields B=2a+(sqrt(2(1-a²))cos Ψ−a)_+, stated support and explicit atom. Derivative gives density 1/[q(a)sqrt(2(1-a²)−(z−a)²)]; integrating the positive part yields the mean. At a=1/sqrt(3) and a=1 only the one-sided regular-conditional limits are asserted. These analytic identities prove the continuum, not the directional samples.

## originality

PASS

No stronger or equivalent covering result was established in the actual comparisons of statements/implications; this is a best-of-knowledge assessment with the precise unread-primary-source and alias risks separately documented.

## value

PASS

This is a motivated joint geometric-probability invariant: nearest-axis alignment is a natural orientation statistic for the regular octahedron, and the full conditional shadow-area law makes a sharp transition from continuous to mixed atomic to deterministic behavior. The exact intermediate atom and support, rather than the classical projection-area formula alone, supply a reusable structural distribution statement; no sweeping general-polytope claim is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
