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

# Reproducibility

Run `python3 verify.py` with SymPy 1.12 or later. The checker constructs the characteristic-specific forms and the six \(2\times2\) minors of their Jacobian matrix, then for each \((p,c)=(2,1),(3,2),(5,2),(7,3),(11,2)\) sets each homogeneous coordinate to one in turn. It checks that the saturated singularity locus has no point in any projective chart: the corresponding ideal has Gröbner basis \([1]\) over the stated prime field. It also checks the rational point in each case. The script executed successfully with SymPy 1.14.0.

# Scope of the checks

These are five characteristic-wise sample checks over prime fields; they are **not** an exhaustive check of all prime powers. The universal smoothness proof uses the gradients directly and treats each characteristic, while the nonsplit Witt-index-one property supplies the gonality lower bound. The projective canonical-model and Riemann–Roch arguments are mathematical, not program-certified.
