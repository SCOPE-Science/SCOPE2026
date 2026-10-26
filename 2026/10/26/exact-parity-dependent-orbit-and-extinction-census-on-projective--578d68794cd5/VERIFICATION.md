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

The adjacent file `verify.py` is self-contained Python 3.10+ standard-library code. Run `python verify.py` from this directory. It constructs projective point–line incidence arrays using finite fields of orders 2, 3, 4, 5, 7, 8 and 9; constructs the bipartite adjacency operator directly; compares all matrix powers and ranks from the proof; and verifies recurrent/fixed counts and exact entry-depth formulas. The order-two case independently checks all 16,384 labelled states. For each other tested order, it checks 129 deterministic trajectories. The output is recorded in `verify_output.txt` and ends with `PROJECTIVE_PLANE_PARITY_VERIFY_OK`.

Scientific proof is the symbolic incidence-identity and rank-nullity argument in `RESULT.md`. Enumeration at one finite order and sample trajectories at other orders are finite checks, not a general completeness argument. The check does not provide independent scientific certification, nor does it determine arbitrary non-Desarguesian incidence ranks.
