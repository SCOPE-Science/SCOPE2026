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

# Verification notes

The proof derives all three formulas for every admissible parameter from feasible explicit rank-one majorants and positive contractions. The middle-regime contraction is verified by an exact ground-state quadratic-form identity. The upper-regime contraction is verified by row-support orthogonality. The attached `verify.py` evaluates these identities with rational arithmetic in the middle regime and representative finite floating-point tests elsewhere. The finite checks are not relied on as an infinite proof.

Scientific limitations: only \(I_3+tS_3\) over real \(\ell_2^3\); neither higher path orders nor arbitrary positive matrices are classified. Historic publication priority is not independently established; foundational literature has not all been inspected completely.
