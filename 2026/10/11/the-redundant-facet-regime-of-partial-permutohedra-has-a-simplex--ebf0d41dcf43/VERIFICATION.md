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
The arbitrary-parameter proof is given in `RESULT.md`.

Critical checks:
- Proposition 2.8 supplies exactly the coordinate facets, the proper subset facets with cardinality at most \(n-1\), and the full-set facet;
- the full-set support is \(T_n=\binom{n+1}{2}\);
- the candidate radius is \(T_n/(m+\sqrt m)\);
- every coordinate facet and the full-set facet is exactly tangent;
- every proper \(k\)-subset facet has crossing value \(\sqrt k(2n-k+1)/(2(\sqrt k+1))\);
- the crossing-value function has no interior minimum;
- both endpoint crossing values are strictly larger than the candidate radius for \(m\ge n+2\);
- summing coordinate clearances with the full-set clearance gives the matching universal upper bound;
- equality in that bound forces the unique diagonal center.

`verify.py` checks all \(1\le n\le60\) and \(n+2\le m\le120\), including every proper subset cardinality. It verifies tangencies, strict proper-facet separation, and the global upper-bound identity. Finite computation is corroborative only and does not assess originality.
