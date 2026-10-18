---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

The explicit parity-lift 32-word construction has only two unbordered binary support patterns 00011 and 00101; changing the pattern flips two coordinates, while a single within-pattern change forces the parity fifth-symbol change, so pairwise Hamming distance>=2. Normalize the first-letter set A and disjoint last-letter set B by relabeling/reversal to |A|=1,2. For both, the complete self-unbordered conflict-graph vertex sets of sizes 180 and 240 are certified by 32 cliques each; every pair within each clique conflicts by a proper overlap or Hamming distance<=1, and all vertices are covered. Fresh independent direct audit of the bundled exact certificate verified all 180/240 vertex identities, the clique pair conflicts and full coverage, plus 32 lower words and all 496 unordered pairs. Thus an independent set has <=32 vertices universally, not merely from solver status. Single-template bound min(l^4,l^3(4-l))<=27 with equality by mod-3 checksum.

## originality

PASS

Blackburn 2013, Levy and Yaakobi 2018, Stanovnik et al 2024 establish non-overlap constructions and unrestricted optima, not the simultaneous exact q=4,n=5,d_H>=2 optimum in the examined relevant results. Published Resultary earlier length-five classification asserts unrestricted max 81, with optimizers I^4J, which cannot be used as distance-constrained classification. Closely relevant Wang/Fang/Feng 2025 restricted-overlap paper could not be read: authorized PDF extraction returned a different 2019 article and cannot be counted as coverage exclusion. Best-of-knowledge PASS with significant residual historical-priority risk.

## value

PASS

This is a natural small exact coding-theoretic extremal invariant with an independently checkable exhaustive upper-bound certificate; optimal size 32 separates mixed-template error detection from the 27-word traditional single-template ceiling, useful for exact finite synchronization code design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
