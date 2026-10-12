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

# Verification and limitations
The general correctness argument is the explicit invertible torus-coordinate substitution, the exact determinant of the odd-cycle Hessian and even cyclic bidiagonal block, the invertible proper minor in the balanced case, and the linear Jacobian scheme. No heuristic finite experiment is used as a general proof.

The standalone file `verify_cycle.py` uses SymPy's exact symbolic differentiation and exact matrix rank. The provided `verification_output.txt` records its successful checks for constant-weight lengths \(4,5,6,8,10,12\), a balanced and an unbalanced weighted eight-cycle, and one explicit point on the balanced eight-gon universal-adjoint singular line, where the polynomial and all first derivatives vanish and Hessian rank is \(6\).

Limits: no assertion about projective coordinate-boundary singularities, rank of the full projective Hessian off the torus, or analogous signatures over fields other than \(\mathbf C\). The input-source originality comparison is not an independent audit.
