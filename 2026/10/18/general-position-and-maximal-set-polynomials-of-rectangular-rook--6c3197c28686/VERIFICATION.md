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
# Reproducibility and limits

Run `python3 verify.py` after extracting all associated artifacts into one directory. Standard Python 3 is sufficient; no third-party packages are used.

The verifier constructs rook-graph adjacency and all-pairs shortest-path distances by breadth-first search. It classifies subsets by the graph-geodesic condition without using the claimed star-forest equivalence. For each valid subset, it directly attempts all one-vertex additions to test inclusion-maximality. It compares each GP and maximal-set polynomial coefficient with a separate exact recursive star-forest count and inclusion-exclusion/restricted-partition formula. These direct checks cover ten boards and exactly 370,512 vertex subsets. Forty-two further boards are checked symbolically for their maximal-support spectrum and the claimed leading coefficients. The emitted output is in `verification_output.txt` and terminates with `VERIFICATION_OK direct_boards=10 direct_subsets=370512 symbolic_boards=42`.

This is reproducible finite evidence, not exhaustive verification of the infinite quantifiers. Infinite correctness relies on the structural five-step proof in `RESULT.md`. No independent scientific audit was performed.
