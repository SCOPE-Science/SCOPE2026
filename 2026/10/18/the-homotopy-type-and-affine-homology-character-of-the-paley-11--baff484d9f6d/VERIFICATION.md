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
# Verification and scope

Reproduce the two deterministic calculations with Python 3 from the package directory:

`python3 check_structural.py`

`python3 check_equivariant.py`

The former enumerates all nonempty faces of the eleven out-neighborhood facets, confirms the difference-set intersections, checks all missing-triangle orbit fillings, and tests each of \(55\) elementary free-face collapses against the evolving simplicial complex. It must report \((1,11,55,110,55,11)\) in cardinalities zero through five and \((1,11,55,66,0,0)\) after the collapses. The latter independently calculates the signed fixed-face Lefschetz traces for every affine automorphism and the invariant dimension. Compare output against `structural_output.txt` and `equivariant_output.txt`.

The proof in `RESULT.md` explains why these finite checks certify a complete fixed eleven-vertex computation, why the remaining complex is simply connected, and why the resulting integral homology implies the homotopy statement. No extrapolation to other tournament orders is claimed. The quotient computation is rational only.

Self-review: passed. Independent audit: not yet performed.
