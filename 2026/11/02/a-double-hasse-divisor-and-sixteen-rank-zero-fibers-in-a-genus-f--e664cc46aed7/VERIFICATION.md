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

# Verification and reproducibility
The symbolic certificate is `verify_symbolic.py`, executable with Python 3 and SymPy. It expands both relevant powers of the branch polynomial, reconstructs the complete Cartier coefficient blocks, computes the discriminant and Hasse determinant identity, checks the matrix restricted to the Hasse conic, computes the gcd of *all* two-by-two minors of the second Frobenius iterate, checks squarefreeness and the irreducible factor degrees, and verifies the third Frobenius iterate vanishes in the polynomial quotient by \(S(u)\). Expected marker: `SYMBOLIC_DIVISOR_AND_STABLE_RANK_OK`.

The independent point counter is `verify_point_counts.py`, executable with the Python 3 standard library. Its elementary arithmetic in fields of orders \(7\), \(49\), \(343\), and \(2401\) counts points on four marked smooth curves and reconstructs the first four Weil coefficients. Expected marker: `INDEPENDENT_POINT_COUNTS_OK`. The checked parameter pairs and geometric ranks are \((0,0):0\), \((6,3):0\), \((2,5):2\), and \((2,0):4\).

Proof limits: the symbolic quotient-ring identity, not the sampled point counts, establishes the theorem for all algebraically closed characteristic-seven parameters. No Newton-polygon, supersingularity, or geometric isomorphism-class claim is made. A priority comparison with one relevant later genus-four superelliptic article remains limited because its full text was unavailable. Independent validation has not been performed.
