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

# Reproducibility
Run `python3 verify.py` using the Python 3 standard library. Successful execution prints:

`VERIFY_OK determinant_degree_t=6 exact_Newton_orders=1..16 brute_orders=3..10 vertex_subsets=1398080 all_coefficients_and_Lucas_maximum_orders=3..40`

The checker reconstructs all sixteen coefficients of \(\det(I-tT(z))\) by Newton identities over \(\mathbb Z[z]\) using independently computed trace polynomials. It exhaustively evaluates every vertex subset of each simple cyclic prism for orders \(3\) through \(10\), comparing its actual induced maximum degree against the weighted cyclic-word transfer. It separately compares the maximum size and coefficient to the Lucas expression through order \(40\).

# Boundaries
No finite test demonstrates an unrestricted identity by itself; the unrestricted graph-theoretic proof, matrix trace relation, and binary-word counting are stated in `RESULT.md`. No independent external audit or formal proof assistant was used. The inaccessible complete text of a relevant 2024 maximal-dissociation enumeration leaves a residual priority uncertainty.
