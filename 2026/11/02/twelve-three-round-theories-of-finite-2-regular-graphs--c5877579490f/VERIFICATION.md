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

# Reproduction and boundaries

Run `python3 verify_2regular_types.py 24` to enumerate all 572 finite cycle-partition graphs with orders 3 through 24. The program constructs explicit adjacency matrices, forms atomic triple types (including equality), and recursively constructs one-, two-, and three-round extension sets. It asserts exactly twelve types and the agreement with the proposed classification.

Run `python3 verify_2regular_game.py` for an independently written adversarial minimax game solver. It asserts pairwise rank-three non-equivalence of all twelve minimal representatives and ten additional positive equivalences.

The attached `verification_output.txt` reproduces both successful command outputs. These programs run with the Python 3 standard library only. The infinite generality follows from the pair-extension proof, not from the finite checks. All statuses are self-review only; independent audit was not performed.
