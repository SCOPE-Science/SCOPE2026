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

The proof is analytic and exact. The accompanying `verify.py` is a finite certificate checker for the symbolic identities used in that proof; it is not being used as finite sampling evidence for an infinite statement.

The checker performs these exact steps:

1. Reconstructs the polynomials \\(U\\) and \\(V\\) over \\(\\mathbb Q(\\sqrt3)\\) from their definitions.
2. Verifies coefficient-by-coefficient that
\\[
U^2-V^2(1+2x^2)=784(x-1)^2\\left(x-\\frac47\\right)^2(x+2)^2Q(x).
\\]
3. Verifies that every Bernstein coefficient of \\(Q'(4u/7)\\) is positive and that \\(Q(4/7)<0\\), proving \\(Q<0\\) on the entire left interval.
4. Expands \\(Q(\\beta+y)\\) exactly, checks the positive low coefficients and the discriminant \\(-10\\) of the remaining quadratic high-degree block, proving \\(Q>0\\) for every \\(y\\ge0\\).
5. Expands \\(U(\\beta+y)\\) exactly and checks that all coefficients are positive.
6. Checks the equilateral equality case exactly.

Run with `python3 verify.py`; the expected output is `VERIFY_OK`.

Limit: this verifies the isosceles theorem only. It does not certify Liu's conjecture for scalene triangles and does not constitute an independent audit.
