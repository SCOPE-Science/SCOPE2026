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

From independent iid update derive covariance T=[[m²+η²σ²,−2βm,β²],[m,−β,0],[1,0,0]], m=1+β−ηµ. Independently symbolically checked det(I−T)=(1+β)η[2µ(1−β)−η((1−β)µ²/(1+β)+σ²)], positive-definite quadratic V and exact conditional drift minus same coefficient times x². Telescoping proves convergence for any deterministic initial pair strictly below bound. At the endpoint T has eigenvalue one; above det(I−T)<0 entails a real eigenvalue >1, and the three deterministic rank-one moment starts span all symmetric moment arrays, proving necessity. The β-derivative is exactly factored; v∈(0,1), v≥1 and v=0 limit cases handled. Independent SymPy det/drift/derivative checks all exact. Assumes scalar iid positive curvature with finite second moment; not general acceleration rates.

## originality

PASS

Best-of-knowledge original necessary-and-sufficient mean-square stability for iid positive scalar random curvature throughout the low-variance regime, and exact unique momentum maximizing stepsize width. Kidambi et al. already derive algebraically identical necessary high-variance bound (c≥2), which is credited rather than misrepresented as new.

## value

PASS

The coefficient of variation v is a natural intrinsic noise measure, and the exact transition v=1 tells when momentum increases versus decreases the maximal mean-square stable constant stepsize for every iid positive scalar curvature law. The reachable low-variance optimum is an actionable sharp boundary beyond a previous necessary high-noise restriction; not claiming faster convergence rate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
