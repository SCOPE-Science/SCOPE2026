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

The proof was checked directly from the halfspace description. For a ball of radius \(\rho\), coordinate constraints have unit normals and cover constraints have normal length \(\sqrt2\). A longest chain has \(h-1\) covers, giving
\[
 (h-1)\sqrt2\,\rho\le1-2\rho.
\]
The candidate center built from longest downward cover distance attains the resulting bound because every cover raises that distance by at least one and every depth is at most \(h-1\).

A standalone checker in `verify_order_polytope.py` exhaustively enumerates all distinct transitive closures compatible with a natural labelling on at most six elements. Every finite poset can be relabelled this way by a linear extension, so this finite census covers every isomorphism type through six elements. For each poset it reconstructs covers, height, longest downward/upward cover distances, verifies both canonical-center inequalities, and checks that the algebraic uniqueness condition agrees with the existence of a longest chain through every element.

Expected replay output:

`VERIFY_OK order-polytope inradius posets=5231 n=1..6`

The exhaustive computation is not an infinite proof and is not used to justify the arbitrary-size theorem. It is a finite stress test of definitions, boundary cases, and the uniqueness criterion.
