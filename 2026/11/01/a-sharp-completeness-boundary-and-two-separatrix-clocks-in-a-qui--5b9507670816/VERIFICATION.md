---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Multiplying y′=-x−βx⁵+αx³y² by e^{−αx⁴/2}y and using V′=e^{−αx⁴/2}(x+βx⁵) exactly conserves H=½e^{−αx⁴/2}y²+V(x). The potential is even, strictly monotone on x>0, with Gaussian ceiling E*=√π/(2√(2α))(1+β/α). For 0<E<E* energy level is a compact periodic oval, E=E* two monotone complete branches with critical speed²~(1+βx⁴)/(αx²), and E>E* two finite-time escaping branches. The one-sided Laplace estimate for R(x)=E*−V(x) yields critical x(t) growth and supercritical tail e^{−αx⁴/4}/(αx³√(2(E−E*))). For periods the ratio of periodic to critical speed away from x=A is 1−R(A)/R(x); a strip h_A=K log A/A³ has reciprocal-speed integral o(1), controlling the singular turning point. Integrating critical reciprocal speed yields T~2√α A² (β=0), T~4√(α/β)log A (β>0); substituting log(E*/δ)~αA⁴/2 gives the stated sqrt-log and log-log laws. Time-preserving coordinate z=∫e^{−αx⁴/4}dx yields local g(z)=z+(β−α/5)z⁵+..., period correction (α−5β)A⁴/16. Independently checked the conservation identity and local coefficient symbolically; finite quadrature cannot establish limits.

## originality

PASS

da Cruz–Llibre identify local-center but non-global-center parameter classes for this quintic family, not the exact energy/temporal trichotomy and period constants. A published opposite-feedback sign result has globally unbounded potential and periods shrinking rather than diverging; cannot imply this statement. Standard Jacobi multipliers and generic period criteria explain transformations but not sharp physical-time laws. Priority risk persists for alternate Liénard sign conventions.

## value

PASS

The problem naturally refines a known local/non-global center distinction: it explicitly resolves which unbounded energy levels are complete, which escape in finite time, and how the period diverges. Any β>0 switches an A² law to a logarithm with an exact coefficient; local period reversal forces multiple orbits of the same period for β>α/5. This is a full two-parameter/energy phase portrait, not a tiny numerical case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
