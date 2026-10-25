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

Run `python3 verify.py` using Python 3.10 or later, with no external packages. The script independently enumerates directed edge orientations, sink/source flips, connected components, and the cubical face data for its chosen graphs. It constructs all mod-two two-boundary vectors and computes the first mod-two Betti number rather than assuming the published homotopy classification. It then enumerates oriented core cycles from cyclic vertex orders, tests graph-automorphism images, and verifies that arrow reversal turns all sink-directed edges into source-directed edges.

The completed output in `verification_output.txt` reports 18 graphs, 126 connected components, 48 circular components, 256 square boundary checks, and 582 automorphism/core instances, terminating with `VERIFY_OK`.

The finite calculations do **not** establish the general core-cycle collapse or rule out unexamined literature. The infinite-family proof uses Kozlov's 2026 Theorem 6.1 for core cycles and Theorem 5.18 for the homotopy dichotomy, then gives an independent cocycle, normalization, and equivariance argument. The proof concerns cellular and singular integral homology of the actual cubical complex, not merely the one-skeleton.
