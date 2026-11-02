---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of finite certificates

The exact theorem and proof are in `RESULT.md`. The accompanying source `verify.py` uses the standard Python library and is self-contained. Command: `python3 verify.py`.

The executed checker directly enumerated 108398 subsets across 13 small rook graphs, tested induced degrees and total domination against their actual graph adjacency, compared counts with a separate bipartite component recurrence, and compared an independently expanded rational exponential series for five parameter pairs. The square two-factor coefficient identity was evaluated exactly for orders two through eight. All tested instances passed and the checker printed `VERIFY_OK`.

This is a finite reproducibility check, not a proof for unbounded graph sizes. The unbounded proof is structural: the degree-sum component classification, labelled exponential formula, two-factor extremality, and the complement-neighborhood argument. Literature-priority comparison has residual risks specified in `REVIEW.md` and `AUDIT.json`.
