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
For the six-vertex witness \(A\),
\[
\chi_A(x)=x(x-6)(x-4)(x-2)(x-1)^2,
\]
so
\[
a(A)=1.
\]

For the six-vertex witness \(B\),
\[
\chi_B(x)=x(x-3)^2(x-2)(x^2-6x+4),
\]
so
\[
a(B)=3-\sqrt5.
\]

Direct cut enumeration gives
\[
e(A)=1,
\qquad
e(B)=2.
\]

The embedded `verify_algebraic_edge_connectivity_boundary.py` regenerates all connected simple graph isomorphism classes through five vertices from labeled edge subsets, obtaining
\[
1,\ 2,\ 6,\ 21
\]
classes for orders \(2,3,4,5\).

Within every common order-and-size layer, it computes exact Laplacian characteristic polynomials, exact real algebraic roots, and exact edge connectivity, and verifies that no strict reversal occurs.

Run:

`python3 verify_algebraic_edge_connectivity_boundary.py`

The first output line must be:

`VERIFY_OK`

The verifier requires SymPy for exact algebraic-number arithmetic.
