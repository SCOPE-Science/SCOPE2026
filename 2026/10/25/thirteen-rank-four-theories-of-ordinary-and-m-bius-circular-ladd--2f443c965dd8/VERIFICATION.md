---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Verified finite simple cubic ladder definition on 2n vertices, n≥3, with last-to-first twist. Exact FO quantifier rank four is described by T0 atomic diagrams and T_{r+1} as the set of all one-vertex extension T_r types, including equality/repeated choices; by induction this captures both existential and universal rank-four formulas. Reconstructed the radius-two local-window argument: for n≥16 no 4-round type depends on long wrap or the twist, giving a common eventual type. Reimplemented an exact finite type recursion independently of package code for every n=3..16 and both twists (28 graphs): found exactly 12 different low-n theories and a single identical common type for n=9..16; no low-n type equals it. The n≥16 uniform locality proof bridges the unbounded part. The maximum minimum representative size within these families is therefore 18, reached by n=9. Finite enumeration by itself is not used for the infinite n statement.

## originality

PASS

Qualified PASS: Brown–Hoshino analyze rank-four Ehrenfeucht–Fraïssé classification for paths and cycles; their cycle threshold is not a cubic ladder/Möbius-ladder theorem. Heinig analyzes prism/Möbius ladders for Hamiltonian cycle-space generation, not FO rank-four type. The explicit thirteen-class ladder/twist classification with sharp n=9 threshold does not follow from either inspected result; related local-model-theoretic general stability theorems may imply coarse eventual convergence but not these exact small thresholds without additional calculations.

## value

PASS

PASS: the exact quantifier-rank-four equivalence partition of two natural graph families is a complete classification of a fundamental finite-model-theory invariant. The twist-invisibility threshold and optimal representative-size bound are crisp, nontrivial finite/infinite boundary results; the exact finite bridge plus infinite locality argument makes this more than isolated experiments.

The dated certificate retains the supplied scientific assessment, sources and limitations.
