---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS: From frozen RESULT.md/verify.py definitions, reconstructed all 720 permutations, each exact-two-consecutive-deletion/standardization descendant mask on the 24 S4 outputs, and 610 distinct nonempty masks with multiplicities. An independent exhaustive subset recurrence selecting the first uncovered receiver yields maximum 12, 67,163,560 labeled code choices and exact union-footprint histogram (16:100,17:3240,18:47958,19:415120,20:2283083,21:8134400,22:18331932,23:23922912,24:14024815), visiting 525,881 receiver subsets. Weighted counts take a multiplier equal to the number of source permutations sharing a mask, with no overcount by first-uncovered-word partition. Verified submitted 12-permutation perfect witness covers all 24 outputs pairwise disjoint. Exhaustive finite dynamic programming is a complete proof for the explicitly finite S6 domain, not a timeout or sampling claim.

## originality

PASS

PASS (best of knowledge): The model coincides with fixed exactly-two-burst PBUD, not at-most-two bursts. Chee et al 2015 and 2020 develop the general model, constructions and asymptotics, with no specific S6 exact all-optima/footprint/perfect-code tabulation in materially accessible descriptions. Resultary yielded different deletion channels, binary length-six codes, and other permutation models, not this identical S6 finite census. Protected Oxford full-text retrieval of the closely relevant 2020 paper was blocked by disconnected institutional VPN; risk retained.

## value

PASS

PASS: S6 is a natural smallest nontrivial exact fixed two-burst instance, and full maximum-code/all-extremizer/perfect-packing structure supplies useful baseline for permutation-burst constructions; neither the exact histogram nor its natural receiver-covering interpretation is a routine translation of generic sphere packing bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
