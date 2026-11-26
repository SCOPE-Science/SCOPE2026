---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

A pointed type at height zero is its color. At positive height it is the root color and the nonempty set of child types, of size at most b; every such set is realizable by coloring disjoint subtrees independently and repeating a type as needed. The exact-height test and the conjunction of the existential tests with the box-of-disjunction test isolate precisely each such type. All types are realized, so Boolean operations give exactly one term operation per subset of the type set, including the case r=0 (one type per height). The polynomial degree obeys d_{j+1}=1+b d_j, and the leading coefficient obeys c_{j+1}=c_j^b/b!, so the top height gives degree n and coefficient (b!)^{−(n−1)/b}, also for b=1. Equal spectra give equal polynomials on infinitely many q=2^r; at fixed n>1 the strict increase of the factorial geometric mean recovers b, then n recovers h. Checked the small height-one exponents q+q² and q+(q³+q²)/2 and the exponents 3,265,298 and 132 for the reported order-31 pair. The frozen code and recorded evidence were read, not executed; the finite evidence does not prove the unrestricted result.

## originality

PASS

The supported distinct result is the exact polynomial census and inverse classification on the multilevel full immediate-child tree family. Finite modal types and their characteristic formulas are standard, and the earlier strict weak-order spectrum includes the height-one star exactly. Its statement is not a classification of higher full successor trees: for h≥2 immediate-child accessibility is not transitive, and the independent choice of descendant types in separate child subtrees is absent in that weak-order theorem. No inspected source supplies or entails the multilevel count and inverse theorem as a special case. This is a bounded best-of-knowledge comparison, not a priority guarantee.

## value

PASS

This is an exact invariant and a losslessness theorem on a natural full-branching family under ordinary ungraded possibility (which cannot count identical child types at one valuation). The polynomial separates potential collisions even at common frame order, such as the binary height-four and five-ary height-two examples. This is more than a bounded catalog or a definability lemma. The height-one star overlap is not counted as an independent advance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
