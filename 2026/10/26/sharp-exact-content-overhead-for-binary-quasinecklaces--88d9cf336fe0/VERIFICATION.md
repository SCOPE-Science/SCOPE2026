---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Definition 3 in Gabrić–Sawada reduces over binary symbols to 0^ell 1 followed by r-1 bounded zero-gap blocks 0^ei 1, 0<=ei<=ell, sum ei=z-ell. This bijection yields the coefficient enumerator. Every nonmonochromatic primitive rotation orbit contributes exactly one admissible start per longest zero-run, implying N<=Q<=z N. Burnside formula has leading r^(z-1)/z! and bounded-composition count r^(z-1)/(z-1)!, so Q/N -> z for each fixed z, including z=1 separately. Independent full binary enumeration through length 12, 777 primitive-orbit checks, and fixed z large-r integer checks passed; unrestricted result is analytic.

## originality

PASS

Best-of-knowledge PASS, with actual primary statement/implication comparison and listed residual priority risks; an unsuccessful search is not historical novelty proof. Existing exact-density pseudonecklace generation cannot be substituted for a cardinality theorem about the larger Gabrić–Sawada quasinecklace set. The latter definition has an elementary binary specialization but the sharp fixed-content overhead is not asserted in the inspected source. Length-only/bounded-weight cardinality bounds are aggregate and do not imply a uniform fixed-content ratio. The present theorem does not claim algorithmic firstness or exclude alternate exact-density algorithms.

## value

PASS

Exact-content analysis matters because length-only or bounded-total-weight amortized generation guarantees do not imply a fixed-weight guarantee for this PARTICULAR candidate superset. The exact run-multiplicity and all-content enumerator give a natural structural classification with sharp overhead z, explicitly not an impossibility theorem for alternative exact-density CAT generation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
