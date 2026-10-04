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

The proof has an analytic continuous part and an exhaustive finite part.

The analytic part identifies a real five-vector Parseval frame with an orthonormal pair of row vectors \(u,v\in\mathbb R^5\), rewrites total \(2\)-volume as a maximum of \(u^{\mathsf T}Sv\) over skew sign matrices, and proves that the fixed-matrix maximum over orthonormal \(u,v\) is the largest singular value of \(S\). For order five, the characteristic polynomial is determined by \(\sigma_1^2+\sigma_2^2=10\) and the sum \(C\) of squared principal Pfaffians.

The bundled `verify.py` checks the finite statements using exact integer arithmetic only. It verifies all \(64\) switching-normalized patterns, all \(1024\) unnormalized sign patterns, and the complete signed-permutation orbit of a maximizing pattern. Expected output is:

`VERIFY_OK normalized_C5=24 normalized_C21=40 all_C5=384 all_C21=640 max_orbit=384`

The verifier does not prove the continuous reduction, the operator-norm equality step, or the trigonometric identity for the regular-pentagon value; those are proved symbolically in `RESULT.md`. No sampled finite experiment is used as evidence for an infinite statement.
