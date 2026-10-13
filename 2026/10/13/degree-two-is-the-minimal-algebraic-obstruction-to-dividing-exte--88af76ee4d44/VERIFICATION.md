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
# Verification

The proof has two conceptual parts. The universal lower bound is formal: an algebraic tuple with orbit size one over the parameters belongs to definable closure, and dividing independence preserves definable closure. The sharpness part uses the published generic-binary-function configuration and an explicit pairwise-inconsistent formula family.

Run `python3 artifacts/verify_degree_two.py`. The script checks three finite combinatorial facts used in the sharpness argument:

1. the setwise stabilizer of a two-element unordered pair has exactly two images of an ordered lift;
2. left-zero finite function patterns with one fixed common point are invariant under every permutation of the varying points, matching the indiscernibility symmetry used in the compactness construction;
3. for every tested family size, the constraints `f(x,c)=u_i` with fixed `c` and distinct `u_i` are pairwise inconsistent, which is the finite core of the dividing witness.

Expected output:

`VERIFY_OK 531279 exact assertions`

The finite computation is a sanity check. Existence of the infinite indiscernible sequence follows from compactness and quantifier elimination in the source theory, and literature priority is not tested by the script.
