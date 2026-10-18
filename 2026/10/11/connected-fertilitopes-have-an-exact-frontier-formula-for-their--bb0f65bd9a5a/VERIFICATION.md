---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The proof correctly normalizes each proper facet normal by projecting 1_I into H_0={sum u_i=0}, giving nu_I=sqrt(|I|(m-|I|)/m). Summing shifted inequalities over every disjoint tree frontier proves the upper bound. The inclusion-tree recursion M_I=max(z_I+rho nu_I,sum_child M_J) and a root-to-leaf mass allocation prove feasibility at the minimum; all optimal centers are exactly the shifted-facet polyhedron. Positive weights and connected root imply all asserted facets; no infinite argument relies on enumeration. Independently solving a Chebyshev LP in two nontrivial laminar examples agrees with the frontier quotients.

## originality

PASS

A laminar frontier-cut inradius theorem is stronger than the existing nestohedral facet system and fertilitope realization. Resultary search exposed the same submitted record and neighboring metric polytopes but no prior result with the identical frontier formula. This is bounded, best-of-knowledge novelty rather than search-based proof of priority.

## value

PASS

The formula replaces a continuous Euclidean inball optimization on a natural class of nestohedra/fertilitopes with an exact finite cut problem on the associated rooted laminar tree, and describes the entire center locus. These are independently useful geometric invariants, not simply relettered facet inequalities or table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
