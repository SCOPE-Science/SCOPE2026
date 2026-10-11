---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

Koponen's tuple equivalence records a tournament diagram exactly up to one global edge reversal, and overlapping triples force a single preserve-or-reverse mode for any automorphism of the reduct. Hence the automorphism group is the known automorphism/anti-automorphism group. An anti-automorphism can be arranged to fix zero or one named point, but none can fix two distinct points because their directed edge would have to reverse while both endpoints remain fixed. Omega-categoricity therefore gives the exact two-parameter definability threshold. For the type formula, equality patterns with k new classes are counted by inclusion-exclusion, every orientation bit is realized by the random-tournament extension property, and global complement halves the orientations exactly when at most one parameter is fixed. Fresh formula replay reproduces the displayed type counts.

## originality

PASS

The global-reversal reduct and its automorphism group are prior and explicitly excluded from novelty. Koponen constructs the four ternary relations and proves homogeneity, while Bennett's reduct classification supplies the global group context. Neither inspected primary source states the two-parameter recovery threshold or the all-arity finite-parameter type spectrum. Resultary searches found only orbit-profile results for other random structures.

## value

PASS

The theorem identifies the exact finite parameter threshold at which a canonical homogeneous reduct recovers its hidden binary orientation and packages the consequence into a closed complete-type spectrum. This is a natural invariant of a standard reduct, not an arbitrary small computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
