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

Let d>=2,m=d+1 and a unit-edge regular d-simplex, X uniform interior, and D(X)=min_i ||X-v_i||. In barycentric coordinates lambda, the exact identity ||X-v_i||²=(1+sum lambda_j²)/2-lambda_i yields Delta=R²-D²=T-H/2 with R²=d/(2m), T=max_i(lambda_i-1/m), H=sum_i(lambda_i-1/m)². The inequality H<=T proves unique farthest nearest-vertex distance at the centroid. For 0<t<=t0=1/[m(m-1)], {T<=t} is a homothetic simplex of normalized volume (mt)^d. Disintegrate by outer facet: conditional Dirichlet_d(1,...,1) direction P independent of radial T, with H=Q T² where Q=m² sum P_j²-m positive in [m/(m-1),m(m-1)]. For epsilon<t0/2, the inequality Delta>=T/2 excludes all outer cells and T->T-Q T²/2 is strictly increasing, so the positive root gives the exact Dirichlet expectation. Lagrange inversion gives absolutely convergent positive moments and explicitly E Q=m, E Q²=m²(m²+7m-6)/[(m+1)(m+2)], hence the stated eps and eps² coefficients. Independent Fraction arithmetic recomputed moments for d=2..14. The iid maximum law e^(-x^d) follows from leading (m epsilon)^d tail. Scope only fixed d and small endpoint window; finite checks not an all-d proof.

## originality

PASS

PASS qualified. Classical simplex second moments and Voronoi quantization papers concern average error and transportation/optimal sites; they do not determine near-maximal error at the fixed original vertices under uniform interior sampling. Published Resultary exact deep-hole spectrum of regular-simplex Minkowski vertex averages is a discrete k-fold averaged-vertex set, not this continuous Dirichlet nearest-original-vertex tail. The exact radial facet shape Q and all-orders endpoint expansion were not found in inspected direct comparisons. As with any exact simplex distribution, an unindexed Dirichlet order-statistics identity could already imply it; priority remains qualified.

## value

PASS

PASS. A regular simplex with fixed vertices is a natural nearest-site quantizer, and its worst-error location and near-worst-error distribution are meaningful reliability invariants for uniform samples, beyond familiar mean-square errors. An exact full endpoint law, all rational coefficients, and the extreme-sample scale address a natural mathematical question; knowing only moments or a discrete vertex-average spectrum is insufficient. It does not concern optimized quantization sites or distributions away from the endpoint window.

The dated certificate retains the supplied scientific assessment, sources and limitations.
