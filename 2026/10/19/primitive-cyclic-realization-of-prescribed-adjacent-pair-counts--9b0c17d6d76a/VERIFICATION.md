---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Balance and weak connectivity of the active support give strong connectivity (a nontrivial condensation source would have an unbalanced cut) and hence an Euler tour. For branching at at least one vertex v, cut a tour at every visit to v. Permuting the resulting first returns preserves all arc multiplicities, and two distinct successor symbols guarantee two distinct vertex-sequence types. Group equal types in one block each. Any ordered boundary between adjacent distinct types occurs exactly once in the cyclic list. A symbol rotation fixing the word must carry all v-occurrences to v-occurrences and preserve their excursion types and boundaries. It therefore fixes the unique occurrence of such a boundary, hence is the identity rotation. Without branching, the strongly connected functional support is a simple directed cycle whose arc multiplicities agree by balance. The least word period is the number d of active vertices, and the obstruction is exactly repetitions r=n/d>=2. Choosing d active labels and a directed cycle gives binom(q,d)(d-1)! distinct matrices per proper divisor d<=q; this includes loops, n=1, and the prime-length consequence. No finite census or external certificate is needed for the exact proof; the supplied script was inspected but not executed.

## originality

PASS

Pass the existence classification by active support and resulting divisor-sum obstruction count for a fixed adjacent-pair profile, not the Euler criterion, the general primitive-necklace census or the total count of Markov types.

## value

PASS

The result resolves exactly which prescribed finite cyclic transition counts force periodicity, a natural realizability question about type classes. Its support-only criterion works even if all multiplicities have a large common divisor, and yields a constructive witness plus a clean exact census of exceptions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
