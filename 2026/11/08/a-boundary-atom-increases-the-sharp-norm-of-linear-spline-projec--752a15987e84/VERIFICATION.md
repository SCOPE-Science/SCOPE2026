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

# Reproducible calculations

With Python 3.10+ and SymPy 1.12 or later installed, run `python verify_leaf_atom.py` in the same directory. All arithmetic in the independent finite examples is performed using exact rational fractions. SymPy verifies the universal parameter identities symbolically rather than sampling them.

The checker verifies the full rational formula for the leaf-kernel norm, the center and atom-leaf formulas, strict-dominance numerator factorizations, the exact derivative identity, and both parameter limits. It separately assembles and inverts \((m+1)\)-by-\((m+1)\) Gram matrices for arm counts from two through ten and seven nonnegative rational atom masses per count. It integrates absolute linear kernels exactly on all edges and adds the atomic contribution; every independent matrix result matches the exact analytic formula, reproduces constants, and yields the predicted norming vertices. Successful output ends with `ALL_LEAF_ATOM_SPLINE_CHECKS_PASSED`.

The proof in `RESULT.md` independently establishes the signs of the coefficient polynomials and the all-parameter claims. Finite examples by themselves do not establish a universal inequality, nor does symbolic identity checking alone establish the kernel-to-norm or norming-location arguments. No external audit or certification has occurred.
