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

# Verification steps and limits

The standalone file `verify_veniani.py` contains every polynomial and matrix used in the proof. Running it with Python 3 and SymPy outputs `VENIANI52_PRINCIPAL_MINORS_ALL_ODD_PRIMES_AND_CHAR2_DOUBLE_PLANE_PASS`. It checks the integer equality \(8F+Q=0\) after coordinate substitution, all \(15\) principal minors, explicit support kernels in selected characteristics, affine Hessian determinants, and \(F\equiv H^2G\pmod2\) together with the exact first derivatives.

Exhaustiveness in arbitrary odd characteristics uses that every geometric critical point gives a nonzero kernel vector for one principal submatrix, and every nonzero such determinant is supported on the prime set \(\{2,3,5\}\). This is a universal algebraic obstruction, not a sample search. The local nodal conclusions use the nondegenerate Hessian test in odd characteristic. The projective scheme calculation in characteristic two also requires the saturation argument included in `RESULT.md` and cannot be inferred from finite-point enumeration.

The original 52-line count and the characteristic-three and characteristic-five line counts belong to the cited literature and are not independently re-enumerated here. Historical priority may be affected by material not indexed in the checked sources. Independent audit has not been performed.
