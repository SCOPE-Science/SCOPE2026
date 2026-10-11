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
The arbitrary-poset proof is given in `RESULT.md`.

Critical checks:
- regularity makes every cover relation an actual facet and excludes marked-to-marked covers;
- a cover facet incident with one marked endpoint has Euclidean normal length \(1\);
- an unmarked-to-unmarked cover facet has Euclidean normal length \(\sqrt2\);
- every marked interval chain yields the necessary barrier
  \[
  \lambda(b)-\lambda(a)\ge r\bigl(2+(k-2)\sqrt2\bigr);
  \]
- longest-path potentials from marked elements prove simultaneous sufficiency of all chain barriers;
- a path passing through intermediate marked elements decomposes into marked interval chains, so no additional constraint is missing;
- at the optimal radius, the shifted cover-facet system is exactly the complete incenter set;
- every minimizing chain has zero total slack and therefore forces tangency to each of its facets;
- the forward and backward path envelopes are both feasible centers, and uniqueness is equivalent to their coordinatewise equality.

`verify.py` tests deterministic regular marked posets with nonuniform markings. It independently solves the full Chebyshev linear program by active-set enumeration and compares its optimum with exhaustive marked-chain enumeration. It also checks the two canonical path-envelope centers. Finite computation is corroborative only and does not assess originality.
