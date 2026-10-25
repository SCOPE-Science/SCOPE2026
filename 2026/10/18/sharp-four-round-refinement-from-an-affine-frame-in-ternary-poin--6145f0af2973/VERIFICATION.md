---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

PASS — Model normalized affine hyperplanes H_{a,b} over F3 with (a,b)~(2a,2b), distinct initially colored point/hyperplane parts and d+1 individually colored affine basis points. For basis {0,e_i}, round1 unique coordinate-zero hyperplanes D_i, round2 distinguishes supports and forces singleton points 2e_i and 2e_i+2e_j using the round1 class with a_i=a_j=1 and other coefficients 0 or 2. The point witness set P has 1+2d+d(d-1)/2 points. Its incidence with e_i/2e_i recovers inhomogeneous hyperplane normals; for homogeneous hyperplanes, incidence with pair points compares signs, yielding normals up to unavoidable global -1. Hence all hyperplanes singleton by round3 and all points by round4. The three points (1,1),(1,2),(2,1) in first two coordinates have the same round2 counts and stay tied in round3, proving sharp 4. Any <=d marked points lie in a proper affine subspace, fixed pointwise by a nontrivial affine automorphism, so cannot give a discrete coloring. Independently built AG(3,3) incidence graph and obtained round color class pairs point/hyperplane (5,1),(5,15),(15,15),(15,39),(27,39), first discrete at round4. Source separately supplies d2..6 refinement tests and witness signatures d2..9; these finite tests are corroboration, not infinite proof.

## originality

PASS

PASS — The notion and complexity of 1-WL color refinement, individualization and fixing number are established; inspected Arvind et al 2015 and 2016 address general amenability/compactness or parameterized complexity. Neither inspected theorem gives the exact AG(d,3) point–hyperplane incidence first-discreteness round 4, minimal point marks d+1, or a quadratic witness set for all d. This is not a statement about arbitrary graph isomorphism identification or general q, and specialization to d>=3 is mathematically structural.

## value

PASS

PASS — The precise individualization threshold and constant refinement depth on a canonical highly symmetric affine incidence graph form a natural extremal example. Explicit small separating family (quadratic in d) that isolates exponentially many hyperplanes supplies conceptual structure beyond a small computational case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
