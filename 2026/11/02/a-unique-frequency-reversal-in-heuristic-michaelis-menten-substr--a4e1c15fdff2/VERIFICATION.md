---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For the explicitly specified open Michaelis–Menten full LNA and its one-substrate heuristic LNA, drift J=[[-a,v],[h,-v]] with a=u+d+k>0,h=u+d,v=k0e, determinant vk>0; diffusion covariance (c/Ω)[[2(d+k),-(2d+k)],[-(2d+k),2(d+k)]]. Stationary OU PSD via (iωI-J)^-1 D(-iωI-Jᵀ)^-1 yields S_full=(2c/Ω)[(d+k)ω²+k(ha+k(d+k))]/[(vk-ω²)²+(a+v)²ω²], S_heur=(2kc/Ω)/(ω²+(vk/a)²). Their difference has numerator -dω⁴+Bω²+C0 with B,C0>0, verified by independent symbolic resolvent algebra. Thus one ω*>0 crossing if d>0, strict heuristic excess for all finite ω if d=0; high-ω sign reverses only for d>0. Gaussian LNA statement, not exact CME or validated physical high-frequency QSSA.

## originality

PASS

Best-of-knowledge PASS for exact sign-frequency classification in the same open enzyme network, not for conventional QSSA, LNA PSD formula or known variance overestimate. Thomas–Straube–Grima gives integrated variance comparisons, and later work applies general spectral/coherence techniques but inspected sections do not state this all-parameter free-substrate auto-spectrum one-crossing theorem. A wider uninspected spectral appendix may entail it.

## value

PASS

A sharp parameter-universal frequency-by-frequency reversal and dissociation-free exception distinguish model reduction error from the known integrated-variance excess. It directly informs which time scales differ between a full and heuristic Gaussian noise description, subject to the high-frequency applicability caveat.

The dated certificate retains the supplied scientific assessment, sources and limitations.
