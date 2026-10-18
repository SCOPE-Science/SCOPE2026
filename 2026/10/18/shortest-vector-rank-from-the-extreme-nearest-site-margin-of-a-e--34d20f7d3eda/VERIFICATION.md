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

The proof is analytical and self-contained in `RESULT.md`. The finite regression checker `check_lattice_margin.py` was run using the ordinary Python standard library, with exact rational halfplane clipping on two nonorthogonal planar lattices and independent three-dimensional lattice competitor comparisons. Its terminal success marker was `LATTICE_MARGIN_TAIL_OK`; detailed intermediate values are reproduced by running the script.

The checker confirms the exact covolume in planar Voronoi polygons and rational near-endpoint area ratios at multiple parameter values; it additionally checks the three possible shortest-vector ranks in dimension three for orthogonal lattices. These are finite tests, not formal certification of the all-dimensional proof. The theorem has no unverified numerical premise. An independent mathematical audit has not been performed.
