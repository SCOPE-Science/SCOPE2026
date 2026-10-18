---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Every five-bit candidate x produces exactly seven distinct six-bit insertion outputs, while every six-bit target must be covered by a five-bit predecessor from its six deletion positions. Branching on every possible predecessor of one uncovered target is logically exhaustive; pruning if uncovered count exceeds 7 times remaining chosen centers cannot remove an actual solution. Independently implemented a different bitset DFS on all 32 candidate centers and all 64 targets, ruled out 11 or fewer centers and enumerated six distinct size-12 codebooks; the six optima match the three displayed representatives and their complements/reversals. The independent enumeration used 13,351 nodes; the two repository verifiers use independent branching orders. This is a complete finite-domain proof, not sampled extrapolation.

## originality

PASS

Existing published work treats arbitrary-alphabet/asymptotic insertion covers and length-three small-alphabet tables. Full text of Xie–Sun–Ge 2026 was read, including insertion lower-bound theorem and conclusions; it gives I(q,n,R)>=q^n/(binom(n+R,R)-1), far weaker at q=2,n=5,R=1, and does not enumerate the exact six binary length-five optimal codebooks. Earlier unpublished small exact computations are a reasonable residual risk.

## value

PASS

The minimum number of codewords and all optimum choices at the smallest nontrivial natural binary synchronization-code benchmark provide precise usable design data. A complete labeled census and symmetry classification adds mathematical information beyond merely constructing one code; the channel equivalence group is intrinsic, not an arbitrary partition of a small table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
