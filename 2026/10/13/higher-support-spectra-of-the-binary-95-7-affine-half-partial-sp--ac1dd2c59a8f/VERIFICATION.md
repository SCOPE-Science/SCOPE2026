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

# Computational verification

Running `python3 verify.py` with a Python 3 interpreter requires no external packages. The completed check reports `VERIFY_OK` and prints both generalized-weight arrays and both minimizer-count arrays.

It enumerates all distinct subspaces of the seven-dimensional message space using their unique reduced-row-echelon bases. For each normal type, it computes *two* full distributions at every dimension: the support cardinality of the span of generator-message rows, and the number of generator columns lying in each orthogonal complement. The two full distributions agree, not only their minima. The total numbers of subspaces in dimensions zero through seven are `1, 127, 2667, 11811, 11811, 2667, 127, 1`.

The code uses the exact binary field, all 63 nonzero evaluation points, and all 32 affine-hyperplane duplicates. The two chosen normals are `1` and `9` in the bit-label convention specified in the proof. The class reduction for arbitrary nonzero normal and arbitrary two complementary three-subspaces is a mathematical basis-change argument, not an extrapolation from random tests.

Limits: This is an exhaustive finite proof for the stated 95-coordinate cases. It does not decide general larger-dimensional formulas, nor does it amount to an independent audit.
