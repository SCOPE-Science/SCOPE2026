---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For n<=4 all length-(n−1) binary outputs number fewer than nine, so all 2^n inputs are compatible. For n=5..8 the one-deletion-plus-at-most-one-flip sets yield a finite graph whose cliques are exactly admissible codebooks. Independently recomputed every ball and pair intersection, obtaining incompatible pair counts 69,555,2373,7835; every listed witness of sizes 18,26,26,24 satisfied pairwise intersection <9. Inspected CHECKER.cpp bitset construction, two independent ball implementations and its valid recursive proper-color clique upper bound; separately compiled and ran an independent C++ bitset branch-and-bound, matching node counts 19,23,820,6756323 and ruling out larger cliques. The finite exhaustive proof covers lengths 1..8 only; n=8 decline does not assert an infinite monotonicity law or nine physically distinct outputs at every codeword.

## originality

PASS

The nine-read deletion/substitution channel and its asymptotic redundancy constructions are established. The precise finite-length maxima and counterintuitive decline at n=8 were not located in the searched published records, with the primary 2026 full text inaccessible.

## value

PASS

Short-blocklength reconstruction capacity is a natural exact coding invariant; 26 at n=7 followed by 24 at n=8 is a meaningful finite boundary demonstrating that length need not improve size under the precise pairwise read model. It is neither a trivial tiny-instance check nor a general asymptotic theorem; bounded 1..8 scope is explicit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
