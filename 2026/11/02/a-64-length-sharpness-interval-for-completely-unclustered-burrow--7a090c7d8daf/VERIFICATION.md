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

For ordered alphabets of cardinality k>=3 and every integer 31<=n<=64, the classical factor-two inequality r(BWT(w))<=2 r(w) for the Lyndon primitive representative gives r_cyclic(w)>=ceil(n/2), since its endpoints differ. The proposed upper bound is not inferred from a search: witnesses.tsv contains exactly one ternary last-column word of each of the 34 lengths. Independently constructed the stable LF first-column permutation, verified it is an n-cycle, inverted it into a primitive input, explicitly sorted all n cyclic rotations to reproduce the last column, checked every linear adjacent last-column pair differs and counted exactly ceil(n/2) cyclic source transitions. Every 34 independent checks passed; third-symbol counts are exactly 14 with 2 occurrences, 16 with 4, 4 with 6, each a perturbation of binary alternating. This verifies the finite certificates and their all-alphabet extension without confusing existence at 34 lengths with a proof at all lengths.

## originality

PASS

Qualified best-of-knowledge originality: compared the exact statement and its logical implications with the cited same-object published results and accessible full texts; prior covered portions are acknowledged, and inaccessible high-relevance papers are recorded explicitly rather than presumed not covering. See four structured checks and source inspections.

## value

PASS

The 34 sharp length instances lie in the explicit conjectural finite range of a natural BWT extremal run problem. Certifying the remaining 28 lengths beyond six existing arithmetic examples provides a usable exact partial resolution and sparse ternary examples for future constructive classification. Finite scope is mathematically motivated by known nontrivial sharpness, not an arbitrary numeric slice; it does not falsely claim the global conjecture.

The dated certificate retains the supplied scientific assessment, sources and limitations.
