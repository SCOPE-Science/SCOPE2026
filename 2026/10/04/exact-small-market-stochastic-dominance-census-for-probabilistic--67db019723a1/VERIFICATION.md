---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The mechanism definitions were reconstructed with exact rational arithmetic. Independent enumeration gives n=1: one equal profile; n=2: four equal profiles; n=3: 144 equal and 72 incomparable profiles. For n=4, independent enumeration of all 17,550 anonymous ranking multisets with exact label multiplicities gives 72,288 equal, 11,664 PS-dominant, and 247,824 incomparable labeled profiles, totaling 331,776 and giving 11,664/331,776=9/256. The package's independent Burnside/object-relabel route yields 209/36/517 symmetry classes, and its exhaustive dominance stratum gives exactly four two-order classes. Finite enumeration is exhaustive here because the theorem itself is confined to n<=4.

## originality

PASS

The known four-agent PS-over-RSD witness, three-agent incomparability witness, and the fact that RSD cannot strictly dominate the stochastic-dominance-efficient PS outcome are prior. The new content is the exhaustive labeled split through four agents, the exact 9/256 four-agent dominance probability, the complete 209/36/517 symmetry quotient, and the four minimal two-order dominance classes. The inspected direct-comparison paper studies examples and empirical mechanism comparisons rather than this exact complete census.

## value

PASS

The result gives the first exact calibration at the smallest market where strict PS dominance occurs, replacing sample-based intuition by a complete distribution and symmetry classification. The four minimal two-order classes also isolate the simplest dominance mechanisms. This is a natural finite classification of two canonical assignment mechanisms rather than an arbitrary census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
