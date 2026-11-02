---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

For a stem class-two L=V⊕Z over F_q, Z=[L,L], dim V=d≥2, dim Z=c, D=d+c, every nonzero rank-one endomorphism has the unique parameterization N=f⊗w modulo the free scalar action (f,w)∼(αf,α^{-1}w). Substituting in Nijenhuis torsion yields f∧g=f(w)h with g(x)=f([w,x]), h(x,y)=f([x,y]). If f|Z=0 then g=h=0 and every nonzero w works, contributing (q^d−1)(q^D−1). If b=f|Z≠0, evaluate at a central z with f(z)≠0 to get g=0, and surjectivity [L,L]=Z forces f(w)=0. Thus w is any nonzero vector in ker(B_b) lifted to L and intersected with ker f, of count q^(D−r_b−1)−1; each b admits q^d f-lifts. Divide by q−1 to get [(q^d−1)(q^D−1)+q^d∑_{b≠0}(q^(D−r_b−1)−1)]/(q−1). Nonzero N² occurs only for f|Z=0, and counts (q^d−1)q^(D−1). Alternating-form rank spectrum for free two-step algebra is standard and the Gaussian-binomial formula is consistent in all characteristics, including q even. Independent exact evaluation gives 833 rank-one Nijenhuis maps and 224 with nonzero square for free d=3 over F2. The rigorous count uses all possible vectors, not a partial enumeration.

## originality

PASS

Qualified PASS for the finite-field arbitrary-stem pencil-count formula and free-algebra distribution, not the Nijenhuis definition or known special Heisenberg cases. Liu–Sheng–Zhou–Bai develop general n-Lie Nijenhuis formalism and examples over complex fields without this finite-field rank-one census. Fulman–Goldstein study alternating/skew matrix rank distributions, which supply the standard rank spectrum but not its novel coupling to Nijenhuis torsion. A 2026 pre-Lie/associative low-dimensional classification is a different algebraic category. Broad low-rank tensor-operator classifications remain a priority risk.

## value

PASS

The count solves a natural question about deformation-compatible operators on the full class of stem two-step Lie algebras. It identifies the commutator-pencil rank spectrum as the precise invariant, separates square-zero versus nonzero-square operators, and yields explicit counts for free nilpotent algebras in all prime-power field sizes. This is a complete structured classification of a motivated algebraic statistic, not an arbitrary small-slice computation; its value survives without classification of every operator rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.
