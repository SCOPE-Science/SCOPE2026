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

The clique and peripheral permutation symmetries reduce the problem to the four allocations. Independently eliminating the peripheral block rI_v gives clique Schur eigenvalues r+m (multiplicity u−1) and w=m+a−uv/r>0. Block inversion yields J_a=(u−1)/(r+m)+v/r+(1+uv/r²)/w, including v=0 by direct interpretation. This equals the frozen trace formula. Exact rational reduction from this expression reproduced the comparisons for m=3,4,5,6 and J_2−J_3=(m−1)(r−6)/(3r(3r+2m−2)). For m≥7, J_3−J_0 has the sign of −[(m−3)(r+m−6)−18], strictly negative throughout; clearing positive denominators in J_1−J_2 and shifting by r=4,m=7 gives the nonnegative-coefficient polynomial with positive constant 92 in the record. Thus 0 and 1 cannot minimize in that range. At m=6,r=6, 0,2,3 tie and 1 is strictly worse. The other inequalities give precisely the listed winning allocations and the binomial count follows from symmetry. I inspected the frozen verification material but did not execute it; the unrestricted inference is algebraic, not from the recorded parameter sweep.

## originality

PASS

The strongest earlier exact-three-leader source is for complete bipartite graphs, not graphs with an internal clique; the same-day strongly regular result excludes this nonregular graph. The later balanced-split theorem is a narrower overlapping case, not an exact result for the two independent part sizes. General coherence tools provide the setup but not the complete optimizer and tie classification. This is a bounded comparison, not a certification of priority.

## value

PASS

The complete split graph is a canonical dense inhomogeneous graph and three leaders allow genuinely mixed optimal choices. The classification resolves when two clique leaders beat both pure allocations, and identifies a triple tie and the separate switch thresholds. This permits exact selection and multiplicity across all sizes, including unequal parts, rather than an illustrative finite grid or a restatement of the trace objective.

The dated certificate retains the supplied scientific assessment, sources and limitations.
