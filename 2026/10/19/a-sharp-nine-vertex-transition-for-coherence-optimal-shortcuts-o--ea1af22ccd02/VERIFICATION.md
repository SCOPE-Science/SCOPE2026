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

Execute `python3 verify.py` (Python 3; standard library only) next to this document. The actual packaged code was executed after extracting it from the complete ledger finding and returned:

`VERIFY_OK direct_rational_inverses= 304 global_exact_chord_comparisons= 246536 macroscopic= [(100, 75, 12), (200, 151, 24), (400, 301, 49), (800, 601, 99)]`

The 304 tests construct the unit path plus one shortcut, invert the shifted connected Laplacian over exact rational numbers, and compare its pseudoinverse trace to the closed formula. The 246536 comparisons evaluate all eligible edges of each tested path and verify the endpoint/critical-tie/strict-loss assertions at exact selected conductances; four additional sizes test convergence of optimal spans and tails. No floating-point comparison determines any scientific conclusion. The infinite-size assertions are proved symbolically by the ramp variance, a factored comparison identity valid for all integer sizes and spans, and a strictly concave limiting gain. Tests are supporting evidence, not exhaustive infinite certification. No independent audit has been performed.
