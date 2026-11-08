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

For the specified order-two four-step BDFL coefficients and exactly alternating positive steps h,rh, consistency isolates a simple constant mode and a three-state parasitic companion C(w). Substituting the actual local time nodes gives u(r),v(r)=u(1/r); their product has cubic char polynomial z³-Tz²+Ez-V. The factorized strict cubic Schur signs reduce on s=r+r^{-1}>=2 to one critical quadratic, with s* and R=4.2228260449... as printed; the other Schur inequalities stay positive up to s*, and for s>s* the real cubic has a root <-1. At equality -1 is simple and the other two modes lie inside unit circle, so propagators remain bounded. At r=4 the frozen companion determinant u(4)>1 even as the monodromy decays. This establishes uniform zero-stability only for the named periodic zero-dynamics method; numerical scans are supplementary and source-paper coefficient attribution is not independently verified because access to that paper was blocked.

## originality

PASS

PASS with explicit priority/access risk: the 2026 source introduces an optimized multistep formula and (in accessible abstract) studies stability; its exact full body could not be checked. In the assessed package, the new exact two-phase monodromy and reciprocal sharp boundary are not automatic from the frozen single-step root condition, while general smooth-grid and classical BDF2/3 stability theorems apply different schemes.

## value

PASS

An exact spectral frontier for a named variable-step method is operationally meaningful: stability occurs on a sharply bounded periodic-ratio interval including a phase at which one frozen step fails. This noncommutative damping distinction and endpoint multiplier classification are useful independently of broader adaptive-grid claims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
