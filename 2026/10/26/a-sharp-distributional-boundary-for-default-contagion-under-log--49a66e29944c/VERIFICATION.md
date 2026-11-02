---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Acyclic clearing makes source shortfall max(0,z−x), with each target losing 1/m thereof, so all targets default exactly when z>(m+1)x; cap not active for (m+1)x<1. Independent direct defaults require each primary loss >x. With S(0)=1 and f=log S convex, Jensen gives f(qx)≥q f(x), q=m+1. Exponential rate mixtures have f second derivative equal tilted rate variance and hence strictly >0 when nondegenerate; constant rate gives equality. Independently checked source/target balance sheets, strict mixture and pure exponential equality on 21 feasible samples. No conclusion for arbitrary network topology, correlated shocks, or aggregate losses.

## originality

PASS

Qualified best-of-knowledge PASS: prior objects, algorithms and general identities acknowledged; independent exact classification/asymptotic/construction is not established by the material read. Specific implication and inaccessible-source risks explicitly retained.

## value

PASS

The exact attainable reverse-probability boundary in an economically standard, fully connected-liability star qualifies the general IFR comparison: even non-heavy-tailed exponential mixtures make contagion strictly more likely than independent joint defaults at every feasible threshold, whereas homogeneous exponential rates sit at equality. Though proof is elementary Jensen, the natural specified event and exact saturating network give a motivated counter-boundary; no broad arbitrary-network significance is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
