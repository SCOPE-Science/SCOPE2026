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

Execute `python verify.py` from the extracted package (requires SymPy). It checks the determinant expansion, five partial derivatives, six-minor Pluecker quadric equation, the four displayed annihilator syzygies, the characteristic-three isolated base point outside the cubic, a rank-four linear reconstruction witness modulo characteristics two, three, five, and seven, and the branch-discriminant formula. A successful run prints `VERIFY_OK`.

The infinite-field assertions rely on the reconstruction and projection proofs in RESULT.md, including a nonempty open rank-four locus and the exact ideal-intersection argument. The finite characteristic checks alone are not used to infer uniform proofs. The degree-two comparison assumes \(\operatorname{char}k\ne2,3\); characteristic two is explicitly excluded from the finite-degree assertion. Independent audit has not been performed.
