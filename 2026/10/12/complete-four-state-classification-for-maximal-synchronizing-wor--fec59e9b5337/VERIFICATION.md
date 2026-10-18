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

Four-state subset recognizer has up to 2^4-4=12 distinguishable reachable states after singleton collapse. Source original verify.py checks all 4^8=65536 ordered letter pairs by reachable-subset minimization and independently by distinguishability table-filling, confirms only maximal pairs have one 4-cycle letter plus one rank-three letter. Independently implemented a separate subset partition-refinement engine over all 65536, confirming complete state complexity histogram, exact 1536 at sc12, normalized rank-three 128/16 antipodal iff split, and 32 classes of orbit size48. Numerical exhaustion is genuinely complete for fixed 4-state finite set, not an infinite inference.

## originality

PASS

Hoffmann 2020/2021 (arXiv:2011.14404) proves general upper bound and sufficient circular rank-(n-1) criteria, explicitly displays four-state maximizer outside those conditions and identifies the missing necessary-and-sufficient characterization. This four-state iff and global 1536/32 census are not implied by his sufficient criteria. Earlier Hoffmann complete-reachability results address necessary structure under an extra reachability premise, not these exact equality cases. Resultary only other automata invariants and five-state classifications; unindexed census remains risk.

## value

PASS

A complete intrinsic obstruction at four states—the first point where the primary sufficient theorem demonstrably fails—answers a structural classification gap named in the primary work. Full orbit census is naturally useful to automata and synchronization researchers, not a random tiny enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
