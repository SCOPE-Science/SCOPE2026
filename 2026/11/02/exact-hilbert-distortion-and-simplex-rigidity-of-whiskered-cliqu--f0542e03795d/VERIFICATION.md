---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For n>=2, graph H_n=K_n with one private leaf per clique vertex has four pair-distance types: 1 core-core, 3 leaf-leaf, 1 matched, and 2 unmatched. For noncontracting embedding with distortion C, core variance V_P<=A C² and leaf variance V_Q>=9A, A=(n-1)/(2n). Hilbert reverse triangle for centered n-tuples and centroid separation gives matched mean squared distance W>=(sqrt(V_Q)-sqrt(V_P))² while W<=C²; for C<3 this forces C²>=A(3-C)², hence c_n=3/(1+sqrt(2n/(n-1))). Homothetic centered simplex points p_i=c_n u_i/sqrt2, q_i=3u_i/sqrt2 achieve all inequalities; unmatched squared distance c_n²+3c_n lies between 4 and 4c_n². Equality forces two regular simplices with identical centroids and homothetic vertices, giving uniqueness and affine dimension n−1. For n=2 formula gives 1; limit n→infinity is 3/(1+sqrt2). Fresh independent checks validated defining quadratic identity and unmatched-pair inequalities for n=2,3,4,7,12,100; inspected exact-rational checker.py also covers finite indices.

## originality

PASS

Point-metric Hilbert bi-Lipschitz distortion of the complete-clique corona K_n⊙K_1 is distinct from Robertson’s complete bipartite/hypercube metric families and from the quadratic embedding constants of corona distance matrices. Robertson’s full Theorem 4.3 does not imply this optimizer rigidity or pendant pairing. Baskoro–Obata and 2025 corona results use negative-type or quadratic form invariants, not the minimax two-sided Euclidean distortion. Resultary near matches were Banach–Mazur distances of Lipschitz-free metric spaces rather than this metric-embedding problem. The 2014 distance-matrix paper has only abstract-level comparison and remains a priority risk.

## value

PASS

The clique corona is a standard graph product/corona with a strongly nonuniform shortest-path metric. Its sharp nonlinear Hilbert embedding distortion and all-optimal configuration rigidity, including minimal affine dimension, answer natural quantitative metric-geometry questions and reveal an exact dependence and nontrivial n→∞ limit; not merely a known negative-type qualitative result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
