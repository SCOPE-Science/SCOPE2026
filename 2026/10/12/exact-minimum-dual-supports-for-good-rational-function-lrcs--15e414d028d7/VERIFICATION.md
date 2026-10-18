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

Theorem 3.2 construction gives each generator column as u(P)⊗(1,d_m,...,d_m^{t−1}) with distinct fiber labels d_m and the extended projective Vandermonde evaluation u(∞)=(0,...,0,1). In the j=0 block every ≤r distinct columns are independent. For each full (r+1)-fiber, a unique all-nonzero Vandermonde dependence annihilates all j blocks, giving dual distance exactly r+1. Conversely a weight-r+1 full-matrix dependence is one-dimensional in the j=0 block; its j=1 coefficients are another null vector and must be proportional. Nonzero coefficients imply equal d_m across its support, so by distinctness all coordinates share the one fiber. For t≥2 this exhausts supports, each contributes q−1 nonzero dual words, and the minimum helper set through any coordinate is uniquely its fiber minus the coordinate. The t=1 exclusion and projective infinity normalization were explicitly checked. Independent F11 r2 t2 full-fiber q11 instance gives exactly four dependent triples and 40 minimum dual words; the symbolic argument gives all q.

## originality

PASS

The precise quantified final claim was compared against primary sources, semantic published-result searches, equivalent mathematical formulations and stronger possible implications. No decisive coverage was found on the actually read material; sources not fully read remain recorded as risks, not represented as full-text negatives.

## value

PASS

The exact dual minimum-support census and unique smallest repair set are structural invariants of a recent broad good-rational-function LRC construction. They improve upon the existence of fiber-local repair and general dual-distance upper bounds by ruling out all other smallest repair sets. This matters directly to understanding repair flexibility and failure incidence in this natural code family, without claiming all LRCs or larger recovery sets.

The dated certificate retains the supplied scientific assessment, sources and limitations.
