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

# Verification and boundaries
The analytic proof follows from the character-sector rank formula, the nonvanishing of finite-field Gauss sums for nontrivial multiplicative and additive characters, cyclic determinant expansions, and counting character values on an element of known finite order. This yields a complete result for all prime-power alphabets and all cycle sizes at least three.

Run the included `verify.py` using Python 3 with NumPy. The script directly constructs bilinear-phase sampling matrices for prime fields, and extends direct tests to the characteristic-two extension field of four elements using exact trace signs. It reports 184 prime-field and 18 order-four field comparisons. Floating-point rank tests are numerical sanity checks; the proof of the infinite parameter family is symbolic and does not rely on a numerical threshold.

No proof of the analogous problem for arbitrary support graphs, partial axis samples, or quantitative conditioning is asserted. Independent validation is not yet performed.
