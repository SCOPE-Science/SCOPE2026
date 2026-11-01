---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Independently inverted the actual frozen RESULT.md two-stage implicit 2×2 linear system and symbolically verified B(s,t), trace −(4st+2s+10t−3)/(2s²+4s+3), determinant 2t(t−2)/(2s²+4s+3), and all three quadratic Jury identities. The real split strip follows from middle Jury polynomial (s−t)²+s−7t+3≥0 and strict ordering 0<T(s)<P(s)<U(s). At t=T(s) the −1 eigenvalue is simple, zero-split eigenvalues are 0,1 simple, so full three-stage matrix is power bounded; above T(s) a root has modulus >1. For fixed t=cs, 0<c<1, as s→∞ the active block tends to cJ=c(−I+N), N²=0, ||N||₂=3; exact powers give (1−c)max_n||(cJ)^n||₂→3/e. Taking each finite n first and then sufficiently large but finite stable s establishes no UNIFORM bound across the stable family; no single finite B is asserted power-unbounded. A standalone independent SymPy derivation confirms the algebra; finite checks are supplementary.

## originality

PASS

Buvoli–Southworth introduce FIMEX-Radau stages and study spectral stability regions for their methods, but the inspected original publication's accessible material does not provide this explicit three-node nonnegative real split strip, the closed radical boundary, or its nonnormal stage-norm transient constant. The existing general-linear-method and Jordan-block spectral theory supplies tools but not this exact specialization with both effects. The full primary source was inaccessible via arXiv/OA and authorized Oxford returned vpn_disconnected; this remains a substantive cited risk, but no covering theorem was positively identified from inspected material. Originality is best-of-knowledge rather than an inaccessible-text claim of not covering.

## value

PASS

A natural first uniterated small FIMEX-Radau method whose stability plots otherwise conflate spectral and nonnormal notions: exact full real damping domain with power-bounded boundaries plus a constructive demonstration that arbitrarily large stable-stage transients occur. This is a useful sharp numerical-analysis diagnostic rather than a textbook Jordan observation in isolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
