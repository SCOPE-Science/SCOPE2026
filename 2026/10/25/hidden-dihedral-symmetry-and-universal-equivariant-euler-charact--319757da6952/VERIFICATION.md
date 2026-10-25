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

# Exact verification and limits

Execute `python3 verify_character.py` in the directory containing this file. The checker uses Python's standard library only and contains its full input-generating procedure.

The recorded execution completed successfully with `ALL_CHECKS_PASS`. It verified 9,686 face candidates against an independent directed-graph cycle test, 9,432 allowed transformations under all eight type symmetries, all twelve cycle-support templates with five exact signed coefficient vectors, and 220 independent full-complex character comparisons on leaf cycle partitions through seven leaves.

The infinite-family result is not extrapolated from the small examples: each invariant simplex contains at most four arcs, so the twelve possible selected leaf-cycle configurations exhaust all possibilities for every parameter. The checker reconstructs all signed binomial coefficients within that finite exhaustive support.

Scientific limits: this computes the alternating character, not separate graded homology characters for arbitrary leaf counts. Independent audit and independent validation have not been performed.
