---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Fixing x_ABC solves the rank equations with direction (+,-,-,+,+,-); remaining equations follow from the margins and nonnegativity gives the two interval ends. The three pairwise counts give the exact strict-win intervals. A winner has 2F+M>n, hence F>L, so at most two candidates qualify across the whole fiber. If two winners occur d steps apart, their shared contest reverses strictly, forcing d>=1 (odd n) or d>=2 (even n). Remove d oppositely oriented cyclic triples from the two profiles, leaving the same n-3d ballots. Each winner has a deficit d against its disadvantaged rival in its cyclic block, so n-3d>d. At the two first layers d is respectively 1 or 2 and there are 2d common ballots. Cyclically label the winners A in the positive cycle and B in the negative cycle. Residual margins must exceed d against C for both, so by parity all residual ballots rank C last. The AB contest must reverse, forcing equal residual counts of ABC and BAC. This gives exactly the stated three matrices at each threshold; their endpoints and even midpoint yield the stated outcomes. Multinomial weights and the strictly decreasing successive ratio give all conditional probabilities and strict log-concavity. Independent finite JS enumeration (replay: /workspace/review-check-2.js) checked 8007 profiles and 6291 matrices, reproducing the first layers and weights (60,60) and (18900,100800,18900). The computation is finite; the cyclic-triple proof provides the all-n bounds. In the frozen text nu in the interval denotes the just-defined u; this is a notational typo, not a different endpoint.

## originality

PASS

The supported distinct contribution is the exact classification of strict-winner switches and conditional outcomes within a three-candidate position-matrix fiber, especially the sharp parity thresholds and complete first layers. It is not a priority claim for elementary rank-equation elimination, a necessary feasibility inequality, or multinomial counting. The closest inspected prior statements do not give this classification or imply it by direct specialization.

## value

PASS

Position counts are a natural lossy summary of ballots. The result gives a complete constant-size decision for what can survive this loss with three alternatives, and identifies and classifies the smallest strict-winner reversals, including the doubling imposed by even-electorate ties. These are useful exact structural and probabilistic boundaries, not merely a small profile census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
