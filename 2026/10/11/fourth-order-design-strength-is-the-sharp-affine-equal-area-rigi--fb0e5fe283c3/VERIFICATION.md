---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Actual frozen RESULT.md and symbolic verify.py read; independently checked the exact implication: area(A F_j)=|det A| |A^{-T}x_j| area(F_j), so equality gives q(x_j)=0 where q(u)=u^TQ u−c. For t≥4, 0=average q(x_j)^2=integral_{S²}q²; hence Q=cI and A positive scalar times orthogonal. For the antipodal orthonormal triple ±v_i, all moments ≤3 match S², and Q0=diag(5/4,5/4,1/2) takes value 1 on each because v_{i,3}²=1/3; Q0 nonscalar. The finite symbolic checker confirms only the witness, not the universal implication.

## originality

PASS

The closest identified source An (arXiv:2608.11570) contains the same geometric setup and key area law, but its full text could not be read; it must be regarded as a significant possible implicit covering source. The searched equivalent frame quadratic-evaluation formulations and current mathematical record index did not reveal a stronger prior statement covering both uniform strength-four rigidity and strict strength-three sharpness. Best-of-knowledge O PASS remains qualified, not a publication priority certificate.

## value

PASS

Fourth-order design exactness has a natural geometric role: it is precisely sufficient to test a squared anisotropic quadratic defect and force affine equality-area rigidity. The explicit strength-three octahedral nonconformal witness shows a sharp structural boundary, not an arbitrary parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
