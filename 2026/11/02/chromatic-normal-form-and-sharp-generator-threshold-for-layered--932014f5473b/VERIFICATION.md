---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Finite colour-preserving bisimulation agrees with modal formula indistinguishability by explicit stable partition refinement. Necessity: two same-level same-colour points and any lower point matching its unique immediate upper singleton admit bisimulation. Sufficiency: downward induction separates pairs using an extra immediate-upper successor when that level has size ≥2; singleton adjacent level is excluded by colour inequality; nonadjacent levels separate by accessible intermediate witnesses. Counting injective assignments top-down yields falling factorial and exact chromatic polynomial. The sharp rank and q/h window follow by positivity of falling factorials and log expansions. Independent direct partition-refinement verified 24 small compositions/palettes against local criterion and count, including direct Boolean closure cases; finite checks only supplement the full proof.

## originality

PASS

The new mathematical object is the exact conflict graph and quantitative named-generator count for finite partial-order antichain layers. General finite bisimulation and modal local-finiteness results do not provide the adjacent-singleton conflict rule or enumeration. A known chain specialization and finite modal separation are classical, credited. Older modal algebra generator-count and distinguishing-colour results under other terminology remain plausible.

## value

PASS

A nontrivial order-specific characterization turns a modal algebra generator problem into a chromatic polynomial, giving sharp minimal ranks and random saturation thresholds. The asymmetric singleton obstruction is structurally informative, as illustrated by two- versus one-generator cases after reversing layer sizes; it is not an arbitrary substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
