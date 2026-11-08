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

Shift u=x-K/2 and complete the logistic square: u'=-u^2/K-P(K/2+u)y, y'=[P(K/2+u)-P(K/2)]y. Positive y makes u strictly decreasing. If u<=0 it reaches x=0 in finite time by Riccati comparison. On a hypothetical global u>0 trajectory, u->0, ∫u² dt<=Ku(0), and ∫u dt=∞, since a finite ∫u would leave y bounded below away from zero and force a crossing. z=u²/y has exactly z'=-2P(r+u)u-[2u/K+P(r+u)-P(r)]z. For alpha<=2, the bracket is bounded below by -Cu², so its integrating factor stays positive and the integral ∫P u diverges, forcing z negative: contradiction. For alpha>2, on y=cu², c<(alpha-2)/(2KP(r)), the outward derivative is negative near u=0, while u' is between two negative multiples of u², proving a nonempty positively invariant wedge with no finite-time boundary contact. Rational derivative alpha=-4K²(bK+4)/(aK²+2bK+4)² and explicit parameter triples verified symbolically; the theorem is for all positive initial predator data on the exact critical parameter surface, not trajectories continued through negative prey densities.

## originality

PASS

Best-of-knowledge originality PASS after searches and real statement-level primary comparisons; no source found to imply the exact final claim. Explicit historical/inaccessible-source risks remain: An unlocated general nilpotent-flow/global extinction result might imply the threshold after a nontrivial reduction; current primary comparison cannot certify historical priority.; Survival wedge is sufficient, not the whole basin; positive coexistence not claimed; exact K/4 and mortality matching are essential.

## value

PASS

Constant harvesting at the logistic maximum sustainable yield is a canonical degenerate predator-prey threshold; arbitrarily small predator densities may either force biological prey extinction or lie in an open surviving basin. The derivative threshold 2, including its equality side and rational group-defense realization, supplies an exact phase boundary rather than a textbook local linearization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
