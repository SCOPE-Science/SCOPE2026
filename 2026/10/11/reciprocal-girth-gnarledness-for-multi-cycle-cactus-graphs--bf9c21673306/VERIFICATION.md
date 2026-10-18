---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

PASS: A connected cactus decomposes into edge-disjoint simple-cycle blocks C_i of lengths ell_i, with oriented sums z_i forming an integral basis of H1 of rank b1>=2. Define F-linear extension s on oriented edges e of C_i by signed z_i/ell_i and s(bridges)=0. Then s(z_i)=z_i, and max unit-edge l1 norm =max_i 1/ell_i=1/g(X). For any chain extension s and any cointegral basis B, nonzero shortest z_i has integral nonzero B-coordinates, so 1<=||z_i||_1^B=||sum_{e in Ci}±s(e)||_1<=g(X)||s||^B. Taking all infima yields exactly reciprocal girth. Non-tree-edge relative generators give geometric G1(X)=1. No 2-cells or overlapping-cycle assumptions are silently used.

## originality

PASS

PASS, best of knowledge: Hofmann-Löh arXiv:2610.02987v1 Example 7.13 computes a single cycle and Proposition 7.16 explicitly assumes dim H1=1. General coefficient-independence gives equality between subfields but does not compute higher-rank value. The shortest-cycle lower estimate survives all cointegral changes, a missing multicycle argument. Geometric quantitative null-cobordism reference treats geometric spanning trees, not this newly defined higher-rank algebraic invariant. Resultary leading exact match was the target itself and not counted as independent prior.

## value

PASS

PASS: A natural complete family for a newly introduced algebraic invariant, showing that familiar graph girth governs a truly higher-homology-rank basis-independent chain extension norm and that the algebraic/geometric discrepancy is arbitrarily large on multicycle cactus graphs. The quantification over arbitrary cointegral basis is the substantive point, not simply rerunning the unicyclic example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
