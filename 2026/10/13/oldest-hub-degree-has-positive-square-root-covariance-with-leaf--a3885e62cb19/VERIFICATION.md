---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

With X_n attachment to the oldest vertex and Y_n attachment to any leaf, E[X|T]=D/2(n-1), E[Y|T]=L/2(n-1), E[XY|T]=1_{D=1}/2(n-1). The mixed product recurrence cancels the D*L terms and gives c_{n+1}-c_n=d_n l_n/(4(n-1)^2)-q_n/(2(n-1)). Exact d=(2n-3)q and l=2(n-1)/3+4q/3 yield the displayed positive increment for n>=3; gamma ratio q~1/sqrt(pi n) then gives c_n~2sqrt(n)/(3sqrt(pi)). An independent exact rational recurrence checked 158 increments. Boundary c2=c3=0 verified.

## originality

PASS

Hartle–Krapivsky (2026) calculates aggregate leaf/degree-class fluctuations and covariances; Peköz–Röllin–Ross (2017) joint old-vertex degrees but not global leaf count. Neither inspected statement gives the distinguished oldest-degree / total-leaves mixed covariance or exact positive increment.

## value

PASS

The local-global covariance quantifies a non-obvious positive coupling in a canonical growth model despite competition for individual edges, and exposes an exact square-root growth scale distinct from aggregate degree-class covariance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
