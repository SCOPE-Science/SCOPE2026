---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The definition requires disjoint nonempty proper prefix/suffix for every ordered pair, including self pairs. Distinct selected words cannot occupy the same primitive length-n cyclic orbit. For n=5..12 Mobius inversion gives necklace limits (1,2,5,8,14,20,30,40). Independently rebuilt all fixed-weight-four words and cyclic orbits; checked actual complete certificate.json codebooks of sizes 1,2,5,8,14,20,30,39 are pairwise nonoverlapping and self-unbordered. At n=12, independently enumerated all 495 words, precisely 128 eligible ones, and validated the 39 disjoint cliques as covering the entire eligible set with pairwise conflicts. Thus an admissible code contains at most 39, and given 39-word code attains it. n=4 only word 1111 self-bordered. Finite enumeration is exhaustive in the asserted interval, not an infinite-length proof.

## originality

PASS

Best-of-knowledge PASS: the first strict deficit for primitive-orbit transversals under the *pairwise* cross-bifix restriction is a new exact fixed-weight packing statement compared with inspected unrestricted bounds and primitive-word counts. Historical constant-composition coding tables may conceal an alias; search silence is not proof.

## value

PASS

This is the first natural failure of the standard primitive-necklace packing upper bound for fixed weight four, with a global pairwise-compatibility obstruction beyond counting orbits and a dual certificate that another researcher can directly reuse in synchronization-code extremal problems. The finite cutoff n=12 is mathematically motivated by first failure and proved exact, not a random sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
