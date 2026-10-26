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

# Reproducible exact checks

The accompanying `verify.py` uses SymPy exact integer Smith normal form, not floating point or randomized linear algebra. It constructs the 16 nodes and 16 tropes from six abstract Weierstrass labels and checks the symmetric design identity, the determinant, and the complete Smith invariant factors of the 16-by-16 incidence matrix. All 720 permutations are checked for incidence equivariance and identical node/trope cycle profiles; 11 cycle partitions exhaust conjugacy types, and their 16-by-32 presentation matrices give the 11 coinvariant group structures.

Execute `python verify.py` in an environment with dependencies from `requirements.txt`. Verified output ends with `VERIFY_OK: 720 equivariant incidence actions, Kummer 16x16 Smith form, 11 exact Frobenius coinvariant groups`.

The proof assumes standard odd-characteristic Kummer node and trope geometry, explicitly attributed to primary literature; the verifier tests its resulting integer incidence model, not an independent proof of every geometric construction. No claim is made about characteristic two, Picard/Brauer invariants, or novelty certification. Independent audit and independent scientific validation have not been performed.
