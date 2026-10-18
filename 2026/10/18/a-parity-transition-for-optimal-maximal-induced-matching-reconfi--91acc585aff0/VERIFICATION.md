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

The standalone standard-library Python checker `verify_induced.py` reconstructs the subdivision from vertices and actual host-graph edges; it checks edge compatibility by graph adjacency, not by the arrow-map theorem. For each order from 2 through 9, it enumerates all induced matchings (including the empty set), flags maximality by direct addable-edge tests, computes the coefficient distributions, and compares these with exact factorial/Stirling expressions. It then constructs minimum-solution adjacency by direct symmetric-difference-one swaps and checks parity-dependent degrees, component sizes and counts.

Run with `python3 verify_induced.py`. The expected transcript is in `verification_output.txt`, and the checker prints a final `VERIFICATION_OK` only after all assertions pass. Across all profiles it examines exactly 342630 induced matchings.

The proof in `RESULT.md` is an infinite-family argument independent of the finite computation. No exhaustive computational assertion is made beyond the tested range. The reconfiguration model allows one edge removed and another added in one atomic move; intermediate deletion-only states need not be inclusion-maximal.
