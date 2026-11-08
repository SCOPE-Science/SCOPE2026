---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For each ordered pair of four-subset embeddings A,B with |A∪B|=t, either their common positions demand incompatible pattern letters, giving zero, or their joint probability is 2^(−t). Counting valid ordered pairs on [t] produces the exact formula E[X_p²]=Σ_{t=4}^8 c_t(p)2^(−t) C(n,t) for every n≥4; mean C(n,4)/16 is immediate. Independent enumeration of all ordered four-subset pairs reproduced the thirty c_t entries for the six reversal/complement orbits: 0000=(1,20,90,140,70), 0001=(1,14,60,110,70), 0011=(1,12,56,104,70), 0010=(1,10,44,94,70), 0110=(1,10,42,84,70), 0101=(1,8,36,80,70). Adjacent rows are coefficientwise nonincreasing, with strictness at n≥6, only the 0010/0110 tie at n=5, and complete n=4 equality; degree-eight cancellation and c7 differences give leading n^7/645120 multipliers 70,40,34,24,14,10. The finite coefficient enumeration is exhaustive because t≤8; it proves the all-n theorem via the exact subset-pair identity.

## originality

PASS

Qualified PASS for the evaluated six-orbit exact second-moment table, universal n≥6 strict variance hierarchy and sevenfold asymptotic ratio, not for the classical overlap approach or common expectation. Menon–Singh analyze binary subsequence frequencies and symmetry and broader hidden-word methods may imply individual formulas algorithmically, but the inspected primary texts do not state this complete comparison.

## value

PASS

All sixteen length-four binary scattered patterns form a natural first moderately rich case of exact subsequence-count fluctuation comparison. The six-orbit hierarchy gives exact finite-n variances and a sharp universal strictness threshold, with constant-pattern fluctuations seven times alternating in the leading order despite equal means. An independently useful comparative statistic beyond a routine restatement of expectation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
