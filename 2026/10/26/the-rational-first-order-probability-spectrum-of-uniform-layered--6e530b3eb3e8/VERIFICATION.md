---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Unique direct-sum decreasing-block decomposition gives exactly 2^(n-1) uniform cut strings, with first-order interpretations in both directions between two orders and binary successor cut predicate with terminal sentinel. First-order word languages are regular, giving an effectively computed rational generating series F(z). Braunfeld-Kukla first-order convergence supplies existence, and the Abel limit p=lim_(s->1-)(1-s)F(s/2) is rational because the removable singularity has rational coefficients. For any q, choose q equal-length distinct words u avoiding 00, and markers w=001u1. Prefix-suffix nonoverlap proves switching the earliest marker gives an exact bijection among all q types at every finite length. Disjoint windows give exponentially decaying probability of no marker, and earliest-marker types are FO-definable; their unions yield each m/q. Fresh finite enumeration checks cut permutations and first-hit symmetry but unrestricted reasoning is combinatorial and logical.

## originality

PASS

Best-of-knowledge PASS for exact spectrum Q intersect [0,1] with explicit realization, NOT for already-known convergence or rational regular-language generating functions. The full newer Falgas-Ravry–Markstrom–Skerman–Raty manuscript proves density for small exponential classes and complete spectra for polynomial-growth classes; its exponential conclusion does not assert every rational is achieved, so it does not imply the converse claim. Markstrom-Raty rational-language machinery covers rationality but not marker realization.

## value

PASS

A complete exact arithmetic spectrum, with constructive FO definitions realizing any given rational, answers a natural next question beyond existence of logical limits and density. Distinguishes exact attainability from arbitrarily good approximation for a canonical exponentially growing permutation class.

The dated certificate retains the supplied scientific assessment, sources and limitations.
