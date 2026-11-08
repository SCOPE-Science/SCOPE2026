---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Conditioning a fixed vertex v to be isolated leaves a uniformly sampled m-edge graph on the B=choose(n-1,2) pairs not touching v. Since H has no isolated vertices, no induced copy contains v; E[X_H|v isolated] follows by prescribed e present and r=choose(h,2)-e absent edges. Dividing by the unconditional induced-count expectation and summing vertex covariances gives R=(n-h)/n (N)_t/(B)_t (B-m)_r/(N-m)_r with N=choose(n,2) and the stated positive normalizing domain. Every factor (B-m-j)/(N-m-j) strictly decreases while positive, and the numerator becomes zero later; hence the one-crossing direction holds. Expanding R at fixed p in (0,1) yields n(R-1)->[2e-h-h(h-2)p]/(1-p). Substituting h=3,e=2 gives M_n=(n-1)(n^3-3n^2+6n+8)/(2(3n^2-3n-4)), with 2<M_n<B. Independently simplified the rational threshold and enumerated all labeled graph outcomes by exact rational counts for wedge counts at n=4,5,6, rather than treating finite enumeration as the all-n proof.

## originality

PASS

Sah and Sawhney, Local limit theorems for subgraph counts (2022), treat G(n,m) graph factors and local limits including induced subgraphs (Section 4.2), but do not state this normalized cross-covariance with isolates or its topology-independent monotone transition. The exact fixed-size hypergeometric identity is standard, so the formula is a short deduction from prior elementary tools and may have existed implicitly in occupancy literature. In the inspected primary sources and Resultary records no implication-complete preexisting joint threshold was identified; best-knowledge PASS with explicit formula-priority risk.

## value

PASS

Isolates and induced motifs are fundamental dependent random-graph statistics. The unexpected positive-to-negative covariance transition at fixed edge count, uniform across motif topology at fixed (h,e), is qualitatively unlike the always-negative independent-edge-model covariance. The all-n rational wedge boundary and universal limiting p* are natural dependence-phase invariants, not arbitrary small-instance arithmetic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
