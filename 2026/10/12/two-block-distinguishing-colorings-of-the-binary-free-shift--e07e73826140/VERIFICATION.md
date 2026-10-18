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

Every connected component of the free shift graph is a bi-infinite path, hence its maps are translations or reversals. Injective ordered-pair colors decode the input; translations then fix vertices and a reversal would impose x_{j+2}=x_j, impossible on the aperiodic set. Each of six unordered pair collisions admits a one-defect or step-sequence witness with an explicit reflection, so each noninjective rule fails for the whole graph. The six complete algebraic constructions work at all integer positions, not just tested ranges. Independent 256-rule, -35..35 finite checks confirmed the witnesses and 24 injective 4-color rules.

## originality

PASS

The unrestricted Borel distinguishing number three (Chen–Zou) and abstract orbit-map criterion concern an entirely broader class and do not state the complete iff classification for homogeneous 2-block maps; Bilge–Kaya gives general Borel distinction; shift-graph chromatic work addresses proper color rather than arbitrary automorphism breaking. Direct check of implications shows palette 3 lower bound in the broad class does not imply a four-color local threshold; a general orbit criterion alone still requires a six-collision classification. Best-of-knowledge local two-block result survives.

## value

PASS

The first nontrivial fixed finite-window neighborhood on a canonical descriptive-combinatorics shift admits complete uniform rule classification. Its four-versus-three locality obstruction is conceptually informative for symbolic factors and Borel distinguishing constructions, not just an arbitrary finite enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
