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

In B_n(G) of size 1+n^2|G|, commuting offdiagonal triples require exact disjoint source/target supports U,W. The zero element contributes e^t; diagonal local groups outside U union W contribute the ordered group-commuting EGF C_G(t), and inclusion-exclusion over missing rows/columns gives E_abg(t) for each unique exact nonempty U,W. This is valid for arbitrary nonabelian G because only same-index diagonal labels need commute. Coefficient of t^r in C_G(t)^n equals n c_r(G) plus lower orders and every E_abg has zero constant, proving recursive recovery. For k_n/sqrt(n)->lambda, diagonal and zero samples have o(1) probability uniformly over arbitrary finite G_n; noncommuting pairs agree asymptotically with directed equality constraints J_a=I_b. The factorial moments sum disjoint-edge patterns ->lambda^(2r) and shared-component patterns vanish as n^(1-v/2), establishing Pois(lambda^2). Independently counted literal semigroup multiplication and EGF for n=1..3 trivial G and n=2,C2, examples including [1,9,41,177] for n2,g2. This finite check is only corroboration; the proof covers all n,G and the specified scaling.

## originality

PASS

Prior Kumar--Dalal--Pandey 2020 describes Brandt commuting graphs, disjoint U,W and clique extrema; this same-object structural ingredient is not new. Margolis--Rhodes--Silva study Brandt subsemigroup complexes, and Mitchell 2004 maximal independent sets aperiodic Brandt. A maximal-container or clique-number count cannot directly supply all labelled ordered pairwise commuting tuples with repetition and nonabelian local-group tuple data: those overlapping containers would require exact inclusion-exclusion. Inspected primary material lacks both the full EGF and universal group-independent Poisson window. Rare-edge Poisson factorial moments are classical technique, not claimed novelty; possible prior clique-polynomial restatement is a residual priority risk.

## value

PASS

The complete c_r(B_n(G)) profile for arbitrary r is a natural enumerative invariant extending clique extrema; its triangular coefficient relation recovers the local-group commuting series, an information-preservation property. The sqrt(n) Poisson collision window is universal even as local groups vary, a sharp probabilistic phenomenon with a nondegenerate e^(-lambda^2) limiting commuting probability. This is a meaningful structural and asymptotic classification, not a fixed tiny table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
