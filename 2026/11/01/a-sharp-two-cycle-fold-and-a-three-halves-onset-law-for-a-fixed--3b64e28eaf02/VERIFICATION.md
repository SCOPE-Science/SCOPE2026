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

Reconstructed equations x'= -x from two y increments and z=y+x/2, giving z²+x²/4=1-1/beta and alpha cos x=beta z x². For 1<beta<=2 the bound x<sqrt2<pi/2 yields z>0 and bijective positive roots of Q_beta(x)=beta x² sqrt(R²-x²/4)/cosx with prime-two orbits. For beta<=1 no nonzero solution. Strict log concavity is reduced to a polynomial P(v) on [0,2] with all nine positive degree-eight Bernstein coefficients. Independently checked the exact polynomial identity and all nine rational Bernstein coefficients using SymPy. Q vanishes at both endpoints and has unique nondegenerate max; its root count is 0,1,2 across alpha*, and Taylor expansion gives square-root fold. Scaling x=2R s shows alpha*~8/(3sqrt3)(beta-1)^(3/2). Monotonicity alpha* follows pointwise Q_beta increasing in beta.

## originality

PASS

Almatroud–Pham Mathematics 11 (2023) 1319 defines exactly FPFM1 with absence of fixed points and numerical bifurcation diagrams; no analytic global prime-two census/fold/onset identified in inspected article material. Related other memristor maps are not the same equation. Resultary similar Rulkov/Gumowski period-two findings use distinct dynamics.

## value

PASS

Closed global prime-two orbit census and nondegenerate fold threshold for a previously studied fixed-point-free real map, with quantitative 3/2 onset near beta=1; stronger than numerical bifurcation diagrams.

The dated certificate retains the supplied scientific assessment, sources and limitations.
