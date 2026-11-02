---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

The base signed clique sector decomposition B_p=positive unit cube plus p disjoint one-negative sectors has volume 2, and independently integrated beta moments reproduce μ,c_perp,c_parallel. Fiber at T=min Y is T B_p; T has Beta(p+1,q), giving volume 2p!q!/n! and conditional covariance decomposition into transverse eigenspaces and 2x2 longitudinal M_pq. Independent exact rational computations matched 121 parameter pairs. In proportional scaling the longitudinal matrix G=diag(a²,b²)+3ab vv^T has trace 1+ab, det 4a²b², largest eigenvalue Λ_+(ab)≥v^TGv=1; smallest whole-covariance eigenvalue is min(a²,b²)/12. Hence limiting ratio ≥4, equality iff a=b=1/2. A transverse eigenvalue collapses in either extreme regime, proving divergence and the iff sequence claim by compactness. The assertion is coordinate-Euclidean asymptotic, not affine invariant or finite-n ≥4.

## originality

PASS

Beck–Hlavacek define the signed-poset class, and the bottom B_p is affine-equivalent to a known complete-graph fractional stable-set polytope (Hamano et al.). Both are credited. A separate two-level signed-chain volume finding concerns volume rather than covariance. No source inspected directly determines the two-layer covariance block spectrum or sharp asymptotic 4 barrier in the specified coordinate metric; residual alias/general conditional-beta literature may exist.

## value

PASS

The complete Euclidean covariance spectrum and sharp balancing criterion identify a natural isotropy barrier for a two-level signed-order family. The exact beta-fiber decomposition makes the high-dimensional statistic reproducible; this is more than deriving a volume already in the literature, while remaining metric-normalization-dependent.

The dated certificate retains the supplied scientific assessment, sources and limitations.
