---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

A rate-r regenerative resolvent supplies the positive unique stationary density. Away from the reset source, substituting psi=exp(V/(2D))*rho into the steady Fokker-Planck equation gives psi double-prime=Q*psi, where Q=k squared+potential derivative squared/(4D squared)-potential second derivative/(2D). The exact Liouville-Green ansatz has integrable residual O(x^{2alpha-4}) in L^1, allowing a unique positive decaying mode; the growing mode cannot produce an integrable density. The leading eikonal shift is lambda^2 alpha^2 x^{2alpha-2}/(8D^2k); integrating yields the trichotomy. Independent exact derivative/eikonal asymptotic tests passed for alpha 1/3,1/2,2/3,0.82; they support but do not establish x→infinity.

## originality

PASS

The inspected full Defaveri–Barkai–Kessler article develops **unreset** weak-potential equilibrium and long-time large-deviation relaxation (including a similar Schrödinger transform), but does not prove the stationary Poisson-reset resolvent spatial WKB correction. Pal supplies the general potential-and-reset stationary framework; his full paper was not accessible, which is a historical-priority risk rather than automatic scientific failure. No searched result demonstrated the exact three-regime subleading spatial law.

## value

PASS

A natural weak-trap resetting model has a qualitatively sharp change in the spatial tail at the critical square-integrability exponent 1/2; an exact positive multiplicative constant at and below the transition and the explicit above-threshold coefficient are useful for distinguishing leading exponential fits from true stationary tails. The value is in the precise resolvent-tail classification, not generic WKB technique.

The dated certificate retains the supplied scientific assessment, sources and limitations.
