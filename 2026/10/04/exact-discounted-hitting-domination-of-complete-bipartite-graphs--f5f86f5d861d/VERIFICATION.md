---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

With a sources in one part and b in the other, symmetry leaves two non-source support values satisfying the stated 2 by 2 linear system. Its determinant is positive for 0<lambda<1. Solving and cross-multiplying gives exactly b>=R_x(a), b>=R_y(a), with positive denominators, so the least feasible b is the capped maximum of their ceilings and zero. The tau=lambda and tau>lambda cases follow from the one-step upper bound. Exact rational verification checks 1280 source-count cases and 28 direct subset-level linear-system cases and confirms the unique (3,3) K_10,10 profile. Those checks corroborate the symbolic proof.

## originality

PASS

Allagan--Pereyra--Massey introduce discounted hitting domination and give exact results for spiders, stars and complete graphs, but their inspected full text contains no arbitrary complete-bipartite theorem beyond stars. Other hitting-probability/random-walk-domination work optimizes different target or aggregate objectives. Resultary did not locate an earlier K_{m,n} formula for this uniform-floor minimum-cardinality parameter.

## value

PASS

Complete bipartite graphs are a canonical next dense family after stars and complete graphs. Collapsing an exponential subset optimization to an exact one-dimensional integer minimum, plus a split-optimum example, is a natural reusable benchmark for the new parameter.

The dated certificate retains the supplied scientific assessment, sources and limitations.
