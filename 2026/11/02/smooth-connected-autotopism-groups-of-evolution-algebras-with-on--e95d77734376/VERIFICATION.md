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

# Verification of the autotopism-group theorem

The mathematical proof is supplied in `RESULT.md`, Steps 1–5. The exact identities verified there are the scalar product-line constraint \(H(u)=tu\), the invertible bilinear-form equivalence \(F^TBG=tB\), and the complete independent block parametrizations of \(H,F,G\). Substituting the displayed blocks into the bilinear identity checks sufficiency; nondegeneracy on a complement to the radical proves necessity. The normal additive shear group and diagonal reductive subgroup intersect trivially and multiply onto the full group, yielding the claimed decomposition.

Run `python3 verify.py` to enumerate finite-field matrices independently of those parametrizations. The checker constructs all invertible matrices in the selected small prime fields, tests the original matrix identity for pairs, computes the first-map stabilizer directly, and compares against the formula. The full set of test cases includes dimension \(1\), all nonzero ranks through dimension \(3\) in characteristic \(2\), dimension \(2\) in characteristic \(3\), generator positions in/out of the radical, and a form with diagonal coefficients \(1,2\) over \(\mathbb F_3\). The run returned `VERIFY_OK`.

These are finite exhaustions only for their stated cases. They are not a symbolic proof for arbitrary \(n,q\) or arbitrary fields; the block argument proves the general statement. No independent external audit was performed.
