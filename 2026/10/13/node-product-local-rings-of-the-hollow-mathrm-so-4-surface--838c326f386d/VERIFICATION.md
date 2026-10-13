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

# Verification of node-product local rings

The supporting source is Brysiewicz--Gesmundo, arXiv:2602.02668 (first public submission 2 February 2026). The statement concerns only algebraically closed fields of characteristic different from two.

**Exact symbolic checks performed:** Running `python3 check.py` on the embedded copy returned `HSO4_EXACT_CHECK_OK`. The program uses only the Python standard library. It verifies that left-right quaternion action has the claimed diagonal Hadamard matrix with no mixed monomials; the Hadamard matrix has square \(4I\); there are 24 one-node support families and 12 two-node support pairs, doubled by the sign quotient to 24 exceptional points; and the exceptional Jacobian ideal has exactly the six squarefree pairwise quadratic generators of the four-axis scheme.

**All-field proof dependencies:** norm-one quaternion pairs give a separable central two-cover of the orthogonal group; at each geometric point, nonzero support coordinates eliminate by the monomial hollow relations, and unit derivatives eliminate two norm equations; finally the explicit Jacobian matrix of \((xy,zw)\) determines a radical Fitting singular ideal. Those steps are written out in RESULT.md and supply the universal proof. The checker itself is a reproducible algebraic sanity check, not an independent audit or a complete machine certification.

**Limits:** no computation here addresses characteristic two, unrelated orthogonal slices, complete deformation spaces, or the absence of equivalent statements in all unpublished mathematics. Independent scientific audit has not been performed.
