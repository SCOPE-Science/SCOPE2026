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

The exact checker `verify.py` uses symbolic arithmetic in \(\mathbb Q[\rho]/(9\rho^2-14\rho+9)\). A successful replay ends with `VERIFY_OK`.

It verifies the following claims directly:

- the displayed Hessian-quartic determinant;
- equality of both quadratic rank-drop discriminants with \(9\rho^2-14\rho+9\);
- the double-root coordinates \(x_0\) and \(y_0\);
- vanishing of every \(3\times3\) Hessian minor at the seven special-fiber rank-drop support points;
- corank-one quadratic parts at the three collision points and reduced fourth-order coefficient \(8\rho\) after solving the transverse critical equations through the order needed for the splitting lemma;
- nondegenerate local quadratic parts at the four fixed rank-drop points and at the three nodes of the cubic;
- rank three of the cubic Hessian at those three nodes; and
- uniqueness, up to projective scale, of the solutions to \(H_\rho(x)k=0\) for each node kernel \(k\).

The checker therefore certifies the new local type and exhaustion steps. It does not independently reconstruct the complete primary decomposition of the \(3\times3\)-minor ideal; that global decomposition is a premise from arXiv:1909.12538.
