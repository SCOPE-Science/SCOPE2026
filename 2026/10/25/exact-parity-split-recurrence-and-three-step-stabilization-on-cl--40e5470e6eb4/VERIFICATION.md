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

# Reproducibility and verification

Run `python3 verify_clique_corona.py` with Python 3.9 or later. This standard-library script constructs the clique and each private leaf as an explicit adjacency list; the vote calculation uses direct neighbour sums and independent tie handling, not the proof's reduced core recurrence. It exhaustively tests all `349504` labelled states at clique orders 3 through 9; for each it checks the least entry time into period one or two, the fixed count and the distinct primitive-two-cycle population against the displayed formulas. Expected terminal output: `CLIQUE_CORONA_MAJORITY_VERIFY_OK`. Recorded output is in `verification_output.txt`.

All seven exhaustive runs succeeded after extraction to their actual package paths; the verifier does not test an infinite set of graph orders. The universal correctness argument is mathematical, in `RESULT.md`. Asymptotics follow by central-binomial estimates, rather than simulations. The open-neighbourhood convention and tie retention are stated explicitly in the proof. No independent audit has been performed.
