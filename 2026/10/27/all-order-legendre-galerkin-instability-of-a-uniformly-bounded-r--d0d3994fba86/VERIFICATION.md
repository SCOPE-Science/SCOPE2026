---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For fixed theta the Q-energy gives the stated two-sided time bound. Projecting multiplication by theta twice misses only the path through the first omitted Legendre polynomial, with coefficient a_s squared. Alternating parity yields the two blocks K and -K, with K=(-T+bU)D. The trace telescopes to (-1)^(s-1)b s^2/(4s^2-1); averaging the real parts gives the claimed abscissa bound for every s, including s=1. At s=2 the block has trace -4b/15 and discriminant (14b/15)^2-4/3<0, giving the displayed example. A positive-real-part eigenspace supplies real exponentially growing solutions. The square evaluation matrix at the s nodes, weighted for the probability measure, is orthogonal by degree 2s-2 exactness. It conjugates T and the quadrature U to the nodes and their squares respectively, including the zero node when present. Each block has the same positive energy bounds as the underlying realization. The rank-one identity concerns the theta-squared product matrix; the difference in the full two-component generators has rank two for b>0.

## originality

PASS

Projection-induced instability, failure of untransformed port-Hamiltonian structure, and Gaussian collocation aliasing are already known. The supported distinct claim is the specific uniformly conservative planar family with an explicit positive abscissa certificate at every finite exact order, contrasted with uniform boundedness at the same Gaussian order. The inspected statements do not yield the nonzero alternating-trace sign law.

## value

PASS

An explicit two-dimensional conservative example rules out restoration of exact coefficient-flow stability merely by taking any larger finite degree. Comparing at identical degree isolates an implementation choice and its exact boundary mechanism, rather than demonstrating only a finite-order numerical anomaly.

The dated certificate retains the supplied scientific assessment, sources and limitations.
