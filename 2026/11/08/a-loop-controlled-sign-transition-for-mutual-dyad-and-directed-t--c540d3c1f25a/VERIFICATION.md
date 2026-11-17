---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

Under independent source-row sampling, p=k/s and the two distinct arc inclusion probability q=k(k-1)/(s(s-1)). Cov(R,T) is zero for disjoint source motifs and splits exhaustively into two-vertex overlaps n(n-1)(n-2) with contribution p²(q-p³), and one-vertex overlaps n(n-1)(n-2)(n-3) with p³(q-p²). Substituting q-p²=-p(1-p)/(s-1) gives -n(n-1)p³(1-p)² for s=n-1, or n(n-2)p³(1-p)(2p-1) for s=n. Independent algebraic checks at all k for n=3..15 and complete enumerations of row-regular digraphs for n=3,4 pass with exact rational covariance. These are finite corroborations; the overlap partition and double count prove all n.

## originality

PASS

The inspected primary directed-closure literature studies triad closure rates and approximate expectations under degree-aware null models, not exact covariance between non-induced reciprocal pairs and 3-cycles in independent uniform fixed-cardinality source rows. Resultary search found related covariance results for different motif pairs or models and the assigned mirror, but no stronger same-model theorem. The loop convention changes covariance sign exactly at p=1/2, a distinctive exact finite-sample contrast.

## value

PASS

Reciprocity and cyclic feedback are natural graph motifs; their joint second-order statistic is a relevant null-model diagnostic. The exact half-target sign reversal caused solely by permitting self-loops demonstrates how otherwise apparently cosmetic row sampling conventions alter motif dependence; the complete all-n,k formula is independently useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
