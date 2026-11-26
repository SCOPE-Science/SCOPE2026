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

On the repaired statement: the bracket kernel forces unsupported neighbors of the support to zero and equates the ratios y_u/x_u within each component of the induced support, leaving the other unsupported coordinates free. This yields rank |N[S]|−c(G[S]) in every characteristic, with (q−1)^|S| vectors for support S. Edge coordinates are immaterial to rank: the full Lie-algebra stratum contains q^|E| times as many vectors as the vertex stratum, not the reverse. Equality of formal polynomials is equivalent to equality of coefficient arrays in the (q−1)^s t^r basis, and different orders are excluded by evaluation at t=1. The reviewed complete canonical enumeration and separate bounded reproduction agree: graph classes/signatures 1,1,2,4,11,34 through five, and 156 classes, 149 signatures, 142 singletons and seven doubletons at six. The listed pairs match CENSUS.txt. The displayed witness has the same six rank counts for both graphs, summing to q^6, but the triangle intersections differ; the graphical Lie-algebra isomorphism theorem gives nonisomorphism in characteristic not two. The repair also distinguishes Rossmann's C from his F and aligns the written certificate description with the actual canonicalization at n≤5 and orbit marking at six. None of the census data or the sharp cutoff changes.

## originality

PASS

Best-of-knowledge pass for the complete six-vertex fiber classification and the sharp lower bound for Rossmann's C polynomial. The formula and its relation to the class-size distribution, graphical Lie-algebra reconstruction and the graph catalogues are not new. A distinct Resultary record explicitly uses the same connected witness, so witness equality alone is not the basis for this originality judgment. No compared source supplies the complete collision partition and minimality together.

## value

PASS

The complete small-order injectivity boundary is a natural test of a known two-variable invariant: it states where all possible adjoint-rank and centralizer-dimension multiplicities first cease to determine an underlying graph and precisely how the first failures occur. The seven-pair partition, no larger fibers at the boundary and equal-dimension nonisomorphic Lie-algebra application are useful exact information, not another computation of a named known polynomial for one isolated graph. The value rests on the complete boundary, not on novelty of the example in isolation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
