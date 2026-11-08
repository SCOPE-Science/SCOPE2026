---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For n>=2, 0<c<1 the independent unit normals have B(p)=2 sum_j p_j u_j u_j^T, trace B=2 and 0<lambda_min<=lambda_max<2, so ||I-B||=1-lambda_min. The normalized common Rayleigh direction q has |u_j.q|^2=(1-c)/[n+(n-2)c] for every j, forcing lambda_min<=2(1-c)/D for all strictly positive p. At p*=([1+(n-2)c],1,...,1)/D, q is a least eigenvector and the other eigenvalues 2(1-c^2)/D (mult. n-2) and 2(1+c)[1+(n-2)c]/D exceed it. Equality Bq=lambda_min q forces every spoke p_j=1/D, so the minimizer is unique without assuming symmetric p. The uniform Gram 2x2 block gives its gap 2lambda_-/n, asymptotic 2(1-c^2)/(c^2 n^2), against optimum 2(1-c)/[(1+c)n]. n=2 and 0<c<1 are covered; n=1/c=0 or c=1 not claimed. Inspected RESULT.md, check.py and SLOGAN at frozen blob identities. Independent numeric eigenchecks over n=2,3,5,8 and c=0.3,0.6,0.9 corroborated the exact proof; no finite check substitutes for it.

## originality

PASS

Best-of-knowledge original as an explicit sharp and unique *probability-shape* optimization for the whole hub-and-spoke family, not as E-optimal design or Rayleigh min-max in general. Related optimal-design theory may contain the specialization in alternate terms.

## value

PASS

The exactly specified simultaneous reflection system is a natural structured frame, and changing the sharp contraction gap from order n^-2 to n^-1 under fixed c is a meaningful optimization and provable spectral improvement; the uniqueness of the optimizer is also structurally informative.

The dated certificate retains the supplied scientific assessment, sources and limitations.
