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

Run `python verify_accidentally_essential.py`. The script uses exact symbolic arithmetic to reconstruct the displayed matrix and checks:

- the determinant formula and the derivative reductions proving the unique projective singular point;
- the coordinate identity \(F=-Xs^2-125st^2+250t^3\), from which the explicit completion-of-square proof gives type \(A_2\);
- the base-point-free cubic normalization and the rational inverse \([u:v]=[x_1+6x_2:x_2]\) away from the cusp;
- the three Cayley quadrics and the local Jacobian determinant \(-20\) at the unique support point;
- the identity \(\operatorname{adj}A(
u)=-u^2yy^T\) and hence the extended kernel vector;
- the smooth conic identity \(Y_0Y_2=2(Y_1+Y_2)^2\) and the cusp-preimage value.

The script must terminate with `VERIFY_OK`. It does not attempt a positive-characteristic classification or a literature search.
