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

The standalone file `verify_acyclic_rook.py` uses only the Python standard library and can be run with `python verify_acyclic_rook.py` (tested with Python 3). It performs three methodologically separate checks.

First, it builds the rook graph from the definition of adjacency by a shared row or a shared column. For all of the tested pairs with at most sixteen cells, it enumerates every vertex subset and uses union-find over all induced edges to decide whether a cycle exists. This calculation does **not** apply the line-graph reduction.

Second, it enumerates labeled alternating bipartite paths and assembles components recursively, deriving complete polynomials independently from the native graph traversal. It checks the highest exponent and the exact factorial/binomial top-coefficient formula for fourteen parameter pairs:

`(1,1), (1,2), (1,4), (2,2), (2,3), (2,4), (2,5), (2,6), (3,3), (3,4), (3,5), (4,4), (3,6), (4,5)`.

Third, it independently expands the rational bivariate exponential generating function using exact `fractions.Fraction` arithmetic and compares every coefficient with the path-component recurrence for eight parameter pairs:

`(2,2), (2,3), (2,5), (3,3), (3,4), (4,4), (4,5), (5,5)`.

The observed output contains `VERIFY_OK` followed by `EGF_VERIFY_OK 8 exact rational coefficient expansions`. Representative full results are

\[
A_{2,2}(z)=1+4z+6z^2+4z^3,
\quad
A_{3,3}(z)=1+9z+36z^2+78z^3+81z^4+36z^5.
\]

All the computations are finite. The full infinite result depends instead on the path-forest bijection and labeled exponential formula, with extremal counts proved by exact combinatorial bijections. No external independent mathematical audit has been performed.
