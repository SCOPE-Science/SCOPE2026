---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The level averages M_n yield M_n(B^mf)≤(b|λ|)^m M_{n+m}(f), with equality at root for level-m common-phase f. For scalar backward shift on ces_p, the identities with increasing cumulative sums u_n and d_k=u_k−u_{k−1}≥0 give exactly ||S^ma||^p=Σ_{k≥m}d_kH_p(k−m+1) and ||a||^p=Σd_kH_p(k+1). Strict log-convexity of Hurwitz tails via their Gamma-integral representation makes the ratio strictly decreasing in k, yielding unique maximizing support at k=m. Finite-rank level truncation gives essential upper bound (b|λ|)^m; normalized weakly-null radial basis vectors in reflexive ces_p give reverse bound against every compact operator. Integral test H_p(m+1)~m^(1−p)/(p−1) yields asymptotic and spectral radius. Independently checked 12 Hurwitz-ratio cases and the Tonelli identities for sample nonnegative vectors; analytical proof covers all m,p,b.

## originality

PASS

Chen–Cheng–Zhang–Zhou 2026 treat exactly rooted-tree Cesàro weighted backward shifts, but their Theorem 2.7 and subsequent mixing/chaos results give boundedness/dynamics rather than sharp all-m power/essential norms and phase-rigidity. Albanese–Asensio 2026 scalar Cesàro shifts supply rough finite p-norm estimates and reflexive basis framework, not this exact Hurwitz-zeta all-power formula. Resultary power-profile hits concern different spaces.

## value

PASS

The exact operator/essential-norm gap and extremizer rigidity settle natural operator-geometric questions for a canonical homogeneous-tree model. In particular at critical b|λ|=1, essential norms remain 1 while usual power norms grow polynomially with sharp coefficient. This distinguishes spectral boundedness from norm dynamics in a natural infinite-dimensional setting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
