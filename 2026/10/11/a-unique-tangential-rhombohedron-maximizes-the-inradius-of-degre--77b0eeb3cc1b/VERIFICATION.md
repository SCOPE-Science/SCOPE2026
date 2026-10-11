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
The proof in `RESULT.md` applies to every full-dimensional three-dimensional lattice zonotope of Ehrhart \(h^*\)-degree exactly \(2\).

The critical independently checkable equalities and limits are:
- the primary Theorem 1.8 dichotomy between width one and the unique exceptional lattice-unimodular class;
- the width-one Euclidean radius upper bound \(1/2\);
- the exceptional generator determinant \(4\) and half-cofactor determinant \(2\);
- the exact exceptional inradius \(1/\max_i\|w_i\|\);
- the even-column-sum congruence of the integral half-cofactors;
- the integral norm and determinant argument giving \(\max_i\|w_i\|\ge\sqrt2\);
- the parity and Gram rigidity at equality;
- the explicit determinant-minus-one transformation to the sharp generator triple;
- the exact Ehrhart polynomial \(1+3m+6m^2+4m^3\) and its \(h^*\)-polynomial \(1+10t+13t^2\) for the extremizer.

`verify.py` performs exact integer arithmetic using Python's standard library. It verifies the actual displayed matrices, both polynomials by lattice-point counting for small dilates, and exhaustively checks all integer half-cofactor candidates of squared column norm at most two. This finite check tests the equality rigidity at the only possible optimal integer norms; it is not used as an exhaustive search over all lattice zonotopes and does not establish literature novelty.
