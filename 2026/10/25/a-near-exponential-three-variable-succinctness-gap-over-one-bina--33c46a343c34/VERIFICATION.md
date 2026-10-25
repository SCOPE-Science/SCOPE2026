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

# Verification record

A direct finite checker (`fixed_signature_gap_checker.py`) executed and returned:

`FIXED_SIGNATURE_CODE_AND_BLOCK_SIMULATION_OK 640`

For \(2\leq r\leq5\), it randomly sampled relations on nonempty domains of sizes one and two, checked the exact tagged-path recovery of each source relation, checked the hard two-edge profile query for even \(r\), and compared blockwise simulation to the full finite adjacency relation for all standard Boolean, converse and composition operations. The checker does not search all input structures, nor does it enumerate relational circuits. The universal bound follows instead from three statements proved in the written result: the bit-path recovery lemma, the \(M_k^3\)-per-composition block simulation, and reduction to Uezato's published Theorem 1.3. Independent replication and an independent mathematical audit have not been performed.
