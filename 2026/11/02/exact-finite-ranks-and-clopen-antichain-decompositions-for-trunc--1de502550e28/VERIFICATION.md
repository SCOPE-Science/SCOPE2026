---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The rightmost coordinate j<m with x(j)<k-1 gives a finite-prefix rank r(x) in {1,...,m(k-1)+1} that STRICTLY decreases along each legal edge, because higher coordinates cannot acquire a low value and y(j)>x(j) if the rightmost low coordinate remains. It decreases along finite transitive paths, yielding a clopen antichain coloring. The construction using k-1 suffix-increment moves at each j=m-1,...,0 gives exactly m(k-1)+1 vertices and proves optimality; k=1 gives the empty-edge case. Independently verified 25 extremal-chain constructions for 1<=m,k<=5, including all ranks and strict decrements, not as a substitute for the general proof.

## originality

PASS

Best-of-knowledge originality of the narrow incremental claim after statement-level comparisons; accessible full primary texts checked where available, material-access limits and priority risks explicit. The sharp numerical-order rank and optimal clopen map, not general Borel finite-rank existence.

## value

PASS

The exact finite-stage rank of a canonical strict numerical truncation upgrades a general exponential bound into a sharp linear formula and an optimal continuous clopen antichain decomposition. This is a motivated structural refinement of the finite-rank approximation used for eventual domination, not a claim about all partial orders.

The dated certificate retains the supplied scientific assessment, sources and limitations.
