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

For K_(2m) with m prescribed vertex pairs, all conductances variable, matching price t>0 and budget B>0, group symmetrization plus concavity yields symmetric eigenvalues 2ma and (2m-2)a+2b and the exact optimum 2B/(2m-2+t) for t<=2, B/m for t>=2. When t<2 the orbit-average of PSD slack L-lambda P vanishes, forcing every optimizer to be the uniform Laplacian. For t>=2, m antisymmetric pair vectors give m lambda2<=B-(t-2)sum d_i; equality implies all four edges between pair i and pair j have one common c_ij, and exactly 2d_i+2sum c_ij=B/m, 2lambda2(L_c)>=B/m, (t-2)sum d_i=0. At t>2 degree equations have affine dimension m(m-3)/2 for m>=3 (m=2 separately) and a strict interior spectral witness; at t=2 dimension m(m-1)/2. Independent matrix tests for 60 parameter sets m2..7 and 480 asymmetric feasible assignments confirmed eigenvalue value/equality inequalities (max roundoff 1.22e-15). Analytic PSD equality and incidence ranks, not random testing, prove all parameters.

## originality

PASS

Best-of-knowledge comparison across named aliases, original statements and implications supports a distinct result; see four checks and residual risks.

## value

PASS

A sharp all-weights spectral-design rigidity transition at the natural relative cost two, with complete high-price and critical optimizer faces (including nonuniform designs) and exact parameter-dependent dimensions, is a motivated and potentially reusable network optimization benchmark beyond existence of one symmetric solution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
