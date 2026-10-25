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

# Reproduction

From the unpacked package directory run `python3 verify_layer_swap.py`. The checker uses exact integer bitmasks and GF(2) elimination. Its five parameter cases are `(2,2)`, `(2,3)`, `(3,2)`, `(2,4)` and `(3,3)`; for each it enumerates every independent face and every fixed face, checks the signed Lefschetz formula, and evaluates the ambient mod-two boundary ranks. The last expected line is `LAYER_SWAP_FIXED_SPACE_AND_TRACE_CHECKS_PASSED 5`.

This finite check is not the source of the all-parameter theorem. The written proof uses an exact geometric-fixed-space identification, the complete bipartite nerve, integer cycle kernels, the classical Lefschetz identity, and the published triple-product sphere-wedge theorem. This check is mathematical self-consistency evidence only, with no claim of independent audit.
