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

Read entire RESULT.md/check_exact.py and rederived the graph parametrization X(r), 0<=r<=2b, d=b-2a>0 and exact S=T|K: S(r)=0 for r<=d/2, 4r-2d for d/2<=r<=d, and 2d for r>=d. Independently computed F cubed with exact rational fractions at 404 interior/breakpoint samples over 4 parameter pairs; checked the prime-three orbit and endpoint r=0,2d. The middle interval is exactly a 1/4 uniform return branch on J=[0,2d], with absorbing masses 1/4 and 1/2, so (T_*u_J)=(δP)/4+(δR)/2+u_J/4. For initial arclength on K, masses w,w,1-2w give closed mixture (α−w/(3*4^{m-1}))δP+(β−2w/(3*4^{m-1}))δR+(w/4^{m-1})σ. Nonatomic σ proves exact TV w4^{-(m-1)}; tail differentiation yields capture P(τ=1)=1−w and P(τ=m>=2)=3w4^{-(m-1)}. The unique nonabsorbing r=2d/3 is a zero-mass repeller. Symbolic piecewise branch proof, not 404 finite points, supports all parameters/time.

## originality

PASS

Cima–Gasull–Mañosa–Mañosas (2024 preprint/2025 article), original Proposition 12 and Figure 1, already present the polygon/invariant-graph and third-iterate branch dynamics; those are explicitly prior. The assessed claim is the exact arclength pushforward, nontrivial parameter-dependent atomic phase weights, TV coefficient and full capture-clock law. They are immediate derivable transfer calculations from existing branch map but not located as a stated probability theorem in inspected relevant sections; this closeness is the chief priority and valuation risk, not concealed.

## value

PASS

For a geometrically specified natural bounded section, the law gives the full time-dependent distribution for every m, not just an attractor/periodic orbit: exact phase bias, sharp TV relaxation factor, exceptional repeller and complete hitting-time generating function. These are motivated observables in piecewise-affine dynamics even though their derivation uses a known simple Markov branch mechanism.

The dated certificate retains the supplied scientific assessment, sources and limitations.
