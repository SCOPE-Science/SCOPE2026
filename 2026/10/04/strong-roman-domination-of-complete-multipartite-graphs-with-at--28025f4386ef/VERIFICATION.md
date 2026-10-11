---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

The construction on a smallest part has weight ceiling((N+m)/2) and satisfies the definition. For any candidate with z zeros, a defender in a zero-free part contributes excess at least ceiling(z/2); because that part has size at least m, z is at most N-m and the desired lower bound follows. If every defender part contains a zero, a zero in one part forces a defender in another zero-containing part, whose zero in turn forces a defender in a second part. Their two excess requirements sum to at least (2z-z_a-z_b)/2. Each defender part retains a positive vertex, and a third part has size at least m, so z_a+z_b is at most N-m-2, giving an even stronger bound. This proves the theorem for all r at least three. The package verifier is only a finite regression check.

## originality

PASS

Originality passes. The founding full-text source gives the exact general upper bound by maximum degree, but does not state equality on arbitrary complete multipartite graphs. Total-strong and k-strong papers study different parameters, and the visible k-strong exact results emphasize complete bipartite cases. The audited two-case lower bound is what turns the general upper bound into an exact formula for every multipartite graph with at least three parts.

## value

PASS

The theorem gives an exact natural infinite-class evaluation of a standard domination invariant and characterizes equality in a classical general bound. The dependence only on order and smallest part, together with the genuine two-part boundary, gives useful structure rather than a one-off computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
