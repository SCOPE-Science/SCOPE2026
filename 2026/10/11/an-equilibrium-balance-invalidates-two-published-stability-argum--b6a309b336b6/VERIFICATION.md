---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The source equation A_dot=lambda(1-A0)y-beta A-phi A y implies at every strictly positive equilibrium A*=lambda(1-A0)y*/(beta+phi y*); positivity of A*,y*,beta forces A0<1 and 0<A*<lambda(1-A0)/phi. The source condition (4.16) demands the opposite strict inequality lambda(1-A0)/phi<A*, making its stated sufficient condition empty. The equilibrium identity further yields phi A* -lambda(1-A0)=-lambda(1-A0) beta/(beta+phi y*)<0. The published Theorem 6 Lyapunov choice L1=L2 c2 phi/[phi A* -lambda(1-A0)] is therefore negative even though L1,L2,c2,phi>0. On line x=x*,y=y* its candidate V=L1(A-A*)²/2<0 for A!=A*, so Sylvester positive-definiteness fails. The complete actual Reshma–Kumar primary PDF including model equations, condition (4.16), Theorem 6 and proof was checked; symbolic equations and their signs were independently reconstructed, and verify.py inspected. This refutes the proof/criterion, not local RH condition or all possible stability conclusions.

## originality

PASS

A source-specific cross-comparison of exact positive-equilibrium balance against a printed sufficient condition and its separate Lyapunov coefficient exposes two mathematical defects. Resultary and direct title/DOI/phrase searches did not locate a published erratum or an already stated implication. Earlier ecological stability work with fear/food concerns different systems or conditions, not this exact model and theorem pair. Best-of-knowledge O with ordinary nonindexed erratum risk.

## value

PASS

Identifying that an advertised sufficient parameter condition is impossible, and that a proposed global Lyapunov function is actually indefinite at every strictly positive equilibrium, materially changes the interpretation of two named stability claims in a published model. The correction is motivated by the original proof and does not overclaim actual dynamics, so it is a useful substantive diagnostic beyond a symbol/normalization quibble.

The dated certificate retains the supplied scientific assessment, sources and limitations.
